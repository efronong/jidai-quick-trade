# Analyst picks for 2026-11-25 SGT (snapshot: US Tue Nov 24 ~3:20pm ET, SGX close Nov 24). Fields: sym, thesis, catalyst, risk, (low, base, high) % expected move, conviction, setup
# Horizons: long = 12 months, swing = ~4 weeks, intraday = rest of session (US) / next session (SGX), ipo = 6 months.
# Context Mon Nov 23: Nvidia reinstated Jensen Huang as CEO; NVDA +31.5%, S&P +4.7% to 7,238, Nasdaq +6.5% (best day since April 2025).
# Context Tue Nov 24 (US close): S&P -0.5% to 7,201.09, Nasdaq -1.5% to 23,733.54, Dow +0.9% to 50,018.70. The chip rally faded:
# NVDA -5.9% to $155.38 (Bernstein upgraded to Outperform, $200 target), MU -11%, AMD -8.9%, AVGO -4%, SanDisk ~-19%, HPE -16%, ADI -17%, Semtech -17%.
# Anthropic (ANT) -6.5% to ~$81.91, below its $83 IPO price. Sanofi agreed to buy Insmed for $175/share cash (~$41B, 46% premium).
# Money moved into health care (pharma +4-5%) and retail (Kohl's +19.5%, Dollar Tree +11%). Brent +2.4% to $88.78; 10-yr 4.93%; bitcoin ~$59.8k.
# Traders price ~95% odds of a 25bp Fed hike in December. GDP and PCE inflation due Wed Nov 25; US closed Thu, early close Fri.
# SGX Tue: STI ~+0.1-0.2% to ~4,960 (sources differ) - it closed BEFORE the US chip reversal. AEM +9%, CSE Global +9%, Sembcorp +2.9%;
# Seatrium -7 to -10% on 2% Singapore layoffs; Keppel -5% on StarHub-M1 merger news. SGX chip names may give back gains next session.
# Base cases discount analyst targets heavily: many targets were set before the November slide and look stale.
P = {}

# ---------- AI & chips ----------
P[('long','ai','US')] = [
 ('TSM', "Makes almost every leading AI chip, whoever designs it. Revenue +51% at about 15x forward earnings, 28% below its high. Fell only ~4% Tuesday while smaller chips fell 9-19%.",
  "November sales (~Dec 10); Q4 results Jan 14", "Taiwan geopolitics; US chip-access rules", (-20,16,38), 'High', 'Core holding'),
 ('NVDA', "Huang is back as CEO; Tuesday gave back ~6% of Monday's 31.5% jump. About 9x forward earnings after revenue +103%; Bernstein upgraded to Outperform ($200).",
  "Estimate upgrades; CES and GTC news", "Board probe still open; export rules; AI-bubble selling", (-28,18,50), 'High', 'Leader, overhang cleared'),
 ('AVGO', "Custom AI chips plus networking: revenue +86% at about 16x forward earnings, 37% off its high. Held up better than most chips Tuesday (-4%).",
  "Q4 results Dec 9", "Lumpy custom-chip orders", (-24,16,42), 'High', 'Leader at a discount'),
 ('MU', "Memory is still the tightest part of AI servers: revenue +379% at about 3x forward earnings. Gave back most of Monday's gain (-11%), 48% off its high.",
  "FQ1 results Dec 17", "Memory falls hard when prices turn; DRAM lawsuit", (-40,18,58), 'Medium', 'Cycle leader'),
 ('COHR', "Coherent: ~$20B multi-year optics deals and a $2B buyback; about 12x forward earnings. Fell ~10% Tuesday with optics but RSI is a neutral 50.",
  "Buyback; FQ2 results (Feb)", "8-9% daily swings", (-35,17,55), 'Medium', 'Optics leader'),
]
P[('long','ai','SGX')] = [
 ('AWX.SI', "AEM rose 9% Tuesday and is about 2.5x this year's start, still 44% off its high at about 16x earnings. Closed before US chips fell again.",
  "US chip read-across; FY results (Feb)", "One large customer; US chip rule for SG data centres", (-40,14,55), 'Medium', 'SGX AI leader'),
 ('V03.SI', "Venture: net cash, about 15x earnings, low volatility; analysts see about 32% upside. Rose 1.3% Tuesday.",
  "Analyst upgrades", "Slow revenue growth (+7%)", (-12,12,25), 'High', 'Steady value'),
 ('558.SI', "UMS makes precision parts for chip-equipment makers: revenue +61%, 44% off its high; +3.8% Tuesday.",
  "Chip-equipment spending outlook", "Tied to Applied Materials spending (-7% Tuesday)", (-32,14,45), 'Medium', 'Equipment supplier'),
 ('5DD.SI', "Micro-Mechanics: revenue +45%, 42% off its high, about 19x earnings; steadier than peers.",
  "Q1 FY27 results", "Small and thinly traded", (-24,13,36), 'Medium', 'Growth at a discount'),
 ('E28.SI', "Frencken builds modules for chip and medical equipment; 55% off its high at about 13x earnings (RSI 29).",
  "Equipment recovery", "Flat revenue", (-26,11,36), 'Medium', 'Recovery'),
]
P[('swing','ai','US')] = [
 ('AVGO', "Fell least of the big chips Tuesday (-4%); results Dec 9 fall inside the window.",
  "Q4 results Dec 9", "Results disappoint", (-13,6,18), 'Medium', 'Into results'),
 ('TSM', "Fell ~4% vs 9-12% for most chips; RSI 41.", "November sales ~Dec 10", "Chip selling spreads", (-11,5,15), 'Medium', 'Quality'),
 ('NVDA', "Bernstein upgrade ($200) and RSI 34 after giving back part of Monday's jump.", "Upgrades", "AI-bubble selling", (-15,6,20), 'Medium', 'Post-news base'),
 ('MRVL', "-9% Tuesday, 58% off its high; results Dec 1.", "Results Dec 1", "Guide disappoints", (-18,5,22), 'Speculative', 'Into results'),
 ('CRDO', "-13% Tuesday after +23% Monday; results Dec 1.", "Results Dec 1", "8-10% daily swings", (-20,5,25), 'Speculative', 'Into results'),
]
P[('swing','ai','SGX')] = [
 ('AWX.SI', "AEM +9% Tuesday (RSI 39), but US chips fell 4-19% after SGX closed.", "Chip sentiment", "Gives back Tuesday", (-18,4,22), 'Medium', 'Momentum, at risk'),
 ('558.SI', "UMS +3.8% (RSI 35) after a 26% one-month drop.", "Equipment read-across", "US equipment makers fell ~7%", (-15,4,16), 'Medium', 'Oversold rebound'),
 ('V03.SI', "Venture RSI 43; the steadiest name in the group.", "Analyst upgrades", "Low growth", (-6,3,9), 'High', 'Range'),
 ('5DD.SI', "Micro-Mechanics RSI 40.", "Results", "Thin trading", (-10,4,12), 'Medium', 'Support'),
 ('E28.SI', "Frencken RSI 29.", "Bounce", "Flat revenue", (-12,3,14), 'Speculative', 'Oversold rebound'),
]
P[('intraday','ai','US')] = [
 ('NVDA', "-7% into the last hour after +31.5% Monday; Bernstein upgrade.", "Dip buying near close", "More AI selling", (-4,0.3,4), 'Medium', 'Post-gap fade'),
 ('AVGO', "-4%, the steadiest big chip.", "Relative strength", "Sector drag", (-3,0.3,3), 'Medium', 'Relative strength'),
 ('MU', "-12%, giving back most of Monday.", "Oversold bounce", "Memory selling", (-5,0.2,5), 'Speculative', 'Washout watch'),
 ('SNDK', "-19% (RSI 26); down 51% in a month.", "Capitulation bounce", "More selling", (-7,0,7), 'Speculative', 'Washout watch'),
 ('PLTR', "+0.5%, one of few AI names up.", "Relative strength", "Valuation (63x)", (-3,0.2,3), 'Medium', 'Relative strength'),
]
P[('intraday','ai','SGX')] = [
 ('AWX.SI', "Rose 9% before US chips fell again.", "Next session", "Gap down after US chip drop", (-6,-1,4), 'Speculative', 'Gap-down risk'),
 ('558.SI', "Rose 3.8%; US equipment makers fell ~7%.", "Next session", "Follows US equipment", (-4,-0.5,3), 'Speculative', 'Gap-down risk'),
 ('V03.SI', "Rose 1.3%; low volatility.", "Next session", "Small range", (-2,0.2,2), 'Medium', 'Range'),
 ('5DD.SI', "Rose 1.4%.", "Next session", "Thin trading", (-3,0,3), 'Speculative', 'Range'),
 ('E28.SI', "Rose 2.6% (RSI 29).", "Next session", "Thin trading", (-3,0,3), 'Speculative', 'Range'),
]

