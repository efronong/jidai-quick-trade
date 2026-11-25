# Analyst picks for 2026-11-26 SGT (snapshot: US Wed Nov 25 ~2:30pm ET, SGX close Nov 25). Fields: sym, thesis, catalyst, risk, (low, base, high) % expected move, conviction, setup
# Horizons: long = 12 months, swing = ~4 weeks, intraday = rest of session (US) / next session (SGX), ipo = 6 months.
# US is closed Thu Nov 26 (Thanksgiving) and closes early (1pm ET) Fri Nov 27, so US intraday picks are for the Friday half-day.
# Context Wed Nov 25 (US close): S&P -0.25% to 7,182.78, Nasdaq -0.6% to 23,585.80, Dow +0.3% to 50,182.95, Russell 2000 +0.8%; VIX ~28.
# Stocks recovered most of a deep morning drop (Nasdaq was down ~4% at midday). October core PCE 3.3% y/y (3.2% expected), headline 3.8%;
# Q3 GDP revised up to 4.3%. December Fed hike odds ~98%. The administration proposed new tariffs of up to 20% on 14 trading partners
# (EU/Japan/Korea 15%, Vietnam 20%, Malaysia/Indonesia 18%); chips, autos and metals excluded; not before January.
# NVDA -3.9% to $149.30. SanDisk ~-6% (to ~$73) after TrendForce cut its NAND price outlook; ~-23% over two days
# (the snapshot shows -22.7% because its daily series is missing Tuesday's close). LRCX -6%, AMAT -5%, MU -5%. AXON +7%.
# Oil +2.5%; 10-yr 4.85% (-6bp); bitcoin ~$60k.
# SGX Wed: STI -0.6% to 4,930.83 as Asian chips caught up with Tuesday's US drop (Kospi -6.2%, Nikkei -2.8%).
# AEM -6.8%, Seatrium -4.2% (worst STI stock), banks lower (DBS -1.2%); Singtel +1.9% top STI gainer.
# Base cases discount analyst targets heavily: many targets were set before the November slide and look stale.
P = {}

# ---------- AI & chips ----------
P[('long','ai','US')] = [
 ('TSM', "Makes almost every leading AI chip, whoever designs it. Revenue +51% at about 15x forward earnings, 30% below its high. Chips are excluded from the new tariff proposal.",
  "November sales (~Dec 10); Q4 results Jan 14", "Taiwan geopolitics; US chip-access rules", (-20,15,36), 'High', 'Core holding'),
 ('NVDA', "Huang is back as CEO, but the stock has given back about 10% over two days to ~$149. About 9x forward earnings after revenue +103%; RSI 37.",
  "Estimate upgrades; CES and GTC news", "Board probe still open; export rules; AI-spending doubts", (-28,18,50), 'High', 'Leader, cheap'),
 ('AVGO', "Custom AI chips plus networking: revenue +86% at about 15x forward earnings, 38% off its high. Flat Wednesday while equipment names fell 5-6%.",
  "Q4 results Dec 9", "Lumpy custom-chip orders", (-24,16,42), 'High', 'Leader at a discount'),
 ('COHR', "Coherent: ~$20B multi-year optics deals and a $2B buyback; about 12.5x forward earnings. Rose 1.3% Wednesday while most chips fell.",
  "Buyback; FQ2 results (Feb)", "8-9% daily swings", (-35,17,55), 'Medium', 'Optics leader'),
 ('MU', "Memory is still the tightest part of AI servers: revenue +379% at about 3x forward earnings, 51% off its high. DRAM stays tight even as NAND prices soften.",
  "FQ1 results Dec 17", "TrendForce sees softer memory pricing in 2027; big swings", (-42,14,55), 'Medium', 'Cycle leader, more risk'),
]
P[('long','ai','SGX')] = [
 ('AWX.SI', "AEM fell 6.8% Wednesday as Asian chips caught up with the US drop (Kospi -6%). Still about 3x this year's start, 48% off its high at about 15x earnings.",
  "US chip read-across; FY results (Feb)", "One large customer; US chip rule for SG data centres", (-40,12,55), 'Medium', 'SGX AI leader'),
 ('V03.SI', "Venture: net cash, about 15x earnings, low volatility; analysts see about 35% upside. Fell 2.3% Wednesday.",
  "Analyst upgrades", "Slow revenue growth (+7%)", (-12,11,25), 'High', 'Steady value'),
 ('558.SI', "UMS makes precision parts for chip-equipment makers: revenue +61%, 46% off its high; -4.2% Wednesday.",
  "Chip-equipment spending outlook", "US equipment makers fell another 5-6% Wednesday", (-32,13,45), 'Medium', 'Equipment supplier'),
 ('5DD.SI', "Micro-Mechanics: revenue +45%, 43% off its high, about 18x earnings; steadier than peers (-2.2%).",
  "Q1 FY27 results", "Small and thinly traded", (-24,12,36), 'Medium', 'Growth at a discount'),
 ('E28.SI', "Frencken builds modules for chip and medical equipment; 57% off its high at about 13x earnings (RSI 29).",
  "Equipment recovery", "Flat revenue", (-26,10,36), 'Medium', 'Recovery'),
]
P[('swing','ai','US')] = [
 ('AVGO', "Held flat Wednesday while chip-equipment names fell 5-6%; results Dec 9 fall inside the window.",
  "Q4 results Dec 9", "Results disappoint", (-13,6,18), 'Medium', 'Into results'),
 ('TSM', "RSI 48; chips are excluded from the new tariffs.", "November sales ~Dec 10", "Chip selling spreads", (-11,5,15), 'Medium', 'Quality'),
 ('NVDA', "RSI 37 after giving back ~10% in two days; bought back off the $141 low Wednesday.", "Upgrades", "AI-spending doubts", (-15,6,20), 'Medium', 'Post-news base'),
 ('MRVL', "59% off its high (RSI 49); results Dec 1.", "Results Dec 1", "Guide disappoints", (-18,5,22), 'Speculative', 'Into results'),
 ('QCOM', "Qualcomm +2.4% Wednesday (RSI 58), up 6% in five days; about 14x forward earnings and less tied to AI spending.",
  "Phone-chip and PC news", "Phone demand; Apple modem loss", (-9,3,11), 'Medium', 'Relative strength'),
]
P[('swing','ai','SGX')] = [
 ('V03.SI', "Venture RSI 43; the steadiest name in the group.", "Analyst upgrades", "Low growth", (-6,3,9), 'High', 'Range'),
 ('AWX.SI', "AEM -6.8% Wednesday (RSI 37); down 27% in a month.", "Chip sentiment", "More chip selling", (-18,4,22), 'Medium', 'Pullback in uptrend'),
 ('558.SI', "UMS RSI 35 after a 26% one-month drop.", "Equipment read-across", "US equipment makers still falling", (-15,4,16), 'Medium', 'Oversold rebound'),
 ('5DD.SI', "Micro-Mechanics RSI 40.", "Results", "Thin trading", (-10,4,12), 'Medium', 'Support'),
 ('E28.SI', "Frencken RSI 29.", "Bounce", "Flat revenue", (-12,3,14), 'Speculative', 'Oversold rebound'),
]
P[('intraday','ai','US')] = [
 ('QCOM', "+2.4% Wednesday; one of few chips up.", "Friday half-day: relative strength", "Sector drag", (-2.5,0.2,2.5), 'Medium', 'Relative strength'),
 ('PLTR', "+2.1% (RSI 57).", "Friday half-day: momentum", "Valuation (65x)", (-3,0.2,3), 'Medium', 'Relative strength'),
 ('COHR', "+1.3% while chips fell.", "Friday half-day", "8-9% daily swings", (-4,0.2,4), 'Medium', 'Relative strength'),
 ('NVDA', "-3.9% to $149.30 but closed well off the $141 low.", "Friday half-day: dip buying", "More AI selling", (-4,0.3,4), 'Medium', 'Reversal watch'),
 ('SNDK', "About -6% Wednesday and -23% in two days (RSI 25) after TrendForce cut its NAND outlook.", "Friday half-day: capitulation bounce", "More NAND downgrades", (-7,0,7), 'Speculative', 'Washout watch'),
]
P[('intraday','ai','SGX')] = [
 ('V03.SI', "Fell 2.3%; low volatility.", "Next session", "Small range", (-2,0.2,2), 'Medium', 'Range'),
 ('5DD.SI', "Fell 2.2%.", "Next session", "Thin trading", (-3,0,3), 'Speculative', 'Range'),
 ('AWX.SI', "Fell 6.8%; US chips recovered off their lows after SGX closed.", "Next session: bounce", "US equipment makers fell 5-6%", (-5,0.3,5), 'Speculative', 'Bounce watch'),
 ('558.SI', "Fell 4.2%.", "Next session", "Follows US equipment", (-4,0,4), 'Speculative', 'Bounce watch'),
 ('E28.SI', "Fell 4.4% (RSI 29).", "Next session", "Thin trading", (-3,0,3), 'Speculative', 'Range'),
]

