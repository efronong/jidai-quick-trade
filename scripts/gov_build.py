"""Build the government-trades datasets for JIDAI Quick Trade.

Inputs (raw/): congress.json (Capitol Trades: House + Senate PTRs), oge.json (Open Cabinet: OGE 278-T / 278e
for the President and senior executive officials), quotes.json (Yahoo quote: type, exchange, name, price, chg),
filings.json (optional: {"pid|pubdate": filing_url} for congressional filings).
Outputs (out/): gov_trades.json (one row per de-duplicated transaction), gov_meta.json.
Scoring is done in the page so filters can re-rank; score() here mirrors the page for picking chart tickers.
"""
import json, re, datetime as dt, os, sys, itertools, math

R = 'raw/'
ASOF = sys.argv[1] if len(sys.argv) > 1 else dt.date.today().isoformat()
ct = json.load(open(R + 'congress.json'))
oc = json.load(open(R + 'oge.json'))
qt = json.load(open(R + 'quotes.json'))
filings = json.load(open(R + 'filings.json')) if os.path.exists(R + 'filings.json') else {}

def norm(t):
    return (t or '').strip().upper().replace('.', '-').replace('/', '-')

def quote(t):
    return qt.get(norm(t))

rows = []
# ---- Congress (House + Senate periodic transaction reports, via Capitol Trades) ----
pol = {p[0]: p for p in ct['pol']}
plist = ct['pol']
seen = {}
for tid, pi, tk, issuer, ty, tx, pub, value, owner in ct['rows']:
    pid, name, party, chamber, state = plist[pi]
    key = ('C', pid, norm(tk), tx, ty, value, owner)
    if key in seen:            # duplicate / amended copy of the same transaction
        seen[key]['dupes'] += 1
        continue
    r = {'id': f'C{tid}', 'official': name, 'official_id': pid, 'group': chamber, 'role': f"{'Rep.' if chamber == 'house' else 'Sen.'} ({(party or '?')[0].upper()}-{(state or '').upper()})",
         'ticker': norm(tk), 'issuer': issuer, 'side': 'buy' if ty == 'b' else 'sell', 'tx_date': tx, 'disclosed': pub,
         'amount': value, 'amount_label': None, 'owner': {'s': 'Spouse', 'j': 'Joint', 'c': 'Child', 'n': 'Not disclosed'}.get(owner, 'Self'),
         'source': 'House PTR' if chamber == 'house' else 'Senate PTR',
         'link': filings.get(f'{pid}|{pub}') or f'https://www.capitoltrades.com/trades/{tid}',
         'link_kind': 'Original filing' if filings.get(f'{pid}|{pub}') else 'Capitol Trades record (links to the filing)',
         'dupes': 0}
    seen[key] = r
    rows.append(r)

# ---- Executive branch (OGE 278-T / annual 278e, via Open Cabinet) ----
offs, urls = oc['off'], oc['urls']
def filed_from_url(u):
    m = re.search(r'(\d{2})\.(\d{1,2})\.(\d{4})-278T', u)
    if m: return f'{m.group(3)}-{m.group(1)}-{int(m.group(2)):02d}'
    return None
for oi, tk, ty, date, mid, ui, sk, desc, amt in oc['rows']:
    o = offs[oi]; u = urls[ui]
    is_trump = o['n'].startswith('Trump, Donald')
    first_last = ' '.join(reversed(o['n'].split(', ', 1))) if ', ' in o['n'] else o['n']
    key = ('E', o['n'], norm(tk), date, ty, amt)
    if key in seen:            # the same trade appears in a 278-T and again in the annual report
        seen[key]['dupes'] += 1
        if sk == 'T' and seen[key]['source'].startswith('OGE annual'):
            seen[key].update(source='OGE 278-T', link=u, disclosed=filed_from_url(u))
        continue
    r = {'id': f'E{len(rows)}', 'official': first_last, 'official_id': o['n'], 'group': 'trump' if is_trump else 'exec',
         'role': o['ti'] if not is_trump else 'President', 'ticker': norm(tk), 'issuer': desc, 'side': 'buy' if ty == 'P' else 'sell',
         'tx_date': date, 'disclosed': filed_from_url(u), 'amount': mid, 'amount_label': amt, 'owner': '',
         'source': 'OGE 278-T' if sk == 'T' else 'OGE annual report', 'link': u, 'link_kind': 'Original OGE filing', 'dupes': 0}
    seen[key] = r
    rows.append(r)

# attach market info; keep individual stocks only
out = []
for r in rows:
    q = quote(r['ticker'])
    if not q or q[0] != 'EQUITY': continue
    r['exchange'] = q[1]
    r['nasdaq'] = 'Nasdaq' in (q[1] or '')
    r['name'] = q[2]
    r.pop('dupes', None)
    out.append(r)

