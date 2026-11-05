"""Daily: collect disclosed stock trades by US officials and write raw/congress.json, raw/oge.json, raw/quotes.json,
raw/filings.json for scripts/gov_build.py.

Sources
- House and Senate periodic transaction reports, via Capitol Trades (each trade links to the original House/Senate filing).
- OGE 278-T and annual reports for the President and senior executive officials, via Open Cabinet's published CSV.
Caches in data/ (gov_filings.json, gov_meta_cache.json) keep repeat runs fast.
"""
import csv, io, json, os, re, sys, time, datetime as dt
import requests
import yfinance as yf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, 'raw'); os.makedirs(RAW, exist_ok=True)
DATA = os.path.join(ROOT, 'data')
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36'}
TODAY = dt.date.today()
CUTOFF = (TODAY - dt.timedelta(days=400)).isoformat()
S = requests.Session(); S.headers.update(UA)


def get(url, tries=3):
    for k in range(tries):
        try:
            r = S.get(url, timeout=30)
            if r.status_code == 200:
                return r.text
        except Exception:
            pass
        time.sleep(2 + 3 * k)
    return ''


def objects(html):
    """Trade objects embedded in a Capitol Trades page (React server payload)."""
    # decode the page's embedded data strings properly (falls back to a simple unescape)
    parts = [json.loads(m.group(1)) for m in re.finditer(r'self\.__next_f\.push\(\[1,("(?:[^"\\]|\\.)*")\]\)', html)]
    sc = ''.join(parts) if parts else html.replace('\\"', '"')
    i, out = 0, []
    while True:
        i = sc.find('{"_issuerId":', i)
        if i < 0:
            return out
        d, j, ins = 0, i, False
        while j < len(sc):
            ch = sc[j]
            if ins:
                if ch == '\\':
                    j += 2; continue
                if ch == '"':
                    ins = False
            elif ch == '"':
                ins = True
            elif ch == '{':
                d += 1
            elif ch == '}':
                d -= 1
                if d == 0:
                    break
            j += 1
        txt = sc[i:j + 1]; i = j + 1
        if '"_txId"' not in txt:
            continue
        try:
            out.append(json.loads(txt))
        except Exception:
            pass


def congress():
    trades, page, oldest = {}, 1, '9999'
    while oldest >= CUTOFF and page < 400:
        html = get(f'https://www.capitoltrades.com/trades?pageSize=96&page={page}')
        if not html:
            break
        objs = objects(html)
        if not objs:
            break
        for o in objs:
            trades[o['_txId']] = o
            oldest = min(oldest, (o.get('pubDate') or '9999')[:10])
        page += 1
        time.sleep(0.6)
    cache = os.path.join(DATA, 'gov_congress_raw.json')
    if not trades:
        if os.path.exists(cache):
            d = json.load(open(cache))
            json.dump(d, open(os.path.join(RAW, 'congress.json'), 'w'))
            print('Capitol Trades unreachable; reusing the last saved congressional trades', len(d['rows']))
            return d['pol'], d['rows']
        sys.exit('Capitol Trades unreachable and no saved data')
    pols, rows = {}, []
    for o in trades.values():
        tk = (o.get('issuer') or {}).get('issuerTicker')
        if not tk or o.get('txType') not in ('buy', 'sell'):
            continue
        p = o.get('politician') or {}
        pid = o['_politicianId']
        if pid not in pols:
            pols[pid] = [pid, f"{p.get('nickname') or p.get('firstName')} {p.get('lastName')}", p.get('party'), o.get('chamber'), p.get('_stateId')]
        rows.append([o['_txId'], pid, tk.replace(':US', ''), ((o.get('issuer') or {}).get('issuerName') or '')[:40], o['txType'][0], o.get('txDate'),
                     (o.get('pubDate') or '')[:10], o.get('value'), (o.get('owner') or '')[:1]])
    plist = list(pols.values()); pi = {p[0]: k for k, p in enumerate(plist)}
    for r in rows:
        r[1] = pi[r[1]]
    json.dump({'pol': plist, 'rows': rows}, open(os.path.join(RAW, 'congress.json'), 'w'))
    json.dump({'pol': plist, 'rows': rows}, open(cache, 'w'))
    print('congress trades', len(rows), 'pages', page - 1, 'oldest', oldest)
    return plist, rows


def filings(plist, rows):
    path = os.path.join(DATA, 'gov_filings.json')
    cache = json.load(open(path)) if os.path.exists(path) else {}
    groups = {}
    for r in rows:
        groups.setdefault(f'{plist[r[1]][0]}|{r[6]}', r[0])
    new = [(k, v) for k, v in groups.items() if not cache.get(k)]
    for k, tid in new[:600]:
        h = get(f'https://www.capitoltrades.com/trades/{tid}')
        m = re.search(r'"filingUrl":"([^"]*)"', h.replace('\\"', '"'))
        if m:
            cache[k] = m.group(1)
        time.sleep(0.4)
    json.dump(cache, open(path, 'w'))
    json.dump(cache, open(os.path.join(RAW, 'filings.json'), 'w'))
    print('filings cached', len(cache), 'new', len(new))


