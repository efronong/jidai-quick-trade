# Analyst picks for 2026-11-20 SGT (snapshot: US Thu Nov 19 ~13:30 ET, SGX close Nov 19). Fields: sym, thesis, catalyst, risk, (low, base, high) % expected move, conviction, setup
# Horizons: long = 12 months, swing = ~4 weeks, intraday = rest of session (US) / next session (SGX), ipo = 6 months.
# Context: Thu Nov 19 close (after the snapshot): Dow -1,101 (-2.2%) to 49,097, S&P -2.0% to 7,176 (sixth straight drop), Nasdaq -2.25%, SOX -2.4%, VIX ~28.
# Nasdaq was up ~2% early and reversed once Anthropic began trading. ANT opened $111.50 (IPO $83), peaked $115.10, closed $97.17 (+17%).
# AMD -8% on a Hunterbrook report (customer backstops; firmware reaching an Entity-List server maker) - allegations, unconfirmed.
# Insmed +19-21% on a Bloomberg report that Sanofi is weighing a takeover (not confirmed). UNH -4.5% more on the CMS audit proposal. Klarna -10%.
# Jobless claims 203k; Philly Fed 6.3 (from 20.9) with prices paid 58.2. 10-yr 5.05%. WTI ~$83 (+1%). Fed's Jefferson: AI spending is adding to inflation now.
# Walmart and Palo Alto beat and raised. JPM, Visa, Mastercard disclosed a third-party vendor breach (limited contact data; no card data).
# SGX Nov 19: AEM -4.1%, Riverstone +5.6% (Q3 revenue at a 3-year high), Geo Energy +9.5% again, ST Engineering +1.2%, CSE Global +2.7%.
# NOTE: snapshot prices are from ~1:30 pm ET, before the late-session slide; most US prices closed lower than shown.
P = {}

# ---------- AI & chips ----------
P[('long','ai','US')] = [
 ('TSM', "Makes almost every leading AI chip, whoever designs it. Revenue +51% at about 15x forward earnings, 27% below its high (RSI 37). Nvidia's $130B guide is a direct read-across for TSMC wafers.",
  "November sales (~Dec 10); Q4 results Jan 14", "Taiwan geopolitics; new US chip-access rules", (-20,16,38), 'High', 'Core holding'),
 ('AVGO', "Custom AI chips plus networking: revenue +86% at about 18x forward earnings, 28% below its high. Best-held big chip name over the month (+3%); results Dec 9.",
  "Q4 results Dec 9", "Lumpy custom-chip orders; AI financing worries", (-24,17,42), 'High', 'Leader'),
 ('MU', "Memory is still the tightest part of AI servers: revenue +379% at about 3.4x forward earnings, 42% off its high. Nvidia and Anthropic purchase commitments both lean on memory.",
  "FQ1 results Dec 23", "DRAM lawsuit; memory falls hard when prices turn", (-40,18,58), 'Medium', 'Cycle leader'),
 ('NVDA', "About 9x forward earnings after a beat and raise, 38% off its high (RSI 17). Gave up an early 4% gain again today. Reports say part of the board wants Huang back.",
  "CEO decision; estimate upgrades", "Leadership vacuum; SEC probe; chip-export rules", (-30,14,50), 'Medium', 'Cheap leader, leadership risk'),
 ('COHR', "Coherent: ~$20B five-year optics deal and, per reports, a new $2B buyback. 49% below its high at about 14x forward earnings; rose 2% while chips fell.",
  "Buyback; FQ2 results (Feb)", "7-8% daily swings", (-35,18,55), 'Medium', 'Optics rebound'),
]
P[('long','ai','SGX')] = [
 ('AWX.SI', "AEM fell 4.1% as Singapore data-centre chip rules weigh, but is up ~265% this year, 44% off its high, with about 110% analyst upside.",
  "Q3 business update (Nov)", "One large customer; US chip-access rule for SG data centres", (-40,15,55), 'Medium', 'SGX AI leader'),
 ('V03.SI', "Venture: net cash, about 15x earnings, low volatility; analysts see about 30% upside.",
  "Analyst upgrades after Q3", "Slow revenue growth (+7%)", (-12,12,25), 'High', 'Steady value'),
 ('558.SI', "UMS makes precision parts for chip-equipment makers: revenue +61%, 41% off its high, about 17x earnings.",
  "Chip-equipment spending outlook", "Tied to Applied Materials spending", (-32,15,45), 'Medium', 'Equipment supplier'),
 ('5DD.SI', "Micro-Mechanics: revenue +45%, 38% off its high; rose 2.6% and is up 5% this week against the market.",
  "Q1 FY27 results (Nov)", "Small and thinly traded", (-24,13,36), 'Medium', 'Growth at a discount'),
 ('E28.SI', "Frencken builds modules for chip and medical equipment; 52% off its high at about 14x earnings (RSI 28).",
  "Q3 business update (Nov)", "Flat revenue so far this year", (-26,12,36), 'Medium', 'Recovery'),
]
P[('swing','ai','US')] = [
 ('AVGO', "Held up best among big chips this month; results on Dec 9 fall inside the swing window.",
  "Q4 results Dec 9", "Broad AI selling (Nasdaq -2.25%)", (-13,5,17), 'Medium', 'Relative strength into results'),
 ('COHR', "Rose 2.1% on a down day after reports of a new $2B buyback (RSI 52).", "Buyback support", "Optics sector swings", (-14,6,18), 'Medium', 'Buyback support'),
 ('LITE', "Marvell is buying Lumentum for 4.5 Marvell shares each; at snapshot prices that is worth about 18% more than LITE's price (RSI 26).",
  "Spread narrows if the deal clears", "Regulatory delay (incl. China); MRVL falls again", (-15,8,22), 'Medium', 'Merger spread'),
 ('MU', "RSI 34; about 3.4x forward earnings; results Dec 23 just outside the window.",
  "Memory price data", "AI capex fears", (-16,6,22), 'Medium', 'Rebound'),
 ('WDC', "Western Digital rose 4.1% (RSI 35) at about 7x forward earnings; storage led today's early AI bounce.",
  "Storage pricing", "Gave back gains late with the market", (-16,6,20), 'Speculative', 'Oversold rebound'),
]
P[('swing','ai','SGX')] = [
 ('5DD.SI', "Micro-Mechanics rose 2.6%; +5% this week (RSI 43).", "Q1 FY27 results", "Thin trading", (-10,4,12), 'Medium', 'Relative strength'),
 ('V03.SI', "Venture RSI 41; the steadiest name in the group.", "Analyst upgrades", "Low growth", (-6,3,9), 'High', 'Range'),
 ('558.SI', "UMS RSI 34 after a 24% one-month drop.", "Chip-equipment read-across", "Chip-equipment sentiment", (-15,5,18), 'Medium', 'Oversold'),
 ('AWX.SI', "AEM fell 4.1% (RSI 34); wait for the selling to settle.", "Q3 update", "US chip rule for SG data centres", (-20,5,25), 'Speculative', 'Oversold, falling'),
 ('E28.SI', "Frencken RSI 28.", "Bounce", "Flat revenue", (-12,4,14), 'Speculative', 'Oversold rebound'),
]
P[('intraday','ai','US')] = [
 ('COHR', "Up 2.1% on buyback reports while chips fell.", "Buyback", "Late market slide", (-4,0.5,4.5), 'Medium', 'Relative strength'),
 ('WDC', "Up 4.1% at the snapshot.", "Storage momentum", "Faded with the market", (-5,0.3,5), 'Speculative', 'Momentum check'),
 ('STX', "Up 3.1% at the snapshot.", "Storage momentum", "Faded with the market", (-5,0.3,5), 'Speculative', 'Momentum check'),
 ('AMD', "Fell ~8-9% on the Hunterbrook report (allegations).", "AMD response", "More selling; export-control follow-up", (-6,0.5,6), 'Speculative', 'News-driven dip'),
 ('NVDA', "RSI 17; gave up a 4% opening gain.", "Dip buying", "More AI selling", (-4,0.3,4), 'Speculative', 'Oversold watch'),
]
P[('intraday','ai','SGX')] = [
 ('5DD.SI', "Rose 2.6%.", "Next session", "Thin trading", (-3,0.3,3), 'Medium', 'Follow-through check'),
 ('V03.SI', "Eased 0.8%.", "Next session", "US tech fell 2% overnight", (-2,0.2,2), 'Medium', 'Range'),
 ('AWX.SI', "Fell 4.1%.", "Next session", "US chips weak again", (-6,0.3,6), 'Speculative', 'Bounce watch'),
 ('558.SI', "Eased 0.6%.", "Next session", "Follows US chip equipment", (-4,0.2,4), 'Speculative', 'Range'),
 ('MZH.SI', "Nanofilm RSI 23.", "Next session", "Thin trading", (-3,0.2,3), 'Speculative', 'Bounce watch'),
]

