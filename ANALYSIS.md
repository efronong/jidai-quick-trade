# Daily analysis procedure (run by Claude's scheduled task, in the cloud — no laptop needed)

Prices and government trades are refreshed by GitHub Actions. This procedure adds Claude's judgment: the top-5 picks,
forecast ranges, events, IPO list and the @aleabitoreddit summaries.

1. Attach the repository with push access (add_repo), clone it to /home/claude/jidai, `cd` there.
2. `mkdir -p raw out && git fetch --depth=1 origin snapshot && git checkout FETCH_HEAD -- d && cp d/collect.json raw/collect.json`
   (the latest price snapshot, saved by every live price run). If that branch is missing, use the `data` branch the same way.
   The snapshot already holds analyst data and headlines. Read the screen with a short script: returns, RSI, distance from high,
   analyst upside, revenue growth, forward P/E, next earnings, volume ratio, today's move — per sector and market.
3. Research with WebSearch / WebFetch: overall US market, each of the six sectors, SGX/STI, the Fed and macro calendar,
   big single-stock moves in the snapshot, the IPO calendar (stockanalysis.com/ipos/calendar/ and /ipos/2026/).
   For @aleabitoreddit: x.com can't be read from the cloud, so search for his latest posts and use trackers such as
   semiconstocks.com; summarise in your own words, and say "via tracker" when the source isn't X itself.
4. Rewrite `scripts/picks.py` (same structure): `P[(style, sector, market)]` for style long/swing/intraday,
   sector ai/hc/fin/pwr/def/nrg, market US/SGX, plus `P[('ipo','all','US')]` — 5 tuples each
   `(sym, thesis, catalyst, risk, (bear, base, bull), conviction, setup)`. Symbols must be in `scripts/universe.json`.
   Base case = analyst upside discounted for sector reliability, adjusted for momentum, valuation and catalysts;
   range width from the stock's own volatility. Update `IPO_LIST`, `SERENITY`, `X_POSTS`, `EVENTS` (upcoming + last 2 days).
   Plain, short sentences.
5. `cp data/picklog.json out/picklog.json && python scripts/build.py raw/collect.json`
   then `cp out/picks.json out/picklog.json out/ipos.json out/events.json data/`.
6. `git add scripts/picks.py data/picks.json data/picklog.json data/ipos.json data/events.json && git commit -m "Daily picks <date>" && git push`
   (the push redeploys the site within a few minutes).
7. Finish with a 3–5 line message: the day's biggest move, the top long-term pick per sector, anything that changed sharply.
   One short line: research, not financial advice.

Never invent prices or trades. If the snapshot is missing or older than 36 hours, stop and say so.