def oge():
    txt = get('https://open-cabinet.org/data/all-transactions.csv')
    if not txt:
        print('Open Cabinet unreachable'); return []
    lines = txt.split('\n', 1)[1] if txt.startswith('#') else txt
    rd = csv.DictReader(io.StringIO(lines))
    offs, oi, urls, ui, rows = [], {}, [], {}, []
    for g in rd:
        if (g.get('date') or '') < CUTOFF or not (g.get('type') or '').startswith(('Purchase', 'Sale')) or g.get('instrument_type') != 'common_stock':
            continue
        tk = g.get('resolved_ticker') or g.get('ticker')
        if not tk:
            continue
        n = g['official_name']
        if n not in oi:
            oi[n] = len(offs); offs.append({'n': n, 'ti': g.get('official_title'), 'ag': g.get('agency')})
        u = g.get('source_filing_url') or ''
        if u not in ui:
            ui[u] = len(urls); urls.append(u)
        sk = g.get('source_kind') or ''
        rows.append([oi[n], tk, g['type'][0], g['date'], float(g.get('amount_midpoint') or 0) or None, ui[u],
                     'T' if sk == '278-T' else 'A' if sk == 'annual-278e' else 'X', (g.get('description') or '')[:40], g.get('amount_range')])
    json.dump({'off': offs, 'urls': urls, 'rows': rows}, open(os.path.join(RAW, 'oge.json'), 'w'))
    print('oge trades', len(rows))
    return rows


def norm(t):
    return (t or '').strip().upper().replace('.', '-').replace('/', '-')


def quotes(tickers):
    path = os.path.join(DATA, 'gov_meta_cache.json')
    cache = json.load(open(path)) if os.path.exists(path) else {}
    missing = [t for t in tickers if t not in cache][:400]
    for t in missing:
        try:
            i = yf.Ticker(t).info or {}
            cache[t] = [i.get('quoteType') or 'NONE', i.get('fullExchangeName') or i.get('exchange') or '', i.get('longName') or i.get('shortName') or t, i.get('marketCap')]
        except Exception:
            cache[t] = ['NONE', '', t, None]
        time.sleep(0.3)
    json.dump(cache, open(path, 'w'))
    eq = [t for t in tickers if cache.get(t, ['NONE'])[0] == 'EQUITY']
    px = {}
    if eq:
        df = yf.download(eq, period='5d', interval='1d', group_by='ticker', auto_adjust=False, progress=False, threads=True)
        for t in eq:
            try:
                c = df[t]['Close'].dropna() if len(eq) > 1 else df['Close'].dropna()
                if len(c) >= 2:
                    px[t] = (float(c.iloc[-1]), float((c.iloc[-1] / c.iloc[-2] - 1) * 100))
                elif len(c) == 1:
                    px[t] = (float(c.iloc[-1]), None)
            except Exception:
                pass
    out = {t: [cache[t][0], cache[t][1], cache[t][2], (px.get(t) or (None, None))[0], (px.get(t) or (None, None))[1], cache[t][3]] for t in tickers if t in cache}
    json.dump(out, open(os.path.join(RAW, 'quotes.json'), 'w'))
    print('quotes', len(out), 'equities', len(eq), 'new lookups', len(missing))


def prices():
    need = json.load(open(os.path.join(RAW, 'need_prices.json')))
    df = yf.download(need, period='1y', interval='1d', group_by='ticker', auto_adjust=False, progress=False, threads=True)
    out = {}
    for t in need:
        try:
            c = df[t]['Close'].dropna() if len(need) > 1 else df['Close'].dropna()
        except Exception:
            continue
        prev, arr = 0, []
        for idx, v in c.items():
            d = int(idx.timestamp() // 86400)
            arr.append([d - prev, float(f'{float(v):.5g}')]); prev = d
        out[t] = arr
    json.dump(out, open(os.path.join(RAW, 'gov_prices.json'), 'w'))
    print('gov prices', len(out))


if __name__ == '__main__':
    step = sys.argv[1] if len(sys.argv) > 1 else 'collect'
    if step == 'collect':
        plist, rows = congress()
        filings(plist, rows)
        orows = oge()
        tickers = sorted({norm(r[2]) for r in rows} | {norm(r[1]) for r in orows})
        quotes([t for t in tickers if t and len(t) <= 6 and t[0].isalpha()])
    elif step == 'prices':
        prices()