# ---------- Health ----------
P[('long','hc','US')] = [
 ('LLY', "Obesity-drug leader: revenue +39%, 3% off its high. Little analyst upside left, so the base case is modest.",
  "Orforglipron launch; Q4 results (Feb)", "Drug-price policy", (-16,8,25), 'High', 'Defensive growth'),
 ('ARGX', "argenx: revenue +52% from Vyvgart, 8% off its high, 18% analyst upside; low daily swings (2%).",
  "New indications in 2027", "Competition in myasthenia gravis", (-15,10,28), 'Medium', 'Growth leader'),
 ('MDGL', "Madrigal's liver drug Rezdiffra is growing fast (revenue +50%); 28% off its high with 59% analyst upside. Up 9% in five days as big pharma buys growth.",
  "Script data; EU rollout", "Competition from GLP-1 drugs", (-22,18,45), 'Medium', 'Takeover-era growth'),
 ('VRTX', "Vertex: steady growth (+12%), at its high, about 28x earnings.",
  "Pain-drug launch; kidney data", "Valuation", (-14,8,22), 'Medium', 'Steady growth'),
 ('MRK', "Merck: about 16x forward earnings, 10% off its high (RSI 39).",
  "Keytruda subcutaneous rollout", "Keytruda patent cliff (2028)", (-12,8,20), 'Medium', 'Value'),
]
P[('long','hc','SGX')] = [
 ('Q0F.SI', "IHH runs hospitals across Asia; analysts see 35% upside. Flat Wednesday ahead of Q3 results.", "Q3 results (Yahoo lists Nov 27)", "Currency swings", (-12,11,24), 'Medium', 'Regional leader'),
 ('C2PU.SI', "Parkway Life REIT: steady hospital and nursing-home rents, 8% off its high.", "Dividend", "US rates (10-yr ~4.85%)", (-8,7,15), 'High', 'Income'),
 ('AP4.SI', "Riverstone: Q3 revenue at a 3-year high; about 14.5x earnings with 19% analyst upside. Up 7% in a month (RSI 63).", "New CEO from Dec 1", "Glove price competition", (-15,9,24), 'Medium', 'Value with momentum'),
 ('BSL.SI', "Raffles Medical: Singapore hospital group, 22% off its high, steady (RSI 57).", "Results (Feb)", "Shrinking revenue (-7%)", (-10,8,18), 'Medium', 'Recovery'),
 ('H02.SI', "Haw Par (Tiger Balm) trades near 9.5x earnings with a large cash and investment pile; 34% off its high (RSI 26).", "Results (Feb)", "Revenue down 8%", (-12,6,16), 'Medium', 'Value'),
]
P[('swing','hc','US')] = [
 ('LLY', "Defensive leader while chips stay weak.", "Orforglipron news", "Rotation back into tech", (-8,3,10), 'High', 'Defensive'),
 ('MDGL', "RSI 61, up 9% in five days; 59% analyst upside.", "Script data; deal talk", "Biotech risk-off", (-12,5,18), 'Medium', 'Momentum'),
 ('ARGX', "RSI 70, near its high; steady.", "Momentum", "Overbought", (-7,2,8), 'Medium', 'Relative strength'),
 ('UNH', "+1.6% Wednesday (RSI 31) after an 18% drop on the CMS audit proposal; about 15x forward earnings.",
  "2027 outlook; comments to Jan 19", "Rule finalised as written", (-15,4,18), 'Speculative', 'Policy-shock rebound'),
 ('INSM', "Sanofi agreed to pay $175 cash; the stock is ~$170, a 2.7% gap. Close expected H1 2027.", "Deal approvals; rival bid", "Deal breaks (falls back toward ~$120)", (-30,1.5,5), 'Medium', 'Merger arbitrage'),
]
P[('intraday','hc','US')] = [
 ('VKTX', "+5.2% Wednesday, +18% in five days (RSI 65).", "Friday half-day: momentum", "Profit-taking", (-5,0.3,5), 'Speculative', 'Momentum'),
 ('NVO', "+2.0% (RSI 54).", "Friday half-day", "Small range", (-2.5,0.2,2.5), 'Medium', 'Relative strength'),
 ('UNH', "+1.6% (RSI 31).", "Friday half-day: rebound", "Policy headlines", (-3,0.2,3), 'Medium', 'Bounce'),
 ('CYTK', "+1.8%, +19% in five days.", "Friday half-day: momentum", "Profit-taking", (-4,0.2,4), 'Speculative', 'Momentum'),
 ('INSM', "Trades ~2.7% under the $175 cash offer.", "Spread narrows", "Deal risk", (-1,0.1,1), 'High', 'Merger arbitrage'),
]
P[('swing','hc','SGX')] = [
 ('Q0F.SI', "IHH (RSI 53) reports Q3 shortly.", "Q3 results (Yahoo lists Nov 27)", "Results miss", (-6,3,9), 'Medium', 'Earnings'),
 ('AP4.SI', "Riverstone up 7% in a month (RSI 63); +1.3% Wednesday.", "New CEO Dec 1", "Glove prices", (-8,4,11), 'Medium', 'Momentum'),
 ('C2PU.SI', "Parkway Life REIT: lowest-volatility name in the group.", "Dividend", "Rates", (-4,2,6), 'High', 'Range'),
 ('BSL.SI', "Raffles Medical +1.2% Wednesday (RSI 57).", "Support", "Low volume", (-5,2,6), 'Medium', 'Range'),
 ('H02.SI', "Haw Par RSI 26; cash-rich.", "Bounce", "Low growth", (-5,2,6), 'Medium', 'Oversold value'),
]
P[('intraday','hc','SGX')] = [
 ('Q0F.SI', "Flat ahead of Q3 results.", "Next session: results reaction", "Results miss", (-3,0.3,3), 'Medium', 'Earnings'),
 ('AP4.SI', "Rose 1.3%.", "Next session", "Glove prices", (-2.5,0.3,2.5), 'Medium', 'Momentum'),
 ('BSL.SI', "Rose 1.2%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('C2PU.SI', "Rose 0.5%.", "Next session", "Small range", (-1,0.2,1), 'Medium', 'Range'),
 ('H02.SI', "Rose 0.6% (RSI 26).", "Next session", "Small range", (-1.2,0.2,1.2), 'Medium', 'Bounce watch'),
]

# ---------- Finance ----------
P[('long','fin','US')] = [
 ('JPM', "Best-run US bank, 13% off its high at about 12.4x forward earnings. Higher rates support interest income.", "Q4 results Jan 14", "Credit cycle; market swings", (-15,8,22), 'High', 'Core holding'),
 ('V', "Visa: steady growth (+13%), 2% off its high; little AI exposure. +2.2% Wednesday.", "Holiday spending", "Card-fee regulation", (-12,6,18), 'High', 'Defensive growth'),
 ('GS', "About 11x forward earnings, 30% off its high; led Anthropic's record IPO.",
  "Deal fees; Q4 results Jan 19", "Volatility hits deals and trading", (-20,10,28), 'Medium', 'Cyclical value'),
 ('NU', "Nubank: revenue +34% at about 11.5x forward earnings, 34% off its high; +4.5% Wednesday (RSI 55).", "Q4 results (Feb)", "Brazil credit; strong dollar", (-30,16,48), 'Medium', 'Growth at a discount'),
 ('SE', "Sea: revenue +43%; $1B buyback. About 14x forward earnings, 52% off its high; +4.7% Wednesday.",
  "Q4 results (Mar)", "Credit costs at Monee; competition", (-30,17,50), 'Medium', 'Oversold growth'),
]
P[('long','fin','SGX')] = [
 ('D05.SI', "DBS kept its 81-cent quarterly dividend and says interest income has bottomed; 17% off its high (RSI 22).",
  "Q4 results Feb", "Margins if rates fall; stronger SGD", (-10,8,16), 'High', 'Income leader'),
 ('O39.SI', "OCBC was the only local bank to beat in Q3 and raised loan-growth guidance.",
  "Q4 results (Feb)", "Margin squeeze", (-10,7,15), 'Medium', 'Income'),
 ('U11.SI', "UOB missed Q3 and cut its margin guidance; RSI 13, 22% off its high.", "Fee recovery", "More credit provisions", (-12,7,17), 'Medium', 'Oversold income'),
 ('AIY.SI', "iFAST: fintech platform, revenue +23%, 35% off its high with 60% analyst upside.", "HK pension business", "Market-driven volumes", (-18,15,36), 'Medium', 'Growth'),
 ('S68.SI', "SGX benefits from high trading volumes; from Jan 2027 its RegCo takes over IPO prospectus reviews.", "Monthly volume data", "Already priced (24x earnings)", (-12,7,18), 'Medium', 'Volatility winner'),
]
P[('swing','fin','US')] = [
 ('MA', "Mastercard +2.2% Wednesday, 2% off its high (RSI 53); holiday spending in focus.", "Holiday spending data", "Rotation into tech", (-6,2.5,7), 'High', 'Steady'),
 ('NU', "Nubank +4.5%, up 3% in five days (RSI 55).", "Momentum", "Brazil swings", (-10,4,12), 'Medium', 'Momentum'),
 ('SCHW', "Schwab RSI 54, up 5% in a month; about 12x forward earnings.", "Monthly client metrics", "Market swings", (-8,3,10), 'Medium', 'Relative strength'),
 ('JPM', "RSI 33; flat Wednesday.", "Dip buying", "Bank lag", (-7,3,9), 'Medium', 'Oversold quality'),
 ('APO', "Apollo up 5% in a month (RSI 55); about 11x forward earnings.", "Private-credit flows", "Credit worries", (-10,3,11), 'Medium', 'Relative strength'),
]
P[('swing','fin','SGX')] = [
 ('D05.SI', "DBS oversold (RSI 22); -1.2% Wednesday.", "Dividend support", "Margin worries", (-4,3,7), 'High', 'Oversold income'),
 ('U11.SI', "UOB RSI 13.", "Rebound", "Further downgrades", (-5,3,8), 'Medium', 'Oversold rebound'),
 ('O39.SI', "OCBC RSI 31; -0.9% Wednesday.", "Post-results recovery", "Margin squeeze", (-4,2,6), 'Medium', 'Pullback'),
 ('S68.SI', "SGX RSI 38; volatile markets lift volumes.", "Volume data", "Valuation", (-5,3,8), 'Medium', 'Volatility winner'),
 ('AIY.SI', "iFAST RSI 36 after a 10% five-day drop.", "Rebound", "Market-driven", (-8,3,10), 'Medium', 'Oversold rebound'),
]
P[('intraday','fin','US')] = [
 ('SE', "+4.7% (RSI 36).", "Friday half-day: follow-through", "Profit-taking", (-3.5,0.3,3.5), 'Medium', 'Rebound'),
 ('NU', "+4.5%.", "Friday half-day: momentum", "Profit-taking", (-3.5,0.3,3.5), 'Medium', 'Momentum'),
 ('V', "+2.2%.", "Friday half-day: holiday spending", "Small range", (-2,0.2,2), 'Medium', 'Range'),
 ('MA', "+2.2%.", "Friday half-day: holiday spending", "Small range", (-2,0.2,2), 'Medium', 'Range'),
 ('UPST', "+4.8% (RSI 29).", "Friday half-day: bounce", "Credit worries", (-5,0.2,5), 'Speculative', 'Bounce'),
]
P[('intraday','fin','SGX')] = [
 ('D05.SI', "Fell 1.2% (RSI 22).", "Next session", "Trend down", (-1.3,0.3,1.6), 'High', 'Bounce watch'),
 ('U11.SI', "Eased 0.4% (RSI 13).", "Next session", "Trend down", (-1.5,0.3,1.8), 'Medium', 'Bounce watch'),
 ('O39.SI', "Eased 1.0%.", "Next session", "Small range", (-1.3,0.2,1.5), 'Medium', 'Range'),
 ('S68.SI', "Eased 0.9%.", "Next session", "Small range", (-1.3,0.2,1.5), 'Medium', 'Range'),
 ('AIY.SI', "Fell 1.8%.", "Next session", "Market-driven", (-2.5,0.2,2.5), 'Medium', 'Bounce watch'),
]

# IPO tab (6-month view), all markets
P[('ipo','all','US')] = [
 ('SPCX', "SpaceX (IPO $135) is about $127, 40% under its high; it cut an early 8% loss Wednesday after an FCC approval for data-centre satellites. Reports say SpaceX and Tesla formed committees to study a merger.",
  "Starship progress; merger news; lock-up expiries", "Valuation; heavy capex; Musk headlines", (-35,12,45), 'Medium', 'Mega-cap IPO'),
 ('CHYM', "Chime (IPO $27) trades about 22% above its IPO price, 4% off its high (RSI 63).",
  "Member growth", "Fintech credit cycle", (-18,8,25), 'Medium', 'Post-IPO uptrend'),
 ('KLAR', "Klarna (IPO $40) is about $13.50, 66% below its IPO price at about 19x forward earnings; up 6% in a month.",
  "Holiday volumes; Q4 results Feb 18", "Buy-now-pay-later credit losses", (-30,12,40), 'Speculative', 'Deep value'),
 ('CTY', "City Therapeutics (IPO $18) is about $20, +21% in five days but -3.6% Wednesday; 85% analyst upside.",
  "Pipeline updates", "Biotech swings (7-8% daily)", (-35,10,45), 'Speculative', 'Post-IPO momentum'),
 ('ASBH', "American Savings Bank (IPO $16) is up 23% since listing with low swings for a new stock (RSI 48).",
  "Q4 results", "Bank-sector selling", (-12,5,15), 'Medium', 'Steady post-IPO'),
]

# ---------- Power & grid (data-center power) ----------
P[('long','pwr','US')] = [
 ('GEV', "GE Vernova: gas turbines and grid gear sold out for years, revenue +27%. 39% off its high with 60% analyst upside.", "Q4 results Jan 27", "Data-centre policy; valuation (27x)", (-25,15,40), 'High', 'Quality at a discount'),
 ('CEG', "Constellation beat Q3 and raised 2026 guidance; 37% off its high (RSI 49).", "New long-term power deals", "Data-centre politics; PJM rules", (-22,13,32), 'High', 'Beat and raise'),
 ('PWR', "Quanta builds the grid: revenue +57%, 27% off its high, RSI 61 even after -2.9% Wednesday.", "Utility capex plans", "Data-centre policy", (-25,12,34), 'Medium', 'Grid builder'),
 ('ETN', "Eaton: electrical gear for data centres and utilities, 31% off its high at about 19x forward earnings.", "Q4 results Feb 2", "Data-centre orders slowing", (-20,13,33), 'Medium', 'Quality at a discount'),
 ('VRT', "Vertiv: data-centre cooling and power, revenue +61% at about 18x forward earnings, 53% off its high.", "Order backlog updates", "Most exposed to a data-centre slowdown", (-35,17,52), 'Medium', 'Oversold growth'),
]
P[('long','pwr','SGX')] = [
 ('U96.SI', "Sembcorp: power and renewables at about 9x earnings; gave back 3% Wednesday after Tuesday's rise.", "New contracts", "Power prices", (-12,8,18), 'Medium', 'Value'),
 ('BN4.SI', "Keppel: power, data centres and asset management, about 14x earnings with 50% analyst upside; RSI 21 after the StarHub-M1 merger news.", "M1 deal terms; asset sales", "Execution; SG data-centre chip rule", (-14,11,25), 'Medium', 'Value'),
 ('DCRU.SI', "Digital Core REIT: US data-centre REIT, about 9x earnings with 57% analyst upside.", "Leasing news", "Tenant concentration; US rates", (-14,10,26), 'Medium', 'Deep value'),
 ('AJBU.SI', "Keppel DC REIT: data-centre rents, 14% off its high (RSI 34).", "Dividend", "Rates", (-10,7,17), 'Medium', 'Income'),
 ('544.SI', "CSE Global: electrification and data-centre work, about 9x earnings, 59% off its high; -3.9% Wednesday.", "New orders", "Small and volatile", (-30,13,45), 'Speculative', 'Recovery'),
]
P[('swing','pwr','US')] = [
 ('TLN', "Talen RSI 59, up 15% in three months; about 11x forward earnings.", "Capacity deals", "Data-centre politics", (-13,5,16), 'Medium', 'Relative strength'),
 ('NEE', "NextEra +1.4% Wednesday (RSI 35) as yields fell.", "Defensive bid; lower yields", "Rates", (-6,2,7), 'Medium', 'Defensive'),
 ('PWR', "Quanta RSI 61; the steadiest name in AI power over a month.", "Utility capex", "Data-centre policy", (-10,4,13), 'Medium', 'Trend'),
 ('CEG', "Constellation RSI 49 after a 10% five-day drop.", "Power deals", "AI capex fears", (-12,5,15), 'Medium', 'Pullback'),
 ('GEV', "GE Vernova RSI 43, -7% in five days.", "Order news", "AI capex fears", (-14,5,18), 'Medium', 'Oversold rebound'),
]
P[('swing','pwr','SGX')] = [
 ('U96.SI', "Sembcorp RSI 37 after -3% Wednesday.", "Contracts", "Power prices", (-5,2.5,7), 'Medium', 'Pullback'),
 ('BN4.SI', "Keppel RSI 21, -11% in five days.", "Deal details", "Execution", (-7,3,10), 'Medium', 'Oversold rebound'),
 ('AJBU.SI', "Keppel DC REIT RSI 34.", "Support", "Rates", (-5,1.5,6), 'Medium', 'Range'),
 ('DCRU.SI', "Digital Core REIT RSI 45.", "Support", "US data-centre worries", (-7,2,8), 'Medium', 'Range'),
 ('544.SI', "CSE Global gave back 3.9% after Tuesday's 9% jump.", "New orders", "Volatile", (-15,4,16), 'Speculative', 'Base building'),
]
P[('intraday','pwr','US')] = [
 ('CCJ', "+3.1% (RSI 40).", "Friday half-day: uranium bounce", "AI power selling", (-3.5,0.2,3.5), 'Medium', 'Bounce'),
 ('NEE', "+1.4% as yields fell.", "Friday half-day: defensive bid", "Rotation to tech", (-1.8,0.2,1.8), 'Medium', 'Relative strength'),
 ('NRG', "+1.1% (RSI 61).", "Friday half-day", "AI power selling", (-4,0.2,4), 'Medium', 'Relative strength'),
 ('VRT', "+0.9% after a 10% five-day drop.", "Friday half-day: bounce", "AI hardware selling", (-5,0.2,5), 'Medium', 'Bounce'),
 ('OKLO', "+1.5% (RSI 51).", "Friday half-day", "8% daily swings", (-6,0,6), 'Speculative', 'Bounce'),
]
P[('intraday','pwr','SGX')] = [
 ('U96.SI', "Fell 3%.", "Next session", "Small range", (-1.5,0.3,1.8), 'Medium', 'Bounce watch'),
 ('BN4.SI', "Fell 1.5% (RSI 21).", "Next session", "More selling", (-2,0.3,2.5), 'Medium', 'Bounce watch'),
 ('AJBU.SI', "Eased 0.5%.", "Next session", "Small range", (-1.2,0.2,1.2), 'Medium', 'Range'),
 ('DCRU.SI', "Eased 1.1%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('544.SI', "Fell 3.9%.", "Next session", "Volatile", (-5,0,5), 'Speculative', 'Range'),
]

# ---------- Defence & industrials ----------
P[('long','def','US')] = [
 ('GE', "GE Aerospace: jet-engine services boom, revenue +16%, 16% off its high; up 7% in a month.", "Q4 results Jan 21", "Valuation (34x)", (-15,10,26), 'High', 'Quality'),
 ('RTX', "RTX: missiles and engines, revenue +11%, steady; 16% analyst upside.", "Q4 results Jan 26", "Engine issues", (-12,10,24), 'High', 'Core defence'),
 ('HWM', "Howmet: jet-engine parts, revenue +29%, 28% off its high with 40% analyst upside; up 10% in a month.", "Aerospace build rates", "Valuation (32x)", (-20,14,34), 'Medium', 'Growth at a discount'),
 ('LHX', "L3Harris: space and missile sensors, 31% off its high, 27% analyst upside; +1.4% Wednesday.", "Golden Dome contracts", "Budget fights", (-15,12,30), 'Medium', 'Value'),
 ('NOC', "Northrop: B-21 and missile defence, about 18.5x earnings, 28% off its high; RSI 68 as defence keeps holding up.", "Golden Dome contracts", "Budget fights", (-15,10,27), 'Medium', 'Value'),
]
P[('long','def','SGX')] = [
 ('S63.SI', "ST Engineering: record S$37.7B order book and nine-month revenue +10%; 26% off its high (RSI 26) with 35% analyst upside.", "Contract wins; FY results (Feb)", "Valuation (22x)", (-12,12,26), 'High', 'Quality on a dip'),
 ('BS6.SI', "Yangzijiang Shipbuilding: about 7x earnings, revenue +36%; 21% off its high.", "New ship orders", "US port fees on Chinese ships; new tariffs", (-18,13,32), 'Medium', 'Value'),
 ('S59.SI', "SIA Engineering: aircraft maintenance, 25% off its high, 34% analyst upside.", "Air travel", "Revenue falling (-11%)", (-10,10,24), 'Medium', 'Recovery'),
 ('C52.SI', "ComfortDelGro: steady transport earnings at about 13x; +1.7% Wednesday.", "Overseas contracts", "Slow growth", (-8,7,15), 'Medium', 'Steady'),
 ('H22.SI', "Hong Leong Asia: engines and building materials at about 7x earnings, 54% off its high (RSI 19).", "Results (Feb)", "China demand; no floor yet", (-28,15,50), 'Speculative', 'Deep value'),
]
P[('swing','def','US')] = [
 ('NOC', "Northrop RSI 68; defence held up as tech fell.", "Golden Dome news", "Overbought", (-6,3,9), 'Medium', 'Relative strength'),
 ('LMT', "Lockheed +2% Wednesday (RSI 58), up 3.5% in five days.", "Defensive rotation", "F-35 issues", (-6,3,9), 'Medium', 'Rotation'),
 ('GD', "General Dynamics +2.4% (RSI 53), 9% off its high.", "Navy and jet orders", "Budget fights", (-6,3,9), 'Medium', 'Rotation'),
 ('HWM', "Howmet up 10% in a month (RSI 57).", "Aerospace data", "Valuation", (-8,4,11), 'Medium', 'Trend'),
 ('AXON', "Axon +7% Wednesday and +14% in five days, still 47% off its high; 58% analyst upside.", "Analyst updates", "Gives back the bounce", (-18,6,22), 'Speculative', 'Post-earnings rebound'),
]
P[('swing','def','SGX')] = [
 ('S63.SI', "ST Engineering RSI 26 after a 17% one-month drop.", "Contract wins", "Holder selling", (-6,4,10), 'Medium', 'Oversold rebound'),
 ('C52.SI', "ComfortDelGro +1.7% Wednesday (RSI 33).", "Support", "Slow growth", (-4,1.5,5), 'Medium', 'Range'),
 ('S59.SI', "SIA Engineering RSI 28.", "Air travel", "Slow growth", (-6,2,7), 'Medium', 'Oversold'),
 ('BS6.SI', "Yangzijiang RSI 34.", "Orders", "Trade fees", (-8,4,12), 'Medium', 'Support'),
 ('H22.SI', "Hong Leong Asia RSI 19 after a 26% one-month drop.", "Bounce", "China demand", (-12,3,14), 'Speculative', 'Oversold, falling'),
]
P[('intraday','def','US')] = [
 ('AXON', "+7.3% (no company news found).", "Friday half-day: follow-through", "Gives back gains", (-4,0.3,4), 'Speculative', 'Momentum'),
 ('KTOS', "+3.8% (RSI 39).", "Friday half-day: drone theme", "Volatile", (-4.5,0.2,4.5), 'Speculative', 'Bounce'),
 ('HII', "+2.5%.", "Friday half-day: navy budget", "Small range", (-2.5,0.2,2.5), 'Medium', 'Rotation'),
 ('GD', "+2.4%.", "Friday half-day: defensive bid", "Small range", (-2,0.2,2), 'Medium', 'Rotation'),
 ('AVAV', "+2.6% (RSI 43); results Dec 8 (per Yahoo).", "Friday half-day", "Volatile", (-5,0.2,5), 'Speculative', 'Bounce'),
]
P[('intraday','def','SGX')] = [
 ('S63.SI', "Fell 2% (RSI 26).", "Next session", "Trend down", (-2.5,0.4,3), 'Medium', 'Bounce watch'),
 ('C52.SI', "Rose 1.7%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Momentum'),
 ('S59.SI', "Flat (RSI 28).", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('BS6.SI', "Fell 2.8%.", "Next session", "Tariff headlines", (-2.5,0.3,2.5), 'Medium', 'Bounce watch'),
 ('H22.SI', "Fell 2.2% (RSI 19).", "Next session", "More selling", (-4,0.3,4), 'Speculative', 'Bounce watch'),
]

# ---------- Energy (oil and gas) ----------
P[('long','nrg','US')] = [
 ('CVX', "Chevron: revenue +35%, about 12.8x earnings, 10% off its high; oil rose ~2.5% Wednesday.", "Hess integration; buybacks", "Oil keeps falling", (-16,8,24), 'High', 'Core energy'),
 ('XOM', "Exxon: steady cash flow, about 12.8x earnings, 16% analyst upside (RSI 38).", "Buybacks", "Oil price drop", (-15,7,21), 'High', 'Core energy'),
 ('LNG', "Cheniere: US gas exports on long contracts; less tied to oil. 9% off its high (RSI 70).", "New export capacity", "Gas price swings", (-15,8,24), 'Medium', 'Steady'),
 ('FANG', "Diamondback: low-cost Permian producer at about 8.3x earnings, 31% analyst upside; +2.6% Wednesday.", "Buybacks", "Oil price drop", (-22,12,32), 'Medium', 'Value'),
 ('EOG', "EOG: about 8.8x earnings, revenue +43%, 10% off its high.", "Buybacks", "Oil price drop", (-16,7,22), 'Medium', 'Value'),
]
P[('long','nrg','SGX')] = [
 ('5E2.SI', "Seatrium builds offshore rigs and wind platforms; fell another 4.2% Wednesday (worst STI stock) after job cuts and is down 25% in a month (RSI 19). About 9.5x earnings, 69% analyst upside.", "New orders", "Order book shrinking; contract delays", (-18,10,28), 'Medium', 'Recovery'),
 ('BN4.SI', "Keppel: energy infrastructure and asset management.", "Asset sales", "Execution", (-13,10,22), 'Medium', 'Value'),
 ('RE4.SI', "Geo Energy: up 17% in five days after saying there was no new Indonesian mining directive; about 6x earnings.", "Q3 update", "Indonesian policy risk", (-35,8,40), 'Speculative', 'Rebound'),
 ('5LY.SI', "Marco Polo Marine is down 15% in a week after guiding to lower FY profit; offshore vessels at about 9x earnings.", "FY results", "Profit falling; thin trading", (-30,5,30), 'Speculative', 'Broken growth'),
 ('5WH.SI', "Rex International is in a long downtrend (-79% from its high); no setup.", "None", "Further losses", (-30,-5,20), 'Speculative', 'Avoid'),
]
P[('swing','nrg','US')] = [
 ('FANG', "Diamondback +2.6% with oil (RSI 52).", "Buybacks", "Oil price drop", (-10,4,12), 'Medium', 'Oil rebound'),
 ('DVN', "Devon +3.3% (RSI 49); about 8x earnings, 40% analyst upside.", "Oil rebound", "Oil price drop", (-10,4,12), 'Medium', 'Oil rebound'),
 ('SLB', "SLB +3.8% (RSI 46).", "Service pricing", "Oil price drop", (-10,4,12), 'Medium', 'Rebound'),
 ('COP', "ConocoPhillips RSI 50, 12% off its high.", "Oil rebound", "Oil price drop", (-8,3,10), 'Medium', 'Oil rebound'),
 ('LNG', "Cheniere RSI 70; gas exports, not crude.", "Export capacity", "Overbought", (-8,2,9), 'Medium', 'Relative strength'),
]
P[('intraday','nrg','US')] = [
 ('SLB', "+3.8%.", "Friday half-day: oil strength", "Oil reverses", (-2.5,0.2,2.5), 'Medium', 'Momentum'),
 ('DVN', "+3.3%.", "Friday half-day: oil strength", "Oil reverses", (-3,0.2,3), 'Medium', 'Momentum'),
 ('HAL', "+2.8%.", "Friday half-day: oil strength", "Oil reverses", (-2.5,0.2,2.5), 'Medium', 'Momentum'),
 ('FANG', "+2.6%.", "Friday half-day: oil strength", "Oil reverses", (-2.5,0.2,2.5), 'Medium', 'Momentum'),
 ('EOG', "+1.6% (RSI 57).", "Friday half-day", "Small range", (-2,0.2,2), 'Medium', 'Range'),
]
P[('swing','nrg','SGX')] = [
 ('5E2.SI', "Seatrium RSI 19 after a 21% five-day drop.", "Orders", "More selling", (-10,3,12), 'Speculative', 'Oversold, falling'),
 ('BN4.SI', "Keppel RSI 21.", "Merger details", "Execution", (-7,3,10), 'Medium', 'Oversold rebound'),
 ('RE4.SI', "Geo Energy eased 2.2% after a 17% five-day gain; oil firmer.", "Follow-through", "Bounce fades", (-25,3,25), 'Speculative', 'Rebound'),
 ('5LY.SI', "Marco Polo Marine down 15% in a week on profit guidance.", "Results detail", "More selling", (-15,2,15), 'Speculative', 'Post-warning'),
 ('5WH.SI', "Rex International: no setup.", "None", "Further losses", (-12,-2,8), 'Speculative', 'Avoid'),
]
P[('intraday','nrg','SGX')] = [
 ('5E2.SI', "Fell 4.2% (RSI 19).", "Next session", "More selling", (-4,0.3,4), 'Speculative', 'Bounce watch'),
 ('BN4.SI', "Fell 1.5%.", "Next session", "More selling", (-2,0.3,2.5), 'Medium', 'Bounce watch'),
 ('RE4.SI', "Eased 2.2%; oil +2.5% overnight.", "Next session", "Bounce fades", (-6,0.5,6), 'Speculative', 'Range'),
 ('5LY.SI', "Fell 4.3%.", "Next session", "More selling", (-5,0,5), 'Speculative', 'Post-warning'),
 ('5WH.SI', "Penny stock in a downtrend; avoid.", "None", "Further losses", (-5,-1,4), 'Speculative', 'Avoid'),
]

IPO_LIST = [
 # sym, name, ipo_date, ipo_price, sector, status
 ('ANT','Anthropic (Nasdaq: ANT; priced $83, record ~$81B raised; day one +17%; Tue Nov 24 first close below the IPO price at ~$81.91; 303M more insider shares unlock Dec 15)','2026-11-19',83.00,'ai','Listed'),
 ('ABGC','American Barrick Gold (Barrick North American carve-out; ~$6B est.; filed, timing not set)','2026-12-01',None,'nrg','Filed'),
 ('BIAI','Bitari (not confirmed)','2026-11-30',7.00,'ai','Expected'),
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

SERENITY = {'NVDA','SPCX','AXTI','LITE','COHR','NBIS','MU','AVGO','AAOI','AEHR','GLW','SNDK','POET','IREN','TSEM','MRVL','AMD','ARM','INTC','TSM','CRDO','CRWV','ORCL','HOOD'}

# Nov 24-25 posts come from a third-party viewer (dates only, no times); older ones from earlier tracker reads.
X_POSTS = [
 ('2026-11-25','NVDA', "Via tracker: pushes back on finance influencers, arguing earnings and durability matter more than market deleveraging phases."),
 ('2026-11-25','', "Via tracker: notes the Fear & Greed index at 9 (extreme fear) and cites backtests where the S&P was higher 12 months later most of the time after readings under 25."),
 ('2026-11-25','HPE DELL', "Via tracker: cites HPE and Dell executives and a JPMorgan note - DRAM stays tight, NAND spot is weaker near term, enterprise NAND looks resilient."),
 ('2026-11-24','SNDK', "Via tracker: says SanDisk's ~$89B market value is matched by at least $89B of long-term supply deals with price floors."),
 ('2026-11-24','AAOI', "Via tracker: highlights Applied Optoelectronics' $2.2B long-term deal with a hyperscaler ($1.5B of 800G transceivers in 2027, $0.7B of lasers in 2028-29)."),
 ('2026-11-24','NBIS', "Via tracker: says Databricks picked Nebius as the neocloud it trusts for its workloads."),
 ('2026-11-24','', "Via tracker: flagged reports that new US tariffs could be unveiled within days, naming Japan, South Korea, the EU and Vietnam."),
 ('2026-11-23T22:00','NVDA', "Via tracker: says the AI trade is back after Nvidia's board reinstated Jensen Huang as CEO."),
 ('2026-11-22T09:46','CRWV', "Via tracker: notes CoreWeave says demand exceeds compute supply through 2027 while others argue for a glut, and calls the split interesting."),
 ('2026-11-22T09:35','ORCL SNDK', "Via tracker: asks why investors distrust Oracle's and SanDisk/Micron's contract statements - either a generational buying chance or the doubt is justified."),
 ('2026-11-20T21:28','', "Via tracker: previews Sivers (SIVE) results due Nov 26 and expects a buyout by a larger chip or electronics firm."),
 ('2026-11-20T12:23','SNDK', "Via tracker: argues the market misreads Chinese enterprise-SSD order cuts as weak demand, citing Phison's CEO on GPU shortages."),
]

EVENTS = [
 ('2026-11-24','Macro','S&P -0.5% to 7,201, Nasdaq -1.5% to 23,734, Dow +0.9% to 50,019', "Chip rally faded: NVDA -5.9% to $155.38, MU -11%, SanDisk ~-17%, AMD -8.9%. Pharma and retail led."),
 ('2026-11-24','Deals','Sanofi to buy Insmed for $175/share cash (~$41B)', "46% premium to the Nov 18 price; close expected H1 2027."),
 ('2026-11-24','IPO','Anthropic closes below its $83 IPO price', "-6.5% to ~$81.91. Thanksgiving week has no US IPOs scheduled."),
 ('2026-11-25','Macro','Core PCE 3.3% y/y (3.2% expected); Q3 GDP revised up to 4.3%', "Headline PCE 3.8%. December hike odds ~98%; markets see two more hikes in 2027."),
 ('2026-11-25','Macro','US proposes tariffs of up to 20% on 14 trading partners', "EU/Japan/Korea 15%, Vietnam 20%, Malaysia/Indonesia 18%. Chips, autos and metals excluded; not before January. US-China truce ends Jan 10."),
 ('2026-11-25','Macro','S&P -0.25% to 7,182.78, Nasdaq -0.6% to 23,585.80, Dow +0.3% to 50,182.95', "Recovered most of a ~4% midday Nasdaq drop. NVDA -3.9% to $149.30; SanDisk ~-6% on a TrendForce NAND price cut; LRCX -6%, AMAT -5%. 10-yr 4.85%; oil +2.5%; VIX ~28."),
 ('2026-11-25','SGX','STI -0.6% to 4,930.83', "Asian chips caught up with Tuesday's US drop (Kospi -6.2%, Nikkei -2.8%). AEM -6.8%, Seatrium -4.2%, DBS -1.2%; Singtel +1.9%."),
 ('2026-11-26','Macro','US Thanksgiving', "US stock market closed; early close (1pm ET) on Fri Nov 27. SGX trades normally."),
 ('2026-11-26','AI','Sivers Semiconductors Q3 report', "On @aleabitoreddit's photonics watchlist."),
 ('2026-11-27','SGX','IHH Q3 results (date per Yahoo)', ""),
 ('2026-11-30','IPO','Bitari expected (not confirmed)', ""),
 ('2026-12-01','IPO','American Barrick Gold (~$6B) may launch', "Filed; timing not set."),
 ('2026-12-01','AI','Marvell and Credo results', ""),
 ('2026-12-08','Defence','AeroVironment results (date per Yahoo)', ""),
 ('2026-12-09','Macro','Fed rate decision (Dec 8-9)', "A 25bp hike is priced at ~98%. Broadcom reports the same day."),
 ('2026-12-10','AI','Ciena results; TSMC November sales', ""),
 ('2026-12-14','AI','Oracle results (date per Yahoo)', ""),
 ('2026-12-15','IPO','Anthropic lock-up: ~303M more insider shares', "Per the prospectus, as reported."),
 ('2026-12-17','AI','Micron FQ1 results (date per Yahoo)', ""),
]
