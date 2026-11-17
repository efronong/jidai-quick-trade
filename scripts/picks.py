# Analyst picks for 2026-11-18 SGT (snapshot: US Tue Nov 17 ~13:50 ET, SGX close Nov 17). Fields: sym, thesis, catalyst, risk, (low, base, high) % expected move, conviction, setup
# Horizons: long = 12 months, swing = ~4 weeks, intraday = rest of session (US) / next session (SGX), ipo = 6 months.
# Context: Tue Nov 17: S&P -1.0%, Dow -1.6% (~-950 pts), Nasdaq -0.7%; almost 9 in 10 S&P stocks fell; VIX ~26. Fourth straight down day.
# October retail sales +0.2% (control group stronger than expected). 10-yr ~5.10%. Dec Fed hike ~95% priced (CME). FOMC minutes Wed.
# Nvidia closed ~$155 (-0.5%), then reported after the bell: revenue $115.8B (+103%) vs ~$109B expected; Q4 guide $130B +/-3% vs ~$125B; extra $150B buyback.
# Shares rose ~2-5% after hours. Huang said on X he would be "honored" to return; chair Harvey Jones says the board does not intend to reinstate him. Reported SEC probe on disclosures.
# Optics (COHR, LITE, GLW, AAOI) gave up early gains after reports the US plans curbs on Chinese data-centre equipment. Banks weak (JPM -2.7%). UNH -4%. Brent +0.8% to ~$93.
# Klarna Q3: revenue +12%, back to profit; KLAR +3%. Anthropic (ANT) keeps $70-78 range; prices Wed, trades Thu Nov 19.
# SGX: STI -1.4% to ~5,110 on US chip-curb worries. AEM -5%, Frencken -5%, UMS -4.5%, CSE Global -7.4%, Keppel -3.1%, DBS -2.2%.
# Geo Energy clarified on Nov 17 it has received no new Indonesian mining directive and operations are normal; no trade in the snapshot on Nov 17.
P = {}

# ---------- AI & chips ----------
P[('long','ai','US')] = [
 ('TSM', "Makes almost every leading AI chip, whoever designs it. Revenue +51% at about 15x forward earnings, 26% below its high after two down days. Nvidia's $130B guide is a direct read-across for TSMC wafers.",
  "November sales (~Dec 10); Q4 results Jan 14", "Taiwan geopolitics; new US chip-access rules", (-20,16,38), 'High', 'Core holding'),
 ('AVGO', "Custom AI chips plus networking: revenue +86% at about 17.5x forward earnings, 30% below its high. Rose on a weak day; results Dec 9.",
  "Q4 results Dec 9", "Lumpy custom-chip orders; AI financing worries", (-24,17,42), 'High', 'Leader, less key-person risk'),
 ('NVDA', "Beat and raised: Q3 revenue $115.8B (+103%), Q4 guide $130B, and $150B more buyback. About 10x forward earnings, 36% off its high. Leadership is still unsettled: the board says it won't bring Huang back.",
  "Post-earnings estimate upgrades; CEO search", "No permanent CEO; SEC disclosure probe; China rules", (-30,15,50), 'Medium', 'Cheap leader, leadership risk'),
 ('MU', "Memory is still the tightest part of AI servers: revenue +379% at about 3.4x forward earnings, 43% off its high (RSI 28). Fell another 3% on the day.",
  "FQ1 results Dec 23", "DRAM lawsuit; memory falls hard when prices turn", (-40,18,58), 'Medium', 'Cycle leader'),
 ('COHR', "Coherent: record quarter and a ~$20B five-year optics deal; 51% below its high at about 13x forward earnings. A US curb on Chinese data-centre gear would favour US optics makers.",
  "Optics orders; FQ2 results (Feb)", "8% daily swings; policy headlines cut both ways", (-35,18,55), 'Medium', 'Optics rebound'),
]
P[('long','ai','SGX')] = [
 ('AWX.SI', "AEM is up ~270% this year but 44% below its high after a 5% drop on Nov 17; analysts see about 100% upside.",
  "Q3 business update (Nov); Nvidia beat", "One large customer; 7% daily swings", (-40,16,55), 'Medium', 'SGX AI leader'),
 ('V03.SI', "Venture: net cash, about 15x earnings, low volatility; analysts see about 30% upside. Flat on a 1.4% STI drop.",
  "Analyst upgrades after Q3", "Slow revenue growth (+7%)", (-12,12,25), 'High', 'Steady value'),
 ('558.SI', "UMS makes precision parts for chip-equipment makers: revenue +61%, 43% off its high, about 17x earnings.",
  "Chip-equipment spending outlook", "Tied to Applied Materials spending", (-32,15,45), 'Medium', 'Equipment supplier'),
 ('5DD.SI', "Micro-Mechanics makes precision tools for chip assembly and test: revenue +45%, 41% off its high.",
  "Q1 FY27 results (Nov)", "Small and thinly traded", (-24,13,36), 'Medium', 'Growth at a discount'),
 ('E28.SI', "Frencken builds modules for chip and medical equipment; 52% off its high at about 14x earnings after a 5% drop.",
  "Q3 business update (Nov)", "Flat revenue so far this year", (-26,12,36), 'Medium', 'Recovery'),
]
P[('swing','ai','US')] = [
 ('NVDA', "RSI 16 into a clear beat and raise; up ~2-5% after hours. Oversold stocks often keep bouncing after a strong print.",
  "Analyst target raises; Anthropic IPO mood", "Leadership or SEC headlines fade the bounce", (-14,7,22), 'Medium', 'Oversold, post-beat'),
 ('LITE', "Marvell is buying Lumentum for 4.5 Marvell shares each. At snapshot prices that is worth about 19% more than LITE's price.",
  "Spread narrows if the deal clears", "Regulatory delay (incl. China); MRVL falls again", (-15,8,22), 'Medium', 'Merger spread'),
 ('TSM', "RSI 31 after a 9% five-day drop; Nvidia's guide points to more TSMC wafer demand.", "November sales (~Dec 10)", "Chip-rule headlines", (-10,5,14), 'Medium', 'Oversold leader'),
 ('MU', "RSI 28 after another 3% drop; still about 3.4x forward earnings with price-floor contracts.",
  "FQ1 results Dec 23", "Lawsuit news; AI capex fears", (-16,7,22), 'Medium', 'Rebound'),
 ('AVGO', "Held up on a down day (RSI 46); results on Dec 9 fall inside the swing window.",
  "Q4 results Dec 9", "AI financing worries", (-13,5,17), 'Medium', 'Pullback in leader'),
]
P[('swing','ai','SGX')] = [
 ('AWX.SI', "AEM fell 5% to RSI 37; down 29% in a month. Nvidia's beat may help the next sessions.", "Q3 update; Nvidia read-across", "US chip curbs", (-20,6,26), 'Speculative', 'Oversold rebound'),
 ('558.SI', "UMS fell 4.5% to RSI 35.", "Chip-equipment read-across", "Chip-equipment sentiment", (-15,5,18), 'Medium', 'Oversold with catalyst'),
 ('V03.SI', "Venture flat (RSI 43); the steadiest name in the group.", "Analyst upgrades", "Low growth", (-6,3,9), 'High', 'Range'),
 ('5DD.SI', "Micro-Mechanics RSI 35; small and steady.", "Q1 FY27 results", "Thin trading", (-10,4,12), 'Medium', 'Support'),
 ('E28.SI', "Frencken fell 5% to RSI 33.", "Bounce", "Flat revenue", (-12,4,14), 'Speculative', 'Oversold rebound'),
]
P[('intraday','ai','US')] = [
 ('NVDA', "Beat and raised after the bell; up ~2-5% after hours. Watch whether the gap holds through the open.", "Post-earnings gap", "Gap fades as in past quarters", (-4,1.5,6), 'Medium', 'Post-earnings gap'),
 ('TSM', "Fell 3.8%; Nvidia's guide is a direct positive read-across.", "Sympathy move", "Taiwan selling", (-3,0.8,4), 'Medium', 'Sympathy bounce'),
 ('MU', "Fell 3.1% (RSI 28).", "Nvidia read-across", "Legal headlines", (-5,0.5,5), 'Speculative', 'Bounce watch'),
 ('CRWV', "AI cloud names move with Nvidia's print and the Anthropic IPO mood.", "Sympathy move", "Debt worries", (-6,0.5,7), 'Speculative', 'Momentum'),
 ('AMD', "Fell 3% after reversing early gains.", "Sympathy move", "Chip-rule headlines", (-5,0.5,5), 'Speculative', 'Range'),
]
P[('intraday','ai','SGX')] = [
 ('AWX.SI', "Fell 5.3%; Nvidia beat overnight.", "Next session", "US chips weak again", (-5,1,6), 'Speculative', 'Bounce watch'),
 ('558.SI', "Fell 4.5%.", "Next session", "Follows US chip equipment", (-4.5,0.5,4.5), 'Speculative', 'Bounce watch'),
 ('E28.SI', "Fell 5%.", "Next session", "Thin trading", (-3.5,0.5,4), 'Speculative', 'Bounce watch'),
 ('V03.SI', "Flat on a weak day.", "Next session", "Small range", (-2,0.3,2.2), 'Medium', 'Range'),
 ('5DD.SI', "Fell 2.2%.", "Next session", "Thin trading", (-3,0.2,3), 'Medium', 'Range'),
]

