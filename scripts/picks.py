# Analyst picks for 2026-11-24 SGT (snapshot: US Mon Nov 23 close, SGX close Nov 23). Fields: sym, thesis, catalyst, risk, (low, base, high) % expected move, conviction, setup
# Horizons: long = 12 months, swing = ~4 weeks, intraday = rest of session (US) / next session (SGX), ipo = 6 months.
# Context Fri Nov 20: S&P -3.7% to 6,910, Nasdaq -5.3%, Dow -1.9%; S&P and Dow in correction. NVDA -14%, MU -14%, AMD -13%, AVGO -12%, TSM -9.5%.
# Anthropic (ANT) fell 8.5% to $88.91 on day two. Bitcoin below $59k. Fed's Cook: waiting longer to hike risks falling behind the curve.
# Context Mon Nov 23: Nvidia board reinstated Jensen Huang as CEO (unanimous; independent-director investigation continues). NVDA +31.5% to ~$165, ~+$1T.
# S&P +4.7% to 7,238, Nasdaq +6.5% to 24,090, Dow ~+3%: best day since April 2025. Chips +10-25%; SanDisk the outlier (-7%).
# CrowdStrike to buy Zscaler in stock (~$43.9B). 10-yr 4.94%, dollar index 104.3 (19-month high), WTI ~$80.8 (-3%), gold +4%. Markets price ~91% odds of a Dec 9 hike.
# SGX: STI -2.05% Fri to 4,975 (first close below 5,000 since June), -0.43% Mon to 4,953.81 - it closed BEFORE the US rally. Marco Polo -9.5% on lower profit guidance.
# Base cases discount analyst targets heavily: many targets were set before the November slide and look stale.
P = {}

# ---------- AI & chips ----------
P[('long','ai','US')] = [
 ('TSM', "Makes almost every leading AI chip, whoever designs it. Revenue +51% at about 15.5x forward earnings, 25% below its high. Rose 14% Monday on heavy volume.",
  "November sales (~Dec 10); Q4 results Jan 14", "Taiwan geopolitics; US chip-access rules", (-20,16,38), 'High', 'Core holding'),
 ('NVDA', "Huang is back as CEO, which removes the biggest overhang; the stock jumped 31.5% to about $165. Still 31% below its high at about 10x forward earnings after a beat and raise.",
  "Estimate upgrades; CES and GTC news", "Board probe still open; export rules; gives back the jump", (-28,18,50), 'High', 'Leader, overhang cleared'),
 ('AVGO', "Custom AI chips plus networking: revenue +86% at about 16x forward earnings, 35% off its high. Lagged Monday's rally (+3%), so it has catching up to do into results.",
  "Q4 results Dec 9", "Lumpy custom-chip orders", (-24,17,42), 'High', 'Leader at a discount'),
 ('MU', "Memory is still the tightest part of AI servers: revenue +379% at about 3.4x forward earnings, 42% off its high; +19% Monday.",
  "FQ1 results (mid/late Dec)", "Memory falls hard when prices turn; DRAM lawsuit", (-40,18,58), 'Medium', 'Cycle leader'),
 ('COHR', "Coherent: ~$20B multi-year optics deals and a reported $2B buyback; about 14x forward earnings and the only big AI name up over the month (+3%).",
  "Buyback; FQ2 results (Feb)", "8-9% daily swings", (-35,18,55), 'Medium', 'Optics leader'),
]
P[('long','ai','SGX')] = [
 ('AWX.SI', "AEM rose 5.5% Monday and is up ~250% this year, still 46% off its high at about 15x earnings. Closed before the US chip rally.",
  "US chip read-across; FY results (Feb)", "One large customer; US chip rule for SG data centres", (-40,15,55), 'Medium', 'SGX AI leader'),
 ('V03.SI', "Venture: net cash, about 15x earnings, low volatility; analysts see about 33% upside. Fell 3.3% Friday.",
  "Analyst upgrades", "Slow revenue growth (+7%)", (-12,12,25), 'High', 'Steady value'),
 ('558.SI', "UMS makes precision parts for chip-equipment makers: revenue +61%, 46% off its high. Applied Materials and Lam rose ~15% Monday.",
  "Chip-equipment spending outlook", "Tied to Applied Materials spending", (-32,15,45), 'Medium', 'Equipment supplier'),
 ('5DD.SI', "Micro-Mechanics: revenue +45%, 43% off its high, about 18x earnings.",
  "Q1 FY27 results", "Small and thinly traded", (-24,13,36), 'Medium', 'Growth at a discount'),
 ('E28.SI', "Frencken builds modules for chip and medical equipment; 56% off its high at about 13x earnings (RSI 25).",
  "Equipment recovery", "Flat revenue", (-26,12,36), 'Medium', 'Recovery'),
]
P[('swing','ai','US')] = [
 ('AVGO', "Rose only 3% while chips jumped 15-30%; results Dec 9 fall inside the window.",
  "Q4 results Dec 9", "Results disappoint", (-13,7,18), 'Medium', 'Laggard into results'),
 ('TSM', "Rose 14% on 1.85x normal volume; less stretched than smaller chips (RSI 42).", "November sales ~Dec 10", "Rally fades", (-11,5,15), 'Medium', 'Quality catch-up'),
 ('MRVL', "+18% Monday; results Dec 1 and the Lumentum deal in progress. 54% off its high.", "Results Dec 1", "Guide disappoints", (-18,6,22), 'Medium', 'Into results'),
 ('COHR', "Held up best through the slide and rose 15% Monday (RSI 52).", "Buyback support", "Optics swings", (-14,6,18), 'Medium', 'Relative strength'),
 ('NVDA', "Follow-through after the leadership fix; RSI only 35 even after +31%.", "Upgrades", "Gap fades", (-15,6,20), 'Medium', 'Post-news trend'),
]
P[('swing','ai','SGX')] = [
 ('AWX.SI', "AEM +5.5% Monday (RSI 37) before the US chip jump.", "US chip catch-up", "US rally fades", (-18,6,25), 'Medium', 'Catch-up'),
 ('558.SI', "UMS RSI 32 after a 29% one-month drop; equipment makers jumped in the US.", "Equipment read-across", "Equipment sentiment", (-15,6,18), 'Medium', 'Oversold rebound'),
 ('V03.SI', "Venture RSI 42; the steadiest name in the group.", "Analyst upgrades", "Low growth", (-6,3,9), 'High', 'Range'),
 ('5DD.SI', "Micro-Mechanics RSI 37.", "Results", "Thin trading", (-10,4,12), 'Medium', 'Support'),
 ('E28.SI', "Frencken RSI 25.", "Bounce", "Flat revenue", (-12,4,14), 'Speculative', 'Oversold rebound'),
]
P[('intraday','ai','US')] = [
 ('NVDA', "+31.5% Monday on Huang's return.", "Follow-through buying", "Profit-taking after a record gain", (-6,0.5,6), 'Medium', 'Post-gap check'),
 ('AVGO', "Lagged with +3%.", "Catch-up", "Rotation out", (-4,0.4,4), 'Medium', 'Laggard'),
 ('MU', "+19%.", "Memory momentum", "Profit-taking", (-6,0.3,6), 'Speculative', 'Momentum'),
 ('CRDO', "+22.6%; results Dec 1.", "Pre-results run", "8-10% daily swings", (-7,0.3,7), 'Speculative', 'Momentum'),
 ('SNDK', "Fell 7.4% while every other chip rose; no clear news found (RSI 29).", "Memory bounce", "More selling", (-7,0,7), 'Speculative', 'Outlier watch'),
]
P[('intraday','ai','SGX')] = [
 ('AWX.SI', "Rose 5.5% before the US chip rally.", "Next session: US chips +15-30%", "Gap fades", (-4,1.5,7), 'Medium', 'Gap-up watch'),
 ('558.SI', "Eased 0.6%; US equipment makers rose ~15%.", "Next session", "Follows US equipment", (-3,1,5), 'Medium', 'Catch-up'),
 ('E28.SI', "Eased 0.6% (RSI 25).", "Next session", "Thin trading", (-3,1,4), 'Speculative', 'Catch-up'),
 ('V03.SI', "Rose 0.6%.", "Next session", "Small range", (-2,0.5,2.5), 'Medium', 'Range'),
 ('5DD.SI', "Eased 0.9%.", "Next session", "Thin trading", (-3,0.5,3.5), 'Speculative', 'Catch-up'),
]