# ---------- Health ----------
P[('long','hc','US')] = [
 ('LLY', "Obesity-drug leader: revenue +39%, 2% off its high; +3.5% Tuesday as money rotated into pharma. Little analyst upside left, so the base case is modest.",
  "Orforglipron launch; Q4 results (Feb)", "Drug-price policy", (-16,8,25), 'High', 'Defensive growth'),
 ('ARGX', "argenx: revenue +52% from Vyvgart, 6% off its high, 15% analyst upside; low daily swings (2%). +5.7% Tuesday.",
  "New indications in 2027", "Competition in myasthenia gravis", (-15,10,28), 'Medium', 'Growth leader'),
 ('MDGL', "Madrigal's liver drug Rezdiffra is growing fast (revenue +50%); +7% Tuesday, 29% off its high with 61% analyst upside. Sanofi-Insmed shows big pharma is buying.",
  "Script data; EU rollout", "Competition from GLP-1 drugs", (-22,18,45), 'Medium', 'Takeover-era growth'),
 ('VRTX', "Vertex: steady growth (+12%), at its high, about 28x earnings; +4.4% Tuesday.",
  "Pain-drug launch; kidney data", "Valuation", (-14,8,22), 'Medium', 'Steady growth'),
 ('MRK', "Merck: about 16x forward earnings, 9% off its high; +4.8% Tuesday (RSI 37).",
  "Keytruda subcutaneous rollout", "Keytruda patent cliff (2028)", (-12,8,20), 'Medium', 'Value'),
]
P[('long','hc','SGX')] = [
 ('Q0F.SI', "IHH runs hospitals across Asia; analysts see 35% upside. Reports Q3 today.", "Q3 results Nov 25", "Currency swings", (-12,11,24), 'Medium', 'Regional leader'),
 ('C2PU.SI', "Parkway Life REIT: steady hospital and nursing-home rents, 8% off its high.", "Dividend", "US rates (10-yr ~4.9%)", (-8,7,15), 'High', 'Income'),
 ('AP4.SI', "Riverstone: Q3 revenue at a 3-year high; about 14x earnings with 20% analyst upside. Up 7% in a month (RSI 60).", "New CEO from Dec 1", "Glove price competition", (-15,9,24), 'Medium', 'Value with momentum'),
 ('BSL.SI', "Raffles Medical: Singapore hospital group, 23% off its high, steady (RSI 55).", "Results (Feb)", "Shrinking revenue (-7%)", (-10,8,18), 'Medium', 'Recovery'),
 ('H02.SI', "Haw Par (Tiger Balm) trades near 9x earnings with a large cash and investment pile; 34% off its high (RSI 23).", "Results (Feb)", "Revenue down 8%", (-12,6,16), 'Medium', 'Value'),
]
P[('swing','hc','US')] = [
 ('LLY', "Defensive leader as money leaves chips.", "Orforglipron news", "Rotation back into tech", (-8,3,10), 'High', 'Defensive'),
 ('ARGX', "RSI 63, near its high; steady.", "Momentum", "Biotech risk-off", (-7,3,9), 'Medium', 'Relative strength'),
 ('MDGL', "RSI 60 after +7%; 61% analyst upside.", "Script data; deal talk", "Biotech risk-off", (-12,5,18), 'Medium', 'Momentum'),
 ('UNH', "Bounced 2% Tuesday (RSI 26) after an 18% drop on the CMS audit proposal; about 15x forward earnings.",
  "2027 outlook; comments to Jan 19", "Rule finalised as written", (-15,4,18), 'Speculative', 'Policy-shock rebound'),
 ('INSM', "Sanofi agreed to pay $175 cash; the stock is ~3% below. Close expected H1 2027.", "Deal approvals; rival bid", "Deal breaks (falls back toward ~$120)", (-30,2,6), 'Medium', 'Merger arbitrage'),
]
P[('intraday','hc','US')] = [
 ('INSM', "+14% on the $175 Sanofi deal.", "Spread narrows", "Deal risk", (-1.5,0.2,1.5), 'High', 'Merger arbitrage'),
 ('CYTK', "+9.8%; no company news found.", "Momentum", "Profit-taking", (-5,0.2,5), 'Speculative', 'Momentum'),
 ('MDGL', "+7%.", "Takeover-theme bid", "Profit-taking", (-4,0.3,4), 'Medium', 'Momentum'),
 ('MRNA', "+6.4%.", "Biotech bid", "Profit-taking", (-5,0.2,5), 'Speculative', 'Momentum'),
 ('LLY', "+3.5%; pharma rotation.", "Defensive bid", "Rotation", (-2.3,0.2,2.3), 'Medium', 'Range'),
]
P[('swing','hc','SGX')] = [
 ('Q0F.SI', "IHH (RSI 53) reports Q3 today.", "Q3 results Nov 25", "Results miss", (-6,3,9), 'Medium', 'Earnings'),
 ('AP4.SI', "Riverstone up 7% in a month (RSI 60).", "New CEO Dec 1", "Glove prices", (-8,4,11), 'Medium', 'Momentum'),
 ('C2PU.SI', "Parkway Life REIT: lowest-volatility name in the group.", "Dividend", "Rates", (-4,2,6), 'High', 'Range'),
 ('BSL.SI', "Raffles Medical up 2% in a month (RSI 55).", "Support", "Low volume", (-5,2,6), 'Medium', 'Range'),
 ('QC7.SI', "Q&M Dental RSI 18; +2.4% Tuesday.", "Bounce", "Small cap", (-8,3,10), 'Speculative', 'Oversold rebound'),
]
P[('intraday','hc','SGX')] = [
 ('Q0F.SI', "Reports Q3 today.", "Next session: results reaction", "Results miss", (-3,0.3,3), 'Medium', 'Earnings'),
 ('AP4.SI', "Rose 0.7%.", "Next session", "Glove prices", (-2.5,0.3,2.5), 'Medium', 'Range'),
 ('QC7.SI', "Rose 2.4%.", "Next session", "Thin trading", (-3,0.3,3), 'Speculative', 'Follow-through check'),
 ('C2PU.SI', "Rose 0.5%.", "Next session", "Small range", (-1,0.2,1), 'Medium', 'Range'),
 ('BSL.SI', "Rose 0.6%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
]

# ---------- Finance ----------
P[('long','fin','US')] = [
 ('JPM', "Best-run US bank, 13% off its high at about 12.4x forward earnings. Higher rates support interest income.", "Q4 results Jan 14", "Credit cycle; market swings", (-15,8,22), 'High', 'Core holding'),
 ('GS', "About 11x forward earnings, 30% off its high; led Anthropic's record IPO.",
  "Deal fees; Q4 results Jan 19", "ANT below IPO price; volatility hits deals", (-20,10,28), 'Medium', 'Cyclical value'),
 ('V', "Visa: steady growth (+13%), 5% off its high; little AI exposure.", "Holiday spending", "Card-fee regulation", (-12,6,18), 'High', 'Defensive growth'),
 ('NU', "Nubank: revenue +34% at about 11x forward earnings, 37% off its high; 47% analyst upside.", "Q4 results (Feb)", "Brazil credit; strong dollar", (-30,16,48), 'Medium', 'Growth at a discount'),
 ('SE', "Sea: revenue +43%; $1B buyback. About 14x forward earnings, 55% off its high (RSI 23).",
  "Q4 results (Mar)", "Credit costs at Monee; competition", (-30,17,50), 'Medium', 'Oversold growth'),
]
P[('long','fin','SGX')] = [
 ('D05.SI', "DBS kept its 81-cent quarterly dividend and says interest income has bottomed; 16% off its high (RSI 23).",
  "Q4 results Feb", "Margins if rates fall; stronger SGD", (-10,8,16), 'High', 'Income leader'),
 ('O39.SI', "OCBC was the only local bank to beat in Q3 and raised loan-growth guidance.",
  "Q4 results (Feb)", "Margin squeeze", (-10,7,15), 'Medium', 'Income'),
 ('U11.SI', "UOB missed Q3 and cut its margin guidance; RSI 13, 21% off its high.", "Fee recovery", "More credit provisions", (-12,7,17), 'Medium', 'Oversold income'),
 ('AIY.SI', "iFAST: fintech platform, revenue +23%, 34% off its high with 57% analyst upside.", "HK pension business", "Market-driven volumes", (-18,15,36), 'Medium', 'Growth'),
 ('S68.SI', "SGX benefits from high trading volumes; from Jan 2027 its RegCo takes over IPO prospectus reviews.", "Monthly volume data", "Already priced (24x earnings)", (-12,7,18), 'Medium', 'Volatility winner'),
]
P[('swing','fin','US')] = [
 ('SCHW', "Schwab RSI 52, +1.7% Tuesday; about 12x forward earnings.", "Monthly client metrics", "Market swings", (-8,3,10), 'Medium', 'Relative strength'),
 ('MA', "Mastercard 4% off its high (RSI 37); holiday spending in focus.", "Holiday spending data", "Rotation into tech", (-6,2,7), 'High', 'Steady'),
 ('JPM', "RSI 26 after a 4% five-day drop; flat Tuesday.", "Dip buying", "Bank lag", (-7,3,9), 'Medium', 'Oversold quality'),
 ('GS', "RSI 31 after an 8% five-day drop.", "Deal fees", "IPO market cools after ANT", (-9,3,12), 'Medium', 'Rebound'),
 ('APO', "Apollo +2.1% Tuesday; about 11x forward earnings.", "Private-credit flows", "Credit worries", (-10,3,11), 'Medium', 'Relative strength'),
]
P[('swing','fin','SGX')] = [
 ('D05.SI', "DBS oversold (RSI 23); +0.4-0.7% Tuesday.", "Dividend support", "Margin worries", (-4,3,7), 'High', 'Oversold income'),
 ('U11.SI', "UOB RSI 13.", "Rebound", "Further downgrades", (-5,3,8), 'Medium', 'Oversold rebound'),
 ('O39.SI', "OCBC RSI 31; +0.5-0.8% Tuesday.", "Post-results recovery", "Margin squeeze", (-4,2,6), 'Medium', 'Pullback'),
 ('S68.SI', "SGX +1.1% Tuesday; volatile markets lift volumes.", "Volume data", "Valuation", (-5,3,8), 'Medium', 'Volatility winner'),
 ('AIY.SI', "iFAST RSI 36 after a 9% five-day drop; +1.3% Tuesday.", "Rebound", "Market-driven", (-8,3,10), 'Medium', 'Oversold rebound'),
]
P[('intraday','fin','US')] = [
 ('SCHW', "+1.7%.", "Relative strength", "Market swings", (-2,0.2,2), 'Medium', 'Relative strength'),
 ('KLAR', "+2.3%.", "Retail spending bid", "Credit worries", (-4,0.2,4), 'Speculative', 'Momentum'),
 ('COIN', "-5.2% (RSI 17); bitcoin ~$59.8k.", "Crypto bounce", "Bitcoin weak", (-5,0,5), 'Speculative', 'Washout watch'),
 ('CRCL', "-7.4% (RSI 15).", "Oversold bounce", "Crypto weakness", (-5,0,5), 'Speculative', 'Washout watch'),
 ('MA', "+1.7%.", "Spending data", "Small range", (-2,0.2,2), 'Medium', 'Range'),
]
P[('intraday','fin','SGX')] = [
 ('D05.SI', "Rose 0.4% (RSI 23).", "Next session", "Trend down", (-1.3,0.3,1.6), 'High', 'Bounce watch'),
 ('U11.SI', "Eased 0.2% (RSI 13).", "Next session", "Trend down", (-1.5,0.3,1.8), 'Medium', 'Bounce watch'),
 ('S68.SI', "Rose 1.1%.", "Next session", "Small range", (-1.3,0.3,1.5), 'Medium', 'Range'),
 ('AIY.SI', "Rose 1.3%.", "Next session", "Market-driven", (-2.5,0.3,3), 'Medium', 'Momentum'),
 ('O39.SI', "Rose 0.5%.", "Next session", "Small range", (-1.3,0.3,1.5), 'Medium', 'Range'),
]

# IPO tab (6-month view), all markets
P[('ipo','all','US')] = [
 ('SPCX', "SpaceX (IPO $135) slipped 5% Tuesday to about $126, below its IPO price and 40% under its high. Jefferies started at Buy ($210).",
  "Starship progress; lock-up expiries", "Valuation; AI-linked selling; Musk headlines", (-35,12,45), 'Medium', 'Mega-cap IPO'),
 ('CHYM', "Chime (IPO $27) trades about 21% above its IPO price, 6% off its high (RSI 63); +2% Tuesday.",
  "Member growth", "Fintech credit cycle", (-18,8,25), 'Medium', 'Post-IPO uptrend'),
 ('KLAR', "Klarna (IPO $40) is about $13, 67% below its IPO price at about 20x forward earnings; up 6% in a month.",
  "Holiday volumes; Q4 results Feb 18", "Buy-now-pay-later credit losses", (-30,12,40), 'Speculative', 'Deep value'),
 ('CTY', "City Therapeutics (IPO $18) rose 7% Tuesday to about $19.8, 12% off its high (RSI 61); 88% analyst upside.",
  "Pipeline updates", "Biotech swings (7% daily)", (-35,10,45), 'Speculative', 'Post-IPO momentum'),
 ('ASBH', "American Savings Bank (IPO $16) is up 23% since listing with low swings for a new stock (RSI 47).",
  "Q4 results", "Bank-sector selling", (-12,5,15), 'Medium', 'Steady post-IPO'),
]

# ---------- Power & grid (data-center power) ----------
P[('long','pwr','US')] = [
 ('GEV', "GE Vernova: gas turbines and grid gear sold out for years, revenue +27%. 39% off its high with 62% analyst upside; fell 5% with AI names.", "Q4 results Jan 27", "Data-centre policy; valuation (27x)", (-25,15,40), 'High', 'Quality at a discount'),
 ('CEG', "Constellation beat Q3 and raised 2026 guidance; 36% off its high (RSI 49).", "New long-term power deals", "Data-centre politics; PJM rules", (-22,13,32), 'High', 'Beat and raise'),
 ('PWR', "Quanta builds the grid: revenue +57%, 25% off its high, still up 5% in a month (RSI 52).", "Utility capex plans", "Data-centre policy", (-25,12,34), 'Medium', 'Grid builder'),
 ('ETN', "Eaton: electrical gear for data centres and utilities, 31% off its high at about 19x forward earnings.", "Q4 results Feb 2", "Data-centre orders slowing", (-20,13,33), 'Medium', 'Quality at a discount'),
 ('VRT', "Vertiv: data-centre cooling and power, revenue +61% at about 18x forward earnings, 54% off its high; -7% Tuesday.", "Order backlog updates", "Most exposed to a data-centre slowdown", (-35,17,52), 'Medium', 'Oversold growth'),
]
P[('long','pwr','SGX')] = [
 ('U96.SI', "Sembcorp: power and renewables at about 9x earnings; led STI gainers Tuesday (+2.5-2.9%).", "New contracts", "Power prices", (-12,8,18), 'Medium', 'Value with momentum'),
 ('BN4.SI', "Keppel: power, data centres and asset management, about 14x earnings with 48% analyst upside; fell 5% Tuesday on StarHub-M1 merger news (RSI 21).", "M1 deal terms; asset sales", "Execution; SG data-centre chip rule", (-14,11,25), 'Medium', 'Value'),
 ('DCRU.SI', "Digital Core REIT: US data-centre REIT, about 9x earnings with 55% analyst upside.", "Leasing news", "Tenant concentration; US rates", (-14,10,26), 'Medium', 'Deep value'),
 ('AJBU.SI', "Keppel DC REIT: data-centre rents, 14% off its high (RSI 40).", "Dividend", "Rates", (-10,7,17), 'Medium', 'Income'),
 ('544.SI', "CSE Global: electrification and data-centre work, about 9x earnings, 57% off its high; +9% Tuesday.", "New orders", "Small and volatile", (-30,13,45), 'Speculative', 'Recovery'),
]
P[('swing','pwr','US')] = [
 ('TLN', "Talen RSI 55, up 3% in a month; about 11x forward earnings.", "Capacity deals", "Data-centre politics", (-13,5,16), 'Medium', 'Relative strength'),
 ('PWR', "Quanta up 5% in a month (RSI 52); the steadiest name in AI power.", "Utility capex", "Data-centre policy", (-10,4,13), 'Medium', 'Trend'),
 ('CEG', "Constellation RSI 49 after a 9% five-day drop.", "Power deals", "AI capex fears", (-12,5,15), 'Medium', 'Pullback'),
 ('NEE', "NextEra +0.7% while AI power fell 3-7% (RSI 23).", "Defensive bid", "Rates", (-6,2,7), 'Medium', 'Defensive'),
 ('GEV', "GE Vernova RSI 36 after -5%.", "Order news", "AI capex fears", (-14,5,18), 'Medium', 'Oversold rebound'),
]
P[('swing','pwr','SGX')] = [
 ('U96.SI', "Sembcorp +2.9% Tuesday (RSI 44).", "Contracts", "Power prices", (-5,2.5,7), 'Medium', 'Momentum'),
 ('BN4.SI', "Keppel RSI 21 after -5% on StarHub-M1 merger news.", "Deal details", "Execution", (-7,3,10), 'Medium', 'Oversold rebound'),
 ('544.SI', "CSE Global +9% Tuesday.", "New orders", "Gives back gains", (-15,4,16), 'Speculative', 'Base building'),
 ('AJBU.SI', "Keppel DC REIT eased 2.8% (RSI 40).", "Support", "Rates", (-5,1.5,6), 'Medium', 'Range'),
 ('DCRU.SI', "Digital Core REIT +2.3% (RSI 48).", "Support", "US data-centre worries", (-7,2,8), 'Medium', 'Range'),
]
P[('intraday','pwr','US')] = [
 ('NEE', "+0.7% while AI power fell.", "Defensive bid", "Rotation to tech", (-1.8,0.2,1.8), 'Medium', 'Relative strength'),
 ('NRG', "-6.3% (RSI 58).", "Dip buying", "AI power selling", (-4,0.2,4), 'Medium', 'Pullback'),
 ('VRT', "-7%.", "Oversold bounce", "AI hardware selling", (-5,0.2,5), 'Medium', 'Pullback'),
 ('BE', "-7%.", "Bounce", "8-9% daily swings", (-6,0,6), 'Speculative', 'Pullback'),
 ('PWR', "-2.9%; held up better than peers.", "Relative strength", "Sector drag", (-3,0.2,3), 'Medium', 'Relative strength'),
]
P[('intraday','pwr','SGX')] = [
 ('U96.SI', "Rose 2.9%.", "Next session", "Small range", (-1.5,0.2,1.8), 'Medium', 'Momentum'),
 ('BN4.SI', "Fell 5% (RSI 21).", "Next session: merger detail", "More selling", (-2,0.4,2.5), 'Medium', 'Bounce watch'),
 ('544.SI', "Rose 9%.", "Next session", "Gives back gains", (-5,-0.5,4), 'Speculative', 'Follow-through check'),
 ('AJBU.SI', "Eased 2.8%.", "Next session", "Small range", (-1.2,0.2,1.2), 'Medium', 'Range'),
 ('DCRU.SI', "Rose 2.3%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
]

# ---------- Defence & industrials ----------
P[('long','def','US')] = [
 ('GE', "GE Aerospace: jet-engine services boom, revenue +16%, 17% off its high; up 10% in a month.", "Q4 results Jan 21", "Valuation (34x)", (-15,10,26), 'High', 'Quality'),
 ('RTX', "RTX: missiles and engines, revenue +11%, steady; 16% analyst upside.", "Q4 results Jan 26", "Engine issues", (-12,10,24), 'High', 'Core defence'),
 ('HWM', "Howmet: jet-engine parts, revenue +29%, 28% off its high with 40% analyst upside; up 9% in a month.", "Aerospace build rates", "Valuation (32x)", (-20,14,34), 'Medium', 'Growth at a discount'),
 ('LHX', "L3Harris: space and missile sensors, 31% off its high, 28% analyst upside; +1.9% Tuesday.", "Golden Dome contracts", "Budget fights", (-15,12,30), 'Medium', 'Value'),
 ('NOC', "Northrop: B-21 and missile defence, about 18.5x earnings, 28% off its high; RSI 67 as defence held up.", "Golden Dome contracts", "Budget fights", (-15,10,27), 'Medium', 'Value'),
]
P[('long','def','SGX')] = [
 ('S63.SI', "ST Engineering: record S$37.7B order book and nine-month revenue +10%; 24% off its high (RSI 27) with 33% analyst upside.", "Contract wins; FY results (Feb)", "Valuation (22x)", (-12,12,26), 'High', 'Quality on a dip'),
 ('BS6.SI', "Yangzijiang Shipbuilding: about 7x earnings, revenue +36%; 19% off its high.", "New ship orders", "US port fees on Chinese ships", (-18,14,32), 'Medium', 'Value'),
 ('S59.SI', "SIA Engineering: aircraft maintenance, 25% off its high, 33% analyst upside.", "Air travel", "Revenue falling (-11%)", (-10,10,24), 'Medium', 'Recovery'),
 ('C52.SI', "ComfortDelGro: steady transport earnings at about 13x.", "Overseas contracts", "Slow growth", (-8,7,15), 'Medium', 'Steady'),
 ('H22.SI', "Hong Leong Asia: engines and building materials at about 7x earnings, 53% off its high (RSI 19).", "Results (Feb)", "China demand; no floor yet", (-28,16,50), 'Speculative', 'Deep value'),
]
P[('swing','def','US')] = [
 ('NOC', "Northrop RSI 67, +1.9%; defence held up as tech fell.", "Golden Dome news", "Budget fights", (-6,3,9), 'Medium', 'Relative strength'),
 ('LMT', "Lockheed +3% Tuesday (RSI 48).", "Defensive rotation", "F-35 issues", (-6,3,9), 'Medium', 'Rotation'),
 ('HWM', "Howmet up 9% in a month (RSI 49).", "Aerospace data", "Valuation", (-8,4,11), 'Medium', 'Trend'),
 ('GE', "GE up 10% in a month (RSI 44).", "Aftermarket demand", "Valuation", (-7,3,9), 'Medium', 'Trend'),
 ('AXON', "Axon +3.9% Tuesday (RSI 26) after a 25% one-month drop; 69% analyst upside.", "Analyst updates", "More downgrades", (-18,6,22), 'Speculative', 'Post-earnings rebound'),
]
P[('swing','def','SGX')] = [
 ('S63.SI', "ST Engineering RSI 27 after a 15% one-month drop.", "Contract wins", "Holder selling", (-6,4,10), 'Medium', 'Oversold rebound'),
 ('BS6.SI', "Yangzijiang RSI 39.", "Orders", "Trade fees", (-8,4,12), 'Medium', 'Support'),
 ('S59.SI', "SIA Engineering RSI 29; +1.1% Tuesday.", "Air travel", "Slow growth", (-6,2,7), 'Medium', 'Oversold'),
 ('C52.SI', "ComfortDelGro RSI 30.", "Support", "Slow growth", (-4,1.5,5), 'Medium', 'Range'),
 ('H22.SI', "Hong Leong Asia RSI 19 after a 27% one-month drop.", "Bounce", "China demand", (-12,3,14), 'Speculative', 'Oversold, falling'),
]
P[('intraday','def','US')] = [
 ('AXON', "+3.9% (RSI 26).", "Bounce", "Gives back gains", (-4,0.3,4), 'Speculative', 'Bounce'),
 ('LMT', "+3%.", "Defensive bid", "Rotation to tech", (-2,0.2,2), 'Medium', 'Rotation'),
 ('HII', "+2.4%.", "Navy budget", "Small range", (-2.5,0.2,2.5), 'Medium', 'Rotation'),
 ('NOC', "+1.9% (RSI 67).", "Defensive bid", "Overbought", (-2,0.1,2), 'Medium', 'Range'),
 ('KTOS', "-0.7% (RSI 30).", "Drone contracts", "Volatile", (-4.5,0.2,4.5), 'Speculative', 'Bounce watch'),
]
P[('intraday','def','SGX')] = [
 ('S63.SI', "Rose 0.5% (RSI 27).", "Next session", "Trend down", (-2.5,0.4,3), 'Medium', 'Bounce watch'),
 ('BS6.SI', "Eased 0.5%.", "Next session", "Small range", (-2.5,0.3,2.5), 'Medium', 'Range'),
 ('S59.SI', "Rose 1.1%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('C52.SI', "Eased 1.7%.", "Next session", "Small range", (-1.5,0.3,1.5), 'Medium', 'Bounce watch'),
 ('H22.SI', "Eased 1.6% (RSI 19).", "Next session", "More selling", (-4,0.3,4), 'Speculative', 'Bounce watch'),
]

# ---------- Energy (oil and gas) ----------
P[('long','nrg','US')] = [
 ('CVX', "Chevron: revenue +35%, about 12.7x earnings, 11% off its high; +1.6% as Brent rose 2.4% to ~$89.", "Hess integration; buybacks", "Oil keeps falling", (-16,8,24), 'High', 'Core energy'),
 ('XOM', "Exxon: steady cash flow, about 12.7x earnings, 16% analyst upside (RSI 33).", "Buybacks", "Oil price drop", (-15,7,21), 'High', 'Core energy'),
 ('LNG', "Cheniere: US gas exports on long contracts; less tied to oil. 10% off its high (RSI 53).", "New export capacity", "Gas price swings", (-15,8,24), 'Medium', 'Steady'),
 ('FANG', "Diamondback: low-cost Permian producer at about 8x earnings, 34% analyst upside; +2.4% Tuesday.", "Buybacks", "Oil price drop", (-22,12,32), 'Medium', 'Value'),
 ('EOG', "EOG: about 8.7x earnings, revenue +43%, 11% off its high.", "Buybacks", "Oil price drop", (-16,7,22), 'Medium', 'Value'),
]
P[('long','nrg','SGX')] = [
 ('5E2.SI', "Seatrium builds offshore rigs and wind platforms; fell 7-10% Tuesday on 2% Singapore job cuts and is down 21% in a month (RSI 21). About 10x earnings, 63% analyst upside.", "New orders", "Order book shrinking; contract delays", (-18,10,28), 'Medium', 'Recovery'),
 ('BN4.SI', "Keppel: energy infrastructure and asset management.", "Asset sales", "Execution", (-13,10,22), 'Medium', 'Value'),
 ('RE4.SI', "Geo Energy: up 20% in five days after saying there was no new Indonesian mining directive; about 6x earnings.", "Q3 update", "Indonesian policy risk", (-35,8,40), 'Speculative', 'Rebound'),
 ('5LY.SI', "Marco Polo Marine is down 13% in a week after guiding to lower FY profit; offshore vessels at about 9x earnings.", "FY results", "Profit falling; thin trading", (-30,5,30), 'Speculative', 'Broken growth'),
 ('5WH.SI', "Rex International is in a long downtrend (-77% from its high); no setup.", "None", "Further losses", (-30,-5,20), 'Speculative', 'Avoid'),
]
P[('swing','nrg','US')] = [
 ('FANG', "Diamondback +2.4% with oil (RSI 42).", "Buybacks", "Oil price drop", (-10,4,12), 'Medium', 'Oil rebound'),
 ('COP', "ConocoPhillips +2.2%, 12% off its high (RSI 47).", "Oil rebound", "Oil price drop", (-8,3,10), 'Medium', 'Oil rebound'),
 ('LNG', "Cheniere RSI 53; gas exports, not crude.", "Export capacity", "Gas price swings", (-8,3,10), 'Medium', 'Relative strength'),
 ('SLB', "SLB +1.6% (RSI 30).", "Service pricing", "Oil price drop", (-10,4,12), 'Medium', 'Oversold rebound'),
 ('MPC', "Marathon Petroleum down 10% in five days (RSI 35); about 6x earnings.", "Refining margins", "Margins fall", (-10,4,12), 'Speculative', 'Oversold rebound'),
]
P[('intraday','nrg','US')] = [
 ('FANG', "+2.4%; Brent +2.4%.", "Oil strength", "Oil reverses", (-2.5,0.2,2.5), 'Medium', 'Momentum'),
 ('COP', "+2.2%.", "Oil strength", "Oil reverses", (-2.5,0.2,2.5), 'Medium', 'Momentum'),
 ('SLB', "+1.6%.", "Oil strength", "Small range", (-2.5,0.2,2.5), 'Medium', 'Momentum'),
 ('OXY', "+1.5% (RSI 34).", "Oil bounce", "Oil reverses", (-2.5,0.2,2.5), 'Medium', 'Bounce'),
 ('MPC', "-0.7% on an oil up day (RSI 35).", "Refining margins", "Weak margins", (-3,0.1,3), 'Speculative', 'Laggard'),
]
P[('swing','nrg','SGX')] = [
 ('5E2.SI', "Seatrium RSI 21 after a 20% five-day drop; job cuts announced.", "Orders", "More selling", (-10,3,12), 'Speculative', 'Oversold, falling'),
 ('BN4.SI', "Keppel RSI 21.", "Merger details", "Execution", (-7,3,10), 'Medium', 'Oversold rebound'),
 ('RE4.SI', "Geo Energy eased 1.1% after a 20% weekly gain; oil firmer.", "Follow-through", "Bounce fades", (-25,3,25), 'Speculative', 'Rebound'),
 ('5LY.SI', "Marco Polo Marine down 13% in a week on profit guidance.", "Results detail", "More selling", (-15,2,15), 'Speculative', 'Post-warning'),
 ('5WH.SI', "Rex International: no setup.", "None", "Further losses", (-12,-2,8), 'Speculative', 'Avoid'),
]
P[('intraday','nrg','SGX')] = [
 ('5E2.SI', "Fell ~10% on job cuts (RSI 21).", "Next session", "More selling", (-4,0.3,4), 'Speculative', 'Bounce watch'),
 ('BN4.SI', "Fell 5%.", "Next session", "More selling", (-2,0.4,2.5), 'Medium', 'Bounce watch'),
 ('RE4.SI', "Eased 1.1%; Brent +2.4% overnight.", "Next session", "Bounce fades", (-6,0.5,6), 'Speculative', 'Range'),
 ('5LY.SI', "Eased 2.1%.", "Next session", "More selling", (-5,0,5), 'Speculative', 'Post-warning'),
 ('5WH.SI', "Penny stock in a downtrend; avoid.", "None", "Further losses", (-5,-1,4), 'Speculative', 'Avoid'),
]

IPO_LIST = [
 # sym, name, ipo_date, ipo_price, sector, status
 ('ANT','Anthropic (Nasdaq: ANT; priced $83, record ~$81B raised; day one +17%; Tue Nov 24 -6.5% to ~$81.91, first close below the IPO price; 303M more insider shares unlock Dec 15)','2026-11-19',83.00,'ai','Listed'),
 ('ABGC','American Barrick Gold (Barrick North American carve-out; ~$6B est.; could launch after Thanksgiving)','2026-12-01',None,'nrg','Filed'),
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

X_POSTS = [
 ('2026-11-23T22:00','NVDA', "Via tracker: says the AI trade is back after Nvidia's board reinstated Jensen Huang as CEO."),
 ('2026-11-23T12:05','NVDA', "Via tracker: says Trump's comment about rehiring Huang made his return more likely, with Washington's backing."),
 ('2026-11-23T03:17','NVDA', "Via tracker: reposts Treasury Secretary Bessent's remarks on Nvidia, the AI selloff and circular financing; sees sentiment improving."),
 ('2026-11-22T09:46','CRWV', "Via tracker: notes CoreWeave says demand exceeds compute supply through 2027 while others argue for a glut, and calls the split interesting."),
 ('2026-11-22T09:35','ORCL SNDK', "Via tracker: asks why investors distrust Oracle's and SanDisk/Micron's contract statements - either a generational buying chance or the doubt is justified."),
 ('2026-11-21T04:39','NVDA', "Via tracker: says NVDA's 12%+ drop followed a report of an SEC look at Nvidia's accounting, hitting indexes and retirement accounts."),
 ('2026-11-21T02:50','SPCX', "Via tracker: cites an industry warning that circuit-board shortages are spreading beyond AI and argues the selloff ignores fundamentals."),
 ('2026-11-21T02:10','CRWV', "Via tracker: jokes that with one party wanting to ban new US data centres and the other overseas ones, CoreWeave is caught in between."),
 ('2026-11-20T23:48','HOOD NBIS', "Via tracker: says growth names like HOOD and NBIS fell hard while consumer-staples valuations look like 1999."),
 ('2026-11-20T21:28','', "Via tracker: previews Sivers (SIVE) results due Nov 26 and expects a buyout by a larger chip or electronics firm."),
 ('2026-11-20T20:56','NVDA', "Via tracker: reads enterprises buying their own AI servers as bad for Anthropic and frontier labs but good for Nvidia GPU demand."),
 ('2026-11-20T13:18','SNDK', "Via tracker: says he holds no SanDisk or Kioxia, but argues the panic overreacts to spot prices and contract visibility is strong."),
 ('2026-11-20T12:23','SNDK', "Via tracker: argues the market misreads Chinese enterprise-SSD order cuts as weak demand, citing Phison's CEO on GPU shortages."),
]

EVENTS = [
 ('2026-11-23','AI','Nvidia reinstates Jensen Huang as CEO', "Unanimous board vote; an independent-director probe continues. NVDA +31.5%, adding nearly $1T. Chips +10-25%."),
 ('2026-11-23','Macro','S&P +4.7% to 7,238, Nasdaq +6.5%, Dow ~+3%', "Best day since April 2025. 10-yr 4.94%, dollar at a 19-month high."),
 ('2026-11-23','SGX','STI -0.43% to 4,953.81', "Closed before the US rally. Marco Polo Marine -9.5% on lower FY profit guidance."),
 ('2026-11-24','Macro','S&P -0.5% to 7,201, Nasdaq -1.5% to 23,734, Dow +0.9% to 50,019', "Chip rally faded: NVDA -5.9% to $155.38 (Bernstein upgrade, $200), MU -11%, AMD -8.9%, HPE -16%, ADI -17%. Pharma and retail led. Brent +2.4% to $88.78; ~95% odds of a December hike."),
 ('2026-11-24','IPO','Anthropic closes below its $83 IPO price', "-6.5% to ~$81.91. Thanksgiving week has no US IPOs scheduled."),
 ('2026-11-24','Deals','Sanofi to buy Insmed for $175/share cash (~$41B)', "46% premium to the Nov 18 price; close expected H1 2027. INSM +14%, Sanofi +11%."),
 ('2026-11-24','SGX','STI ~+0.1-0.2% to ~4,960', "Sembcorp led (+2.5%); Seatrium -7% on 2% Singapore job cuts; Keppel -4.6% on StarHub-M1 merger news; AEM and CSE Global +9%."),
 ('2026-11-24','Earnings','Dell, HP, Workday, Autodesk, Ambarella report after the US close', "Results not yet known at snapshot time."),
 ('2026-11-25','Macro','Q3 GDP second estimate; October PCE inflation (8:30am ET)', "Key input for the December Fed decision."),
 ('2026-11-25','SGX','IHH Q3 results', "SIA goes ex-dividend (7 cents)."),
 ('2026-11-26','Macro','US Thanksgiving', "US stock market closed; early close (1pm ET) on Nov 27."),
 ('2026-11-26','AI','Sivers Semiconductors Q3 report', "On @aleabitoreddit's photonics watchlist."),
 ('2026-11-30','IPO','Bitari expected (not confirmed)', ""),
 ('2026-12-01','IPO','American Barrick Gold (~$6B) and Core Specialty Insurance may launch', "Both filed; timing not set."),
 ('2026-12-01','AI','Marvell and Credo results', ""),
 ('2026-12-02','Defence','AeroVironment results', "Yahoo lists Dec 8."),
 ('2026-12-09','Macro','Fed rate decision (Dec 8-9)', "A 25bp hike is priced at ~95%. Broadcom reports the same day."),
 ('2026-12-10','AI','Ciena results; TSMC November sales', ""),
 ('2026-12-15','IPO','Anthropic lock-up: ~303M more insider shares', "Per the prospectus, as reported."),
 ('2026-12-17','AI','Micron FQ1 results (date per Yahoo)', ""),
]
