# JIDAI Quick Trade

Daily trending stocks for US and SGX markets across six sectors, by trading style (long-term, swing, intraday, IPOs),
with forecasts, a pick log and a Top 10 Government-Traded Stocks page.

**Open the dashboard:** `https://<your-username>.github.io/jidai-quick-trade/`

## How it stays fresh
| What | How often | Where |
|---|---|---|
| Prices, intraday charts, open / previous close | every 10 min on weekdays, 08:00–05:50 SGT | `.github/workflows/live.yml` (Yahoo Finance via yfinance) |
| Analyst targets, earnings dates, headlines | twice a day | `.github/workflows/daily.yml` → `data/fundamentals.json` |
| Top-5 picks, forecasts, events, IPOs, pick log | once a day | Claude scheduled task → `data/*.json` |
| Government trades | once a day | Claude scheduled task → `data/gov_*.json` |

The page also re-reads its data every 2 minutes while open, and has a Refresh button.
Prices are as fresh as the last 10-minute run (GitHub can delay scheduled runs by a few minutes at busy times).

Research only, not financial advice.
