# Analyst picks for 2026-11-17 SGT (snapshot: US Mon Nov 16 ~14:50 ET, SGX close Nov 16). Fields: sym, thesis, catalyst, risk, (low, base, high) % expected move, conviction, setup
# Horizons: long = 12 months, swing = ~4 weeks, intraday = rest of session (US) / next session (SGX), ipo = 6 months.
# Context: Fri Nov 13: S&P -0.4% to 7,562, Nasdaq -0.9%, Dow +0.1%. Chip index -3.4%: AMD -8.8%, Broadcom -4.8% (downgrade), Arm -4.6% (FT: Nvidia board approached Rene Haas),
# Cisco -6.2% and Applied Materials -2.7% despite beats. October PPI +0.3% m/m, +6.5% y/y. 10-yr 5.15%. A Dec Fed hike is fully priced. Modine +28% on Samsung talks report.
# Mon Nov 16: S&P -1.9% to ~7,417, Nasdaq -2.5%, Dow -1.4%, Russell -1.7%, VIX 23. Chips sold again on a new US rule on remote access to advanced chips (aimed at Chinese firms renting Nvidia compute abroad).
# NVDA -4% to ~$156 before Tuesday's results (down ~13% in five days); board reportedly not considering Huang's return even as Trump and Musk back it. Micron -7% as a judge let a DRAM supply lawsuit proceed. Intel -7% on a class action.
# Bitcoin ~$64K (lowest since July); Robinhood, Coinbase, Circle -6 to -8%. WTI -3.7% to ~$85 as Hormuz shipping recovers. Big banks -2% on app-outage reports. Altimeter to put $5B into the Anthropic IPO.
# SGX: STI -0.9% to 5,184.66. ST Engineering -6.6% to S$9.03 with no news (record S$37.7B order book in Friday's update). AEM -6%. Yangzijiang +2.6% (US$6.98B of orders vs a US$4.5B target).
# Geo Energy -23% to S$0.38; last trade 9:55am SGT and no announcement found.
P = {}

# ---------- AI & chips ----------
P[('long','ai','US')] = [
 ('TSM', "Makes almost every leading AI chip, whoever designs it. Revenue +51% at about 16x forward earnings, 23% below its high after a 6% drop on Nov 16. The Nvidia turmoil does not change TSMC's order book.",
  "November sales (~Dec 10); Q4 results Jan 14", "Taiwan geopolitics; new US chip-access rules", (-20,16,38), 'High', 'Core holding'),
 ('AVGO', "Custom AI chips plus networking: revenue +86% at about 17x forward earnings, 31% below its high after a downgrade and two down days.",
  "Q4 results Dec 9", "Lumpy custom-chip orders; AI financing worries", (-24,17,42), 'High', 'Leader, less key-person risk'),
 ('MU', "Memory is still the tightest part of AI servers: revenue +379% at about 3.5x forward earnings, 40% off its high. Fell 7% on Nov 16 after a judge let a DRAM supply lawsuit proceed.",
  "FQ1 results Dec 23", "Lawsuit; memory falls hard when prices turn", (-40,18,58), 'Medium', 'Cycle leader'),
 ('NVDA', "Revenue +106% at about 10x forward earnings, 35% off its high (RSI 16). The board reportedly won't bring back Jensen Huang; CFO Colette Kress is interim CEO. Cheap, but leadership risk caps the base case.",
  "Q3 results Nov 17 (~$109B revenue expected; options price ~10%); permanent CEO choice", "Strategy without Huang; governance probe; China rules", (-35,12,50), 'Speculative', 'Cheap, but leadership shock'),
 ('COHR', "Coherent: record quarter and a ~$20B five-year optics deal; 52% below its high at about 13x forward earnings.",
  "Optics orders; FQ2 results (Feb)", "8% daily swings; capex keeps rising", (-35,18,55), 'Medium', 'Optics rebound'),
]
P[('long','ai','SGX')] = [
 ('AWX.SI', "AEM is up ~290% this year but 40% below its high after a 6% drop on Nov 16; analysts see about 100% upside.",
  "Q3 business update (Nov)", "One large customer; 7% daily swings", (-40,16,55), 'Medium', 'SGX AI leader'),
 ('V03.SI', "Venture: net cash, about 15x earnings, low volatility; analysts see about 30% upside after a 22% rise in Q3 profit.",
  "Analyst upgrades after Q3", "Slow revenue growth (+7%)", (-12,12,25), 'High', 'Steady value'),
 ('558.SI', "UMS makes precision parts for chip-equipment makers: revenue +61%, 40% off its high, about 17x earnings.",
  "Applied Materials' upbeat outlook", "Tied to Applied Materials spending", (-32,15,45), 'Medium', 'Equipment supplier'),
 ('5DD.SI', "Micro-Mechanics makes precision tools for chip assembly and test: revenue +45%, 40% off its high.",
  "Q1 FY27 results (Nov)", "Small and thinly traded", (-24,13,36), 'Medium', 'Growth at a discount'),
 ('E28.SI', "Frencken builds modules for chip and medical equipment; 50% off its high at about 15x earnings.",
  "Q3 business update (Nov)", "Flat revenue so far this year", (-26,12,36), 'Medium', 'Recovery'),
]
P[('swing','ai','US')] = [
 ('NVDA', "RSI 16 after a 13% five-day drop into results; about 10x forward earnings. A solid quarter and outlook could spark a sharp bounce.",
  "Q3 results Nov 17 after the close", "Weak guidance or more leadership news", (-20,6,22), 'Speculative', 'Oversold into earnings'),
 ('LITE', "Marvell is buying Lumentum for 4.5 Marvell shares each. At snapshot prices that is worth about 20% more than LITE's price.",
  "Spread narrows if the deal clears", "Regulatory delay (incl. China); MRVL falls again", (-15,8,22), 'Medium', 'Merger spread'),
 ('MU', "Fell 7% to RSI 35 on the lawsuit headline; still about 3.5x forward earnings with price-floor contracts.",
  "FQ1 results Dec 23", "Lawsuit news; AI capex fears", (-16,7,22), 'Medium', 'Rebound'),
 ('TSM', "RSI 34 after a 6% drop; least exposed to who runs Nvidia.", "November sales (~Dec 10)", "Chip-rule headlines", (-10,5,14), 'Medium', 'Oversold leader'),
 ('AVGO', "RSI 48 after two down days; results on Dec 9 fall inside the swing window.",
  "Q4 results Dec 9", "Downgrade worries about AI financing", (-13,5,17), 'Medium', 'Pullback in leader'),
]
P[('swing','ai','SGX')] = [
 ('AWX.SI', "AEM fell 6% to RSI 42; down 24% in a month.", "Q3 update; Nvidia results", "Bounce fades if Nvidia disappoints", (-20,6,26), 'Speculative', 'Oversold rebound'),
 ('558.SI', "UMS fell 4% to RSI 39.", "Applied Materials read-across", "Chip-equipment sentiment", (-15,5,18), 'Medium', 'Oversold with catalyst'),
 ('V03.SI', "Venture eased 2% (RSI 42); the steadiest name in the group.", "Analyst upgrades", "Low growth", (-6,3,9), 'High', 'Pullback'),
 ('E28.SI', "Frencken fell 3% to RSI 37.", "Q3 business update (Nov)", "No clear catalyst", (-14,5,16), 'Speculative', 'Oversold rebound'),
 ('5DD.SI', "Micro-Mechanics RSI 34 after a 1% dip.", "Q1 FY27 results (Nov)", "Thin trading", (-12,4,14), 'Medium', 'Rebound'),
]
P[('intraday','ai','US')] = [
 ('NVDA', "Results come after Tuesday's close; the stock usually drifts with headlines into the print.", "Pre-earnings positioning", "Leadership headlines", (-4,0.5,4), 'Speculative', 'Pre-earnings'),
 ('MU', "Fell 7% on the lawsuit ruling.", "Bounce", "More legal headlines", (-5,0.3,5), 'Speculative', 'Bounce watch'),
 ('INTC', "Fell 7% on a shareholder class action (RSI 21).", "Bounce", "More selling", (-5,0,5), 'Speculative', 'Bounce watch'),
 ('AMD', "Fell 5% after an 8.8% drop on Friday; closed its $8.2B World Labs deal.", "Bounce", "Chip-rule headlines", (-5,0.3,5), 'Speculative', 'Range'),
 ('TSM', "Fell 6% on the chip-access rule.", "Bounce", "Taiwan selling", (-3.5,0.3,3.5), 'Medium', 'Bounce watch'),
]
P[('intraday','ai','SGX')] = [
 ('AWX.SI', "Fell 6%.", "Next session", "US chips weak again", (-5,0.3,5), 'Speculative', 'Bounce watch'),
 ('558.SI', "Fell 4.4%.", "Next session", "Follows US chip equipment", (-4.5,0.3,4.5), 'Speculative', 'Bounce watch'),
 ('V03.SI', "Fell 2%.", "Next session", "Small range", (-2,0.3,2.2), 'Medium', 'Range'),
 ('E28.SI', "Fell 3.3%.", "Next session", "Thin trading", (-3.5,0.3,3.5), 'Speculative', 'Bounce watch'),
 ('5DD.SI', "Fell 1.3%.", "Next session", "Thin trading", (-3,0.2,3), 'Medium', 'Range'),
]

