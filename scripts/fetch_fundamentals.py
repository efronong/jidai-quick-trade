"""Twice a day: names, exchanges, analyst targets, earnings dates and recent headlines for every stock -> data/fundamentals.json."""
import json, os, time, datetime as dt
import yfinance as yf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U = json.load(open(os.path.join(ROOT, 'scripts', 'universe.json')))
SYMS = sorted({s for v in U.values() for s in v})
PATH = os.path.join(ROOT, 'data', 'fundamentals.json')
old = json.load(open(PATH)) if os.path.exists(PATH) else {}


def news_items(t):
    out = []
    try:
        for a in (t.news or [])[:4]:
            c = a.get('content') or {}
            title = c.get('title') or a.get('title')
            if not title:
                continue
            when = c.get('pubDate') or (dt.datetime.fromtimestamp(a.get('providerPublishTime', 0), dt.timezone.utc).isoformat() if a.get('providerPublishTime') else '')
            url = (c.get('canonicalUrl') or {}).get('url') or (c.get('clickThroughUrl') or {}).get('url') or a.get('link') or ''
            pub = (c.get('provider') or {}).get('displayName') or a.get('publisher') or ''
            out.append({'t': title, 'p': pub, 'd': (when or '')[:16], 'u': url})
    except Exception:
        pass
    return out


res = {}
for s in SYMS:
    t = yf.Ticker(s)
    try:
        i = t.info or {}
    except Exception:
        i = {}
    if not i:
        if s in old:
            res[s] = old[s]
        continue
    earn = i.get('earningsTimestamp') or i.get('earningsTimestampStart')
    if earn and earn < time.time() - 86400 and i.get('earningsTimestampEnd'):
        earn = i.get('earningsTimestampEnd')
    res[s] = {
        'meta': {'name': i.get('longName') or i.get('shortName') or s, 'ex': i.get('fullExchangeName') or i.get('exchange') or '', 'cur': i.get('currency')},
        'fund': {'tgt': i.get('targetMeanPrice'), 'tHi': i.get('targetHighPrice'), 'tLo': i.get('targetLowPrice'), 'rec': i.get('recommendationKey'),
                 'nA': i.get('numberOfAnalystOpinions'), 'rg': i.get('revenueGrowth'), 'eg': i.get('earningsGrowth'), 'fpe': i.get('forwardPE'),
                 'mcap': i.get('marketCap'), 'beta': i.get('beta'), 'ind': i.get('industry'),
                 'earn': dt.datetime.fromtimestamp(earn, dt.timezone.utc).date().isoformat() if earn else None},
        'news': news_items(t) or (old.get(s, {}).get('news') or []),
    }
    time.sleep(0.4)
json.dump(res, open(PATH, 'w'), separators=(',', ':'))
print('fundamentals', len(res), 'of', len(SYMS))