# ---------- Health ----------
P[('long','hc','US')] = [
 ('LLY', "Obesity-drug leader: revenue +39%, 5% off its high. Little analyst upside left, so the base case is modest. Not exposed to the Medicare Advantage audit rule.",
  "Orforglipron launch; Q4 results (Feb)", "Drug-price policy", (-16,8,25), 'High', 'Defensive growth'),
 ('ARGX', "argenx: revenue +52% from Vyvgart, 11% off its high, 22% analyst upside; low daily swings (2%).",
  "New indications in 2027", "Competition in myasthenia gravis", (-15,10,28), 'Medium', 'Growth leader'),
 ('MDGL', "Madrigal's liver drug Rezdiffra is growing fast (revenue +50%); 34% off its high with 73% analyst upside; +5% Monday.",
  "Script data; EU rollout", "Competition from GLP-1 drugs", (-22,20,45), 'Medium', 'Oversold growth'),
 ('VRTX', "Vertex: steady growth (+12%), 4% off its high, about 27x earnings; +4.6% Monday.",
  "Pain-drug launch; kidney data", "Valuation", (-14,9,22), 'Medium', 'Steady growth'),
 ('INSM', "Insmed is up 21% in five days on a report that Sanofi is weighing a bid (unconfirmed). Revenue +268% from its lung drug, but RSI 84 now.",
  "Takeover talks; Brinsupri launch numbers", "No deal: the jump fades", (-28,10,32), 'Medium', 'Takeover candidate'),
]
P[('long','hc','SGX')] = [
 ('Q0F.SI', "IHH runs hospitals across Asia; analysts see 36% upside; eased 1.6% ahead of results.", "Q3 results Nov 25", "Currency swings", (-12,11,24), 'Medium', 'Regional leader'),
 ('C2PU.SI', "Parkway Life REIT: steady hospital and nursing-home rents, 8% off its high.", "Dividend", "US rates (10-yr ~4.9%)", (-8,7,15), 'High', 'Income'),
 ('AP4.SI', "Riverstone: Q3 revenue at a 3-year high (profit +35%); about 14x earnings with 24% analyst upside. Up 1.4% this week.", "New CEO from Dec 1", "Glove price competition", (-15,10,26), 'Medium', 'Value with momentum'),
 ('BSL.SI', "Raffles Medical: Singapore hospital group, 24% off its high, steady (RSI 50).", "Results (Feb)", "Shrinking revenue (-7%)", (-10,8,18), 'Medium', 'Recovery'),
 ('H02.SI', "Haw Par (Tiger Balm) trades near 9x earnings with a large cash and investment pile; 34% off its high (RSI 21).", "Results (Feb)", "Revenue down 8%", (-12,6,16), 'Medium', 'Value'),
]
P[('swing','hc','US')] = [
 ('LLY', "Near its high; defensive if the rally fades.", "Orforglipron news", "Rotation into tech", (-8,3,10), 'High', 'Defensive'),
 ('ARGX', "RSI 59, 11% off its high; steady through the slide.", "Momentum", "Biotech risk-off", (-7,3,9), 'Medium', 'Relative strength'),
 ('MDGL', "RSI 51, rose 5% Monday; 73% analyst upside.", "Script data", "Biotech risk-off", (-12,6,18), 'Medium', 'Rebound'),
 ('UNH', "Down 18% in five days on the CMS audit proposal and fell again Monday while the market jumped (RSI 25); about 14x forward earnings. Still only a proposal.",
  "2027 outlook; comments to Jan 19", "Rule finalised as written", (-15,4,18), 'Speculative', 'Policy-shock rebound'),
 ('VKTX', "Viking rose 12% Monday (RSI 55), up 14% in a month; no specific news found.", "Obesity-drug data", "Biotech swings", (-18,5,20), 'Speculative', 'Momentum'),
]
P[('intraday','hc','US')] = [
 ('VKTX', "Up 12%.", "Momentum", "Profit-taking", (-6,0.3,6), 'Speculative', 'Momentum'),
 ('CRSP', "Up 10.8%.", "Gene-editing rally", "Profit-taking", (-5,0.3,5), 'Speculative', 'Momentum'),
 ('UNH', "Fell 1% on a +4.7% day (RSI 25).", "Dip buying", "More insurer selling", (-4,0.3,4), 'Speculative', 'Bounce watch'),
 ('INSM', "RSI 84 on takeover talk.", "Deal news", "Profit-taking", (-6,0,6), 'Speculative', 'Event-driven'),
 ('LLY', "Up 1.5%.", "Defensive bid", "Rotation", (-2.3,0.2,2.3), 'Medium', 'Range'),
]
P[('swing','hc','SGX')] = [
 ('Q0F.SI', "IHH (RSI 46) reports Q3 Nov 25.", "Q3 results Nov 25", "Results miss", (-6,3,9), 'Medium', 'Pre-earnings'),
 ('AP4.SI', "Riverstone up 1.4% this week (RSI 53).", "New CEO Dec 1", "Glove prices", (-8,4,11), 'Medium', 'Post-results momentum'),
 ('C2PU.SI', "Parkway Life REIT: lowest-volatility name in the group.", "Dividend", "Rates", (-4,2,6), 'High', 'Range'),
 ('BSL.SI', "Raffles Medical flat over the month (RSI 50).", "Support", "Low volume", (-5,2,6), 'Medium', 'Range'),
 ('QC7.SI', "Q&M Dental rose 2.4% after scrapping the EM2AI stake deal (RSI 18).", "Bounce", "Small cap", (-8,3,10), 'Speculative', 'Oversold rebound'),
]
P[('intraday','hc','SGX')] = [
 ('Q0F.SI', "Eased 1.6% before results.", "Next session; Q3 results Nov 25", "Results reaction", (-3,0.3,3), 'Medium', 'Pre-earnings'),
 ('QC7.SI', "Rose 2.4% after dropping the EM2AI deal.", "Next session", "Thin trading", (-3,0.3,3), 'Speculative', 'Follow-through check'),
 ('AP4.SI', "Eased 2.6%.", "Next session", "Glove prices", (-3,0.3,3), 'Medium', 'Dip watch'),
 ('C2PU.SI', "Flat.", "Next session", "Small range", (-1,0.2,1), 'Medium', 'Range'),
 ('BSL.SI', "Eased 0.6%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
]

# ---------- Finance ----------
P[('long','fin','US')] = [
 ('JPM', "Best-run US bank, 13% off its high at about 12.4x forward earnings. Higher rates support interest income.", "Q4 results Jan 14", "Credit cycle; market swings", (-15,8,22), 'High', 'Core holding'),
 ('GS', "About 11x forward earnings, 28% off its high; led Anthropic's record IPO and gains from volatile trading.",
  "Deal fees; Q4 results Jan 19", "Volatility hits deals", (-20,11,28), 'Medium', 'Cyclical value'),
 ('V', "Visa: steady growth (+13%), 6% off its high; little AI exposure.", "Holiday spending", "Card-fee regulation", (-12,6,18), 'High', 'Defensive growth'),
 ('NU', "Nubank: revenue +34% at about 11x forward earnings, 37% off its high; 48% analyst upside.", "Q4 results (Feb)", "Brazil credit; strong dollar", (-30,16,48), 'Medium', 'Growth at a discount'),
 ('SE', "Sea: revenue +43%; $1B buyback. About 14x forward earnings, 54% off its high.",
  "Q4 results (Mar)", "Credit costs at Monee; competition", (-30,18,50), 'Medium', 'Oversold growth'),
]
P[('long','fin','SGX')] = [
 ('D05.SI', "DBS kept its 81-cent quarterly dividend and says interest income has bottomed; 16% off its high (RSI 21).",
  "Q4 results Feb", "Margins if rates fall; stronger SGD", (-10,8,16), 'High', 'Income leader'),
 ('O39.SI', "OCBC was the only local bank to beat in Q3 and raised loan-growth guidance.",
  "Q4 results (Feb)", "Margin squeeze", (-10,7,15), 'Medium', 'Income'),
 ('U11.SI', "UOB missed Q3 and cut its margin guidance; RSI 12, 22% off its high.", "Fee recovery", "More credit provisions", (-12,7,17), 'Medium', 'Oversold income'),
 ('AIY.SI', "iFAST: fintech platform, revenue +23%, 34% off its high with 57% analyst upside; +1.5% Monday.", "HK pension business", "Market-driven volumes", (-18,16,36), 'Medium', 'Growth'),
 ('S68.SI', "SGX benefits from high trading volumes; from Jan 2027 its RegCo takes over IPO prospectus reviews.", "Monthly volume data", "Already priced (23x earnings)", (-12,7,18), 'Medium', 'Volatility winner'),
]
P[('swing','fin','US')] = [
 ('SCHW', "Schwab RSI 60, flat over five days while banks fell; about 12x forward earnings.", "Monthly client metrics", "Market swings", (-8,3,10), 'Medium', 'Relative strength'),
 ('IBKR', "Interactive Brokers +7.4% Monday; volatile markets lift trading income.", "Monthly metrics (early Dec)", "Volumes cool", (-10,4,13), 'Medium', 'Volatility winner'),
 ('GS', "RSI 39 after a 7.6% five-day drop; rose 4.2% Monday.", "Deal fees", "Volatility", (-9,4,12), 'Medium', 'Rebound'),
 ('MA', "Mastercard 5.5% off its high (RSI 45).", "Holiday spending data", "Rotation into tech", (-6,2,7), 'High', 'Steady'),
 ('HOOD', "+8.4% Monday (RSI 31); retail trading lifts with the rally.", "Retail volumes", "Crypto weakness", (-18,6,24), 'Speculative', 'Oversold rebound'),
]
P[('swing','fin','SGX')] = [
 ('D05.SI', "DBS oversold (RSI 21).", "Dividend support", "Margin worries", (-4,3,7), 'High', 'Oversold income'),
 ('U11.SI', "UOB RSI 12.", "Rebound", "Further downgrades", (-5,3,8), 'Medium', 'Oversold rebound'),
 ('O39.SI', "OCBC RSI 28.", "Post-results recovery", "Margin squeeze", (-4,2,6), 'Medium', 'Pullback'),
 ('S68.SI', "SGX fell 3.1% Friday; volatile markets lift volumes.", "Volume data", "Valuation", (-5,3,8), 'Medium', 'Volatility winner'),
 ('AIY.SI', "iFAST RSI 36 after a 9% five-day drop.", "Rebound", "Market-driven", (-8,3,10), 'Medium', 'Oversold rebound'),
]
P[('intraday','fin','US')] = [
 ('HOOD', "Up 8.4%.", "Retail volumes", "Crypto weakness", (-5,0.4,5), 'Speculative', 'Momentum'),
 ('KLAR', "Up 8.6%.", "Bounce", "Credit worries", (-5,0.3,5), 'Speculative', 'Momentum'),
 ('COIN', "Up 6.7% (RSI 25); bitcoin ~$61k.", "Crypto bounce", "Bitcoin weak", (-5,0,5), 'Speculative', 'Crypto beta'),
 ('IBKR', "Up 7.4%.", "Volumes", "Profit-taking", (-3.5,0.3,3.5), 'Medium', 'Momentum'),
 ('JPM', "Up 2% (RSI 38).", "Dip buying", "Bank lag", (-2,0.2,2), 'Medium', 'Range'),
]
P[('intraday','fin','SGX')] = [
 ('D05.SI', "Eased 0.6% (RSI 21).", "Next session: US +4.7%", "Trend down", (-1.3,0.4,1.6), 'High', 'Bounce watch'),
 ('U11.SI', "Eased 0.9% (RSI 12).", "Next session", "Trend down", (-1.5,0.4,1.8), 'Medium', 'Bounce watch'),
 ('S68.SI', "Up 0.2%.", "Next session", "Small range", (-1.3,0.3,1.5), 'Medium', 'Range'),
 ('AIY.SI', "Up 1.5%.", "Next session", "Market-driven", (-2.5,0.4,3), 'Medium', 'Momentum'),
 ('O39.SI', "Eased 0.5%.", "Next session", "Small range", (-1.3,0.3,1.5), 'Medium', 'Range'),
]

# IPO tab (6-month view), all markets
P[('ipo','all','US')] = [
 ('SPCX', "SpaceX (IPO $135) is back near its IPO price, 37% under its high; +4.2% Monday as Jefferies started at Buy ($210 target).",
  "Starship progress; lock-up expiries", "Valuation and Musk headlines", (-35,14,45), 'Medium', 'Mega-cap IPO'),
 ('CHYM', "Chime (IPO $27) trades about 18% above its IPO price, 7.5% off its high (RSI 66).",
  "Member growth", "Fintech credit cycle", (-18,8,25), 'Medium', 'Post-IPO uptrend'),
 ('KLAR', "Klarna (IPO $40) is about $13, 67% below its IPO price at about 18x forward earnings; +8.6% Monday.",
  "Holiday volumes; Q4 results Feb 18", "Buy-now-pay-later credit losses", (-30,12,40), 'Speculative', 'Deep value'),
 ('ACCV', "Accelevation (IPO $18) makes electrical gear for data centres: revenue +66% at about 9x forward earnings, 40% below its IPO price; +12% Monday.",
  "Order updates", "Data-centre slowdown; 9% daily swings", (-40,10,50), 'Speculative', 'Post-IPO value'),
 ('ASBH', "American Savings Bank (IPO $16) is up 22% since listing with low swings for a new stock (RSI 52).",
  "Q4 results", "Bank-sector selling", (-12,5,15), 'Medium', 'Steady post-IPO'),
]

# ---------- Power & grid (data-center power) ----------
P[('long','pwr','US')] = [
 ('GEV', "GE Vernova: gas turbines and grid gear sold out for years, revenue +27%. 36% off its high with 54% analyst upside.", "Q4 results Jan 27", "Data-centre policy; valuation (29x)", (-25,15,40), 'High', 'Quality at a discount'),
 ('CEG', "Constellation beat Q3 and raised 2026 guidance; 34% off its high.", "New long-term power deals", "Data-centre politics; PJM rules", (-22,13,32), 'High', 'Beat and raise'),
 ('PWR', "Quanta builds the grid: revenue +57%, 22% off its high, up 11.5% in a month.", "Utility capex plans", "Data-centre policy", (-25,12,34), 'Medium', 'Grid builder'),
 ('ETN', "Eaton: electrical gear for data centres and utilities, 27% off its high at about 20x earnings.", "Q4 results Feb 2", "Data-centre orders slowing", (-20,13,33), 'Medium', 'Quality at a discount'),
 ('VRT', "Vertiv: data-centre cooling and power, revenue +61% at about 19x forward earnings, 50% off its high; +12% Monday.", "Order backlog updates", "Most exposed to a data-centre slowdown", (-35,18,52), 'Medium', 'Oversold growth'),
]
P[('long','pwr','SGX')] = [
 ('BN4.SI', "Keppel: power, data centres and asset management, about 15x earnings with 44% analyst upside (RSI 24).", "Asset sales", "Execution; SG data-centre chip rule", (-13,12,25), 'Medium', 'Value'),
 ('U96.SI', "Sembcorp: power and renewables at about 9x earnings.", "New contracts", "Power prices", (-12,7,18), 'Medium', 'Value'),
 ('DCRU.SI', "Digital Core REIT: US data-centre REIT, about 9x earnings with 59% analyst upside.", "Leasing news", "Tenant concentration; US rates", (-14,11,27), 'Medium', 'Deep value'),
 ('AJBU.SI', "Keppel DC REIT: data-centre rents, 13% off its high (RSI 45).", "Dividend", "Rates", (-10,7,17), 'Medium', 'Income'),
 ('544.SI', "CSE Global: electrification and data-centre work, about 9x earnings, 58% off its high; +7.1% Monday.", "New orders", "Small and volatile", (-30,14,45), 'Speculative', 'Recovery'),
]
P[('swing','pwr','US')] = [
 ('TLN', "Talen RSI 52, up 11% in a month; about 11x forward earnings.", "Capacity deals", "Data-centre politics", (-13,5,16), 'Medium', 'Relative strength'),
 ('PWR', "Quanta up 11.5% in a month; the steadiest name in AI power.", "Utility capex", "Data-centre policy", (-10,4,13), 'Medium', 'Trend'),
 ('VRT', "Vertiv +12% Monday; RSI still 36.", "AI hardware rebound", "Rally fades", (-15,6,20), 'Medium', 'Oversold rebound'),
 ('GEV', "GE Vernova RSI 33 even after +8%.", "Order news", "AI capex fears", (-14,6,20), 'Medium', 'Oversold rebound'),
 ('NRG', "NRG up 4% in five days and 6% in a month (RSI 51).", "Data-centre deals", "Power prices", (-12,5,15), 'Medium', 'Relative strength'),
]
P[('swing','pwr','SGX')] = [
 ('BN4.SI', "Keppel RSI 24 after a 3.1% drop Friday.", "Asset-sale news", "Execution", (-6,3,9), 'Medium', 'Oversold rebound'),
 ('544.SI', "CSE Global +7.1% Monday.", "New orders", "No floor yet", (-15,4,16), 'Speculative', 'Base building'),
 ('AJBU.SI', "Keppel DC REIT up 2% in a month (RSI 45).", "Support", "Rates", (-5,1.5,6), 'Medium', 'Range'),
 ('U96.SI', "Sembcorp RSI 31.", "Contracts", "Power prices", (-5,2,7), 'Medium', 'Oversold'),
 ('DCRU.SI', "Digital Core REIT RSI 42.", "Support", "US data-centre worries", (-7,2,8), 'Medium', 'Range'),
]
P[('intraday','pwr','US')] = [
 ('BE', "Up 18%.", "AI power momentum", "8-9% daily swings", (-7,0.3,7), 'Speculative', 'Momentum'),
 ('VRT', "Up 12%.", "AI hardware momentum", "Profit-taking", (-5,0.3,5), 'Medium', 'Momentum'),
 ('NRG', "Up 11%.", "Momentum", "Profit-taking", (-4,0.3,4), 'Medium', 'Momentum'),
 ('GEV', "Up 8% (RSI 33).", "Catch-up", "Rally fades", (-4,0.3,4), 'Medium', 'Rebound'),
 ('NEE', "Up 0.7%; lagged the rally.", "Defensive bid", "Rotation to tech", (-1.8,0.2,1.8), 'Medium', 'Range'),
]
P[('intraday','pwr','SGX')] = [
 ('544.SI', "Rose 7.1%.", "Next session", "Small cap", (-4,0.3,4), 'Speculative', 'Follow-through check'),
 ('BN4.SI', "Eased 0.3% (RSI 24).", "Next session: US +4.7%", "More selling", (-1.8,0.4,2.2), 'Medium', 'Bounce watch'),
 ('U96.SI', "Flat.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('AJBU.SI', "Eased 1.4%.", "Next session", "Small range", (-1.2,0.2,1.2), 'Medium', 'Range'),
 ('DCRU.SI', "Flat.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
]

# ---------- Defence & industrials ----------
P[('long','def','US')] = [
 ('GE', "GE Aerospace: jet-engine services boom, revenue +16%, 16% off its high; up 12.5% in a month.", "Q4 results Jan 21", "Valuation (34x)", (-15,10,26), 'High', 'Quality'),
 ('RTX', "RTX: missiles and engines, revenue +11%, steady; 17% analyst upside.", "Q4 results Jan 26", "Engine issues", (-12,10,24), 'High', 'Core defence'),
 ('HWM', "Howmet: jet-engine parts, revenue +29%, 26% off its high with 36% analyst upside; up 17% in a month.", "Aerospace build rates", "Valuation (33x)", (-20,14,34), 'Medium', 'Growth at a discount'),
 ('LHX', "L3Harris: space and missile sensors, 33% off its high, 31% analyst upside.", "Golden Dome contracts", "Budget fights", (-15,12,30), 'Medium', 'Value'),
 ('NOC', "Northrop: B-21 and missile defence, about 18x earnings, 29% off its high.", "Golden Dome contracts", "Budget fights", (-15,10,27), 'Medium', 'Value'),
]
P[('long','def','SGX')] = [
 ('S63.SI', "ST Engineering: record S$37.7B order book and nine-month revenue +10%; 26% off its high (RSI 25) with 35% analyst upside.", "Contract wins; FY results (Feb)", "Valuation (22x)", (-12,12,26), 'High', 'Quality on a dip'),
 ('BS6.SI', "Yangzijiang Shipbuilding: about 7x earnings, revenue +36%; 18% off its high.", "New ship orders", "US port fees on Chinese ships", (-18,14,32), 'Medium', 'Value'),
 ('S59.SI', "SIA Engineering: aircraft maintenance, 26% off its high, 35% analyst upside.", "Air travel", "Revenue falling (-11%)", (-10,10,24), 'Medium', 'Recovery'),
 ('C52.SI', "ComfortDelGro: steady transport earnings at about 13x.", "Overseas contracts", "Slow growth", (-8,7,15), 'Medium', 'Steady'),
 ('H22.SI', "Hong Leong Asia: engines and building materials at about 7x earnings, 55% off its high; fell 6% Monday (RSI 17).", "Results (Feb)", "China demand; no floor yet", (-28,18,50), 'Speculative', 'Deep value'),
]
P[('swing','def','US')] = [
 ('HWM', "Howmet up 17% in a month (RSI 47).", "Aerospace data", "Valuation", (-8,4,11), 'Medium', 'Relative strength'),
 ('GE', "GE up 12.5% in a month (RSI 50).", "Aftermarket demand", "Valuation", (-7,3,9), 'Medium', 'Trend'),
 ('CAT', "Caterpillar +7% Monday (RSI 37), 49% off its high; data-centre generators ride the AI rebound.", "Dealer data", "AI capex fears return", (-12,6,16), 'Medium', 'Oversold rebound'),
 ('AXON', "Axon RSI 25 after a 27% one-month drop; 76% analyst upside; +5.7% Monday.", "Analyst updates", "More downgrades", (-18,6,22), 'Speculative', 'Post-earnings rebound'),
 ('BA', "Boeing 36% off its high (RSI 35); production recovering.", "Monthly deliveries", "Quality issues", (-10,5,15), 'Medium', 'Recovery'),
]
P[('swing','def','SGX')] = [
 ('S63.SI', "ST Engineering RSI 25 after a 5% five-day drop.", "Contract wins", "Holder selling", (-6,4,10), 'Medium', 'Oversold rebound'),
 ('BS6.SI', "Yangzijiang rose 0.5% Monday (RSI 40).", "Orders", "Trade fees", (-8,4,12), 'Medium', 'Support'),
 ('S59.SI', "SIA Engineering RSI 22.", "Air travel", "Slow growth", (-6,2,7), 'Medium', 'Oversold'),
 ('C52.SI', "ComfortDelGro RSI 29.", "Support", "Slow growth", (-4,1.5,5), 'Medium', 'Range'),
 ('H22.SI', "Hong Leong Asia RSI 17 after a 30% one-month drop.", "Bounce", "China demand", (-12,4,14), 'Speculative', 'Oversold, falling'),
]
P[('intraday','def','US')] = [
 ('CAT', "Up 7.3%.", "Momentum", "Profit-taking", (-3.5,0.3,3.5), 'Medium', 'Momentum'),
 ('KTOS', "Up 6% (RSI 24).", "Drone contracts", "Volatile", (-4.5,0.2,4.5), 'Speculative', 'Bounce'),
 ('AXON', "Up 5.7% (RSI 25).", "Bounce", "Gives back gains", (-4,0.3,4), 'Speculative', 'Bounce'),
 ('AVAV', "Up 4.5%; results Dec 2 (RSI 32).", "Pre-results", "Volatile", (-5,0.2,5), 'Speculative', 'Pre-earnings'),
 ('LMT', "Up 1.1%; lagged the rally (RSI 31).", "Defensive bid", "Rotation to tech", (-2,0.2,2), 'Medium', 'Range'),
]
P[('intraday','def','SGX')] = [
 ('S63.SI', "Eased 1.2% (RSI 25).", "Next session: US +4.7%", "Trend down", (-2.5,0.5,3), 'Medium', 'Bounce watch'),
 ('BS6.SI', "Rose 0.5%.", "Next session", "Small range", (-2.5,0.3,2.5), 'Medium', 'Range'),
 ('C52.SI', "Eased 2.5%.", "Next session", "Small range", (-1.5,0.3,1.5), 'Medium', 'Bounce watch'),
 ('S59.SI', "Eased 0.7% (RSI 22).", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Bounce watch'),
 ('H22.SI', "Fell 6% (RSI 17).", "Next session", "More selling", (-4,0.3,4), 'Speculative', 'Bounce watch'),
]

# ---------- Energy (oil and gas) ----------
P[('long','nrg','US')] = [
 ('CVX', "Chevron: revenue +35%, about 12.5x earnings, 12% off its high (RSI 27). Fell 1% as WTI dropped 3% to ~$81.", "Hess integration; buybacks", "Oil keeps falling", (-16,8,24), 'High', 'Core energy'),
 ('XOM', "Exxon: steady cash flow, about 12.6x earnings, 17% analyst upside (RSI 22).", "Buybacks", "Oil price drop", (-15,7,21), 'High', 'Core energy'),
 ('LNG', "Cheniere: US gas exports on long contracts; less tied to oil. 11% off its high, flat Monday while oil fell.", "New export capacity", "Gas price swings", (-15,8,24), 'Medium', 'Steady'),
 ('FANG', "Diamondback: low-cost Permian producer at about 8x earnings, 38% analyst upside (RSI 24).", "Buybacks", "Oil price drop", (-22,12,32), 'Medium', 'Value'),
 ('EOG', "EOG: about 8.5x earnings, revenue +43%, 12% off its high.", "Buybacks", "Oil price drop", (-16,7,22), 'Medium', 'Value'),
]
P[('long','nrg','SGX')] = [
 ('5E2.SI', "Seatrium builds offshore rigs and wind platforms; 55% analyst upside after an 8.8% fall Friday.", "New orders", "Contract delays", (-15,12,28), 'Medium', 'Recovery'),
 ('BN4.SI', "Keppel: energy infrastructure and asset management.", "Asset sales", "Execution", (-13,10,22), 'Medium', 'Value'),
 ('RE4.SI', "Geo Energy: up 20% in five days after saying there was no new Indonesian mining directive; about 6x earnings.", "Q3 update", "Indonesian policy risk", (-35,8,40), 'Speculative', 'Rebound'),
 ('5LY.SI', "Marco Polo Marine fell 9.5% after guiding to lower FY profit; offshore vessels at about 8x earnings.", "FY results", "Profit falling; thin trading", (-30,5,30), 'Speculative', 'Broken growth'),
 ('5WH.SI', "Rex International is in a long downtrend (-69% this year); no setup.", "None", "Further losses", (-30,-5,20), 'Speculative', 'Avoid'),
]
P[('swing','nrg','US')] = [
 ('LNG', "Cheniere RSI 40; gas exports, not crude.", "Export capacity", "Gas price swings", (-8,3,10), 'Medium', 'Relative strength'),
 ('SLB', "SLB rose 0.6% while oil fell 3% (RSI 24).", "Service pricing", "Oil price drop", (-10,4,12), 'Medium', 'Oversold rebound'),
 ('FANG', "Diamondback oversold (RSI 24).", "Buybacks", "Oil price drop", (-11,4,13), 'Medium', 'Oversold rebound'),
 ('HAL', "Halliburton flat on an oil down day (RSI 29).", "Service pricing", "Oil price drop", (-10,4,12), 'Medium', 'Oversold rebound'),
 ('CVX', "Chevron RSI 27.", "Buybacks", "More oil weakness", (-8,3,9), 'Medium', 'Oversold'),
]
P[('intraday','nrg','US')] = [
 ('SLB', "Up 0.6% while oil fell.", "Relative strength", "Oil weakness", (-2.5,0.2,2.5), 'Medium', 'Relative strength'),
 ('LNG', "Up 0.2%.", "Gas exports", "Small range", (-2.5,0.2,2.5), 'Medium', 'Range'),
 ('XOM', "Fell 1.9% (RSI 22).", "Dip buying", "Oil keeps falling", (-2,0.2,2), 'Medium', 'Bounce watch'),
 ('MPC', "Fell 2.6% (RSI 27).", "Refining margins", "Oil weakness", (-3,0.2,3), 'Speculative', 'Bounce watch'),
 ('COP', "Fell 2.9%.", "Oil bounce", "Oil keeps falling", (-2.5,0.2,2.5), 'Speculative', 'Bounce watch'),
]
P[('swing','nrg','SGX')] = [
 ('5E2.SI', "Seatrium RSI 25 after a 13% five-day drop.", "Orders", "Delays", (-8,4,12), 'Medium', 'Oversold rebound'),
 ('BN4.SI', "Keppel RSI 24.", "Asset sales", "Execution", (-6,3,9), 'Medium', 'Oversold rebound'),
 ('RE4.SI', "Geo Energy eased 1.1% after a 20% weekly gain.", "Follow-through", "Bounce fades", (-25,3,25), 'Speculative', 'Rebound'),
 ('5LY.SI', "Marco Polo Marine fell 9.5% on profit guidance.", "Results detail", "More selling", (-15,2,15), 'Speculative', 'Post-warning'),
 ('5WH.SI', "Rex International: no setup.", "None", "Further losses", (-12,-2,8), 'Speculative', 'Avoid'),
]
P[('intraday','nrg','SGX')] = [
 ('5E2.SI', "Eased 1.9% (RSI 25).", "Next session", "Oil weakness", (-2.5,0.3,2.5), 'Medium', 'Bounce watch'),
 ('BN4.SI', "Eased 0.3%.", "Next session: US +4.7%", "Small range", (-1.8,0.4,2.2), 'Medium', 'Bounce watch'),
 ('RE4.SI', "Eased 1.1%.", "Next session", "Bounce fades", (-6,0.3,6), 'Speculative', 'Range'),
 ('5LY.SI', "Fell 9.5% on lower profit guidance.", "Next session", "More selling", (-6,0,6), 'Speculative', 'Post-warning'),
 ('5WH.SI', "Penny stock in a downtrend; avoid.", "None", "Further losses", (-5,-1,4), 'Speculative', 'Avoid'),
]

IPO_LIST = [
 # sym, name, ipo_date, ipo_price, sector, status
 ('ANT','Anthropic (Nasdaq: ANT; priced $83, record ~$81B raised; day one $97.17, Fri $88.91, Mon ~$87.6; 303M more insider shares unlock Dec 15)','2026-11-19',83.00,'ai','Listed'),
 ('BIAI','Bitari (not confirmed)','2026-11-30',7.00,'ai','Expected'),
 ('ABGC','American Barrick Gold (Barrick carve-out; ~$6B est.; filed week of Nov 9)','2026-11-13',None,'nrg','Filed'),
 ('RZRA','Rezera ($11-13 range; ~$200M; postponed, still on calendars)','2026-11-12',None,'hc','Postponed'),
 ('VVVV','vVardis (dental tech; NYSE; priced below range, -8% on day one)','2026-11-13',18.00,'hc','Listed'),
 ('WWB','Windward Bio (Nasdaq; priced at midpoint, +68% on day one)','2026-11-13',17.00,'hc','Listed'),
 ('AGLT','Agility Robotics (merger listing with Churchill Capital XI)','2026-11-05',None,'ai','Expected'),
 ('LYCA','Lycia Therapeutics','2026-10-23',18.00,'hc','Listed'),
 ('CTY','City Therapeutics','2026-10-16',18.00,'hc','Listed'),
 ('AMRO','Amaero','2026-10-15',4.25,'ai','Listed'),
 ('IAM','Iambic Therapeutics','2026-10-15',16.00,'hc','Listed'),
 ('RTSN','Retension Pharmaceuticals','2026-10-09',12.00,'hc','Listed'),
 ('TRXB','TRex Bio','2026-10-09',14.00,'hc','Listed'),
 ('ACCV','Accelevation Holdings','2026-09-30',18.00,'ai','Listed'),
 ('ADRX','ADARx Pharmaceuticals','2026-09-25',17.00,'hc','Listed'),
 ('ETRA','Electra Therapeutics','2026-09-18',15.00,'hc','Listed'),
 ('OIG','Orion180 Insurance Group','2026-09-18',12.00,'fin','Listed'),
 ('ASBH','American Savings Bank','2026-09-16',16.00,'fin','Listed'),
 ('SPCX','SpaceX','2026-06-12',135.00,'ai','Listed'),
 ('KLAR','Klarna','2025-09-10',40.00,'fin','Listed'),
 ('FIG','Figma','2025-07-31',33.00,'ai','Listed'),
 ('CHYM','Chime','2025-06-12',27.00,'fin','Listed'),
 ('CRCL','Circle','2025-06-05',31.00,'fin','Listed'),
 ('CRWV','CoreWeave','2025-03-28',40.00,'ai','Listed'),
]

SERENITY = {'NVDA','SPCX','AXTI','LITE','COHR','NBIS','MU','AVGO','AAOI','AEHR','GLW','SNDK','POET','IREN','TSEM','MRVL','AMD','ARM','INTC','TSM','CRDO'}

X_POSTS = [
 ('2026-11-20T18:50','', "Via digest: flags an industry-group warning that printed-circuit-board shortages will hit auto, medical and defence makers, with relief unlikely before mid-2028."),
 ('2026-11-20T13:00','', "Via digest: says ordinary insurers and banks are now buying their own GPU systems to run open-weight AI models."),
 ('2026-11-20T04:20','SNDK', "Via search snippet: argues the market is misreading Chinese enterprise-SSD cuts as weak demand and NAND oversupply, citing Phison's CEO on the SanDisk/Kioxia selloff."),
 ('2026-11-19T20:00','COHR', "Via tracker: says Coherent announced a new $2B buyback and argues optical stocks are undervalued, pointing to its ~$20B long-term deals."),
 ('2026-11-19T19:00','ANT', "Via tracker: notes Anthropic's day-one valuation was well above Meta's."),
 ('2026-11-19T18:00','SOI', "Via tracker: says Soitec's photonics pipeline jumped from about $25M to about $1.2B in agreements, citing strong optics demand."),
 ('2026-11-18T22:00','', "On X: cites Goldman prime data: hedge-fund momentum exposure fell from ~60% to 8%, with the heaviest tech selling in nine years before Nov 13."),
 ('2026-11-18T21:00','SNDK BE', "On X: says Leopold Aschenbrenner's early AI picks (SanDisk to Bloom Energy) were right and sees MLCC capacitors as a 2027 bottleneck, but warns leverage and crowded longs hurt."),
 ('2026-11-18T18:00','AVGO MU AMD CRWV IREN', "Via tracker: lists ~$900B of Anthropic purchase agreements with chip and cloud suppliers and argues the IPO helps semis."),
 ('2026-11-18T15:00','NVDA', "Via tracker: shares a Semafor report that part of Nvidia's board wanted Jensen Huang back as CEO - which happened on Nov 23."),
 ('2026-11-17T23:34','NVDA MU', "On X: reads Nvidia's call as 'demand far exceeds supply'; supply commitments rose from $279B to $390B, mostly multi-year memory buying."),
]

EVENTS = [
 ('2026-11-20','Macro','S&P -3.7% to 6,910, Nasdaq -5.3%, Dow -1.9%', "S&P and Dow close in correction. NVDA -14%, MU -14%, AMD -13%, AVGO -12%, TSM -9.5%. Bitcoin below $59k. UMich sentiment 51.5. Fed's Cook warns against waiting to hike."),
 ('2026-11-20','IPO','Anthropic -8.5% to $88.91 on day two', "Still above the $83 IPO price. 2x Anthropic ETFs from Tradr were due to start Nov 23. DayOne Data Centers put its US IPO on hold (reported)."),
 ('2026-11-20','SGX','STI -2.05% to 4,975.17', "First close below 5,000 since June; week -4.9%. Seatrium -8.8%, SATS -5.3%, Venture -3.3%, SGX -3.1%, Keppel -3.1%."),
 ('2026-11-23','AI','Nvidia reinstates Jensen Huang as CEO', "Unanimous board vote; an independent-director probe continues. NVDA +31.5% to ~$165, adding nearly $1T. Chips +10-25%; SanDisk fell 7%."),
 ('2026-11-23','Macro','S&P +4.7% to 7,238, Nasdaq +6.5% to 24,090, Dow ~+3%', "Best day since April 2025. VIX ~27. 10-yr 4.94%, dollar at a 19-month high, WTI ~$80.8 (-3%), gold +4%. Markets price ~91% odds of a Dec 9 hike."),
 ('2026-11-23','Deals','CrowdStrike to buy Zscaler (~$43.9B, all stock)', "1.135 CRWD shares per ZS share; ZS +16%, CRWD -10%. Applied Digital +23% on a ~$5.4B lease. Jefferies starts SpaceX at Buy ($210)."),
 ('2026-11-23','SGX','STI -0.43% to 4,953.81', "Closed before the US rally. Marco Polo Marine -9.5% on lower FY profit guidance; AEM +5.5%, CSE Global +7.1%. October core inflation eased to 1.5%."),
 ('2026-11-24','Earnings','Thanksgiving-week results', "Dell, HP, Workday and Deere report this week; HPE and Zoom reported after Monday's close."),
 ('2026-11-25','Macro','October PCE inflation; Q3 GDP second estimate', "First GDP estimate was 3.4%. Key input for the Dec 9 Fed decision."),
 ('2026-11-25','SGX','IHH Q3 results', "SIA goes ex-dividend (7 cents)."),
 ('2026-11-26','Macro','US Thanksgiving', "US stock market closed; early close (1pm ET) on Nov 27."),
 ('2026-11-26','AI','Sivers Semiconductors Q3 report', "On @aleabitoreddit's photonics watchlist."),
 ('2026-11-30','IPO','Bitari expected (not confirmed)', ""),
 ('2026-12-01','AI','Marvell and Credo results', ""),
 ('2026-12-02','Defence','AeroVironment results', ""),
 ('2026-12-09','Macro','Fed rate decision (Dec 8-9)', "A hike is widely expected. Broadcom reports the same day."),
 ('2026-12-10','AI','Ciena results; TSMC November sales', ""),
 ('2026-12-15','IPO','Anthropic lock-up: ~303M more insider shares', "Per the prospectus, as reported."),
 ('2026-12-17','AI','Micron FQ1 results (date per Yahoo)', "Earlier reports said Dec 23."),
]
