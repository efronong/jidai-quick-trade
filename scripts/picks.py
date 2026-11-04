# Analyst picks for 2026-11-04 (snapshot: US close Nov 3, SGX morning Nov 4). Fields: sym, thesis, catalyst, risk, (low, base, high) % expected move, conviction, setup
# Horizons: long = 12 months, swing = ~4 weeks, intraday = rest of session (US) / next session (SGX), ipo = 6 months.
# Context: Democrats won Congress on Nov 3; on Nov 4 the Dow rose 3%, Brent fell below $100, energy fell ~4%, defence and Nvidia slipped.
P = {}

# ---------- AI & chips ----------
P[('long','ai','US')] = [
 ('NVDA', "Revenue still about doubles (+106%) while the stock trades near 13x forward earnings, 14% below its high. Analysts see 58% upside.",
  "Q3 results Nov 17", "Data-centre limits after the Democratic sweep (Texas pause proposal); supply caps", (-18,25,50), 'High', 'Quality at a discount'),
 ('MU', "Memory is still the tightest part of AI servers: revenue +379% at about 4x forward earnings. SK Hynix says HBM/DRAM is sold out.",
  "FQ1 results Dec 23", "Peak-cycle earnings; memory falls hard when prices turn", (-30,30,70), 'Medium', 'Cycle leader'),
 ('AMD', "Q3 revenue $13.4B (+45%), beating estimates, with data-centre sales nearly doubling; Q4 guide about $17B. Shares rose about 5% after hours.",
  "MI-series GPU ramp; analyst target raises", "Already 25% off its high on AI-capex nerves; priced for execution", (-20,22,45), 'High', 'Earnings momentum'),
 ('AVGO', "Custom AI chips plus networking: revenue +86% at about 17x forward earnings, 31% below its high.",
  "Q4 results Dec 9", "Lumpy custom-chip orders; customer concentration", (-15,22,45), 'Medium', 'Pullback in a leader'),
 ('TSM', "Makes almost every leading AI chip. Revenue +51% at about 17x forward earnings: the steadiest way to own the build-out.",
  "October sales (~Nov 10); Q4 results Jan 14", "Taiwan geopolitics and US tariffs", (-12,18,35), 'High', 'Core holding'),
]
P[('long','ai','SGX')] = [
 ('AWX.SI', "AEM makes test handlers for AI and server chips. Up 330% this year but 34% below its high; analysts rate it Strong Buy with big upside.",
  "Q3 business update (Nov)", "One large customer; very volatile", (-25,25,55), 'Medium', 'SGX AI leader'),
 ('558.SI', "UMS machines precision parts for chip-equipment makers. 33% off its high after a 31% monthly drop while the equipment cycle keeps growing.",
  "Q3 results mid-November", "Tied to Applied Materials spending", (-20,20,45), 'Medium', 'Equipment supplier'),
 ('5DD.SI', "Micro-Mechanics makes precision tools for chip assembly and test: revenue +45%, 38% off its high.",
  "Q1 FY27 results (Nov)", "Small and thinly traded", (-20,18,40), 'Medium', 'Growth at a discount'),
 ('E28.SI', "Frencken builds modules for chip and medical equipment. 45% off its high with Strong Buy ratings.",
  "Q3 business update (Nov)", "Flat revenue so far this year", (-20,15,38), 'Medium', 'Recovery'),
 ('V03.SI', "Venture builds electronics for chip-equipment, medical and AI-server makers. Net cash, about 15x earnings.",
  "Q3 business update (Nov)", "Slow growth (+7%)", (-10,10,22), 'Medium', 'Steady value'),
]
P[('swing','ai','US')] = [
 ('LITE', "Marvell is buying Lumentum for 4.5 Marvell shares each. At the snapshot prices that is worth about 14% more than LITE's price.",
  "Deal spread narrows if MRVL recovers", "Regulatory delay (incl. China); MRVL keeps falling", (-12,8,20), 'Medium', 'Merger spread'),
 ('MRVL', "Down 29% in a week on the Lumentum deal (RSI 28). Analysts still see 87% upside; Serenity argues a MRVL rebound also lifts LITE.",
  "Q3 results Dec 1", "Deal dilution worries persist", (-15,12,28), 'Medium', 'Oversold rebound'),
 ('COHR', "Oversold optics maker (RSI 31, 51% off high) at about 15x forward earnings. Serenity names independent laser makers as possible M&A targets.",
  "Earnings Nov 4", "Earnings gap risk either way", (-18,12,30), 'Medium', 'Earnings setup'),
 ('SNDK', "Flash memory at about 4x forward earnings with revenue +378%, now 52% off its high.",
  "NAND contract prices", "Very volatile; 5% daily swings", (-18,12,30), 'Medium', 'Oversold value'),
 ('AAOI', "Laser and transceiver maker 71% off its high; Serenity says it gains strategic value after the MRVL/LITE deal.",
  "Earnings Nov 5", "Small cap; 7% daily swings", (-30,15,45), 'Speculative', 'M&A optionality'),
]
P[('swing','ai','SGX')] = [
 ('AWX.SI', "AEM fell 32% in a month (RSI 33); US chips rebounded on Nov 3 and AMD beat.",
  "Q3 business update (Nov)", "High beta to US chips overnight", (-15,10,25), 'Medium', 'Oversold rebound'),
 ('558.SI', "UMS is oversold (RSI 31) after a 31% monthly drop; analysts still see 75% upside.",
  "Q3 results mid-November", "Chip-equipment sentiment", (-12,9,22), 'Medium', 'Oversold rebound'),
 ('V03.SI', "Venture is the most oversold SGX tech name (RSI 26) with low volatility.",
  "Q3 business update (Nov)", "Flat revenue", (-6,5,11), 'Medium', 'Range trade'),
 ('E28.SI', "Frencken fell 26% this month (RSI 31); a move back toward its 50-day average is about +10%.",
  "Q3 business update (Nov)", "No clear catalyst before results", (-10,8,18), 'Medium', 'Oversold rebound'),
 ('MZH.SI', "Nanofilm is 54% off its high; volume is picking up (0.4x by mid-morning vs 0.1x for peers).",
  "Q3 business update (Nov)", "Tiny price steps mean large % moves", (-12,6,18), 'Speculative', 'Turnaround'),
]
P[('intraday','ai','US')] = [
 ('AMD', "Beat on Q3 and guided Q4 to about $17B; up about 5% after hours.",
  "Holding above the post-earnings opening range", "Gap fills if chips sell off", (-3,1.2,4), 'Medium', 'Post-earnings follow-through'),
 ('AEHR', "Jumped 26% on 2.9x volume after record revenue and a $150M full-year outlook.",
  "Second-day continuation above Tuesday's close", "Big gappers often fade on day two", (-6,1,7), 'Speculative', 'Momentum watch'),
 ('SMCI', "Reported a large revenue beat; rose about 8% before Wednesday's open.",
  "Hold above the gap", "History of sharp reversals", (-4,1,5), 'Speculative', 'Earnings gap'),
 ('ARM', "Reports Nov 4 after the close; RSI 36 and 54% off its high going in.",
  "Trade the direction of the first 30 minutes", "Gap either way", (-5,0.5,5), 'Speculative', 'Earnings reaction'),
 ('NVDA', "Slipped about 3% on Nov 4 on data-centre policy worries while the market rallied.",
  "Reclaiming $206 (Tuesday close)", "More policy headlines", (-2.5,0.6,3), 'Medium', 'Bounce watch'),
]
P[('intraday','ai','SGX')] = [
 ('AWX.SI', "Down 0.5% this morning; watch whether AMD's beat lifts AI test names at the next open.",
  "Next session: gap on US chip strength", "Nvidia's Nov 4 dip drags the group", (-3,1,4), 'Medium', 'Gap watch'),
 ('558.SI', "Flat and oversold; candidate for a reflex bounce.", "Next session open", "Trend still down", (-2.5,0.8,3), 'Medium', 'Bounce watch'),
 ('5DD.SI', "Down 0.8% on light volume after last week's breakout faded.", "Holding S$2.40", "Thin order book", (-2,0.5,2.5), 'Medium', 'Support test'),
 ('MZH.SI', "Down 2.6% but on the heaviest relative volume in the group.", "Next session open", "Small company; S$0.005 steps", (-3,0.5,3), 'Speculative', 'Volume watch'),
 ('V03.SI', "Oversold, low-volatility name near support.", "Next session", "Little momentum", (-1.5,0.4,1.5), 'Medium', 'Range'),
]