# ---------- Health ----------
P[('long','hc','US')] = [
 ('LLY', "Obesity-drug leader: revenue +39%, 2% off its high (+31% this year). Little analyst upside left, so the base case is modest.",
  "Orforglipron launch; Q4 results (Feb)", "Drug-price policy", (-16,8,25), 'High', 'Defensive growth'),
 ('ARGX', "argenx: revenue +52% from its immune-disease drug Vyvgart, 10% off its high, 21% analyst upside.",
  "New indications in 2027", "Competition in myasthenia gravis", (-15,10,28), 'Medium', 'Growth leader'),
 ('MDGL', "Madrigal's liver drug Rezdiffra is growing fast (revenue +50%); 30% off its high with 63% analyst upside. Flat on a weak day.",
  "Script data; EU rollout", "Competition from GLP-1 drugs", (-22,20,45), 'Medium', 'Oversold growth'),
 ('INSM', "Insmed's lung drug launch drives revenue +268%; up 28% in a month, still 42% off its high.",
  "Brensocatib launch numbers", "Overbought short term (RSI 74); high valuation", (-30,16,45), 'Medium', 'Launch story'),
 ('VRTX', "Vertex: steady growth (+12%), 4% off its high, about 27x earnings; less exposed to drug-price headlines than most.",
  "Pain-drug launch; kidney data", "Valuation", (-14,9,22), 'Medium', 'Steady growth'),
]
P[('long','hc','SGX')] = [
 ('Q0F.SI', "IHH runs hospitals across Asia; analysts see 36% upside. Fell 2% ahead of Q3 results.", "Q3 results Nov 25", "Currency swings", (-12,11,24), 'Medium', 'Regional leader'),
 ('C2PU.SI', "Parkway Life REIT: steady hospital and nursing-home rents, 6% off its high.", "Dividend", "US 10-yr yield above 5%", (-8,7,15), 'High', 'Income'),
 ('AP4.SI', "Riverstone makes cleanroom and medical gloves at about 14x earnings with 37% analyst upside; rose 2% on a weak day.", "Q3 results (Nov)", "Glove price competition", (-15,11,28), 'Medium', 'Value'),
 ('BSL.SI', "Raffles Medical: Singapore hospital group, 22% off its high, steady (RSI 67).", "Results (Feb)", "Shrinking revenue (-7%)", (-10,8,18), 'Medium', 'Recovery'),
 ('H02.SI', "Haw Par (Tiger Balm) trades near 10x earnings with a large cash and investment pile; 32% off its high.", "Results (Feb)", "Revenue down 8%", (-12,6,16), 'Medium', 'Value'),
]
P[('swing','hc','US')] = [
 ('LLY', "Near its high; a place to hide from the chip sell-off.", "Orforglipron news", "Money rotating back into chips", (-8,3,10), 'High', 'Relative strength'),
 ('GILD', "Gilead rose 1.8% on a down day, 2% off its high (RSI 64); about 17x earnings.", "HIV franchise; pipeline news", "Rotation out of defensives", (-6,2,7), 'Medium', 'Relative strength'),
 ('MDGL', "Steady (RSI 46); 63% analyst upside.", "Script data", "Biotech risk-off", (-12,6,18), 'Medium', 'Rebound'),
 ('ALNY', "Oversold (RSI 18), 67% off its high; 91% analyst upside.", "Amvuttra script data", "Trend still down", (-15,7,22), 'Speculative', 'Oversold rebound'),
 ('CYTK', "Cytokinetics' heart drug launch is starting; 41% off its high (RSI 32), about 110% analyst upside.", "Launch numbers", "Launch slower than hoped", (-15,6,20), 'Speculative', 'Launch rebound'),
]
P[('intraday','hc','US')] = [
 ('UNH', "Fell 4.3%; no single cause found beyond a weak tape.", "Dip buying", "Policy headlines", (-2.5,0.3,2.5), 'Medium', 'Bounce watch'),
 ('MRNA', "Fell 4.9%; down 18% in five days.", "Bounce", "6% daily swings", (-6,0,6), 'Speculative', 'Bounce watch'),
 ('GILD', "Rose 1.8% against the market.", "Momentum", "Gives back gains", (-2,0.3,2.2), 'Medium', 'Relative strength'),
 ('HIMS', "Fell 4.8% (RSI 24).", "Bounce", "More selling", (-6,0,6), 'Speculative', 'Bounce watch'),
 ('LLY', "Small dip near its high.", "Defensive bid", "Rotation into tech after Nvidia", (-2.2,0.2,2.2), 'Medium', 'Range'),
]
P[('swing','hc','SGX')] = [
 ('Q0F.SI', "IHH eased 2% (RSI 40) ahead of Q3 results.", "Q3 results Nov 25", "Results miss", (-6,3,9), 'Medium', 'Pre-earnings'),
 ('C2PU.SI', "Parkway Life REIT: lowest-volatility name in the group.", "Dividend", "Rates", (-4,2,6), 'High', 'Range'),
 ('AP4.SI', "Riverstone rose 2% (RSI 52); large analyst upside.", "Q3 results (Nov)", "Glove prices", (-8,3,10), 'Medium', 'Support'),
 ('BSL.SI', "Raffles Medical holding a mild uptrend (RSI 67).", "Momentum", "Low volume", (-5,2,6), 'Medium', 'Trend'),
 ('QC7.SI', "Q&M Dental is very oversold (RSI 9).", "Bounce", "Small cap", (-8,3,10), 'Speculative', 'Oversold rebound'),
]
P[('intraday','hc','SGX')] = [
 ('AP4.SI', "Rose 2%.", "Next session", "Gives back gains", (-2,0.2,2), 'Medium', 'Follow-through check'),
 ('Q0F.SI', "Fell 2%.", "Next session", "Malaysia market swings", (-2,0.3,2), 'Medium', 'Bounce watch'),
 ('C2PU.SI', "Eased 0.3%.", "Next session", "Small range", (-1,0.2,1), 'Medium', 'Range'),
 ('BSL.SI', "Flat.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('H02.SI', "Fell 0.8%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
]

# ---------- Finance ----------
P[('long','fin','US')] = [
 ('JPM', "Best-run US bank, 10% off its high at about 13x forward earnings. Higher rates (10-yr ~5.1%) support interest income. Named a new CFO for 2027.", "Q4 results Jan 14", "Credit cycle; outage and AI-spending worries", (-15,8,22), 'High', 'Core holding'),
 ('V', "Visa: steady growth (+13%), 4% off its high; little AI exposure.", "Holiday spending", "Regulation of card fees", (-12,6,18), 'High', 'Defensive growth'),
 ('GS', "Trading and deal-making boom, about 12x forward earnings, 24% off its high. A lead bank on the record Anthropic IPO.",
  "Anthropic prices Nov 18, trades Nov 19", "Market volatility hits deals", (-20,10,28), 'Medium', 'Cyclical value'),
 ('NU', "Nubank: revenue +34% at about 11x forward earnings, 34% off its high; 45% analyst upside.", "Q4 results (Feb)", "Brazil credit and currency", (-30,16,48), 'Medium', 'Growth at a discount'),
 ('SE', "Sea: revenue +43%; $1B buyback. About 15x forward earnings, 53% off its high.",
  "Q4 results (Mar)", "Rising credit costs at Monee; competition", (-30,18,50), 'Medium', 'Oversold growth'),
]
P[('long','fin','SGX')] = [
 ('D05.SI', "DBS kept its 81-cent quarterly dividend and says interest income has bottomed; 14% off its high (RSI 18) after a 2.2% drop.",
  "Q4 results (Feb)", "Margins if rates fall; stronger SGD", (-10,8,16), 'High', 'Income leader'),
 ('O39.SI', "OCBC was the only local bank to beat in Q3 and raised loan-growth guidance.",
  "Q4 results (Feb)", "Margin fell 18 bp to 1.66%", (-10,7,15), 'Medium', 'Income'),
 ('U11.SI', "UOB missed Q3 and cut its margin guidance; RSI 16, 18% off its high.", "Recovery in fees", "More credit provisions", (-12,7,17), 'Medium', 'Oversold income'),
 ('AIY.SI', "iFAST: fintech platform, revenue +23%, 28% off its high with 44% analyst upside.", "HK pension business", "Market-driven volumes", (-18,16,36), 'Medium', 'Growth'),
 ('S68.SI', "SGX benefits from high trading volumes; from Jan 2027 its RegCo takes over IPO prospectus reviews.", "Monthly volume data", "Already priced (24x earnings)", (-12,7,18), 'Medium', 'Volatility winner'),
]
P[('swing','fin','US')] = [
 ('GS', "Anthropic prices on Nov 18 and trades on Nov 19; books reportedly ~6x covered.", "Deal fees", "Volatility (VIX ~26)", (-9,4,12), 'Medium', 'Deal pipeline'),
 ('MA', "Mastercard is near its high (RSI 64).", "Holiday spending data", "Rotation out of defensives", (-6,2,7), 'High', 'Relative strength'),
 ('KLAR', "Klarna's Q3: revenue +12% and back to a profit; shares +3% (RSI 58), still 60% below the high.", "Holiday volumes", "Credit losses", (-12,6,18), 'Speculative', 'Post-results momentum'),
 ('SCHW', "Schwab about 12x forward earnings with 28% analyst upside (RSI 57).", "Monthly client metrics", "Rates and market swings", (-8,3,10), 'Medium', 'Support'),
 ('HOOD', "RSI 25 after a 16% five-day drop; retail access to the Anthropic IPO runs partly through Robinhood.", "Anthropic IPO demand", "More crypto weakness", (-18,6,24), 'Speculative', 'Oversold rebound'),
]
P[('swing','fin','SGX')] = [
 ('D05.SI', "DBS is oversold (RSI 18).", "Dividend support", "Margin worries", (-4,3,7), 'High', 'Oversold income'),
 ('U11.SI', "UOB RSI 16.", "Rebound", "Further downgrades", (-5,3,8), 'Medium', 'Oversold rebound'),
 ('O39.SI', "OCBC fell 2.2% (RSI 36).", "Post-results recovery", "Margin squeeze", (-4,2,6), 'Medium', 'Pullback'),
 ('AIY.SI', "iFAST RSI 47.", "Momentum", "Market-driven", (-8,3,10), 'Medium', 'Range'),
 ('S68.SI', "SGX benefits when markets are volatile.", "Volume data", "Valuation", (-5,2,7), 'Medium', 'Volatility winner'),
]
P[('intraday','fin','US')] = [
 ('HOOD', "Fell 5.4% (RSI 25); Anthropic IPO prices tonight.", "Anthropic IPO interest", "Crypto weakness", (-5,0.5,5.5), 'Speculative', 'Bounce watch'),
 ('COIN', "Fell 3.2% with bitcoin near $64K (RSI 23).", "Crypto bounce", "More crypto selling", (-5,0,5), 'Speculative', 'Crypto beta'),
 ('KLAR', "Rose 3% after Q3.", "Follow-through", "Gives back gains", (-3.5,0.3,3.5), 'Speculative', 'Post-results'),
 ('JPM', "Fell 2.3-2.7%.", "Dip buying", "Bank weakness", (-2,0.3,2), 'Medium', 'Dip watch'),
 ('GS', "Fell 2%; Anthropic pricing tonight.", "IPO fees", "Market risk-off", (-2.5,0.3,2.5), 'Medium', 'Range'),
]
P[('intraday','fin','SGX')] = [
 ('D05.SI', "Fell 2.2%; RSI 18.", "Next session", "Market-wide risk-off", (-1.3,0.4,1.5), 'High', 'Bounce watch'),
 ('U11.SI', "Fell 1.9%; RSI 16.", "Next session", "Trend down", (-1.5,0.3,1.6), 'Medium', 'Bounce watch'),
 ('O39.SI', "Fell 2.2%.", "Next session", "Small range", (-1.3,0.3,1.4), 'Medium', 'Bounce watch'),
 ('G07.SI', "Fell 2.5%.", "Next session", "Thin trading", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('AIY.SI', "Fell 1.3%.", "Next session", "Small range", (-1.8,0.2,1.8), 'Medium', 'Range'),
]

# IPO tab (6-month view), all markets
P[('ipo','all','US')] = [
 ('SPCX', "SpaceX listed in June at $135 and trades about 4% above that, 33% under its high; rose 2.6% on a weak day.",
  "Starship progress; lock-up expiries", "Valuation and Musk headlines", (-35,12,45), 'Medium', 'Mega-cap IPO'),
 ('CHYM', "Chime (IPO $27) trades about 24% above its IPO price, near its high.",
  "Member growth", "Overbought (RSI 77); fintech credit cycle", (-18,8,25), 'Medium', 'Post-IPO uptrend'),
 ('KLAR', "Klarna (IPO $40) is 65% below its IPO price at about 18x forward earnings. Q3 revenue +12% and back to profit; rose 3%.",
  "Holiday volumes; Q4 results", "Buy-now-pay-later credit losses", (-25,14,40), 'Speculative', 'Deep value'),
 ('IAM', "Iambic (IPO $16, AI drug discovery) jumped 18% to $14 but is still below its IPO price; 95% analyst upside.",
  "Pipeline data; partnerships", "Cash burn; 10% daily swings", (-40,12,55), 'Speculative', 'Post-IPO rebound'),
 ('ACCV', "Accelevation (IPO $18) makes electrical gear for data centres: revenue +66% at about 10x forward earnings. Fell 7.5% again; 42% below its IPO price.",
  "Order updates", "Data-centre slowdown; 9% daily swings", (-40,10,50), 'Speculative', 'Post-IPO value'),
]

# ---------- Power & grid (data-center power) ----------
P[('long','pwr','US')] = [
 ('GEV', "GE Vernova: gas turbines and grid gear sold out for years, revenue +27%. 35% off its high with 54% analyst upside; flat on a weak day.", "Q4 results Jan 27", "Data-centre policy; valuation (30x)", (-25,15,40), 'High', 'Quality at a discount'),
 ('CEG', "Constellation beat Q3 and raised 2026 guidance; 28% off its high, up 1% in five days.", "New long-term power deals", "Data-centre politics; PJM rules", (-22,13,32), 'High', 'Beat and raise'),
 ('ETN', "Eaton: electrical gear for data centres and utilities, 27% off its high at about 20x earnings.", "Q4 results Feb 2", "Data-centre orders slowing", (-20,13,33), 'Medium', 'Quality at a discount'),
 ('VRT', "Vertiv: data-centre cooling and power, revenue +61% at about 19x forward earnings, 50% off its high. Nvidia's $130B guide supports its orders.", "Order backlog updates", "Most exposed to a data-centre slowdown", (-35,18,52), 'Medium', 'Oversold growth'),
 ('PWR', "Quanta builds the grid: revenue +57%, 25% off its high; rose on a down day.", "Utility capex plans", "Data-centre policy", (-25,12,34), 'Medium', 'Grid builder'),
]
P[('long','pwr','SGX')] = [
 ('BN4.SI', "Keppel: power, data centres and asset management, about 15x earnings with 37% analyst upside. Fell 3.1% on Nov 17.", "Asset sales", "Execution", (-13,12,25), 'Medium', 'Value'),
 ('U96.SI', "Sembcorp: power and renewables at about 9x earnings.", "New contracts", "Power prices", (-12,7,18), 'Medium', 'Value'),
 ('DCRU.SI', "Digital Core REIT: US data-centre REIT, about 9x earnings with 55% analyst upside.", "Leasing news", "Tenant concentration; US rates above 5%", (-14,11,27), 'Medium', 'Deep value'),
 ('AJBU.SI', "Keppel DC REIT: data-centre rents, 9% off its high.", "Dividend", "Rates", (-10,7,17), 'Medium', 'Income'),
 ('544.SI', "CSE Global: electrification and data-centre work, about 9x earnings, 58% off its high after another 7% drop.", "New orders", "Falling knife; small and volatile", (-30,14,45), 'Speculative', 'Recovery'),
]
P[('swing','pwr','US')] = [
 ('NEE', "NextEra eased only 0.4% on a weak day (RSI 66); regulated utility earnings.", "Renewables deals", "10-yr yield above 5%", (-6,3,8), 'Medium', 'Defensive'),
 ('GEV', "GE Vernova RSI 36, down 16% in a month; held flat on Nov 17.", "Order news; Nvidia read-across", "AI capex fears", (-14,6,20), 'Medium', 'Oversold rebound'),
 ('VRT', "Vertiv RSI 33, 50% off its high; most direct play on Nvidia's guide among power names.", "Order news", "AI hardware selling", (-16,7,22), 'Speculative', 'Oversold rebound'),
 ('TLN', "Talen's new 750 MW capacity deal; about 11x forward earnings, flat over the month.", "Analyst target updates", "Data-centre politics", (-13,5,16), 'Medium', 'New-contract momentum'),
 ('VST', "Vistra RSI 40 after a 15% monthly drop; 57% analyst upside.", "Analyst updates", "Texas data-centre proposal", (-14,6,20), 'Medium', 'Oversold rebound'),
]
P[('swing','pwr','SGX')] = [
 ('AJBU.SI', "Keppel DC REIT eased 0.9% (RSI 64).", "Momentum", "Rates", (-5,1.5,6), 'Medium', 'Trend'),
 ('BN4.SI', "Keppel fell 3.1% to RSI 31.", "Asset-sale news", "Execution", (-6,3,9), 'Medium', 'Oversold rebound'),
 ('U96.SI', "Sembcorp RSI 34.", "Contracts", "Power prices", (-5,2,7), 'Medium', 'Oversold'),
 ('DCRU.SI', "Digital Core REIT fell 2.2% (RSI 50).", "Support", "US data-centre worries", (-7,2,8), 'Medium', 'Range'),
 ('544.SI', "CSE Global fell 7.4% to a new low.", "New orders", "No floor yet", (-15,3,16), 'Speculative', 'Falling knife'),
]
P[('intraday','pwr','US')] = [
 ('VRT', "Fell 0.8%; Nvidia beat overnight.", "Sympathy move", "AI hardware selling", (-5,0.8,6), 'Speculative', 'Sympathy bounce'),
 ('BE', "Fell 4.4%.", "Bounce", "8% daily swings", (-7,0.3,7), 'Speculative', 'Range'),
 ('CEG', "Fell 2.5%.", "Dip buying", "Data-centre politics", (-3,0.3,3), 'Medium', 'Dip watch'),
 ('OKLO', "Fell 3%; down 11% in five days.", "Bounce", "Cash burn", (-7,0,7), 'Speculative', 'Bounce watch'),
 ('NEE', "Small dip on a weak day.", "Defensive bid", "Small range", (-1.8,0.2,1.8), 'Medium', 'Range'),
]
P[('intraday','pwr','SGX')] = [
 ('BN4.SI', "Fell 3.1%.", "Next session", "More selling", (-1.8,0.4,2), 'Medium', 'Bounce watch'),
 ('544.SI', "Fell 7.4% to a new low.", "Next session", "Small cap", (-4,0.2,4), 'Speculative', 'Range'),
 ('U96.SI', "Fell 0.9%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('AJBU.SI', "Fell 0.9%.", "Next session", "Small range", (-1.2,0.2,1.2), 'Medium', 'Range'),
 ('DCRU.SI', "Fell 2.2%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
]

# ---------- Defence & industrials ----------
P[('long','def','US')] = [
 ('GE', "GE Aerospace: jet-engine services boom, revenue +16%, 15% off its high.", "Q4 results Jan 21", "Valuation (35x)", (-15,10,26), 'High', 'Quality'),
 ('RTX', "RTX: missiles and engines, revenue +11%, steady; rose 1.2% on a weak day, 16% analyst upside.", "Q4 results Jan 26", "Engine issues", (-12,10,24), 'High', 'Core defence'),
 ('LHX', "L3Harris: space and missile sensors, 31% off its high, 28% analyst upside.", "Golden Dome contracts", "Budget fights with a split government", (-15,12,30), 'Medium', 'Value'),
 ('HWM', "Howmet: jet-engine parts, revenue +29%, 27% off its high with 39% analyst upside.", "Aerospace build rates", "Valuation (32x)", (-20,14,34), 'Medium', 'Growth at a discount'),
 ('NOC', "Northrop: B-21 and missile defence, about 19x earnings, 28% off its high; rose 1.8% on Nov 17.", "Golden Dome contracts", "Budget fights", (-15,10,27), 'Medium', 'Value'),
]
P[('long','def','SGX')] = [
 ('S63.SI', "ST Engineering: record S$37.7B order book and nine-month revenue +10%. Fell another 2.3% to S$8.82 (RSI 23); one broker cut to Hold (S$10 target) while others keep Buy.", "Contract wins; FY results (Feb)", "Selling pressure; valuation (23x)", (-12,12,26), 'High', 'Quality on a dip'),
 ('BS6.SI', "Yangzijiang Shipbuilding: about 7x earnings, revenue +36%; orders of US$6.98B are well above its US$4.5B target.", "New ship orders", "US port fees on Chinese ships", (-18,14,32), 'Medium', 'Value'),
 ('S59.SI', "SIA Engineering: aircraft maintenance, 24% off its high, 30% analyst upside.", "Air travel", "Revenue falling (-11%)", (-10,10,24), 'Medium', 'Recovery'),
 ('C52.SI', "ComfortDelGro: steady transport earnings at about 13x; flat on a weak day.", "Overseas contracts", "Slow growth", (-8,7,15), 'Medium', 'Steady'),
 ('H22.SI', "Hong Leong Asia: engines and building materials at about 8x earnings, 48% off its high.", "Results (Feb)", "China demand", (-25,20,50), 'Speculative', 'Deep value'),
]
P[('swing','def','US')] = [
 ('CAT', "Caterpillar is 47% off its high (RSI 25).", "Rebound", "Data-centre generator orders slowing", (-12,6,18), 'Medium', 'Oversold rebound'),
 ('NOC', "Northrop rose 1.8% on a weak day (RSI 52).", "Golden Dome contracts", "Budget fights", (-7,3,9), 'Medium', 'Relative strength'),
 ('AXON', "RSI 21 after a Q3 miss; 80% analyst upside.", "Analyst updates", "More downgrades", (-18,6,22), 'Speculative', 'Post-earnings dip'),
 ('GD', "General Dynamics: 10% off its high, steady (RSI 52).", "Contracts", "Budget fights", (-7,3,9), 'Medium', 'Steady'),
 ('BA', "Boeing 35% off its high (RSI 46); production recovering.", "Monthly deliveries", "Quality issues", (-10,5,15), 'Medium', 'Recovery'),
]
P[('swing','def','SGX')] = [
 ('S63.SI', "ST Engineering RSI 23 after a 7% five-day drop.", "Bounce; contract wins", "Large holder selling; downgrade", (-6,4,10), 'Medium', 'Oversold rebound'),
 ('BS6.SI', "Yangzijiang gave back 2.5%.", "Orders", "Trade fees", (-8,4,12), 'Medium', 'Pullback'),
 ('H22.SI', "Hong Leong Asia RSI 32.", "Bounce", "China demand", (-10,4,12), 'Speculative', 'Oversold rebound'),
 ('S59.SI', "SIA Engineering RSI 39.", "Air travel", "Slow growth", (-6,2,7), 'Medium', 'Range'),
 ('C52.SI', "ComfortDelGro steady (RSI 44).", "Support", "Slow growth", (-4,1.5,5), 'Medium', 'Range'),
]
P[('intraday','def','US')] = [
 ('NOC', "Rose 1.8% on a weak day.", "Defence bid", "Gives back gains", (-2,0.2,2), 'Medium', 'Relative strength'),
 ('AVAV', "Fell 3.4%; results Dec 2.", "Bounce", "Volatile", (-5,0,5), 'Speculative', 'Bounce watch'),
 ('KTOS', "Down 15% in five days.", "Drone contracts", "Volatile", (-4.5,0,4.5), 'Speculative', 'Bounce watch'),
 ('AXON', "Fell 1.8% (RSI 21).", "Bounce", "More selling", (-4,0.3,4), 'Speculative', 'Bounce watch'),
 ('RTX', "Rose 1.2%.", "Defence bid", "Small range", (-1.8,0.2,1.8), 'Medium', 'Range'),
]
P[('intraday','def','SGX')] = [
 ('S63.SI', "Fell 2.3% (RSI 23).", "Next session", "More selling", (-2.5,0.5,3), 'Medium', 'Bounce watch'),
 ('BS6.SI', "Fell 2.5%.", "Next session", "Thin bids", (-2.5,0.3,2.5), 'Medium', 'Range'),
 ('H22.SI', "Rose 0.5%.", "Next session", "Thin trading", (-3,0.2,3), 'Speculative', 'Range'),
 ('S59.SI', "Eased 0.4%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('C52.SI', "Flat.", "Next session", "Small range", (-1.2,0.2,1.2), 'Medium', 'Range'),
]

# ---------- Energy (oil and gas) ----------
P[('long','nrg','US')] = [
 ('CVX', "Chevron: revenue +35%, about 13x earnings, 8% off its high.", "Hess integration; buybacks", "Oil falls further as Hormuz shipping recovers", (-16,8,24), 'High', 'Core energy'),
 ('XOM', "Exxon: steady cash flow, about 13x earnings, 10% analyst upside; rose on a weak day.", "Buybacks", "Oil price drop", (-15,7,21), 'High', 'Core energy'),
 ('LNG', "Cheniere: US gas exports on long contracts; less tied to oil. Up 3.5% in five days.", "New export capacity", "Gas price swings", (-15,8,24), 'Medium', 'Steady'),
 ('FANG', "Diamondback: low-cost Permian producer at about 8x earnings, 33% analyst upside.", "Buybacks", "Oil price drop", (-22,12,32), 'Medium', 'Value'),
 ('EOG', "EOG: about 9x earnings, revenue +43%, 6% off its high; up 2.6% in five days.", "Buybacks", "Oil price drop", (-16,7,22), 'Medium', 'Value'),
]
P[('long','nrg','SGX')] = [
 ('5E2.SI', "Seatrium builds offshore rigs and wind platforms; 46% analyst upside.", "New orders", "Contract delays", (-15,12,28), 'Medium', 'Recovery'),
 ('BN4.SI', "Keppel: energy infrastructure and asset management.", "Asset sales", "Execution", (-13,10,22), 'Medium', 'Value'),
 ('5LY.SI', "Marco Polo Marine: offshore vessels, revenue +40% at about 10x earnings.", "Results (Nov)", "Thin trading", (-25,10,35), 'Speculative', 'Growth value'),
 ('RE4.SI', "Geo Energy fell 23% to S$0.38 on Nov 16. On Nov 17 it said it received no new Indonesian mining directive and operations are normal. About 5x earnings; wait for trading to settle.", "Trading resumes normally; Q3 update", "Indonesian policy risk; could fall further", (-35,8,40), 'Speculative', 'Wait'),
 ('5WH.SI', "Rex International is in a long downtrend (-64% this year); no setup.", "None", "Further losses", (-30,-5,20), 'Speculative', 'Avoid'),
]
P[('swing','nrg','US')] = [
 ('LNG', "Cheniere is up 3.5% in five days (RSI 53).", "Export capacity", "Gas price swings", (-8,3,10), 'Medium', 'Relative strength'),
 ('FANG', "Diamondback oversold (RSI 25); about 8x earnings; rose on a weak day.", "Buybacks", "Oil price drop", (-11,4,13), 'Medium', 'Oversold rebound'),
 ('SLB', "SLB oversold (RSI 27), 18% off its high; 26% analyst upside.", "Offshore orders", "Oil price drop", (-10,4,12), 'Medium', 'Oversold rebound'),
 ('DVN', "Devon RSI 30; about 9x earnings, 36% analyst upside.", "Buybacks", "Oil price drop", (-12,4,14), 'Medium', 'Oversold rebound'),
 ('XOM', "Exxon RSI 32; rose on a weak day.", "Buybacks", "Gulf calm returns", (-7,2,8), 'Medium', 'Support'),
]
P[('intraday','nrg','US')] = [
 ('FANG', "Rose 0.6% as Brent firmed to ~$93.", "Oil", "Oil reverses", (-2.8,0.2,2.8), 'Medium', 'Range'),
 ('MPC', "Fell 2%.", "Margins", "Oil swings", (-3,0.2,3), 'Medium', 'Bounce watch'),
 ('PSX', "Fell 1.9%.", "Margins", "Oil swings", (-2.8,0.2,2.8), 'Medium', 'Bounce watch'),
 ('XOM', "Rose 0.4%.", "Oil", "Hormuz shipping normalises", (-2,0.2,2), 'Medium', 'Range'),
 ('SLB', "Fell 1.4% (RSI 27).", "Bounce", "Oil reverses", (-2.5,0.2,2.5), 'Medium', 'Bounce watch'),
]
P[('swing','nrg','SGX')] = [
 ('5E2.SI', "Seatrium fell 2.3% (RSI 40).", "Orders", "Delays", (-8,3,10), 'Medium', 'Support'),
 ('BN4.SI', "Keppel fell 3.1% to RSI 31.", "Asset sales", "Execution", (-6,3,9), 'Medium', 'Oversold rebound'),
 ('RE4.SI', "Geo Energy: company says operations are normal after the 23% drop.", "Bounce once trading settles", "Policy risk", (-25,4,25), 'Speculative', 'Wait'),
 ('5LY.SI', "Marco Polo Marine RSI 45.", "Results", "Thin trading", (-10,3,12), 'Speculative', 'Range'),
 ('5WH.SI', "Rex International: no setup.", "None", "Further losses", (-12,-2,8), 'Speculative', 'Avoid'),
]
P[('intraday','nrg','SGX')] = [
 ('RE4.SI', "No trade in the snapshot on Nov 17; company says operations are normal.", "Next session", "More selling", (-10,1,12), 'Speculative', 'Wait'),
 ('5E2.SI', "Fell 2.3%.", "Next session", "Small range", (-2,0.2,2), 'Medium', 'Range'),
 ('BN4.SI', "Fell 3.1%.", "Next session", "Small range", (-1.8,0.4,2), 'Medium', 'Bounce watch'),
 ('5LY.SI', "Fell 3.7%.", "Next session", "Thin trading", (-4,0,4), 'Speculative', 'Range'),
 ('5WH.SI', "Penny stock in a downtrend; avoid.", "None", "Further losses", (-5,-1,4), 'Speculative', 'Avoid'),
]

IPO_LIST = [
 # sym, name, ipo_date, ipo_price, sector, status
 ('ANT','Anthropic (Nasdaq: ANT; range $70-78 kept, 825M shares, up to ~$64B; prices Nov 18, trading Nov 19; books ~6x covered per Bloomberg; may price at or above the top)','2026-11-19',None,'ai','Roadshow'),
 ('TRCX','Tracx Logis ($18-22 range; 1M shares)','2026-11-23',None,'ai','Expected'),
 ('FBLLU','Football Manager SPAC','2026-11-23',10.00,'fin','Expected'),
 ('BIAI','Bitari','2026-11-30',7.00,'ai','Expected'),
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
 ('2026-11-15T19:19','NVDA', "On X: shares the FT report that Huang is discussing a comeback and calls it his 'redemption arc'. No newer posts found for Nov 16-17."),
 ('2026-11-15T19:03','AXTI', "Via tracker: says his AXT thesis is narrow, using indium phosphide substrate capacity as an example of an AI bottleneck."),
 ('2026-11-15T18:47','NVDA', "Via tracker: expects buying of bottleneck parts to speed up through 2027, naming laminates, ABF substrates, PCBs and optical parts."),
 ('2026-11-15T06:27','NVDA', "On X: says Western media coverage of Nvidia and Huang has gone too far."),
 ('2026-11-14T08:16','NVDA', "Via tracker: shares a letter from Altimeter and Atreides to Nvidia's board."),
 ('2026-11-14T05:07','NVDA', "Via tracker: says Musk's involvement raised the odds of Huang returning as CEO; separately posted an FT report that Huang is discussing a comeback."),
 ('2026-11-14T04:25','LITE MU', "Via tracker: argues demand stays supply-limited for optics and memory even if AI capex slows."),
 ('2026-11-14T01:07','TSM', "Via tracker: calls rumours of TSMC capacity cuts hypothetical; says they have not happened."),
 ('2026-11-13T23:36','NVDA COHR AMD', "Via tracker: says a CFO-led Nvidia is a negative for companies built around the Nvidia ecosystem."),
 ('2026-11-13T21:21','AXTI COHR LITE', "Via tracker: still bullish on AXT, citing backlog growth and visibility on customers."),
]

EVENTS = [
 ('2026-11-16','Macro','S&P -1.9%, Nasdaq -2.5%; VIX 23', "S&P ~7,417; Dow -1.4%; Russell -1.7%. Empire State index 7.8 (vs 16.7 expected). Bitcoin ~$64K, lowest since July. Banks -2% on app-outage reports."),
 ('2026-11-16','AI','New US rule on remote chip access; NVDA -4%', "Commerce rule targets Chinese firms renting advanced chips abroad. NVDA ~$156, -13% in five days. Micron -7% (DRAM lawsuit), Intel -7% (class action)."),
 ('2026-11-16','SGX','STI -0.9% to 5,184.66', "ST Engineering -6.6% with no news; AEM -6%; Yangzijiang +2.6%. Geo Energy -23%."),
 ('2026-11-17','Macro','S&P -1.0%, Dow -1.6%, Nasdaq -0.7%', "Fourth straight drop; ~9 in 10 S&P stocks fell; VIX ~26. October retail sales +0.2% (control group beat). 10-yr ~5.10%. Dec hike ~95% priced."),
 ('2026-11-17','AI','Nvidia beats and raises; shares up after hours', "Q3 revenue $115.8B (+103%) vs ~$109B expected; Q4 guide $130B +/-3%; $150B added to buyback. Huang says he'd be 'honored' to return; chair says the board doesn't intend to reinstate him. Optics names gave up gains on reported US curbs on Chinese data-centre gear."),
 ('2026-11-17','Finance','Klarna Q3: revenue +12%, back to profit', "KLAR +3%. JPMorgan names a new CFO for 2027; banks -2 to -3%."),
 ('2026-11-17','SGX','STI -1.4% to ~5,110', "Selling on US chip-curb worries. AEM -5%, Frencken -5%, CSE Global -7.4%, Keppel -3.1%, DBS -2.2%. Geo Energy says no new Indonesian mining directive; operations normal."),
 ('2026-11-18','Macro','FOMC minutes (Oct meeting)', "2pm ET. Markets price a December hike."),
 ('2026-11-18','IPO','Anthropic prices IPO', "Range $70-78 kept; 825M shares; may price at or above the top."),
 ('2026-11-19','IPO','Anthropic starts trading (Nasdaq: ANT)', "Book ~6x oversubscribed per Bloomberg; Altimeter to invest $5B."),
 ('2026-11-23','IPO','Tracx Logis and Football Manager SPAC expected', ""),
 ('2026-11-25','SGX','IHH Q3 results', ""),
 ('2026-11-26','Macro','US Thanksgiving', "US stock market closed."),
 ('2026-12-01','AI','Marvell and Credo results', ""),
 ('2026-12-02','Defence','AeroVironment results', ""),
 ('2026-12-09','Macro','Fed rate decision (Dec 8-9)', "A hike is ~95% priced. Broadcom reports the same day."),
 ('2026-12-10','AI','Ciena results; TSMC November sales', ""),
 ('2026-12-23','AI','Micron FQ1 results', ""),
]