# ---------- Health ----------
P[('long','hc','US')] = [
 ('LLY', "Obesity-drug leader: revenue +39%, 6% off its high (+26% this year). Little analyst upside left, so the base case is modest. Not exposed to the Medicare Advantage audit rule.",
  "Orforglipron launch; Q4 results (Feb)", "Drug-price policy", (-16,8,25), 'High', 'Defensive growth'),
 ('ARGX', "argenx: revenue +52% from Vyvgart, 11% off its high, 22% analyst upside; low daily swings (2%).",
  "New indications in 2027", "Competition in myasthenia gravis", (-15,10,28), 'Medium', 'Growth leader'),
 ('MDGL', "Madrigal's liver drug Rezdiffra is growing fast (revenue +50%); 34% off its high with 73% analyst upside.",
  "Script data; EU rollout", "Competition from GLP-1 drugs", (-22,20,45), 'Medium', 'Oversold growth'),
 ('INSM', "Insmed jumped ~19% on a report that Sanofi is weighing a takeover (unconfirmed). Lung-drug launch drives revenue +268%. The report puts a soft floor under the stock but caps upside if a deal comes.",
  "Takeover talks; Brinsupri launch numbers", "No deal: the jump fades", (-28,12,35), 'Medium', 'Takeover candidate'),
 ('VRTX', "Vertex: steady growth (+12%), 6% off its high, about 26x earnings; RSI 31 after a 2.4% dip.",
  "Pain-drug launch; kidney data", "Valuation", (-14,9,22), 'Medium', 'Steady growth'),
]
P[('long','hc','SGX')] = [
 ('Q0F.SI', "IHH runs hospitals across Asia; analysts see 36% upside. Flat ahead of Q3 results.", "Q3 results Nov 25", "Currency swings", (-12,11,24), 'Medium', 'Regional leader'),
 ('C2PU.SI', "Parkway Life REIT: steady hospital and nursing-home rents, 8% off its high.", "Dividend", "US rates (10-yr at 5%)", (-8,7,15), 'High', 'Income'),
 ('AP4.SI', "Riverstone rose 5.6% after Q3 revenue hit a 3-year high (profit +35%); about 14x earnings with 22% analyst upside.", "New CEO from Dec 1", "Glove price competition", (-15,10,26), 'Medium', 'Value with momentum'),
 ('BSL.SI', "Raffles Medical: Singapore hospital group, 22% off its high, steady (RSI 59).", "Results (Feb)", "Shrinking revenue (-7%)", (-10,8,18), 'Medium', 'Recovery'),
 ('H02.SI', "Haw Par (Tiger Balm) trades near 10x earnings with a large cash and investment pile; 34% off its high.", "Results (Feb)", "Revenue down 8%", (-12,6,16), 'Medium', 'Value'),
]
P[('swing','hc','US')] = [
 ('LLY', "Near its high; no Medicare Advantage exposure while insurers sell off.", "Orforglipron news", "Drug-price headlines", (-8,3,10), 'High', 'Defensive'),
 ('ARGX', "Flat on a down day (RSI 60), 11% off its high.", "Momentum", "Biotech risk-off", (-7,3,9), 'Medium', 'Relative strength'),
 ('MDGL', "RSI 36; 73% analyst upside.", "Script data", "Biotech risk-off", (-12,6,18), 'Medium', 'Rebound'),
 ('INSM', "Up ~19% on Sanofi takeover talk; swings both ways until a deal is confirmed or denied.", "Deal confirmation", "Denial; fade", (-18,4,15), 'Speculative', 'Event-driven'),
 ('UNH', "Down 17.5% in five days on the CMS audit proposal (RSI 22), now about 14x forward earnings. The rule is only a proposal.",
  "2027 outlook; comment period to Jan 19", "Rule finalised as written; more insurer selling", (-15,4,18), 'Speculative', 'Policy-shock rebound'),
]
P[('intraday','hc','US')] = [
 ('INSM', "Up ~19% on takeover talk.", "Deal news", "Profit-taking", (-6,0.5,6), 'Speculative', 'Event-driven'),
 ('MRNA', "Up 3.3% against the market.", "Momentum", "5% daily swings", (-5,0.3,5), 'Speculative', 'Momentum'),
 ('UNH', "Fell 4.5% more (RSI 22).", "Dip buying", "More insurer selling", (-4,0.3,4), 'Speculative', 'Bounce watch'),
 ('ARGX', "Flat on a weak day.", "Defensive bid", "Small range", (-2,0.2,2), 'Medium', 'Relative strength'),
 ('LLY', "Eased 1.9%.", "Defensive bid", "Rotation", (-2.3,0.2,2.3), 'Medium', 'Range'),
]
P[('swing','hc','SGX')] = [
 ('Q0F.SI', "IHH flat (RSI 42) ahead of Q3 results.", "Q3 results Nov 25", "Results miss", (-6,3,9), 'Medium', 'Pre-earnings'),
 ('AP4.SI', "Riverstone +5.6% after strong Q3 (RSI 54).", "Follow-through", "Glove prices", (-8,4,11), 'Medium', 'Post-results momentum'),
 ('C2PU.SI', "Parkway Life REIT: lowest-volatility name in the group.", "Dividend", "Rates", (-4,2,6), 'High', 'Range'),
 ('BSL.SI', "Raffles Medical holding up (RSI 59).", "Momentum", "Low volume", (-5,2,6), 'Medium', 'Trend'),
 ('QC7.SI', "Q&M Dental is very oversold (RSI 8).", "Bounce", "Small cap", (-8,3,10), 'Speculative', 'Oversold rebound'),
]
P[('intraday','hc','SGX')] = [
 ('AP4.SI', "Rose 5.6% after results.", "Next session", "Profit-taking", (-3,0.4,3), 'Medium', 'Follow-through check'),
 ('Q0F.SI', "Flat ahead of results.", "Next session", "Malaysia market swings", (-2,0.3,2), 'Medium', 'Range'),
 ('C2PU.SI', "Eased 0.3%.", "Next session", "Small range", (-1,0.2,1), 'Medium', 'Range'),
 ('BSL.SI', "Flat.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('H02.SI', "Eased 1.3% (RSI 25).", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Bounce watch'),
]

# ---------- Finance ----------
P[('long','fin','US')] = [
 ('JPM', "Best-run US bank, 12% off its high at about 12.5x forward earnings. Higher rates support interest income. Vendor breach disclosed today touched only limited contact data.", "Q4 results Jan 14", "Credit cycle; market slide", (-15,8,22), 'High', 'Core holding'),
 ('V', "Visa: steady growth (+13%), 8% off its high; little AI exposure. Same vendor breach as JPM (no card data).", "Holiday spending", "Regulation of card fees", (-12,6,18), 'High', 'Defensive growth'),
 ('GS', "About 11.5x forward earnings, 26% off its high; led Anthropic's record ~$81B IPO, which closed +17% on day one.",
  "IPO fees; Q4 results Jan 19", "Market volatility hits deals", (-20,10,28), 'Medium', 'Cyclical value'),
 ('NU', "Nubank: revenue +34% at about 11x forward earnings, 37% off its high; 50% analyst upside.", "Q4 results (Feb)", "Brazil credit and currency; strong dollar", (-30,16,48), 'Medium', 'Growth at a discount'),
 ('SE', "Sea: revenue +43%; $1B buyback. About 14x forward earnings, 53% off its high.",
  "Q4 results (Mar)", "Rising credit costs at Monee; competition", (-30,18,50), 'Medium', 'Oversold growth'),
]
P[('long','fin','SGX')] = [
 ('D05.SI', "DBS kept its 81-cent quarterly dividend and says interest income has bottomed; 15% off its high (RSI 19), rose 0.5% today.",
  "Q4 results (Feb)", "Margins if rates fall; stronger SGD", (-10,8,16), 'High', 'Income leader'),
 ('O39.SI', "OCBC was the only local bank to beat in Q3 and raised loan-growth guidance.",
  "Q4 results (Feb)", "Margin fell 18 bp to 1.66%", (-10,7,15), 'Medium', 'Income'),
 ('U11.SI', "UOB missed Q3 and cut its margin guidance; RSI 12, 20% off its high.", "Recovery in fees", "More credit provisions", (-12,7,17), 'Medium', 'Oversold income'),
 ('AIY.SI', "iFAST: fintech platform, revenue +23%, 29% off its high with 47% analyst upside.", "HK pension business", "Market-driven volumes", (-18,16,36), 'Medium', 'Growth'),
 ('S68.SI', "SGX benefits from high trading volumes; from Jan 2027 its RegCo takes over IPO prospectus reviews.", "Monthly volume data", "Already priced (24x earnings)", (-12,7,18), 'Medium', 'Volatility winner'),
]
P[('swing','fin','US')] = [
 ('SCHW', "Schwab is up this week while banks fell (RSI 65); about 12x forward earnings, 26% analyst upside.", "Monthly client metrics", "Market swings", (-8,3,10), 'Medium', 'Relative strength'),
 ('APO', "Apollo rose 0.6% on a down day (RSI 53).", "Private-credit flows", "Credit worries", (-9,3,11), 'Medium', 'Relative strength'),
 ('GS', "Anthropic fees; RSI 42.", "Deal fees", "Volatility", (-9,4,12), 'Medium', 'Deal pipeline'),
 ('MA', "Mastercard 6.5% off its high (RSI 47); breach was at a vendor.", "Holiday spending data", "Breach headlines", (-6,2,7), 'High', 'Steady'),
 ('HOOD', "RSI 32 after a 14% five-day drop; rose 1.4% as retail traded the Anthropic debut.", "Retail volumes", "Crypto weakness", (-18,6,24), 'Speculative', 'Oversold rebound'),
]
P[('swing','fin','SGX')] = [
 ('D05.SI', "DBS is oversold (RSI 19) and rose 0.5%.", "Dividend support", "Margin worries", (-4,3,7), 'High', 'Oversold income'),
 ('U11.SI', "UOB RSI 12.", "Rebound", "Further downgrades", (-5,3,8), 'Medium', 'Oversold rebound'),
 ('O39.SI', "OCBC RSI 27.", "Post-results recovery", "Margin squeeze", (-4,2,6), 'Medium', 'Pullback'),
 ('AIY.SI', "iFAST RSI 48.", "Momentum", "Market-driven", (-8,3,10), 'Medium', 'Range'),
 ('S68.SI', "SGX benefits when markets are volatile.", "Volume data", "Valuation", (-5,2,7), 'Medium', 'Volatility winner'),
]
P[('intraday','fin','US')] = [
 ('HOOD', "Up 1.4% on Anthropic retail trading.", "Retail volumes", "Crypto weakness", (-5,0.4,5), 'Speculative', 'Momentum'),
 ('COIN', "Up 1.6% (RSI 29).", "Crypto bounce", "Bitcoin ~$62k, still weak", (-5,0,5), 'Speculative', 'Crypto beta'),
 ('APO', "Up 0.6% on a weak day.", "Momentum", "Small range", (-2.5,0.2,2.5), 'Medium', 'Relative strength'),
 ('KLAR', "Fell 10%; no clear news found.", "Bounce", "More selling", (-5,0,5), 'Speculative', 'Bounce watch'),
 ('JPM', "Fell 1.1%; vendor breach disclosed.", "Dip buying", "Bank weakness", (-2,0.2,2), 'Medium', 'Dip watch'),
]
P[('intraday','fin','SGX')] = [
 ('D05.SI', "Rose 0.5%; RSI 19.", "Next session", "US slide overnight", (-1.3,0.3,1.4), 'High', 'Bounce watch'),
 ('U11.SI', "Flat; RSI 12.", "Next session", "Trend down", (-1.5,0.2,1.5), 'Medium', 'Bounce watch'),
 ('O39.SI', "Flat.", "Next session", "Small range", (-1.3,0.2,1.3), 'Medium', 'Range'),
 ('S68.SI', "Up 0.2%.", "Next session", "Small range", (-1.3,0.2,1.3), 'Medium', 'Range'),
 ('AIY.SI', "Flat.", "Next session", "Small range", (-1.8,0.2,1.8), 'Medium', 'Range'),
]

# IPO tab (6-month view), all markets
P[('ipo','all','US')] = [
 ('SPCX', "SpaceX (IPO $135) trades about 2% above its IPO price, 35% under its high; fell ~4% with tech today.",
  "Starship progress; lock-up expiries", "Valuation and Musk headlines", (-35,12,45), 'Medium', 'Mega-cap IPO'),
 ('CHYM', "Chime (IPO $27) trades about 16% above its IPO price, 10% off its high (RSI 66).",
  "Member growth", "Fintech credit cycle", (-18,8,25), 'Medium', 'Post-IPO uptrend'),
 ('KLAR', "Klarna (IPO $40) fell 10% to about $13, 67% below its IPO price at about 20x forward earnings; back to profit in Q3.",
  "Holiday volumes; Q4 results Feb 18", "Buy-now-pay-later credit losses", (-30,12,40), 'Speculative', 'Deep value'),
 ('ASBH', "American Savings Bank (IPO $16) is up 28% (RSI 65) with low swings for a new listing.",
  "Q4 results", "Bank-sector selling", (-12,6,16), 'Medium', 'Steady post-IPO'),
 ('ACCV', "Accelevation (IPO $18) makes electrical gear for data centres: revenue +66% at about 9x forward earnings, but 39% below its IPO price.",
  "Order updates", "Data-centre slowdown; 9% daily swings", (-40,10,50), 'Speculative', 'Post-IPO value'),
]

# ---------- Power & grid (data-center power) ----------
P[('long','pwr','US')] = [
 ('GEV', "GE Vernova: gas turbines and grid gear sold out for years, revenue +27%. 35% off its high with 53% analyst upside.", "Q4 results Jan 27", "Data-centre policy; valuation (29x)", (-25,15,40), 'High', 'Quality at a discount'),
 ('CEG', "Constellation beat Q3 and raised 2026 guidance; 33% off its high.", "New long-term power deals", "Data-centre politics; PJM rules", (-22,13,32), 'High', 'Beat and raise'),
 ('ETN', "Eaton: electrical gear for data centres and utilities, 27% off its high at about 20x earnings.", "Q4 results Feb 2", "Data-centre orders slowing", (-20,13,33), 'Medium', 'Quality at a discount'),
 ('PWR', "Quanta builds the grid: revenue +57%, 24% off its high; held up better than peers this week (-2%).", "Utility capex plans", "Data-centre policy", (-25,12,34), 'Medium', 'Grid builder'),
 ('VRT', "Vertiv: data-centre cooling and power, revenue +61% at about 19x forward earnings, 50% off its high; fell 3.6%.", "Order backlog updates", "Most exposed to a data-centre slowdown", (-35,18,52), 'Medium', 'Oversold growth'),
]
P[('long','pwr','SGX')] = [
 ('BN4.SI', "Keppel: power, data centres and asset management, about 15x earnings with 40% analyst upside (RSI 24).", "Asset sales", "Execution; SG data-centre chip rule", (-13,12,25), 'Medium', 'Value'),
 ('U96.SI', "Sembcorp: power and renewables at about 9x earnings.", "New contracts", "Power prices", (-12,7,18), 'Medium', 'Value'),
 ('DCRU.SI', "Digital Core REIT: US data-centre REIT, about 9x earnings with 55% analyst upside; rose 1.2%.", "Leasing news", "Tenant concentration; US rates", (-14,11,27), 'Medium', 'Deep value'),
 ('AJBU.SI', "Keppel DC REIT: data-centre rents, 10% off its high (RSI 59).", "Dividend", "Rates", (-10,7,17), 'Medium', 'Income'),
 ('544.SI', "CSE Global: electrification and data-centre work, about 9x earnings, 57% off its high; rose 2.7%.", "New orders", "Small and volatile", (-30,14,45), 'Speculative', 'Recovery'),
]
P[('swing','pwr','US')] = [
 ('NEE', "NextEra: up 7% in a month (RSI 51); regulated utility earnings.", "Renewables deals", "Yields at 5%", (-6,3,8), 'Medium', 'Defensive'),
 ('TLN', "Talen RSI 54, flat over the month; about 11x forward earnings.", "Capacity deals", "Data-centre politics", (-13,5,16), 'Medium', 'Relative strength'),
 ('PWR', "Quanta RSI 46; the steadiest name in AI power.", "Utility capex", "Data-centre policy", (-10,4,13), 'Medium', 'Support'),
 ('GEV', "GE Vernova RSI 39, down 17% in a month.", "Order news", "AI capex fears", (-14,6,20), 'Medium', 'Oversold rebound'),
 ('VST', "Vistra RSI 41 after a 20% monthly drop; 59% analyst upside.", "Analyst updates", "Texas data-centre proposal", (-14,6,20), 'Medium', 'Oversold rebound'),
]
P[('swing','pwr','SGX')] = [
 ('AJBU.SI', "Keppel DC REIT up 5% in a month (RSI 59).", "Momentum", "Rates", (-5,1.5,6), 'Medium', 'Trend'),
 ('DCRU.SI', "Digital Core REIT rose 1.2% (RSI 50).", "Support", "US data-centre worries", (-7,2,8), 'Medium', 'Range'),
 ('BN4.SI', "Keppel RSI 24.", "Asset-sale news", "Execution", (-6,3,9), 'Medium', 'Oversold rebound'),
 ('U96.SI', "Sembcorp RSI 36.", "Contracts", "Power prices", (-5,2,7), 'Medium', 'Oversold'),
 ('544.SI', "CSE Global bounced 2.7% after a 13% five-day drop.", "New orders", "No floor yet", (-15,3,16), 'Speculative', 'Base building'),
]
P[('intraday','pwr','US')] = [
 ('NRG', "Up 0.8% on a weak day.", "Momentum", "Gives back gains", (-4,0.3,4), 'Medium', 'Relative strength'),
 ('BE', "Flat after a 15% five-day drop.", "Bounce", "8% daily swings", (-6,0.3,6), 'Speculative', 'Bounce watch'),
 ('NEE', "Eased 1%.", "Defensive bid", "Small range", (-1.8,0.2,1.8), 'Medium', 'Range'),
 ('VRT', "Fell 3.6%.", "Bounce", "AI hardware selling", (-6,0.3,6), 'Speculative', 'Bounce watch'),
 ('CEG', "Fell 2.7%.", "Bounce", "Power stocks follow AI", (-4,0.3,4), 'Medium', 'Bounce watch'),
]
P[('intraday','pwr','SGX')] = [
 ('544.SI', "Rose 2.7%.", "Next session", "Small cap", (-4,0.2,4), 'Speculative', 'Follow-through check'),
 ('DCRU.SI', "Rose 1.2%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('BN4.SI', "Eased 0.3% (RSI 24).", "Next session", "More selling", (-1.8,0.3,2), 'Medium', 'Bounce watch'),
 ('U96.SI', "Flat.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('AJBU.SI', "Eased 0.5%.", "Next session", "Small range", (-1.2,0.2,1.2), 'Medium', 'Range'),
]

# ---------- Defence & industrials ----------
P[('long','def','US')] = [
 ('GE', "GE Aerospace: jet-engine services boom, revenue +16%, 16% off its high; up 9% in a month.", "Q4 results Jan 21", "Valuation (34x)", (-15,10,26), 'High', 'Quality'),
 ('RTX', "RTX: missiles and engines, revenue +11%, steady; 17% analyst upside.", "Q4 results Jan 26", "Engine issues", (-12,10,24), 'High', 'Core defence'),
 ('HWM', "Howmet: jet-engine parts, revenue +29%, 25% off its high with 35% analyst upside (RSI 61).", "Aerospace build rates", "Valuation (33x)", (-20,14,34), 'Medium', 'Growth at a discount'),
 ('LHX', "L3Harris: space and missile sensors, 32% off its high, 30% analyst upside; rose on a weak day.", "Golden Dome contracts", "Budget fights with a split government", (-15,12,30), 'Medium', 'Value'),
 ('NOC', "Northrop: B-21 and missile defence, about 18x earnings, 29% off its high; rose on a weak day.", "Golden Dome contracts", "Budget fights", (-15,10,27), 'Medium', 'Value'),
]
P[('long','def','SGX')] = [
 ('S63.SI', "ST Engineering: record S$37.7B order book and nine-month revenue +10%. Bounced 1.2% from RSI 21; 31% analyst upside.", "Contract wins; FY results (Feb)", "Valuation (22x)", (-12,12,26), 'High', 'Quality on a dip'),
 ('BS6.SI', "Yangzijiang Shipbuilding: about 7x earnings, revenue +36%; 17% off its high.", "New ship orders", "US port fees on Chinese ships", (-18,14,32), 'Medium', 'Value'),
 ('S59.SI', "SIA Engineering: aircraft maintenance, 25% off its high, 32% analyst upside.", "Air travel", "Revenue falling (-11%)", (-10,10,24), 'Medium', 'Recovery'),
 ('C52.SI', "ComfortDelGro: steady transport earnings at about 13.5x; rose 0.8%.", "Overseas contracts", "Slow growth", (-8,7,15), 'Medium', 'Steady'),
 ('H22.SI', "Hong Leong Asia: engines and building materials at about 8x earnings, 49% off its high.", "Results (Feb)", "China demand", (-25,20,50), 'Speculative', 'Deep value'),
]
P[('swing','def','US')] = [
 ('HWM', "Howmet RSI 61, up 5.5% in a month.", "Aerospace data", "Valuation", (-8,4,11), 'Medium', 'Relative strength'),
 ('NOC', "Northrop rose on a weak day (RSI 43).", "Golden Dome contracts", "Budget fights", (-7,3,9), 'Medium', 'Support'),
 ('AXON', "Rose 3.8% from RSI 21 after a Q3 miss; 74% analyst upside.", "Analyst updates", "More downgrades", (-18,6,22), 'Speculative', 'Post-earnings rebound'),
 ('LHX', "L3Harris up 4% in a month (RSI 34 after a dip).", "Contracts", "Budget fights", (-7,3,9), 'Medium', 'Pullback'),
 ('BA', "Boeing 36% off its high (RSI 34); production recovering.", "Monthly deliveries", "Quality issues", (-10,5,15), 'Medium', 'Recovery'),
]
P[('swing','def','SGX')] = [
 ('S63.SI', "ST Engineering bounced 1.2% from RSI 21.", "Contract wins", "Holder selling; downgrade", (-6,4,10), 'Medium', 'Oversold rebound'),
 ('BS6.SI', "Yangzijiang flat over five days (RSI 42).", "Orders", "Trade fees", (-8,4,12), 'Medium', 'Support'),
 ('H22.SI', "Hong Leong Asia RSI 22.", "Bounce", "China demand", (-10,4,12), 'Speculative', 'Oversold rebound'),
 ('S59.SI', "SIA Engineering RSI 32.", "Air travel", "Slow growth", (-6,2,7), 'Medium', 'Range'),
 ('C52.SI', "ComfortDelGro steady (RSI 42).", "Support", "Slow growth", (-4,1.5,5), 'Medium', 'Range'),
]
P[('intraday','def','US')] = [
 ('AXON', "Up 3.8% (RSI 21).", "Bounce", "Gives back gains", (-4,0.3,4), 'Speculative', 'Momentum'),
 ('LHX', "Up 0.5% on a weak day.", "Defensive bid", "Small range", (-2.2,0.2,2.2), 'Medium', 'Relative strength'),
 ('NOC', "Up 0.4% on a weak day.", "Defensive bid", "Small range", (-1.8,0.2,1.8), 'Medium', 'Relative strength'),
 ('KTOS', "Down 13% in five days (RSI 24).", "Drone contracts", "Volatile", (-4.5,0,4.5), 'Speculative', 'Bounce watch'),
 ('CAT', "Fell 3%.", "Bounce", "Data-centre generator worries", (-3.5,0.2,3.5), 'Medium', 'Bounce watch'),
]
P[('intraday','def','SGX')] = [
 ('S63.SI', "Rose 1.2% (RSI 24).", "Next session", "US slide overnight", (-2.5,0.4,2.8), 'Medium', 'Follow-through check'),
 ('C52.SI', "Rose 0.8%.", "Next session", "Small range", (-1.2,0.2,1.2), 'Medium', 'Range'),
 ('BS6.SI', "Eased 0.7%.", "Next session", "Small range", (-2.5,0.2,2.5), 'Medium', 'Range'),
 ('H22.SI', "Eased 0.5% (RSI 22).", "Next session", "Thin trading", (-3,0.3,3), 'Speculative', 'Bounce watch'),
 ('S59.SI', "Up 0.4%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
]

# ---------- Energy (oil and gas) ----------
P[('long','nrg','US')] = [
 ('CVX', "Chevron: revenue +35%, about 12.5x earnings, 12% off its high; steadied as WTI rose 1% to ~$83 (RSI 20).", "Hess integration; buybacks", "Oil falls further on stock builds", (-16,8,24), 'High', 'Core energy'),
 ('XOM', "Exxon: steady cash flow, about 13x earnings, 16% analyst upside (RSI 17).", "Buybacks", "Oil price drop", (-15,7,21), 'High', 'Core energy'),
 ('LNG', "Cheniere: US gas exports on long contracts; less tied to oil. 11% off its high.", "New export capacity", "Gas price swings", (-15,8,24), 'Medium', 'Steady'),
 ('FANG', "Diamondback: low-cost Permian producer at about 8x earnings, 35% analyst upside (RSI 17); rose 1.1%.", "Buybacks", "Oil price drop", (-22,12,32), 'Medium', 'Value'),
 ('EOG', "EOG: about 9x earnings, revenue +43%, 10% off its high.", "Buybacks", "Oil price drop", (-16,7,22), 'Medium', 'Value'),
]
P[('long','nrg','SGX')] = [
 ('5E2.SI', "Seatrium builds offshore rigs and wind platforms; 46% analyst upside.", "New orders", "Contract delays", (-15,12,28), 'Medium', 'Recovery'),
 ('BN4.SI', "Keppel: energy infrastructure and asset management.", "Asset sales", "Execution", (-13,10,22), 'Medium', 'Value'),
 ('5LY.SI', "Marco Polo Marine: offshore vessels, revenue +40% at about 10x earnings.", "Results (Nov)", "Thin trading", (-25,10,35), 'Speculative', 'Growth value'),
 ('RE4.SI', "Geo Energy rose another 9.5% to S$0.46 after saying there was no new Indonesian mining directive; about 6x earnings.", "Q3 update", "Indonesian policy risk", (-35,8,40), 'Speculative', 'Rebound'),
 ('5WH.SI', "Rex International is in a long downtrend (-65% this year); no setup.", "None", "Further losses", (-30,-5,20), 'Speculative', 'Avoid'),
]
P[('swing','nrg','US')] = [
 ('FANG', "Diamondback oversold (RSI 17) and rose 1.1%.", "Buybacks", "Oil price drop", (-11,4,13), 'Medium', 'Oversold rebound'),
 ('HAL', "Halliburton rose 1.7% from RSI 28.", "Service pricing", "Oil price drop", (-10,4,12), 'Medium', 'Oversold rebound'),
 ('CVX', "Chevron RSI 20.", "Buybacks", "More inventory builds", (-8,3,9), 'Medium', 'Oversold'),
 ('LNG', "Cheniere up 4% in a month (RSI 32); gas exports, not crude.", "Export capacity", "Gas price swings", (-8,3,10), 'Medium', 'Relative strength'),
 ('DVN', "Devon RSI 23; about 8x earnings, 42% analyst upside.", "Buybacks", "Oil price drop", (-12,4,14), 'Medium', 'Oversold rebound'),
]
P[('intraday','nrg','US')] = [
 ('HAL', "Up 1.7%.", "Oil +1%", "Gives back gains", (-2.5,0.2,2.5), 'Medium', 'Momentum'),
 ('FANG', "Up 1.1% (RSI 17).", "Oil +1%", "Oil reverses", (-2.5,0.2,2.5), 'Medium', 'Bounce'),
 ('CVX', "Up 0.4% (RSI 20).", "Oil +1%", "Small range", (-2,0.2,2), 'Medium', 'Bounce'),
 ('OXY', "Flat (RSI 19).", "Oil bounce", "Oil reverses", (-2.5,0.2,2.5), 'Speculative', 'Bounce watch'),
 ('XOM', "Fell 1% (RSI 17).", "Dip buying", "Oil reverses", (-2,0.2,2), 'Medium', 'Bounce watch'),
]
P[('swing','nrg','SGX')] = [
 ('5E2.SI', "Seatrium rose 0.6% (RSI 37).", "Orders", "Delays", (-8,3,10), 'Medium', 'Support'),
 ('RE4.SI', "Geo Energy rose 9.5% again after the company's clarification.", "Follow-through", "Policy risk; bounce fades", (-25,4,25), 'Speculative', 'Rebound'),
 ('BN4.SI', "Keppel RSI 24.", "Asset sales", "Execution", (-6,3,9), 'Medium', 'Oversold rebound'),
 ('5LY.SI', "Marco Polo Marine flat (RSI 40).", "Results", "Thin trading", (-10,3,12), 'Speculative', 'Range'),
 ('5WH.SI', "Rex International: no setup.", "None", "Further losses", (-12,-2,8), 'Speculative', 'Avoid'),
]
P[('intraday','nrg','SGX')] = [
 ('RE4.SI', "Rose 9.5% for a second day.", "Next session", "Bounce fades", (-8,0.5,8), 'Speculative', 'Follow-through check'),
 ('5E2.SI', "Rose 0.6%.", "Next session", "Oil weakness", (-2,0.2,2), 'Medium', 'Range'),
 ('BN4.SI', "Eased 0.3%.", "Next session", "Small range", (-1.8,0.3,2), 'Medium', 'Bounce watch'),
 ('5LY.SI', "Flat.", "Next session", "Thin trading", (-4,0,4), 'Speculative', 'Range'),
 ('5WH.SI', "Penny stock in a downtrend; avoid.", "None", "Further losses", (-5,-1,4), 'Speculative', 'Avoid'),
]

IPO_LIST = [
 # sym, name, ipo_date, ipo_price, sector, status
 ('ANT','Anthropic (Nasdaq: ANT; priced at $83, record ~$81B raised; opened $111.50, high $115.10, closed $97.17 (+17%) on day one)','2026-11-19',83.00,'ai','Listed'),
 ('TRCX','Tracx Logis ($18-22 range; 1M shares; not confirmed)','2026-11-23',None,'ai','Expected'),
 ('FBLLU','Football Manager SPAC (not confirmed)','2026-11-23',10.00,'fin','Expected'),
 ('BIAI','Bitari (not confirmed)','2026-11-30',7.00,'ai','Expected'),
 ('ABGC','American Barrick Gold (Barrick carve-out; ~$6B est.; filed week of Nov 9)','2026-11-13',None,'nrg','Filed'),
 ('YNTE','Primagrove ($4-6 range; not confirmed)','2026-11-16',None,'fin','Expected'),
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
 ('2026-11-19T20:00','COHR', "Via tracker: says Coherent announced a new $2B buyback and argues optical stocks are undervalued, pointing to its ~$20B long-term deals."),
 ('2026-11-19T19:00','ANT', "Via tracker: notes Anthropic's day-one valuation (~$1.7T at the time) is now well above Meta's."),
 ('2026-11-19T18:00','SOI', "Via tracker: says Soitec's photonics revenue pipeline jumped from about $25M to about $1.2B in agreements, citing strong optics demand."),
 ('2026-11-18T22:00','', "On X: cites Goldman prime data: hedge-fund momentum exposure fell from ~60% to 8%, with the heaviest tech selling in nine years before Nov 13."),
 ('2026-11-18T21:00','SNDK BE', "On X: says Leopold Aschenbrenner's early AI picks (SanDisk to Bloom Energy) were right, sees MLCC capacitors as a 2027 bottleneck, but says leverage and crowded longs hurt."),
 ('2026-11-18T18:00','AVGO MU AMD CRWV IREN', "Via tracker: lists ~$900B of Anthropic purchase agreements with chip and cloud suppliers and argues the IPO helps semis."),
 ('2026-11-18T15:00','NVDA', "Via tracker: shares a Semafor report that part of Nvidia's board wants Jensen Huang back as CEO."),
 ('2026-11-18T12:00','NVDA MU', "Via tracker: says Nvidia's $111B+ of memory buying is good news for Micron and SK Hynix."),
 ('2026-11-17T23:34','NVDA MU', "On X: reads Nvidia's call as 'demand far exceeds supply'; supply commitments rose from $279B to $390B, mostly multi-year memory buying."),
 ('2026-11-17T00:22','NVDA', "On X: says DeepSeek is rationing users for lack of compute, and calls compute shortages a bullish sign for AI infrastructure."),
 ('2026-11-15T19:19','NVDA', "On X: shares the FT report that Huang is discussing a comeback and calls it his 'redemption arc'."),
]

EVENTS = [
 ('2026-11-18','Macro','Dow -561 (-1.1%), S&P -0.2%, Nasdaq +0.4%', "FOMC minutes: almost all officials see further hikes as likely appropriate. WTI -4% on bigger US crude and gasoline builds."),
 ('2026-11-18','Health','CMS audit proposal hits insurers', "Proposed 'CRUSH' rule would extrapolate Medicare Advantage audit findings back to 2018. UNH -10%, HUM -13%. Comments until Jan 19, 2027."),
 ('2026-11-18','SGX','STI -1.1% to 5,054.89', "Fifth straight drop. New US rule requires Singapore and other SE Asian data centres to get licences for US AI chips."),
 ('2026-11-19','Macro','Dow -1,101 (-2.2%), S&P -2.0%, Nasdaq -2.25%', "Sixth straight S&P drop; Nasdaq reversed from +2% once Anthropic began trading. SOX -2.4%, VIX ~28. Jobless claims 203k; Philly Fed 6.3 with prices paid up to 58.2. 10-yr 5.05%."),
 ('2026-11-19','IPO','Anthropic debuts: $83 IPO, opens $111.50, closes $97.17', "Record ~$81B raised. Peaked at $115.10, then fell with the market; about $1.27T at the close."),
 ('2026-11-19','AI','AMD -8% on Hunterbrook report', "Report alleges customer backstops and firmware reaching an Entity-List server maker; unconfirmed. Coherent rose on a reported $2B buyback."),
 ('2026-11-19','Health','Insmed +19% on Sanofi takeover report', "Bloomberg says Sanofi is weighing a bid; neither company confirmed. UNH fell another 4.5%."),
 ('2026-11-19','Finance','Vendor breach at JPM, Visa, Mastercard', "Limited contact data exposed at third-party vendors; no card or payment data. Klarna -10%."),
 ('2026-11-19','SGX','AEM -4%, Riverstone +5.6%, Geo Energy +9.5%', "Riverstone Q3 revenue at a 3-year high (profit +35%). ST Engineering +1.2%, DBS +0.5%."),
 ('2026-11-20','Macro','Monthly options expiry', "VIX near 28 after Thursday's slide."),
 ('2026-11-23','IPO','Tracx Logis and Football Manager SPAC expected', "Not confirmed on major calendars."),
 ('2026-11-25','SGX','IHH Q3 results', "SIA goes ex-dividend (7 cents)."),
 ('2026-11-26','Macro','US Thanksgiving', "US stock market closed; early close (1pm ET) on Nov 27."),
 ('2026-12-01','AI','Marvell and Credo results', ""),
 ('2026-12-02','Defence','AeroVironment results', ""),
 ('2026-12-09','Macro','Fed rate decision (Dec 8-9)', "A hike is widely expected. Broadcom reports the same day."),
 ('2026-12-10','AI','Ciena results; TSMC November sales', ""),
 ('2026-12-23','AI','Micron FQ1 results', ""),
]