# ---------- Health ----------
P[('long','hc','US')] = [
 ('LLY', "Leader in obesity and diabetes drugs: revenue +39% and shares at a record. Steady compounder rather than a bargain (analyst upside ~2%).",
  "Orforglipron launch; Q4 results (late Jan/Feb)", "Drug-pricing pressure from a Democratic Congress", (-12,10,25), 'High', 'Quality compounder'),
 ('ARGX', "argenx: revenue +52% from its autoimmune franchise, 15% below its high, analysts see 27% upside.",
  "Pipeline readouts", "Competition in FcRn drugs", (-15,15,35), 'Medium', 'Growth at a discount'),
 ('INSM', "Insmed: revenue +268% from its lung-disease launch; 51% below its high with 86% analyst upside.",
  "Launch numbers each quarter", "High valuation on current earnings", (-25,25,55), 'Medium', 'Launch growth'),
 ('VRTX', "Vertex: steady +13% growth with cystic-fibrosis cash flow funding pain and kidney drugs.",
  "Pipeline updates", "Fell 4% on Nov 3 after results", (-12,10,22), 'Medium', 'Defensive growth'),
 ('ALNY', "Alnylam fell 30% in the week of its Oct 29 results and trades at about 14x forward earnings, 66% below its high.",
  "Heart-disease drug sales trend", "Further downgrades; sentiment broken", (-25,20,50), 'Speculative', 'Deep value'),
]
P[('long','hc','SGX')] = [
 ('Q0F.SI', "IHH runs hospitals across Asia; analysts see 36% upside.", "Q3 results Nov 25", "Currency swings", (-12,12,25), 'Medium', 'Regional leader'),
 ('C2PU.SI', "Parkway Life REIT: steady hospital and nursing-home rents, near its high.", "Dividend", "Higher rates", (-8,8,15), 'High', 'Income'),
 ('AP4.SI', "Riverstone makes cleanroom and medical gloves at about 14x earnings with 42% analyst upside.", "Q3 results (Nov)", "Glove price competition", (-15,12,30), 'Medium', 'Value'),
 ('BSL.SI', "Raffles Medical: Singapore hospital group, 23% off its high.", "Results (Feb)", "Shrinking revenue (-7%)", (-10,8,18), 'Medium', 'Recovery'),
 ('QC7.SI', "Q&M Dental is oversold (RSI 21) with 43% analyst upside.", "Results (Feb)", "Small and thinly traded", (-15,10,25), 'Speculative', 'Value'),
]
P[('swing','hc','US')] = [
 ('MDGL', "Fell 8% on 6x volume after Nov 3 results (RSI 23); revenue still +71% and analysts see 73% upside.",
  "Post-earnings flush often rebounds", "Launch growth slowing further", (-15,10,25), 'Medium', 'Oversold rebound'),
 ('ALNY', "RSI 21 after a 30% weekly drop; a rebound toward the 50-day average is worth about +15%.",
  "Analyst updates", "Trend still down", (-15,10,25), 'Speculative', 'Oversold rebound'),
 ('NVO', "Novo Nordisk at about 12x forward earnings, 37% off its high and trending up (RSI 65).",
  "Results Nov 4", "Obesity price war with Lilly", (-12,6,18), 'Medium', 'Earnings setup'),
 ('HIMS', "Hims & Hers is 42% off its high with revenue +38%.", "Earnings Nov 9", "Compounded-drug rules", (-20,10,30), 'Speculative', 'Earnings setup'),
 ('VKTX', "Viking Therapeutics: obesity drug developer with very large analyst upside, 38% off its high.",
  "Trial updates", "No revenue; financing risk", (-25,10,40), 'Speculative', 'Pipeline bet'),
]
P[('swing','hc','SGX')] = [
 ('QC7.SI', "Q&M is the most oversold SGX health name (RSI 21).", "Rebound toward 50-day average", "Thin trading", (-8,6,15), 'Speculative', 'Oversold rebound'),
 ('Q0F.SI', "IHH is oversold (RSI 36) ahead of Nov 25 results.", "Q3 results Nov 25", "Weak results", (-6,5,12), 'Medium', 'Pre-results'),
 ('AP4.SI', "Riverstone is 26% off its high (RSI 39).", "Q3 results (Nov)", "Glove pricing", (-8,5,12), 'Medium', 'Rebound'),
 ('C2PU.SI', "Parkway Life is a low-volatility defensive while rates ease.", "US 10-year yield dipping", "Rate rise", (-4,3,6), 'High', 'Defensive'),
 ('H02.SI', "Haw Par (Tiger Balm) holds net cash and investments well above its share price.", "Results (Nov)", "Shrinking revenue", (-6,4,10), 'Medium', 'Value'),
]
P[('intraday','hc','US')] = [
 ('ARGX', "Led large-cap biotech (+3%) on Nov 3; healthcare rose with the market on Nov 4.", "Holding above the open", "Sector rotation", (-2,0.8,3), 'Medium', 'Momentum long'),
 ('MDGL', "Down 8% on 6x volume after results; watch for a reflex bounce.", "Reclaiming the first-hour high", "Further selling", (-4,1,5), 'Speculative', 'Bounce watch'),
 ('MRNA', "Up 3.5% before Nov 6 results after a 675% run this year.", "Momentum into earnings", "Analysts see 39% downside", (-5,0.5,5), 'Speculative', 'Momentum watch'),
 ('NVO', "Reports Nov 4; trade the reaction.", "First 30 minutes", "Gap either way", (-4,0.5,4), 'Medium', 'Earnings reaction'),
 ('VRTX', "Fell 4% after results; large-cap quality names often stabilise the next day.", "Holding Tuesday's low", "Continued selling", (-2.5,0.6,3), 'Medium', 'Bounce watch'),
]
P[('intraday','hc','SGX')] = [
 ('QC7.SI', "Up 1% from an oversold level.", "Next session", "Thin trading", (-2,0.8,3), 'Speculative', 'Bounce'),
 ('C2PU.SI', "Up 0.75%, holding near its high.", "Next session", "Small range", (-1,0.4,1.5), 'High', 'Range'),
 ('AP4.SI', "Down 0.7% on light volume.", "Next session", "Glove pricing", (-1.5,0.3,2), 'Medium', 'Range'),
 ('H02.SI', "Down 0.8%; little momentum.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('BSL.SI', "Flat; very low volume.", "Next session", "Little momentum", (-1,0.2,1), 'Medium', 'Range'),
]

# ---------- Finance ----------
P[('long','fin','US')] = [
 ('SE', "Sea Ltd (Shopee, Garena, SeaMoney): revenue +48% at about 15x forward earnings, 51% below its high. Analysts see 93% upside.",
  "Q3 results Nov 10", "E-commerce competition in Southeast Asia", (-25,30,60), 'Medium', 'Growth at a discount'),
 ('SCHW', "Schwab trades at about 11x forward earnings, 21% off its high, with 31% analyst upside.",
  "Monthly client-asset reports", "Rate swings hit cash income", (-12,15,30), 'High', 'Quality value'),
 ('BAC', "Bank of America at under 10x forward earnings with a Strong Buy consensus.",
  "Q4 results Jan 15", "Credit losses if the economy slows", (-12,15,28), 'Medium', 'Value'),
 ('NU', "Nu Holdings: revenue +52% at about 10x forward earnings, oversold (RSI 20) since the Brazil election.",
  "Q3 results Nov 12", "Brazil policy and currency", (-25,25,55), 'Medium', 'Oversold growth'),
 ('IBKR', "Interactive Brokers: steady account growth, 21% off its high.",
  "Monthly metrics", "Lower trading volumes", (-15,15,32), 'Medium', 'Quality compounder'),
]
P[('long','fin','SGX')] = [
 ('D05.SI', "DBS is Singapore's largest and most profitable bank at about 16x earnings; now oversold (RSI 16) before results.",
  "Q3 results Nov 5", "Lower rates squeeze margins", (-10,12,22), 'High', 'Quality bank'),
 ('O39.SI', "OCBC: diversified bank and insurer at about 14x earnings, 15% off its high.",
  "Q3 results Nov 6", "Margin pressure", (-10,10,20), 'High', 'Quality bank'),
 ('AIY.SI', "iFAST: wealth platform with revenue +23% and 50% analyst upside, 31% off its high.",
  "Q3 results (Nov)", "Its UK digital bank still costs money", (-18,20,40), 'Medium', 'Growth'),
 ('S68.SI', "SGX: exchange earnings rise with trading volumes; 21% off its high.",
  "Monthly volume data", "Volumes fall in calm markets", (-10,10,20), 'Medium', 'Steady compounder'),
 ('U11.SI', "UOB fell 5% after a Q3 miss and margin warning; now about 11x earnings.",
  "Management guidance for 2027", "More provisions", (-12,6,18), 'Speculative', 'Value after a miss'),
]
P[('swing','fin','US')] = [
 ('XYZ', "Block was up about 15% midday on Nov 4 after its results; a possible trend change after a flat year.",
  "Analyst target raises", "Post-earnings fade", (-12,8,20), 'Medium', 'Post-earnings momentum'),
 ('GRAB', "Grab rose 9% on 2.3x volume after results; analysts see 76% upside.",
  "Breakout above the 50-day average", "Southeast Asia ride-hailing competition", (-12,10,25), 'Medium', 'Breakout'),
 ('HOOD', "Robinhood is oversold (RSI 30) and 42% off its high.",
  "Monthly metrics", "Crypto volumes", (-15,10,25), 'Speculative', 'Oversold rebound'),
 ('APO', "Apollo fell 5% on 2.8x volume after Nov 3 results; revenue +64% at about 11x forward earnings.",
  "Analyst updates", "Private-credit worries", (-10,8,18), 'Medium', 'Post-earnings dip'),
 ('SCHW', "Oversold (RSI 26) quality broker.", "Monthly metrics", "Rate swings", (-6,5,12), 'Medium', 'Oversold rebound'),
]
P[('swing','fin','SGX')] = [
 ('D05.SI', "DBS is very oversold (RSI 16) before Nov 5 results.", "Q3 results Nov 5", "Weak margin guide", (-7,5,12), 'Medium', 'Pre-results'),
 ('U11.SI', "UOB is oversold (RSI 17) after the 5% results drop.", "Reflex rebound", "More downgrades", (-7,4,10), 'Speculative', 'Oversold rebound'),
 ('O39.SI', "OCBC is oversold (RSI 25) before Nov 6 results.", "Q3 results Nov 6", "Weak margin guide", (-6,4,10), 'Medium', 'Pre-results'),
 ('S68.SI', "SGX is oversold (RSI 26).", "Monthly volume data", "Lower volumes", (-5,4,9), 'Medium', 'Oversold rebound'),
 ('AIY.SI', "iFAST is 31% off its high (RSI 39).", "Q3 results (Nov)", "UK bank costs", (-10,6,15), 'Speculative', 'Rebound'),
]
P[('intraday','fin','US')] = [
 ('XYZ', "Block was up about 15% midday on Nov 4 after results.", "Day-two hold above the gap", "Gap fade", (-4,0.8,4), 'Medium', 'Post-earnings follow-through'),
 ('GRAB', "Up 9% on results with 2.3x volume.", "Hold above $3.05", "Profit-taking", (-3,0.8,4), 'Medium', 'Momentum long'),
 ('COIN', "Up 5.7% on Nov 3, leading fintech.", "Crypto prices", "Crypto drops", (-4,0.8,4), 'Speculative', 'Momentum watch'),
 ('CRCL', "Circle reports Nov 4; trade the reaction.", "First 30 minutes", "Gap either way", (-5,0.5,5), 'Speculative', 'Earnings reaction'),
 ('APO', "Down 5% after results; watch for stabilisation.", "Holding Tuesday's low", "More selling", (-2.5,0.6,3), 'Medium', 'Bounce watch'),
]
P[('intraday','fin','SGX')] = [
 ('U11.SI', "Down 5% this morning on its Q3 miss.", "Next session: stabilisation above today's low", "More selling", (-2.5,0.5,2.5), 'Speculative', 'Bounce watch'),
 ('D05.SI', "Down 1.9% in sympathy before its own results tomorrow.", "Q3 results Nov 5", "Results gap", (-3,0.5,3), 'Medium', 'Pre-results'),
 ('O39.SI', "Down 1.5%; reports Nov 6.", "Next session", "Bank sentiment", (-2,0.4,2), 'Medium', 'Range'),
 ('S68.SI', "Down 0.7%; oversold.", "Next session", "Small range", (-1.5,0.4,1.5), 'Medium', 'Range'),
 ('AIY.SI', "Down 1%; light volume.", "Next session", "Small range", (-2,0.3,2), 'Speculative', 'Range'),
]

# IPO tab (6-month view), all markets
P[('ipo','all','US')] = [
 ('SPCX', "SpaceX listed in June at $135 (the largest IPO on record) and trades about 5% above that, 33% below its high. Analysts see 82% upside.",
  "xAI/GPU news; lock-up expiries", "Valuation and Musk headline risk; fell about 6% early on Nov 4", (-25,15,45), 'Medium', 'Mega-cap IPO'),
 ('ACCV', "Accelevation (IPO Sept 30 at $18) makes electrical gear for data centres: revenue +80% at about 14x forward earnings.",
  "First full quarter as a public company", "Data-centre policy risk; 6% daily swings", (-30,15,45), 'Speculative', 'Post-IPO value'),
 ('CHYM', "Chime (IPO June 2025 at $27) trades just above its IPO price with 40% analyst upside.",
  "Results Nov 4", "Fintech credit cycle", (-15,15,35), 'Medium', 'Post-IPO uptrend'),
 ('ADRX', "ADARx (IPO Sept 25 at $17) is oversold (RSI 32) with Strong Buy ratings.",
  "Pipeline updates", "Biotech volatility", (-30,15,50), 'Speculative', 'Oversold new listing'),
 ('CRCL', "Circle (IPO June 2025 at $31): stablecoin issuer 43% off its high.",
  "Results Nov 4", "Lower rates shrink interest income", (-25,12,40), 'Speculative', 'Recovery'),
]

# ---------- Power & grid (data-center power) ----------
P[('long','pwr','US')] = [
 ('GEV', "GE Vernova: gas turbines and grid gear sold out for years; Strong Buy with 29% upside.",
  "Q4 results Jan 27", "Data-centre build limits after the Democratic sweep", (-18,18,38), 'High', 'Core holding'),
 ('ETN', "Eaton rose 7% on Nov 3 after results; electrical gear for data centres and the grid at about 24x earnings.",
  "Order backlog updates", "Data-centre policy risk", (-15,15,30), 'High', 'Quality compounder'),
 ('VRT', "Vertiv: power and cooling for AI racks, revenue +61%, 37% off its high with 44% analyst upside.",
  "Q4 results (Feb)", "High beta; capex slowdown", (-25,22,50), 'Medium', 'Growth at a discount'),
 ('PWR', "Quanta builds power lines and substations: revenue +57%, up 14% in a week after results.",
  "Utility capex plans", "Valuation (30x)", (-15,12,28), 'Medium', 'Grid builder'),
 ('CEG', "Constellation: largest US nuclear fleet, 31% off its high with 29% analyst upside.",
  "Q3 results Nov 9", "Power-price regulation", (-18,15,35), 'Medium', 'Nuclear value'),
]
P[('long','pwr','SGX')] = [
 ('U96.SI', "Sembcorp: gas and renewables in Singapore and India at about 9x earnings.", "Results (Feb)", "Power-price swings", (-10,10,22), 'High', 'Value utility'),
 ('544.SI', "CSE Global: grid and data-centre engineering (Amazon deal), +6% today, 91% analyst upside.", "Order wins", "Small cap", (-20,20,45), 'Medium', 'Recovery'),
 ('BN4.SI', "Keppel: infrastructure, power and data-centre assets; 26% off its high.", "Asset sales", "Execution", (-12,12,25), 'Medium', 'Value'),
 ('DCRU.SI', "Digital Core REIT owns US data centres at a deep discount; 50% analyst upside.", "Leasing news", "Tenant concentration", (-12,12,28), 'Medium', 'Income + value'),
 ('AJBU.SI', "Keppel DC REIT: Asian data centres, steady income.", "Acquisitions", "Higher rates", (-8,8,16), 'Medium', 'Income'),
]
P[('swing','pwr','US')] = [
 ('TLN', "Talen rose 7% on 2x volume after Nov 3 results; Strong Buy with 27% upside.", "Data-centre power deals", "Policy risk", (-12,8,20), 'Medium', 'Post-earnings momentum'),
 ('BE', "Bloom Energy rose 9% on Nov 3; on-site fuel cells for data centres, revenue +138%.", "Order news", "Very volatile", (-20,10,28), 'Speculative', 'Momentum'),
 ('NRG', "NRG at about 9x forward earnings, 48% off its high with 80% analyst upside.", "Q3 results Nov 9", "Texas power-market rules", (-12,8,20), 'Medium', 'Pre-earnings value'),
 ('VST', "Vistra is down 28% from its high and fell on Nov 4 on the Texas data-centre pause proposal.", "Q3 results Nov 6", "Texas policy", (-15,6,20), 'Speculative', 'Pre-earnings'),
 ('CCJ', "Cameco is oversold (RSI 33) after a 12% weekly drop on 2x volume.", "Uranium contract prices", "Nuclear sentiment", (-12,7,18), 'Medium', 'Oversold rebound'),
]
P[('swing','pwr','SGX')] = [
 ('544.SI', "CSE Global broke higher (+6%) on normal volume.", "Order wins", "Small cap", (-10,8,18), 'Medium', 'Breakout'),
 ('BN4.SI', "Keppel is oversold (RSI 32).", "Asset monetisation news", "Slow execution", (-6,5,12), 'Medium', 'Oversold rebound'),
 ('DCRU.SI', "Digital Core REIT up 2.3% today with RSI 57.", "Leasing news", "Thin trading", (-6,5,12), 'Medium', 'Momentum'),
 ('AJBU.SI', "Keppel DC REIT is trending up (RSI 64).", "Rates easing", "Rate rise", (-5,3,8), 'Medium', 'Trend'),
 ('U96.SI', "Sembcorp is near support (RSI 39).", "Renewables deals", "Power prices", (-5,4,9), 'Medium', 'Range'),
]
P[('intraday','pwr','US')] = [
 ('TLN', "Up 7% on results with 2x volume.", "Hold above the open", "Profit-taking", (-3,0.8,3.5), 'Medium', 'Momentum long'),
 ('ETN', "Up 7% on results; large-cap trend day.", "Hold above Tuesday's close", "Rotation", (-2.5,0.6,3), 'Medium', 'Momentum long'),
 ('BE', "Up 9% on Nov 3; very volatile.", "Hold above $210", "Sharp reversals", (-5,1,5), 'Speculative', 'Momentum watch'),
 ('VST', "Fell on Nov 4 on the Texas data-centre pause proposal; reports Nov 6.", "Below the open = weak", "Policy headlines", (-4,-0.5,3), 'Speculative', 'Fade / avoid'),
 ('OKLO', "Oversold (RSI 25) on 2.1x volume before Nov 6 results.", "Reflex bounce", "Small-reactor sentiment", (-5,0.5,5), 'Speculative', 'Bounce watch'),
]
P[('intraday','pwr','SGX')] = [
 ('544.SI', "Up 6% this morning.", "Next session: hold today's gain", "Profit-taking", (-3,1,4), 'Medium', 'Follow-through'),
 ('DCRU.SI', "Up 2.3%.", "Next session", "Thin trading", (-2,0.5,2.5), 'Medium', 'Momentum'),
 ('AJBU.SI', "Up 0.9%, trending.", "Next session", "Small range", (-1.5,0.4,1.5), 'Medium', 'Trend'),
 ('U96.SI', "Small gain near support.", "Next session", "Small range", (-1.5,0.3,1.5), 'Medium', 'Range'),
 ('BN4.SI', "Down 0.9%, oversold.", "Next session", "Small range", (-1.5,0.3,1.5), 'Medium', 'Range'),
]

# ---------- Defence & industrials ----------
P[('long','def','US')] = [
 ('HWM', "Howmet makes engine and airframe parts: revenue +29%, up 16% in a week after results; Strong Buy.",
  "Aircraft build rates", "Valuation (34x)", (-15,18,35), 'High', 'Aerospace compounder'),
 ('GE', "GE Aerospace: jet engines and aftermarket service, a commercial (not budget-driven) story.",
  "Q4 results Jan 21", "Engine supply chain", (-12,14,28), 'High', 'Quality compounder'),
 ('AXON', "Axon: Tasers, body cameras and software, revenue +35%, 43% off its high with 63% analyst upside.",
  "Q3 results Nov 5", "Earnings gap risk", (-20,20,45), 'Medium', 'Growth at a discount'),
 ('RTX', "RTX: missiles plus commercial engines; less exposed to a defence-budget squeeze than pure primes.",
  "Q4 results Jan 26", "Defence budget under a Democratic Congress", (-12,10,22), 'Medium', 'Core holding'),
 ('KTOS', "Kratos: drones and hypersonics, 69% off its high with 119% analyst upside.",
  "Q3 results Nov 5", "Budget priorities may shift", (-30,20,55), 'Speculative', 'Deep value'),
]
P[('long','def','SGX')] = [
 ('S63.SI', "ST Engineering: defence, aerospace and smart-city work, oversold (RSI 23).", "Q3 update (Nov)", "Valuation (25x)", (-10,12,22), 'High', 'Quality compounder'),
 ('BS6.SI', "Yangzijiang Shipbuilding at about 8x earnings with revenue +36%; Strong Buy.", "New orders", "US port fees on China-built ships", (-15,15,30), 'Medium', 'Value'),
 ('S59.SI', "SIA Engineering: aircraft maintenance as Asian air travel grows; 29% analyst upside.", "Results (Nov)", "Flat revenue", (-10,12,24), 'Medium', 'Recovery'),
 ('H22.SI', "Hong Leong Asia: diesel engines and building materials at about 9x earnings, 42% off its high.", "Results (Feb)", "China demand", (-18,18,40), 'Speculative', 'Deep value'),
 ('C52.SI', "ComfortDelGro: buses, rail and taxis; steady and cheap.", "Results (Nov)", "Low growth", (-8,8,16), 'Medium', 'Defensive'),
]
P[('swing','def','US')] = [
 ('CAT', "Caterpillar is oversold (RSI 23) after a 27% monthly drop; data-centre generators are a growth line.",
  "Rebound toward the 50-day average", "Industrial slowdown", (-10,8,18), 'Medium', 'Oversold rebound'),
 ('AXON', "Reports Nov 5; 43% off its high.", "Q3 results Nov 5", "Earnings gap", (-15,8,22), 'Medium', 'Earnings setup'),
 ('KTOS', "Reports Nov 5 with RSI 56 and 69% off its high.", "Q3 results Nov 5", "Earnings gap", (-18,8,25), 'Speculative', 'Earnings setup'),
 ('BA', "Boeing 31% off its high with 35% analyst upside; delivery recovery.", "Monthly deliveries", "Production problems", (-12,7,18), 'Medium', 'Recovery'),
 ('LMT', "Lockheed is overbought (RSI 84) with only 2% analyst upside; defence names fell after the Democratic sweep.",
  "Mean reversion", "New war headlines", (-10,-4,5), 'Medium', 'Fade / avoid'),
]
P[('swing','def','SGX')] = [
 ('S63.SI', "ST Engineering is oversold (RSI 23).", "Q3 update (Nov)", "Defence sentiment", (-5,4,9), 'Medium', 'Oversold rebound'),
 ('BS6.SI', "Yangzijiang pulled back 7% this month (RSI 35).", "New orders", "Port-fee news", (-8,6,14), 'Medium', 'Pullback buy'),
 ('H22.SI', "Hong Leong Asia fell 15% this month.", "Rebound", "Thin trading", (-10,6,16), 'Speculative', 'Oversold rebound'),
 ('S59.SI', "SIA Engineering up 1.7% today and trending (RSI 69).", "Results (Nov)", "Overbought short-term", (-5,3,8), 'Medium', 'Momentum'),
 ('C52.SI', "ComfortDelGro trending up (RSI 64) with low volatility.", "Results (Nov)", "Low growth", (-3,2,5), 'Medium', 'Trend'),
]
P[('intraday','def','US')] = [
 ('HWM', "Up 4.7% on 2.8x volume; strongest name in the group.", "Hold above the open", "Profit-taking", (-2.5,0.6,3), 'Medium', 'Momentum long'),
 ('GE', "Up 1.6% on 2.2x volume.", "Hold above the open", "Rotation", (-2,0.5,2.5), 'Medium', 'Momentum long'),
 ('CAT', "Oversold (RSI 23); industrials lagged on Nov 4.", "Reflex bounce", "Further selling", (-2.5,0.5,3), 'Medium', 'Bounce watch'),
 ('GD', "Overbought (RSI 87); defence primes fell after the election.", "Below the open = weak", "War headlines", (-2,-0.4,1.5), 'Medium', 'Fade / avoid'),
 ('LMT', "Overbought (RSI 84) with little analyst upside.", "Below the open = weak", "War headlines", (-2,-0.4,1.5), 'Medium', 'Fade / avoid'),
]
P[('intraday','def','SGX')] = [
 ('S59.SI', "Up 1.7%, leading the group.", "Next session", "Small range", (-1.5,0.5,2), 'Medium', 'Momentum'),
 ('BS6.SI', "Up 0.4%.", "Next session", "Port-fee news", (-2,0.4,2.5), 'Medium', 'Range'),
 ('S63.SI', "Flat and oversold.", "Next session", "Defence sentiment after US vote", (-1.5,0.3,1.5), 'Medium', 'Bounce watch'),
 ('C52.SI', "Flat; very light volume.", "Next session", "Small range", (-1,0.2,1), 'Medium', 'Range'),
 ('H22.SI', "Down 0.9%.", "Next session", "Thin trading", (-2,0.2,2), 'Speculative', 'Range'),
]

# ---------- Energy (oil and gas) ----------
P[('long','nrg','US')] = [
 ('XOM', "Exxon: lowest-cost large oil producer with chemicals and refining as buffers. Oil fell below $100 on Nov 4 as war-premium fades.",
  "Q4 results Jan 29", "Oil keeps falling on an Iran deal", (-20,4,18), 'Medium', 'Defensive oil'),
 ('DVN', "Devon at about 9x forward earnings with 30% analyst upside; Strong Buy.",
  "Q3 results Nov 5", "Oil price drop", (-25,8,25), 'Medium', 'Value'),
 ('FANG', "Diamondback: low-cost Permian producer at about 9x forward earnings, 25% analyst upside.",
  "Q3 reported Nov 2", "Oil price drop", (-25,6,22), 'Medium', 'Value'),
 ('LNG', "Cheniere: long-term LNG contracts, at a record; less tied to oil prices.", "Export growth", "Little analyst upside (3%)", (-15,4,15), 'Medium', 'Steady'),
 ('SLB', "SLB: oilfield services with 20% analyst upside.", "Q4 results Jan 22", "Drilling cuts at lower oil", (-20,6,20), 'Medium', 'Value'),
]
P[('long','nrg','SGX')] = [
 ('5E2.SI', "Seatrium builds offshore rigs and wind platforms; 36% analyst upside.", "New orders", "Contract delays", (-15,12,28), 'Medium', 'Recovery'),
 ('BN4.SI', "Keppel: energy infrastructure and asset management.", "Asset sales", "Execution", (-12,10,22), 'Medium', 'Value'),
 ('RE4.SI', "Geo Energy: Indonesian coal at about 7x earnings.", "Coal prices", "Coal price drop", (-25,8,30), 'Speculative', 'Value'),
 ('5LY.SI', "Marco Polo Marine: offshore vessels, revenue +40% at about 10x earnings.", "Results (Nov)", "Thin trading", (-25,10,35), 'Speculative', 'Growth value'),
 ('5WH.SI', "Rex International is in a long downtrend; no setup.", "None", "Further losses", (-30,-5,20), 'Speculative', 'Avoid'),
]
P[('swing','nrg','US')] = [
 ('DVN', "Reports Nov 5; down 7% this week with Strong Buy ratings.", "Q3 results Nov 5", "Oil drop", (-12,4,12), 'Medium', 'Earnings setup'),
 ('MPC', "Marathon Petroleum is oversold (RSI 27) after a 163% run this year.", "Refining margins", "Margins fall with crude", (-12,3,12), 'Speculative', 'Oversold'),
 ('PSX', "Phillips 66 is oversold (RSI 33).", "Refining margins", "Margins fall", (-12,3,12), 'Speculative', 'Oversold'),
 ('OXY', "Occidental reports Nov 9; 9% off its high.", "Q3 results Nov 9", "Oil drop", (-12,2,10), 'Medium', 'Earnings setup'),
 ('COP', "Energy fell about 4% on Nov 4 as Brent dropped below $100; trend is turning down.", "Q3 results Nov 5", "An Iran deal pushes oil lower", (-12,-3,6), 'Medium', 'Fade / avoid'),
]
P[('swing','nrg','SGX')] = [
 ('5E2.SI', "Seatrium is neutral (RSI 50) and 25% off its high.", "Orders", "Contract delays", (-8,5,12), 'Medium', 'Recovery'),
 ('BN4.SI', "Keppel is oversold (RSI 32).", "Asset sales", "Execution", (-6,4,10), 'Medium', 'Oversold rebound'),
 ('5LY.SI', "Marco Polo fell 14% this month.", "Results (Nov)", "Thin trading", (-10,5,15), 'Speculative', 'Rebound'),
 ('RE4.SI', "Geo Energy fell 14% this month.", "Coal prices", "Coal drop", (-10,3,12), 'Speculative', 'Rebound'),
 ('5WH.SI', "Rex is in a downtrend; no setup.", "None", "Further losses", (-15,-2,10), 'Speculative', 'Avoid'),
]
P[('intraday','nrg','US')] = [
 ('XOM', "Energy fell about 4% on Nov 4; large-cap majors usually stabilise first.", "Holding the morning low", "Oil keeps sliding", (-2,0.3,2), 'Medium', 'Bounce watch'),
 ('COP', "Reports Nov 5 into falling oil.", "First 30 minutes", "Gap either way", (-3,0,3), 'Medium', 'Earnings reaction'),
 ('EOG', "Reports Nov 5.", "First 30 minutes", "Gap either way", (-3,0,3), 'Medium', 'Earnings reaction'),
 ('LNG', "Less tied to oil; held near a record.", "Relative strength", "Sector selling", (-2,0.4,2), 'Medium', 'Relative strength'),
 ('FANG', "Fell 3.7% on Nov 3; the energy sector fell another ~4% on Nov 4.", "Below the open = weak", "Oil slide", (-3,-0.3,2.5), 'Medium', 'Fade / avoid'),
]
P[('intraday','nrg','SGX')] = [
 ('5E2.SI', "Flat on light volume.", "Next session", "Small range", (-2,0.4,2), 'Medium', 'Range'),
 ('BN4.SI', "Down 0.9%, oversold.", "Next session", "Small range", (-1.5,0.3,1.5), 'Medium', 'Range'),
 ('RE4.SI', "Flat; coal names follow oil lower.", "Next session", "Oil drop", (-2.5,0,2), 'Speculative', 'Range'),
 ('5LY.SI', "Down 0.9%.", "Next session", "Thin trading", (-2.5,0.3,2.5), 'Speculative', 'Range'),
 ('5WH.SI', "Flat penny stock in a downtrend; avoid.", "None", "Further losses", (-5,-1,4), 'Speculative', 'Avoid'),
]

IPO_LIST = [
 # sym, name, ipo_date, ipo_price, sector, status
 ('ANTHROPIC','Anthropic (not yet listed; roadshow may start week of Nov 9)','2026-10-26',None,'ai','Filed'),
 ('AGLT','Agility Robotics (merger listing)','2026-11-05',None,'ai','Expected'),
 ('FBLLU','Football Manager SPAC','2026-11-02',10.00,'fin','Expected'),
 ('SCQC','SPACCircle Acquisition Corp.','2026-10-27',10.00,'fin','Expected'),
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
 ('2026-11-03T02:44','AEHR AMD', "Via tracker: says Aehr's earnings beat and strong demand contradict the recent selloff, and points to an AMD-linked chip burn-in opportunity."),
 ('2026-11-03T02:04','SPCX LITE SNDK NBIS COHR', "Via tracker: argues hyperscaler and optics spending show real demand, and that cybersecurity and biotech look more bubbly than memory stocks."),
 ('2026-11-03T00:43','LITE MRVL NVDA', "Via tracker: walks through Lumentum's new $5B co-packaged optics contract and the Marvell deal terms and timing."),
 ('2026-11-02T22:15','CRDO MRVL', "Via tracker: notes Credo has no in-house CW lasers, so it could become an acquisition target like Lumentum."),
 ('2026-11-02T20:33','LITE MRVL', "Via tracker: explains the all-stock deal means Lumentum's value now tracks Marvell, so a Marvell recovery lifts LITE too."),
 ('2026-11-02T20:14','AAOI COHR LITE MRVL AVGO', "Via tracker: expects independent Western laser makers (AAOI, Coherent, Sivers) to draw M&A interest and premium valuations."),
 ('2026-11-02T19:43','AAOI INTC TSEM', "Via tracker: says October saw record hedge-fund de-grossing and rising short interest despite strong AI-capex earnings; calls photonics and memory a generational opportunity."),
]

EVENTS = [
 ('2026-11-02','AI','Marvell agrees to buy Lumentum', "All-stock deal: 4.5 Marvell shares per Lumentum share (about $115B). Marvell fell sharply; Lumentum now trades below the deal value."),
 ('2026-11-03','AI','Chips rebound; Aehr +26%', "Nasdaq +0.8%, S&P +0.4%, ending a 3-day slide. Aehr posted record revenue and a $150M full-year outlook."),
 ('2026-11-03','AI','AMD beats on Q3', "Revenue $13.4B (+45%), EPS $2.09 vs $1.95 expected; Q4 guide about $17B. Shares up about 5% after hours."),
 ('2026-11-03','Macro','US midterm elections: Democrats win Congress', "Worries about tighter data-centre rules; Texas governor-elect Hinojosa has proposed pausing new data-centre projects."),
 ('2026-11-04','Macro','Dow +3.0%, best post-midterm day in 44 years', "S&P +1.6%, Nasdaq +1.4%. Brent fell about $10 to below $100; energy was the worst sector (about -4%); defence and Nvidia slipped."),
 ('2026-11-04','Fin','UOB misses Q3 estimates', "Shares fell about 5% to a four-month low on profit miss and margin pressure."),
 ('2026-11-04','AI','ARM, Qualcomm, Coherent report', "After the US close."),
 ('2026-11-05','Fin','DBS Q3 results', "Before the SGX open. OCBC follows on Nov 6."),
 ('2026-11-05','Mixed','Earnings: IREN, AAOI, Axon, Kratos, ConocoPhillips, EOG, Devon, Affirm', "Also Agility Robotics expected to start trading after its merger closes."),
 ('2026-11-06','Power','Vistra, Oklo, Moderna report', "Vistra is the most exposed to the Texas data-centre proposal."),
 ('2026-11-09','AI','Anthropic IPO roadshow may begin', "Reported timing; listing targeted before Thanksgiving (Nov 26). Not confirmed."),
 ('2026-11-10','Mixed','CoreWeave and Sea report', "Nebius, Applied Materials and Nu follow on Nov 12."),
 ('2026-11-17','AI','Nvidia Q3 results', "The main AI-demand checkpoint this month."),
 ('2026-10-28','Macro','Fed held rates (10-2 vote)', "Two Fed presidents since said rates may need to rise; markets price a December hike. 10-year yield about 4.9%."),
]
