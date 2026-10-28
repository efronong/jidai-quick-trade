import json, statistics as st, datetime as dt, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from picks import P, IPO_LIST, SERENITY, X_POSTS, EVENTS

SRC = next((a for a in sys.argv[1:] if not a.startswith('--')), 'raw/collect.json')
D = json.load(open(SRC))
Q, U = D['q'], D['U']
ASOF = D['fetchedAt']
TODAY = (dt.datetime.fromisoformat(ASOF.replace('Z', '+00:00')) + dt.timedelta(hours=8)).date().isoformat()  # SGT date
SECTOR = {}
for k in [x for x in U if x != 'ipo']:
    for s in U[k]: SECTOR.setdefault(s, k)
os.makedirs('out', exist_ok=True)

def day(n): return (dt.date(1970, 1, 1) + dt.timedelta(days=n)).isoformat()

def decode(o):
    s = o['ser']; last = s['last']
    def dec(ds, cs):
        if not ds: return []
        dd = [int(x) for x in ds.split(',')]; cc = [int(x) for x in cs.split(',')]
        t = []; acc = 0
        for i, x in enumerate(dd):
            acc = x if i == 0 else acc + x; t.append(acc)
        return [(t[i], cc[i] / 1000 * last) for i in range(len(t))]
    return dec(s['wd'], s['wc']), dec(s['dd'], s['dc'])

def r(x, n=2): return None if x is None else round(x, n)

stocks, prices, intraday, news = [], [], [], []
for sym, o in Q.items():
    if 'ser' not in o or 'meta' not in o: continue
    m, f = o['meta'], o.get('fund') or {}
    wk, dy = decode(o)
    closes = [c for _, c in dy]
    px = m['px'] or closes[-1]
    def ret(n):
        return r((px / closes[-1 - n] - 1) * 100, 1) if len(closes) > n else None
    full = wk + dy
    ytd_base = [c for t, c in full if day(t) < TODAY[:4] + '-01-01']
    r5y = r((px / full[0][1] - 1) * 100, 1) if full and full[0][0] < (dy[-1][0] - 365 * 4.9) else None
    k = min(20, len(closes) - 1)
    rets = [closes[i] / closes[i - 1] - 1 for i in range(len(closes) - k, len(closes))] if k > 0 else [0]
    g = l = 0
    for i in range(max(1, len(closes) - 14), len(closes)):
        dlt = closes[i] - closes[i - 1]; g += max(dlt, 0); l += max(-dlt, 0)
    rsi = 100 if l == 0 else 100 - 100 / (1 + g / l)
    hi = max(closes[-252:]); sma50 = st.mean(closes[-50:]); sma200 = st.mean(closes[-200:])
    mkt = 'SGX' if sym.endswith('.SI') else 'US'
    tgt = f.get('tgt')
    stocks.append({
        'sym': sym, 'name': m['name'], 'market': mkt, 'sector': SECTOR.get(sym, 'ipo'), 'exchange': m['ex'], 'currency': m['cur'],
        'price': r(px, 4 if px < 1 else 2), 'chg_1d': r(m['chg'], 2), 'ret_5d': ret(5), 'ret_1m': ret(21), 'ret_3m': ret(63), 'ret_6m': ret(126),
        'ret_ytd': r((px / ytd_base[-1] - 1) * 100, 1) if ytd_base else None, 'ret_1y': r((px / closes[0] - 1) * 100, 1) if len(closes) >= 250 else None, 'ret_5y': r5y,
        'off_high': r((px / hi - 1) * 100, 1), 'rsi14': round(rsi) if len(closes) >= 15 else None, 'daily_vol': r(st.pstdev(rets) * 100, 2) if len(closes) >= 10 else None,
        'vol_ratio': r(o['ser']['vLast'] / o['ser']['v20'], 2) if o['ser']['v20'] else None,
        'above_50d': px > sma50, 'above_200d': px > sma200 if len(closes) >= 200 else None,
        'analyst_target': r(tgt, 2), 'target_upside': r((tgt / px - 1) * 100, 1) if tgt else None, 'rating': (f.get('rec') or '').replace('_', ' ') or None,
        'analysts': f.get('nA'), 'rev_growth': r(f['rg'] * 100, 1) if f.get('rg') is not None else None, 'fwd_pe': r(f.get('fpe'), 1),
        'mcap_b': r(f['mcap'] / 1e9, 1) if f.get('mcap') else None, 'earnings_date': f.get('earn'), 'industry': f.get('ind'),
        'serenity': sym in SERENITY, 'updated_utc': ASOF[:16],
        'open': r((o.get('intra') or {}).get('open'), 4 if px < 1 else 2), 'prev_close': r((o.get('intra') or {}).get('pc'), 4 if px < 1 else 2),
        'day_high': r((o.get('intra') or {}).get('high'), 4 if px < 1 else 2), 'day_low': r((o.get('intra') or {}).get('low'), 4 if px < 1 else 2),
        'price_time': dt.datetime.fromtimestamp(((o.get('intra') or {}).get('time') or m.get('time') or 0), dt.timezone.utc).isoformat()[:16] + 'Z' if ((o.get('intra') or {}).get('time') or m.get('time')) else None,
    })
    for t, c in wk: prices.append({'sym': sym, 'date': day(t), 'close': r(c, 4 if c < 5 else 2), 'step': 'week'})
    for t, c in dy: prices.append({'sym': sym, 'date': day(t), 'close': r(c, 4 if c < 5 else 2), 'step': 'day'})
    it = o.get('intra') or {}
    if it.get('t0'):
        for i, c in enumerate(it['c']):
            if c is not None:
                intraday.append({'sym': sym, 'time': dt.datetime.fromtimestamp(it['t0'] + 300 * i, dt.timezone.utc).isoformat()[:16] + 'Z', 'price': c})
    for a in (o.get('news') or [])[:4]:
        news.append({'sym': sym, 'when': a['d'], 'title': a['t'], 'publisher': a['p'], 'url': a['u'], 'kind': 'news'})

