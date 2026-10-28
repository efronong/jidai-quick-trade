"""Fetch prices for every stock in universe.json from Yahoo Finance (via yfinance) and write raw/collect.json
in the same shape the browser collector produced, so scripts/build.py can turn it into the dashboard's data files.

Analyst targets, earnings dates, names and headlines change slowly: they come from data/fundamentals.json,
which scripts/fetch_fundamentals.py refreshes twice a day.
"""
import json, math, os, sys, datetime as dt
import pandas as pd
import yfinance as yf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U = json.load(open(os.path.join(ROOT, 'scripts', 'universe.json')))
SYMS = sorted({s for v in U.values() for s in v})
FUND_PATH = os.path.join(ROOT, 'data', 'fundamentals.json')
FUND = json.load(open(FUND_PATH)) if os.path.exists(FUND_PATH) else {}


def frame(df, sym):
    """Pull one ticker's columns out of a multi-ticker yfinance download."""
    if df is None or df.empty:
        return None
    if isinstance(df.columns, pd.MultiIndex):
        if sym not in df.columns.get_level_values(0):
            return None
        f = df[sym]
    else:
        f = df
    f = f.dropna(subset=['Close'])
    return f if not f.empty else None


def num(x):
    try:
        x = float(x)
        return None if math.isnan(x) else x
    except Exception:
        return None


def main():
    daily = yf.download(SYMS, period='5y', interval='1d', group_by='ticker', auto_adjust=False, progress=False, threads=True)
    intra = yf.download(SYMS, period='1d', interval='5m', group_by='ticker', auto_adjust=False, progress=False, threads=True, prepost=False)
    q, failed = {}, []
    for s in SYMS:
        d = frame(daily, s)
        if d is None:
            failed.append(s)
            continue
        f = FUND.get(s, {})
        i = frame(intra, s)
        t = [int(pd.Timestamp(x).timestamp() // 86400) for x in d.index]
        c = [float(x) for x in d['Close']]
        vv = [float(x or 0) for x in d['Volume'].fillna(0)]
        o = {'fund': f.get('fund') or {}, 'news': f.get('news') or []}
        last_day = t[-1]
        intra_obj = None
        px = c[-1]
        if i is not None:
            ts = [int(pd.Timestamp(x).timestamp()) for x in i.index]
            t0 = ts[0]
            n = (ts[-1] - t0) // 300 + 1
            grid = [None] * n
            for k, x in zip(ts, i['Close']):
                grid[(k - t0) // 300] = float(f'{float(x):.5g}')
            iday = ts[-1] // 86400
            px = float(i['Close'].iloc[-1])
            if iday == last_day:
                c[-1] = px                      # today's daily bar = latest intraday price
                pc = c[-2] if len(c) > 1 else None
            elif iday > last_day:
                pc = c[-1]
                t.append(iday); c.append(px); vv.append(float(i['Volume'].fillna(0).sum()))
            else:
                pc = c[-2] if len(c) > 1 else None
            intra_obj = {'t0': t0, 'c': grid, 'open': num(i['Open'].iloc[0]), 'high': num(i['High'].max()), 'low': num(i['Low'].min()), 'pc': pc, 'time': ts[-1]}
        else:
            pc = c[-2] if len(c) > 1 else None
        last = c[-1]
        nn = len(c); cut = max(0, nn - 252)
        wi = list(range(0, cut, 5)); di = list(range(cut, nn))
        enc = lambda idx: ','.join(str(round(c[k] / last * 1000)) for k in idx)
        dd = lambda idx: ','.join(str(t[k] if j == 0 else t[k] - t[idx[j - 1]]) for j, k in enumerate(idx))
        o['ser'] = {'last': last, 'wd': dd(wi), 'wc': enc(wi), 'dd': dd(di), 'dc': enc(di),
                    'v20': sum(vv[-21:-1]) / 20 if len(vv) > 21 else (sum(vv[:-1]) / max(1, len(vv) - 1)), 'vLast': vv[-1]}
        meta = f.get('meta') or {}
        o['meta'] = {'name': meta.get('name') or s, 'ex': meta.get('ex') or '', 'cur': meta.get('cur') or ('SGD' if s.endswith('.SI') else 'USD'),
                     'px': px, 'chg': (px / pc - 1) * 100 if pc else None, 'time': intra_obj['time'] if intra_obj else None,
                     'vol': vv[-1], 'hi52': max(c[-252:]), 'lo52': min(c[-252:]), 'pc': pc}
        if intra_obj:
            o['intra'] = intra_obj
        q[s] = o
    os.makedirs(os.path.join(ROOT, 'raw'), exist_ok=True)
    out = {'fetchedAt': dt.datetime.now(dt.timezone.utc).isoformat().replace('+00:00', 'Z'), 'U': U, 'q': q}
    json.dump(out, open(os.path.join(ROOT, 'raw', 'collect.json'), 'w'))
    print('stocks', len(q), 'failed', failed)
    if len(q) < len(SYMS) * 0.6:
        sys.exit('Too many tickers failed; keeping the previous data.')


if __name__ == '__main__':
    main()