# ---------- Health ----------
P[('long','hc','US')] = [
 ('LLY', "Obesity-drug leader: revenue +39%, at its high (+34% this year) and barely moved in Monday's sell-off. Little analyst upside left, so the base case is modest.",
  "Orforglipron launch; Q4 results (Feb)", "Drug-price policy", (-16,8,25), 'High', 'Defensive growth'),
 ('ARGX', "argenx: revenue +52% from its immune-disease drug Vyvgart, 10% off its high, 20% analyst upside.",
  "New indications in 2027", "Competition in myasthenia gravis", (-15,10,28), 'Medium', 'Growth leader'),
 ('MDGL', "Madrigal's liver drug Rezdiffra is growing fast (revenue +50%); 30% off its high with 63% analyst upside.",
  "Script data; EU rollout", "Competition from GLP-1 drugs", (-22,20,45), 'Medium', 'Oversold growth'),
 ('INSM', "Insmed's lung drug launch drives revenue +268%; up 28% in a month and rose on Monday, still 42% off its high.",
  "Brensocatib launch numbers", "Overbought short term (RSI 77)", (-30,16,45), 'Medium', 'Launch story'),
 ('ALNY', "Alnylam is 66% off its high (RSI 22); analysts see 88% upside.",
  "Amvuttra script data", "Trend still down", (-30,16,48), 'Speculative', 'Deep value'),
]
P[('long','hc','SGX')] = [
 ('Q0F.SI', "IHH runs hospitals across Asia; analysts see 33% upside. Held flat on a weak day.", "Q3 results Nov 25", "Currency swings", (-12,11,24), 'Medium', 'Regional leader'),
 ('C2PU.SI', "Parkway Life REIT: steady hospital and nursing-home rents, 6% off its high; rose on Monday.", "Dividend", "US 10-yr yield above 5%", (-8,7,15), 'High', 'Income'),
 ('AP4.SI', "Riverstone makes cleanroom and medical gloves at about 14x earnings with 40% analyst upside.", "Q3 results (Nov)", "Glove price competition", (-15,11,28), 'Medium', 'Value'),
 ('BSL.SI', "Raffles Medical: Singapore hospital group, 21% off its high, steady (RSI 63).", "Results (Feb)", "Shrinking revenue (-7%)", (-10,8,18), 'Medium', 'Recovery'),
 ('H02.SI', "Haw Par (Tiger Balm) trades near 10x earnings with a large cash and investment pile; 32% off its high.", "Results (Feb)", "Revenue down 8%", (-12,6,16), 'Medium', 'Value'),
]
P[('swing','hc','US')] = [
 ('LLY', "Near its high and flat while the Nasdaq fell 2.5%; a place to hide from the chip sell-off.", "Orforglipron news", "Money rotating back into chips", (-8,3,10), 'High', 'Relative strength'),
 ('ABBV', "AbbVie is at its high and barely moved on Monday; revenue +10% at about 18x earnings.", "Immunology growth", "Rotation out of defensives", (-6,2,7), 'Medium', 'Relative strength'),
 ('MDGL', "Pulled back 6% in a month (RSI 41); 63% analyst upside.", "Script data", "Biotech risk-off", (-12,6,18), 'Medium', 'Rebound'),
 ('ALNY', "Oversold (RSI 22), 66% off its high.", "Amvuttra script data", "Trend still down", (-15,7,22), 'Speculative', 'Oversold rebound'),
 ('CYTK', "Cytokinetics' heart drug launch is starting; 39% off its high (RSI 34), about 100% analyst upside. Fell 5% on Monday.", "Launch numbers", "Launch slower than hoped", (-15,6,20), 'Speculative', 'Launch rebound'),
]
P[('intraday','hc','US')] = [
 ('INSM', "Rose 1.7% against the market; strong trend (RSI 77).", "Momentum", "Overbought", (-3,0.3,3), 'Medium', 'Relative strength'),
 ('VKTX', "Fell 8%.", "Bounce", "More biotech selling", (-6,0,6), 'Speculative', 'Bounce watch'),
 ('TEM', "Fell 7% with AI names.", "Bounce", "Follows AI stocks", (-6,0,6), 'Speculative', 'Bounce watch'),
 ('UNH', "Rose 0.5% on a down day.", "Defensive bid", "Policy headlines", (-2,0.2,2), 'Medium', 'Range'),
 ('LLY', "Small dip near its high.", "Defensive bid", "Rotation into tech", (-2.2,0.2,2.2), 'Medium', 'Range'),
]
P[('swing','hc','SGX')] = [
 ('Q0F.SI', "IHH steady (RSI 63) ahead of Q3 results.", "Q3 results Nov 25", "Results miss", (-6,3,9), 'Medium', 'Pre-earnings'),
 ('C2PU.SI', "Parkway Life REIT: lowest-volatility name in the group.", "Dividend", "Rates", (-4,2,6), 'High', 'Range'),
 ('BSL.SI', "Raffles Medical holding a mild uptrend (RSI 63).", "Momentum", "Low volume", (-5,2,6), 'Medium', 'Trend'),
 ('AP4.SI', "Riverstone steady (RSI 52); large analyst upside.", "Q3 results (Nov)", "Glove prices", (-8,3,10), 'Medium', 'Support'),
 ('QC7.SI', "Q&M Dental is very oversold (RSI 17) after a 4% drop.", "Bounce", "Small cap", (-8,3,10), 'Speculative', 'Oversold rebound'),
]
P[('intraday','hc','SGX')] = [
 ('C2PU.SI', "Rose 0.3%.", "Next session", "Small range", (-1,0.2,1), 'Medium', 'Range'),
 ('Q0F.SI', "Flat.", "Next session", "Malaysia market swings", (-2,0.2,2), 'Medium', 'Range'),
 ('BSL.SI', "Flat.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('AP4.SI', "Fell 0.7%.", "Next session", "Thin trading", (-2,0.2,2), 'Medium', 'Range'),
 ('H02.SI', "Fell 0.3%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
]

# ---------- Finance ----------
P[('long','fin','US')] = [
 ('JPM', "Best-run US bank, 8% off its high at about 13x forward earnings. Higher rates (10-yr ~5.1%) support interest income.", "Q4 results Jan 14", "Credit cycle; app-outage headlines", (-15,8,22), 'High', 'Core holding'),
 ('V', "Visa: steady growth (+13%), near its high and flat on a 2% down day; little AI exposure.", "Holiday spending", "Regulation of card fees", (-12,6,18), 'High', 'Defensive growth'),
 ('GS', "Trading and deal-making boom, about 12x forward earnings, 23% off its high. A lead bank on the record Anthropic IPO.",
  "Anthropic prices Nov 18, trades Nov 19", "Market volatility hits deals", (-20,10,28), 'Medium', 'Cyclical value'),
 ('NU', "Nubank: revenue +34% at about 12x forward earnings, 32% off its high; 41% analyst upside.", "Q4 results (Feb)", "Brazil credit and currency", (-30,16,48), 'Medium', 'Growth at a discount'),
 ('SE', "Sea: revenue +43%; $1B buyback. About 15x forward earnings, 51% off its high.",
  "Q4 results (Mar)", "Rising credit costs at Monee; competition", (-30,18,50), 'Medium', 'Oversold growth'),
]
P[('long','fin','SGX')] = [
 ('D05.SI', "DBS kept its 81-cent quarterly dividend and says interest income has bottomed; 12% off its high (RSI 21).",
  "Q4 results (Feb)", "Margins if rates fall; stronger SGD", (-10,8,16), 'High', 'Income leader'),
 ('O39.SI', "OCBC was the only local bank to beat in Q3 and raised loan-growth guidance.",
  "Q4 results (Feb)", "Margin fell 18 bp to 1.66%", (-10,7,15), 'Medium', 'Income'),
 ('U11.SI', "UOB missed Q3 and cut its margin guidance; RSI 18, 17% off its high.", "Recovery in fees", "More credit provisions", (-12,7,17), 'Medium', 'Oversold income'),
 ('AIY.SI', "iFAST: fintech platform, revenue +23%, 27% off its high with 42% analyst upside; rose on a down day.", "HK pension business", "Market-driven volumes", (-18,16,36), 'Medium', 'Growth'),
 ('S68.SI', "SGX benefits from high trading volumes; from Jan 2027 its RegCo takes over IPO prospectus reviews.", "Monthly volume data", "Already priced (25x earnings)", (-12,7,18), 'Medium', 'Volatility winner'),
]
P[('swing','fin','US')] = [
 ('GS', "Anthropic prices on Nov 18 and trades on Nov 19; books reportedly ~6x covered.", "Deal fees", "Volatility (VIX 23)", (-9,4,12), 'Medium', 'Deal pipeline'),
 ('MA', "Mastercard is near its high and flat on a down day (RSI 70).", "Holiday spending data", "Rotation out of defensives", (-6,2,7), 'High', 'Relative strength'),
 ('SCHW', "Schwab held flat on a weak day; about 12x forward earnings with 26% analyst upside.", "Monthly client metrics", "Rates and market swings", (-8,3,10), 'Medium', 'Relative strength'),
 ('NU', "Fell 4% (RSI 53); 41% analyst upside.", "Analyst updates", "Brazil credit", (-14,5,18), 'Medium', 'Pullback'),
 ('HOOD', "RSI 26 after a 7% drop as bitcoin hit ~$64K; retail access to the Anthropic IPO runs partly through Robinhood.", "Anthropic IPO demand", "More crypto weakness", (-18,6,24), 'Speculative', 'Oversold rebound'),
]
P[('swing','fin','SGX')] = [
 ('D05.SI', "DBS is oversold (RSI 21).", "Dividend support", "Margin worries", (-4,3,7), 'High', 'Oversold income'),
 ('U11.SI', "UOB RSI 18.", "Rebound", "Further downgrades", (-5,3,8), 'Medium', 'Oversold rebound'),
 ('O39.SI', "OCBC eased 0.8% (RSI 41).", "Post-results recovery", "Margin squeeze", (-4,2,6), 'Medium', 'Range'),
 ('AIY.SI', "iFAST rose slightly on a down day (RSI 50).", "Momentum", "Market-driven", (-8,3,10), 'Medium', 'Range'),
 ('S68.SI', "SGX benefits when markets are volatile.", "Volume data", "Valuation", (-5,2,7), 'Medium', 'Volatility winner'),
]
P[('intraday','fin','US')] = [
 ('HOOD', "Fell 7% with crypto (RSI 26).", "Anthropic IPO interest", "Crypto weakness", (-5,0.3,5), 'Speculative', 'Bounce watch'),
 ('COIN', "Fell 6% as bitcoin hit its lowest since July (RSI 25).", "Crypto bounce", "More crypto selling", (-5,0,5), 'Speculative', 'Crypto beta'),
 ('CRCL', "Fell 7% to RSI 17.", "Bounce", "Crypto weakness", (-5,0,5), 'Speculative', 'Bounce watch'),
 ('JPM', "Fell 2.5% on app-outage reports.", "Dip buying", "More outage news", (-2,0.3,2), 'Medium', 'Dip watch'),
 ('GS', "Fell 3%; Anthropic pricing on Wednesday.", "IPO fees", "Market risk-off", (-2.5,0.3,2.5), 'Medium', 'Range'),
]
P[('intraday','fin','SGX')] = [
 ('D05.SI', "Fell 0.9%; RSI 21.", "Next session", "Market-wide risk-off", (-1.3,0.3,1.4), 'High', 'Bounce watch'),
 ('U11.SI', "Fell 0.8%; RSI 18.", "Next session", "Trend down", (-1.5,0.3,1.6), 'Medium', 'Bounce watch'),
 ('O39.SI', "Fell 0.8%.", "Next session", "Small range", (-1.3,0.2,1.3), 'Medium', 'Range'),
 ('G07.SI', "Flat.", "Next session", "Thin trading", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('AIY.SI', "Rose 0.1%.", "Next session", "Small range", (-1.8,0.2,1.8), 'Medium', 'Range'),
]

# IPO tab (6-month view), all markets
P[('ipo','all','US')] = [
 ('SPCX', "SpaceX listed in June at $135 and trades about 3% above that, 34% under its high. Starship flight 15 flew Nov 13; the upper stage was caught, the booster catch was aborted.",
  "Starship progress; lock-up expiries", "Valuation and Musk headlines", (-35,12,45), 'Medium', 'Mega-cap IPO'),
 ('CHYM', "Chime (IPO $27) trades about 27% above its IPO price at its high, and rose on a 2% down day.",
  "Member growth", "Overbought (RSI 84); fintech credit cycle", (-18,8,25), 'Medium', 'Post-IPO uptrend'),
 ('ASBH', "American Savings Bank (IPO $16, Sept) is 39% above its IPO price and at its high; rose 5% on Monday.",
  "First full quarter as a public company", "Overbought (RSI 79); small float", (-20,6,22), 'Speculative', 'Post-IPO momentum'),
 ('KLAR', "Klarna (IPO $40) is 66% below its IPO price at about 17x forward earnings; revenue +27%. New CFO and a C-suite shake-up before the holidays.",
  "Q3 results Nov 17", "Buy-now-pay-later credit losses", (-25,14,40), 'Speculative', 'Deep value'),
 ('ACCV', "Accelevation (IPO $18) makes electrical gear for data centres: revenue +66% at about 10x forward earnings. Fell 15% on Monday after its first results; 39% below its IPO price.",
  "Order updates", "Data-centre slowdown; 9% daily swings", (-40,10,50), 'Speculative', 'Post-IPO value'),
]

# ---------- Power & grid (data-center power) ----------
P[('long','pwr','US')] = [
 ('GEV', "GE Vernova: gas turbines and grid gear sold out for years, revenue +27%. 35% off its high with 53% analyst upside.", "Q4 results Jan 27", "Data-centre policy; valuation (29x)", (-25,15,40), 'High', 'Quality at a discount'),
 ('CEG', "Constellation beat Q3 and raised 2026 guidance; held up better than peers (-0.9% in five days), 28% off its high.", "New long-term power deals", "Data-centre politics; PJM rules", (-22,13,32), 'High', 'Beat and raise'),
 ('ETN', "Eaton: electrical gear for data centres and utilities, 27% off its high at about 20x earnings.", "Q4 results Feb 2", "Data-centre orders slowing", (-20,13,33), 'Medium', 'Quality at a discount'),
 ('VRT', "Vertiv: data-centre cooling and power, revenue +61% at about 19x forward earnings, 50% off its high after a 7% drop.", "Order backlog updates", "Most exposed to a data-centre slowdown", (-35,18,52), 'Medium', 'Oversold growth'),
 ('PWR', "Quanta builds the grid: revenue +57%, 25% off its high.", "Utility capex plans", "Data-centre policy", (-25,12,34), 'Medium', 'Grid builder'),
]
P[('long','pwr','SGX')] = [
 ('BN4.SI', "Keppel: power, data centres and asset management, about 16x earnings with 33% analyst upside. Fell 2.8% on Monday.", "Asset sales", "Execution", (-13,12,25), 'Medium', 'Value'),
 ('U96.SI', "Sembcorp: power and renewables at about 9x earnings.", "New contracts", "Power prices", (-12,7,18), 'Medium', 'Value'),
 ('DCRU.SI', "Digital Core REIT: US data-centre REIT, about 10x earnings with 54% analyst upside.", "Leasing news", "Tenant concentration; US rates above 5%", (-14,11,27), 'Medium', 'Deep value'),
 ('AJBU.SI', "Keppel DC REIT: data-centre rents, 9% off its high; rose on a down day.", "Dividend", "Rates", (-10,7,17), 'Medium', 'Income'),
 ('544.SI', "CSE Global: electrification and data-centre work, about 10x earnings, now at a 52-week low (-54% from its high).", "New orders", "Falling knife; small and volatile", (-30,14,45), 'Speculative', 'Recovery'),
]
P[('swing','pwr','US')] = [
 ('NEE', "NextEra was flat on a 2% down day (RSI 60); regulated utility earnings.", "Renewables deals", "10-yr yield above 5%", (-6,3,8), 'Medium', 'Defensive'),
 ('CEG', "Held up best among AI-power names; RSI 57.", "Analyst target updates", "Data-centre politics; higher yields", (-12,5,16), 'Medium', 'Relative strength'),
 ('TLN', "Talen's new 750 MW capacity deal; about 12x forward earnings, flat over five days.", "Analyst target updates", "Data-centre politics", (-13,5,16), 'Medium', 'New-contract momentum'),
 ('VST', "Vistra RSI 38 after a 16% monthly drop; 56% analyst upside.", "Analyst updates", "Texas data-centre proposal", (-14,6,20), 'Medium', 'Oversold rebound'),
 ('GEV', "GE Vernova RSI 35, down 17% in a month.", "Order news", "AI capex fears", (-14,6,20), 'Medium', 'Oversold rebound'),
]
P[('swing','pwr','SGX')] = [
 ('AJBU.SI', "Keppel DC REIT rose 0.9% (RSI 65).", "Momentum", "Overbought", (-5,1.5,6), 'Medium', 'Trend'),
 ('BN4.SI', "Keppel fell 2.8% to RSI 36.", "Asset-sale news", "Execution", (-6,3,9), 'Medium', 'Oversold rebound'),
 ('U96.SI', "Sembcorp RSI 40.", "Contracts", "Power prices", (-5,2,7), 'Medium', 'Range'),
 ('DCRU.SI', "Digital Core REIT steady (RSI 54).", "Support", "US data-centre worries", (-7,2,8), 'Medium', 'Range'),
 ('544.SI', "CSE Global fell 4.7% to a 52-week low.", "New orders", "No floor yet", (-15,3,16), 'Speculative', 'Falling knife'),
]
P[('intraday','pwr','US')] = [
 ('VRT', "Fell 7%.", "Bounce", "AI hardware selling", (-6,0.3,6), 'Speculative', 'Bounce watch'),
 ('BE', "Fell 7%.", "Bounce", "8% daily swings", (-7,0,7), 'Speculative', 'Range'),
 ('SMR', "Fell 7%; down 20% in five days.", "Bounce", "Cash burn; rate-sensitive", (-7,0,7), 'Speculative', 'Bounce watch'),
 ('CCJ', "Fell 5.6% (RSI 28).", "Bounce", "Uranium sentiment", (-4,0.3,4), 'Speculative', 'Bounce watch'),
 ('NEE', "Flat on a weak day.", "Defensive bid", "Small range", (-1.8,0.2,1.8), 'Medium', 'Range'),
]
P[('intraday','pwr','SGX')] = [
 ('BN4.SI', "Fell 2.8%.", "Next session", "More selling", (-1.8,0.3,2), 'Medium', 'Bounce watch'),
 ('544.SI', "Fell 4.7% to a 52-week low.", "Next session", "Small cap", (-4,0.2,4), 'Speculative', 'Range'),
 ('AJBU.SI', "Rose 0.9%.", "Next session", "Small range", (-1.2,0.2,1.2), 'Medium', 'Range'),
 ('U96.SI', "Fell 0.9%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('DCRU.SI', "Flat.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
]

# ---------- Defence & industrials ----------
P[('long','def','US')] = [
 ('GE', "GE Aerospace: jet-engine services boom, revenue +16%, 15% off its high.", "Q4 results Jan 21", "Valuation (35x)", (-15,10,26), 'High', 'Quality'),
 ('RTX', "RTX: missiles and engines, revenue +11%, steady; 17% analyst upside.", "Q4 results Jan 26", "Engine issues", (-12,10,24), 'High', 'Core defence'),
 ('LHX', "L3Harris: space and missile sensors, 31% off its high, 29% analyst upside.", "Golden Dome contracts", "Budget fights with a split government", (-15,12,30), 'Medium', 'Value'),
 ('HWM', "Howmet: jet-engine parts, revenue +29%, 27% off its high with 39% analyst upside.", "Aerospace build rates", "Valuation (32x)", (-20,14,34), 'Medium', 'Growth at a discount'),
 ('NOC', "Northrop: B-21 and missile defence, about 18x earnings, 29% off its high; fell least among defence names on Monday.", "Golden Dome contracts", "Budget fights", (-15,10,27), 'Medium', 'Value'),
]
P[('long','def','SGX')] = [
 ('S63.SI', "ST Engineering's order book hit a record S$37.7B and nine-month revenue rose 10% to S$10B; yet the stock fell 6.6% on Nov 16 with no news. 21% off its high, 28% analyst upside.", "Contract wins; FY results (Feb)", "Unexplained selling; valuation (23x)", (-12,12,26), 'High', 'Quality on a dip'),
 ('BS6.SI', "Yangzijiang Shipbuilding: about 7.5x earnings, revenue +36%; orders of US$6.98B are well above its US$4.5B target. Rose 2.6% on a down day.", "New ship orders", "US port fees on Chinese ships", (-18,14,32), 'Medium', 'Value'),
 ('S59.SI', "SIA Engineering: aircraft maintenance, 24% off its high, 30% analyst upside.", "Air travel", "Revenue falling (-11%)", (-10,10,24), 'Medium', 'Recovery'),
 ('C52.SI', "ComfortDelGro: steady transport earnings at about 13.5x.", "Overseas contracts", "Slow growth", (-8,7,15), 'Medium', 'Steady'),
 ('H22.SI', "Hong Leong Asia: engines and building materials at about 8x earnings, 48% off its high.", "Results (Feb)", "China demand", (-25,20,50), 'Speculative', 'Deep value'),
]
P[('swing','def','US')] = [
 ('CAT', "Caterpillar is 46% off its high (RSI 26) after a 4.6% drop.", "Rebound", "Data-centre generator orders slowing", (-12,6,18), 'Medium', 'Oversold rebound'),
 ('AXON', "RSI 21 after a Q3 miss; 75% analyst upside.", "Analyst updates", "More downgrades", (-18,6,22), 'Speculative', 'Post-earnings dip'),
 ('GD', "General Dynamics: 10% off its high, steady (RSI 52).", "Contracts", "Budget fights", (-7,3,9), 'Medium', 'Steady'),
 ('LMT', "Lockheed RSI 39 after a 2.4% dip; up 5% in a month.", "Contracts", "Budget fights", (-8,3,10), 'Medium', 'Pullback'),
 ('BA', "Boeing 35% off its high (RSI 46); production recovering.", "Monthly deliveries", "Quality issues", (-10,5,15), 'Medium', 'Recovery'),
]
P[('swing','def','SGX')] = [
 ('S63.SI', "ST Engineering fell 6.6% to RSI 25 with no news.", "Bounce; contract wins", "Large holder selling", (-6,4,10), 'Medium', 'Oversold rebound'),
 ('BS6.SI', "Yangzijiang rose 2.6% on strong orders.", "Orders", "Trade fees", (-8,4,12), 'Medium', 'Relative strength'),
 ('H22.SI', "Hong Leong Asia RSI 29.", "Bounce", "China demand", (-10,4,12), 'Speculative', 'Oversold rebound'),
 ('S59.SI', "SIA Engineering RSI 43.", "Air travel", "Slow growth", (-6,2,7), 'Medium', 'Range'),
 ('C52.SI', "ComfortDelGro steady (RSI 47).", "Support", "Slow growth", (-4,1.5,5), 'Medium', 'Range'),
]
P[('intraday','def','US')] = [
 ('KTOS', "Fell 6.4%.", "Drone contracts", "Volatile", (-4.5,0,4.5), 'Speculative', 'Bounce watch'),
 ('AVAV', "Fell 6.4%; results Dec 2.", "Bounce", "Volatile", (-5,0,5), 'Speculative', 'Bounce watch'),
 ('CAT', "Fell 4.6% (RSI 26).", "Bounce", "Rotation out of cyclicals", (-3,0.3,3), 'Medium', 'Bounce watch'),
 ('NOC', "Fell 1.2%; steadiest defence name.", "Defence bid", "Small range", (-2,0.2,2), 'Medium', 'Range'),
 ('GE', "Fell 2.3%.", "Dip buying", "More profit-taking", (-2.5,0.3,2.5), 'Medium', 'Dip watch'),
]
P[('intraday','def','SGX')] = [
 ('S63.SI', "Fell 6.6% with no news.", "Next session", "More block selling", (-2.5,0.5,3), 'Medium', 'Bounce watch'),
 ('BS6.SI', "Rose 2.6%.", "Next session", "Gives back gains", (-2.5,0.2,2.5), 'Medium', 'Follow-through check'),
 ('H22.SI', "Fell 2.4%.", "Next session", "Thin trading", (-3,0.3,3), 'Speculative', 'Bounce watch'),
 ('S59.SI', "Fell 1.7%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('C52.SI', "Fell 1.6%.", "Next session", "Small range", (-1.2,0.2,1.2), 'Medium', 'Range'),
]

# ---------- Energy (oil and gas) ----------
P[('long','nrg','US')] = [
 ('CVX', "Chevron: revenue +35%, about 13x earnings, 8% off its high.", "Hess integration; buybacks", "Oil keeps falling as Hormuz shipping recovers", (-16,8,24), 'High', 'Core energy'),
 ('XOM', "Exxon: steady cash flow, about 13x earnings, 10% analyst upside.", "Buybacks", "Oil price drop", (-15,7,21), 'High', 'Core energy'),
 ('LNG', "Cheniere: US gas exports on long contracts; less tied to oil. Up 7.5% in five days.", "New export capacity", "Gas price swings", (-15,8,24), 'Medium', 'Steady'),
 ('FANG', "Diamondback: low-cost Permian producer at about 8x earnings, 32% analyst upside.", "Buybacks", "Oil price drop", (-22,12,32), 'Medium', 'Value'),
 ('COP', "ConocoPhillips: about 12x earnings, revenue +29%.", "Buybacks", "Oil price drop", (-18,7,23), 'Medium', 'Value'),
]
P[('long','nrg','SGX')] = [
 ('5E2.SI', "Seatrium builds offshore rigs and wind platforms; 42% analyst upside.", "New orders", "Contract delays", (-15,12,28), 'Medium', 'Recovery'),
 ('BN4.SI', "Keppel: energy infrastructure and asset management.", "Asset sales", "Execution", (-13,10,22), 'Medium', 'Value'),
 ('5LY.SI', "Marco Polo Marine: offshore vessels, revenue +40% at about 10x earnings.", "Results (Nov)", "Thin trading", (-25,10,35), 'Speculative', 'Growth value'),
 ('RE4.SI', "Geo Energy crashed 23% to S$0.38 on Nov 16 with trading apparently stopping at 9:55am; no announcement found. Wait for an explanation before acting.", "Company announcement", "Unknown cause; could fall further", (-40,0,35), 'Speculative', 'Wait'),
 ('5WH.SI', "Rex International is in a long downtrend (-63% this year); no setup.", "None", "Further losses", (-30,-5,20), 'Speculative', 'Avoid'),
]
P[('swing','nrg','US')] = [
 ('LNG', "Cheniere is up 7.5% in five days and fell least as oil dropped.", "Export capacity", "Gas price swings", (-8,3,10), 'Medium', 'Relative strength'),
 ('FANG', "Diamondback oversold (RSI 27); about 8x earnings.", "Buybacks", "Oil price drop", (-11,4,13), 'Medium', 'Oversold rebound'),
 ('SLB', "SLB oversold (RSI 29), 16% off its high; 24% analyst upside.", "Offshore orders", "Oil price drop", (-10,4,12), 'Medium', 'Oversold rebound'),
 ('DVN', "Devon RSI 31 after a 4% drop; about 9x earnings, 35% analyst upside.", "Buybacks", "Oil price drop", (-12,4,14), 'Medium', 'Oversold rebound'),
 ('CVX', "Chevron RSI 38.", "Buybacks", "Gulf calm returns", (-7,2,8), 'Medium', 'Support'),
]
P[('intraday','nrg','US')] = [
 ('DVN', "Fell 4% as WTI dropped to ~$85.", "Bounce", "Oil keeps falling", (-3,0.2,3), 'Medium', 'Bounce watch'),
 ('FANG', "Fell 3.1%.", "Bounce", "Oil keeps falling", (-2.8,0.2,2.8), 'Medium', 'Bounce watch'),
 ('MPC', "Fell 3.1%.", "Margins", "Oil swings", (-3,0.2,3), 'Medium', 'Range'),
 ('XOM', "Fell 2.1%.", "Oil", "Hormuz shipping normalises", (-2,0.2,2), 'Medium', 'Range'),
 ('LNG', "Fell 0.8%; held up best.", "Relative strength", "Gas swings", (-2.5,0.2,2.5), 'Medium', 'Range'),
]
P[('swing','nrg','SGX')] = [
 ('5E2.SI', "Seatrium fell 1.7% toward support.", "Orders", "Delays", (-8,3,10), 'Medium', 'Support'),
 ('BN4.SI', "Keppel fell 2.8% to RSI 36.", "Asset sales", "Execution", (-6,3,9), 'Medium', 'Oversold rebound'),
 ('5LY.SI', "Marco Polo Marine RSI 47.", "Results", "Thin trading", (-10,3,12), 'Speculative', 'Range'),
 ('RE4.SI', "Geo Energy -23% with no explanation found.", "Company announcement", "Unknown cause", (-25,0,20), 'Speculative', 'Wait'),
 ('5WH.SI', "Rex International: no setup.", "None", "Further losses", (-12,-2,8), 'Speculative', 'Avoid'),
]
P[('intraday','nrg','SGX')] = [
 ('RE4.SI', "Fell 23%; check for a company announcement before the open.", "Next session", "More selling or a halt", (-12,0,12), 'Speculative', 'Wait'),
 ('5E2.SI', "Fell 1.7%.", "Next session", "Small range", (-2,0.2,2), 'Medium', 'Range'),
 ('BN4.SI', "Fell 2.8%.", "Next session", "Small range", (-1.8,0.3,2), 'Medium', 'Bounce watch'),
 ('5LY.SI', "Fell 1.8%.", "Next session", "Thin trading", (-4,0,4), 'Speculative', 'Range'),
 ('5WH.SI', "Penny stock in a downtrend; avoid.", "None", "Further losses", (-5,-1,4), 'Speculative', 'Avoid'),
]

IPO_LIST = [
 # sym, name, ipo_date, ipo_price, sector, status
 ('ANT','Anthropic (Nasdaq: ANT; range $70-78, 825M shares, up to ~$64B; ~6x oversubscribed per Bloomberg; prices Nov 18, trading Nov 19; Altimeter to invest $5B)','2026-11-19',None,'ai','Roadshow'),
 ('BIAI','Bitari','2026-11-30',7.00,'ai','Expected'),
 ('FBLLU','Football Manager SPAC','2026-11-23',10.00,'fin','Expected'),
 ('ABGC','American Barrick Gold (Barrick carve-out; ~$6B est.; filed week of Nov 9)','2026-11-13',None,'nrg','Filed'),
 ('YNTE','Primagrove ($4-6 range; not confirmed)','2026-11-16',None,'fin','Expected'),
 ('RZRA','Rezera ($11-13 range; postponed)','2026-11-12',None,'hc','Postponed'),
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
 ('2026-11-15T23:01','NVDA', "Via tracker: backs Jensen Huang as '1 of 1' and shares a petition for his return."),
 ('2026-11-15T19:03','AXTI', "Via tracker: says his AXT thesis is narrow, using indium phosphide substrate capacity as an example of an AI bottleneck."),
 ('2026-11-15T18:47','NVDA', "Via tracker: expects buying of bottleneck parts to speed up through 2027, naming laminates, ABF substrates, PCBs and optical parts."),
 ('2026-11-14T08:16','NVDA', "Via tracker: shares a letter from Altimeter and Atreides to Nvidia's board."),
 ('2026-11-14T05:07','NVDA', "Via tracker: says Musk's involvement raised the odds of Huang returning as CEO; separately posted an FT report that Huang is discussing a comeback."),
 ('2026-11-14T04:25','LITE MU', "Via tracker: argues demand stays supply-limited for optics and memory even if AI capex slows."),
 ('2026-11-14T01:07','TSM', "Via tracker: calls rumours of TSMC capacity cuts hypothetical; says they have not happened."),
 ('2026-11-13T23:36','NVDA COHR AMD', "Via tracker: says a CFO-led Nvidia is a negative for companies built around the Nvidia ecosystem."),
 ('2026-11-13T21:21','AXTI COHR LITE', "Via tracker: still bullish on AXT, citing backlog growth and visibility on customers."),
 ('2026-11-13T19:27','NVDA AMD AVGO', "Via tracker: Nvidia's roadmap is intact, but its next leg of growth is less certain without Huang."),
 ('2026-11-13T18:57','NVDA', "Via tracker: says buybacks may support the shares and that 'going to zero' fears are overblown."),
]

EVENTS = [
 ('2026-11-13','Macro','S&P -0.4%, Nasdaq -0.9%; PPI 6.5% y/y', "S&P 7,562; Dow +0.1%. October PPI +0.3% m/m. 10-yr 5.15% (+~30 bp on the week). Dec Fed hike fully priced; Daly and Collins back more tightening."),
 ('2026-11-13','AI','Chip index -3.4%; AMD -8.8%, Broadcom -4.8%', "Arm -4.6% on an FT report that Nvidia's board approached Rene Haas. Cisco -6.2% and Applied Materials -2.7% despite beats."),
 ('2026-11-13','SGX','ST Engineering nine-month update', "Record order book S$37.7B; revenue +10% to S$10B. No profit figure."),
 ('2026-11-16','Macro','S&P -1.9%, Nasdaq -2.5%; VIX 23', "S&P ~7,417; Dow -1.4%; Russell -1.7%. Empire State index 7.8 (vs 16.7 expected). Bitcoin ~$64K, lowest since July. Banks -2% on app-outage reports."),
 ('2026-11-16','AI','New US rule on remote chip access; NVDA -4%', "Commerce rule targets Chinese firms renting advanced chips abroad. NVDA ~$156, -13% in five days; board reportedly not considering Huang's return. Micron -7% (DRAM lawsuit), Intel -7% (class action)."),
 ('2026-11-16','Energy','WTI -3.7% to ~$85', "Shipping through Hormuz is recovering; Brent ~$92."),
 ('2026-11-16','SGX','STI -0.9% to 5,184.66', "ST Engineering -6.6% with no news; AEM -6%; Yangzijiang +2.6%. Geo Energy -23%, no announcement found."),
 ('2026-11-17','Macro','US retail sales (Oct)', "8:30am ET."),
 ('2026-11-17','AI','Nvidia Q3 results', "~4:20pm ET. About $109B revenue expected; options price a ~10% move. First call under interim CEO Kress. Klarna also reports."),
 ('2026-11-18','IPO','Anthropic prices IPO', "Range $70-78; 825M shares."),
 ('2026-11-19','IPO','Anthropic starts trading (Nasdaq: ANT)', "Book ~6x oversubscribed per Bloomberg; Altimeter to invest $5B."),
 ('2026-11-25','SGX','IHH Q3 results', ""),
 ('2026-11-26','Macro','US Thanksgiving', "US stock market closed."),
 ('2026-12-01','AI','Marvell and Credo results', ""),
 ('2026-12-02','Defence','AeroVironment results', ""),
 ('2026-12-09','Macro','Fed rate decision (Dec 8-9)', "A hike is fully priced. Broadcom reports the same day."),
 ('2026-12-10','AI','Ciena results; TSMC November sales', ""),
 ('2026-12-23','AI','Micron FQ1 results', ""),
]