for when, syms, text in X_POSTS:
    news.append({'sym': syms, 'when': when[:10], 'title': text, 'publisher': '@aleabitoreddit on X', 'url': 'https://x.com/aleabitoreddit', 'kind': 'x'})

S = {s['sym']: s for s in stocks}
HORIZON = {'long': '12 months', 'swing': '4 weeks', 'intraday': 'Rest of session', 'ipo': '6 months'}
picks = []
for (style, sector, mkt), lst in P.items():
    for i, (sym, thesis, cat, risk, (lo, base, hi), conv, setup) in enumerate(lst):
        if sym not in S: print('missing', sym); continue
        hz = HORIZON[style]
        if style == 'intraday' and mkt == 'SGX': hz = 'Next session'
        picks.append({'key': f'{style}|{sector}|{mkt}|{i+1}', 'style': style, 'sector': sector, 'market': mkt, 'rank': i + 1, 'sym': sym,
                      'setup': setup, 'thesis': thesis, 'catalyst': cat, 'risk': risk, 'exp_low': lo, 'exp_base': base, 'exp_high': hi,
                      'horizon': hz, 'conviction': conv, 'price_at_pick': S[sym]['price'], 'picked': TODAY})

ipos = []
for sym, name, d, p, sec, status in IPO_LIST:
    s = S.get(sym)
    ipos.append({'sym': sym, 'name': name, 'ipo_date': d, 'ipo_price': p, 'sector': sec, 'status': status,
                 'price': s['price'] if s else None, 'since_ipo': r((s['price'] / p - 1) * 100, 1) if (s and p) else None,
                 'chg_1d': s['chg_1d'] if s else None})

markets = [
 {'market': 'US', 'name': 'Nasdaq / NYSE', 'tz': 'America/New_York', 'open': '09:30', 'close': '16:00', 'pre_open': '04:00', 'after_close': '20:00', 'break_start': None, 'break_end': None},
 {'market': 'SGX', 'name': 'Singapore Exchange', 'tz': 'Asia/Singapore', 'open': '09:00', 'close': '17:00', 'pre_open': '08:30', 'after_close': '17:06', 'break_start': '12:00', 'break_end': '13:00'},
]
events = [{'date': d, 'area': a, 'event': e, 'detail': x} for d, a, e, x in EVENTS]

# pick log: append today's picks to the existing log (if passed), replacing today's rows
log_path = 'out/picklog.json'
old = json.load(open(log_path)) if os.path.exists(log_path) else []
old = [x for x in old if x['picked'] != TODAY]
log = old + [{k: p[k] for k in ('picked', 'style', 'sector', 'market', 'rank', 'sym', 'price_at_pick', 'exp_base', 'horizon')} | {'id': p['picked'] + '|' + p['key']} for p in picks]

OUTS = [('stocks', stocks), ('prices', prices), ('intraday', intraday), ('news', news), ('picks', picks), ('ipos', ipos), ('markets', markets), ('events', events), ('picklog', log)]
if '--prices-only' in sys.argv:   # hourly intraday refresh: never touch picks, the pick log, IPOs or events
    OUTS = OUTS[:4]
for name, rows in OUTS:
    json.dump(rows, open(f'out/{name}.json', 'w'), separators=(',', ':'))
    print(name, len(rows), os.path.getsize(f'out/{name}.json'))
print('asof', ASOF, 'sgt date', TODAY)