ASOF_D = dt.date.fromisoformat(ASOF)
def score(trs, side, window):
    """Government Trading Score (0-100) for one stock: 40 breadth + 25 recency + 15 repeat + 20 net direction."""
    act = [t for t in trs if side == 'both' or t['side'] == side]
    if not act: return None
    officials = {t['official_id'] for t in act}
    last = max(t['tx_date'] for t in act)
    days = (ASOF_D - dt.date.fromisoformat(last)).days
    occasions = {(t['official_id'], t['tx_date']) for t in act}
    buys = sum(1 for t in trs if t['side'] == 'buy'); sells = len(trs) - buys
    net = (buys if side != 'sell' else sells) / (buys + sells)
    s = 40 * min(len(officials), 5) / 5 + 25 * max(0, 1 - days / window) + 15 * min(len(occasions), 10) / 10 + 20 * net
    return round(s), len(officials), last

PERIODS = {'7d': 7, '30d': 30, '90d': 90, '180d': 180, '1y': 365}
GROUPS = {'all': None, 'trump': {'trump'}, 'house': {'house'}, 'senate': {'senate'}}
need = set()
for (pk, w), (gk, g), side, nas in itertools.product(PERIODS.items(), GROUPS.items(), ['buy', 'sell', 'both'], [True, False]):
    start = (ASOF_D - dt.timedelta(days=w)).isoformat()
    sel = [t for t in out if t['tx_date'] >= start and t['tx_date'] <= ASOF and (g is None or t['group'] in g) and (t['nasdaq'] or not nas)]
    by = {}
    for t in sel: by.setdefault(t['ticker'], []).append(t)
    ranked = sorted(((score(v, side, w), k) for k, v in by.items()), key=lambda x: (-(x[0] or (0,))[0], -(x[0] or (0, 0))[1]) if x[0] else (1, 0))
    for sc, k in ranked[:10]:
        if sc: need.add(k)

os.makedirs('out', exist_ok=True)
json.dump(out, open('out/gov_trades.json', 'w'), separators=(',', ':'))
json.dump(sorted(need), open('raw/need_prices.json', 'w'))
print('trades', len(out), 'nasdaq', sum(t['nasdaq'] for t in out), 'groups', {g: sum(t['group'] == g for t in out) for g in ['house', 'senate', 'trump', 'exec']})
print('tickers needing price history', len(need))
print('removed duplicates', len(rows) and (len(ct['rows']) + len(oc['rows']) - len(rows)))

# ---------- final datasets for the dashboard ----------
import datetime as _dt
gp = json.load(open(R + 'gov_prices.json')) if os.path.exists(R + 'gov_prices.json') else {}
trades = [{k: t[k] for k in ('id', 'official', 'official_id', 'group', 'role', 'ticker', 'issuer', 'side', 'tx_date', 'disclosed', 'amount', 'amount_label', 'owner', 'source', 'link', 'nasdaq')} for t in out]
json.dump(trades, open('out/gov_trades.json', 'w'), separators=(',', ':'))
stocks = []
for tk in sorted({t['ticker'] for t in out}):
    q = quote(tk)
    stocks.append({'ticker': tk, 'name': q[2], 'exchange': q[1], 'price': q[3], 'chg_1d': round(q[4], 2) if q[4] is not None else None, 'mcap_b': round(q[5] / 1e9, 1) if q[5] else None})
json.dump(stocks, open('out/gov_stocks.json', 'w'), separators=(',', ':'))
prices = []
for tk, arr in gp.items():
    d = 0
    for delta, c in arr:
        d += delta
        prices.append({'ticker': tk, 'date': (_dt.date(1970, 1, 1) + _dt.timedelta(days=d)).isoformat(), 'close': c})
json.dump(prices, open('out/gov_prices.json', 'w'), separators=(',', ':'))
def rng(g):
    xs = [t for t in out if t['group'] in g]
    return min(t['tx_date'] for t in xs), max(t['tx_date'] for t in xs), len(xs)
UPDATED = sys.argv[2] if len(sys.argv) > 2 else ASOF
src = [{'source': 'as_of', 'as_of': ASOF, 'updated': UPDATED, 'url': '', 'covers': '', 'tx_from': None, 'tx_to': None, 'records': len(out), 'note': ''}]
for name, g, url, covers, note in [
    ('US House periodic transaction reports', {'house'}, 'https://disclosures-clerk.house.gov/FinancialDisclosure', 'House members (via Capitol Trades, linked to each original PDF)', ''),
    ('US Senate periodic transaction reports', {'senate'}, 'https://efdsearch.senate.gov/search/', 'Senators (via Capitol Trades, linked to each original eFD report)', ''),
    ('OGE Form 278-T and annual reports', {'trump', 'exec'}, 'https://open-cabinet.org/download', 'President Trump and senior executive-branch officials (parsed by Open Cabinet from OGE filings)',
     "Trump's newest 278-T reports may not be included yet, and annual-report trades have no separate disclosure date."),
]:
    a, b, n = rng(g)
    src.append({'source': name, 'as_of': None, 'updated': None, 'url': url, 'covers': covers, 'tx_from': a, 'tx_to': b, 'records': n, 'note': note})
json.dump(src, open('out/gov_sources.json', 'w'), separators=(',', ':'))
for f in ['gov_trades', 'gov_stocks', 'gov_prices', 'gov_sources']:
    print(f, os.path.getsize(f'out/{f}.json'))
