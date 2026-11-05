# Analyst picks for 2026-11-06 (snapshot: US close Nov 5, SGX close Nov 5). Fields: sym, thesis, catalyst, risk, (low, base, high) % expected move, conviction, setup
# Horizons: long = 12 months, swing = ~4 weeks, intraday = rest of session (US) / next session (SGX), ipo = 6 months.
# Context: Nov 5 "AI meltdown": S&P -4.4%, Nasdaq -5.5% (correction), Dow -1,833, chip index (SOX) -12.3%, VIX ~28.
# Drivers: fear that the Democratic Congress slows data-centre building (UBS: ~30% of 2028 additions at risk), hedge funds locking in gains.
# SGX traded before the US crash; SGX chip names will open Nov 6 after it. US October jobs report is out Nov 6.
P = {}

# ---------- AI & chips ----------
P[('long','ai','US')] = [
 ('NVDA', "Revenue still about doubles (+106%) and the stock is now about 12x forward earnings, down 24% from its high and negative for 2026.",
  "Q3 results Nov 17", "Data-centre policy under the new Congress; more hedge-fund selling", (-22,22,48), 'High', 'Quality at a discount'),
 ('TSM', "Makes almost every leading AI chip. Revenue +51% at about 15x forward earnings, 27% below its high.",
  "October sales (~Nov 10); Q4 results Jan 14", "Taiwan geopolitics; AI capex cuts", (-18,20,42), 'High', 'Core holding'),
 ('AVGO', "Custom AI chips plus networking: revenue +86% at about 15x forward earnings, 39% below its high.",
  "Q4 results Dec 9", "Lumpy custom-chip orders; customer concentration", (-22,20,45), 'Medium', 'Pullback in a leader'),
 ('COHR', "Record quarter (revenue +50%, EPS $2.09 vs $1.80) and a new ~$20B five-year optics deal with a major AI company, yet the stock fell 12%. About 12x forward earnings.",
  "Q2 guide $2.55-2.75B; first $3B quarter targeted by FY27 end", "Capex keeps rising; 6% daily swings", (-32,25,65), 'Medium', 'Beat-and-sold'),
 ('MU', "Memory is still the tightest part of AI servers: revenue +379% at about 3x forward earnings. Down 45% from its high after a 16% one-day drop.",
  "FQ1 results Dec 23", "Peak-cycle earnings; memory falls hard when prices turn", (-38,22,65), 'Medium', 'Cycle leader'),
]
P[('long','ai','SGX')] = [
 ('AWX.SI', "AEM fell 20% on Nov 5 and is 43% below its high. Still up 270% this year; analysts rate it Strong Buy.",
  "Q3 business update (Nov)", "One large customer; very volatile; US chip crash hits the next open", (-38,18,55), 'Medium', 'SGX AI leader'),
 ('558.SI', "UMS makes precision parts for chip-equipment makers. Down 40% from its high after a 16% drop on Nov 5.",
  "Q3 results mid-November", "Tied to Applied Materials spending", (-30,15,45), 'Medium', 'Equipment supplier'),
 ('5DD.SI', "Micro-Mechanics makes precision tools for chip assembly and test: revenue +45%, 39% off its high.",
  "Q1 FY27 results (Nov)", "Small and thinly traded", (-22,14,35), 'Medium', 'Growth at a discount'),
 ('E28.SI', "Frencken builds modules for chip and medical equipment. 48% off its high after a 10% drop, about 15x earnings.",
  "Q3 business update (Nov)", "Flat revenue so far this year", (-25,14,38), 'Medium', 'Recovery'),
 ('V03.SI', "Venture builds electronics for chip-equipment, medical and AI-server makers. Net cash, about 16x earnings, low volatility.",
  "Q3 business update (Nov)", "Slow growth (+7%)", (-12,10,22), 'Medium', 'Steady value'),
]
P[('swing','ai','US')] = [
 ('COHR', "Fell 12% on the day after a strong beat and raised long-term targets; the selloff was about the sector, not the results.",
  "Analyst target updates after the call", "Sector still being de-risked", (-20,8,25), 'Medium', 'Beat-and-sold'),
 ('LITE', "Marvell is buying Lumentum for 4.5 Marvell shares each. At the close that is worth about 18% more than LITE's price.",
  "Spread narrows if MRVL recovers", "Regulatory delay (incl. China); MRVL keeps falling", (-15,8,22), 'Medium', 'Merger spread'),
 ('NVDA', "RSI 28 after a 9% drop; the cheapest it has looked on earnings in years, two weeks before results.",
  "Q3 results Nov 17", "Results day gap either way", (-14,6,18), 'Medium', 'Oversold into earnings'),
 ('AAOI', "Q3 revenue +127% to $270M and a Q4 guide of $385-420M plus a multi-year hyperscaler deal, after a 19% drop on the day.",
  "After-hours reaction and analyst updates", "Power and construction delays on US capacity; 7% daily swings", (-30,10,40), 'Speculative', 'Earnings rebound'),
 ('MU', "Down 28% in a week (RSI 32) at about 3x forward earnings.",
  "Memory contract prices", "Very volatile; 5% daily swings", (-22,8,25), 'Medium', 'Oversold value'),
]
P[('swing','ai','SGX')] = [
 ('V03.SI', "Venture is the least volatile SGX tech name and is oversold (RSI 34).",
  "Q3 business update (Nov)", "Flat revenue", (-8,4,10), 'Medium', 'Range trade'),
 ('5DD.SI', "Micro-Mechanics fell 4% on Nov 5, less than peers; RSI 33.",
  "Q1 FY27 results (Nov)", "Thin order book", (-12,4,13), 'Medium', 'Oversold rebound'),
 ('AWX.SI', "AEM is down 43% in a month (RSI 29). A bounce is likely once US chips stabilise, but not before.",
  "US chips stabilising; Q3 update", "Opens Nov 6 after a 12% fall in US chips", (-25,5,28), 'Speculative', 'Oversold rebound'),
 ('558.SI', "UMS is down 38% in a month (RSI 27); analysts still see large upside.",
  "Q3 results mid-November", "Chip-equipment sentiment", (-20,5,22), 'Speculative', 'Oversold rebound'),
 ('E28.SI', "Frencken is down 30% in a month (RSI 27).",
  "Q3 business update (Nov)", "No clear catalyst before results", (-16,4,18), 'Speculative', 'Oversold rebound'),
]
P[('intraday','ai','US')] = [
 ('AAOI', "Reported after the close: revenue +127% and a Q4 guide well above Q3. Watch whether the stock holds an opening gap.",
  "Holding above the opening range", "Gap fades in a weak tape", (-9,1.5,10), 'Speculative', 'Earnings gap'),
 ('IREN', "AI cloud revenue nearly tripled to about $200M, but the stock fell 14% on Microsoft data-centre delay chatter.",
  "Reaction to results", "Texas data-centre headlines", (-9,0,9), 'Speculative', 'Earnings reaction'),
 ('COHR', "Strong results ignored on Nov 5; first candidate for a relief bounce if chips steady.",
  "Reclaiming $180", "Second day of de-grossing", (-5,1,6), 'Medium', 'Bounce watch'),
 ('NVDA', "Closed below its 2025 year-end price on 2.4x normal volume; RSI 28.",
  "Jobs report at 8:30 ET; holding $180", "Further forced selling", (-4,0.5,4), 'Medium', 'Bounce watch'),
 ('TSM', "Fell 10% with the group; October sales are due around Nov 10.",
  "Holding $350", "Taiwan opens lower first", (-3.5,0.5,3.5), 'Medium', 'Support test'),
]
P[('intraday','ai','SGX')] = [
 ('AWX.SI', "Fell 20% on Nov 5, before the US chip index fell another 12%.",
  "Next session: watch the first hour for a low", "Gap down at the open", (-8,-2,5), 'Speculative', 'Gap-down risk'),
 ('558.SI', "Fell 16% on Nov 5; likely to open lower again.", "Next session open", "Trend still down", (-7,-1.5,4), 'Speculative', 'Gap-down risk'),
 ('E28.SI', "Fell 10% on Nov 5.", "Next session open", "Follows US chip equipment", (-5,-1,3), 'Medium', 'Gap-down risk'),
 ('5DD.SI', "Fell 4%; smaller drawdown than peers.", "Holding S$2.30", "Thin order book", (-4,-1,2.5), 'Medium', 'Support test'),
 ('V03.SI', "Low-volatility name; fell 2%.", "Next session", "Little momentum", (-3,-0.5,2), 'Medium', 'Range'),
]

# ---------- Health ----------
P[('long','hc','US')] = [
 ('LLY', "Obesity-drug leader: revenue +39%, 3% below its high. Health held up best on Nov 5.",
  "Orforglipron launch; Q4 results (Feb)", "Drug-price policy under the new Congress", (-15,10,28), 'High', 'Defensive growth'),
 ('ARGX', "argenx: revenue +52% from its immune-disease drug Vyvgart, 15% off its high, 28% analyst upside.",
  "New indications in 2027", "Competition in myasthenia gravis", (-15,13,32), 'Medium', 'Growth leader'),
 ('MDGL', "Madrigal's liver drug Rezdiffra is growing fast (revenue +50%); stock is oversold (RSI 28) and 34% off its high.",
  "Script data; EU rollout", "Competition from GLP-1 drugs", (-22,20,45), 'Medium', 'Oversold growth'),
 ('INSM', "Insmed's lung drug launch drives revenue +268%; 49% off its high with Strong Buy ratings.",
  "Brensocatib launch numbers", "Expensive on near-term earnings", (-30,18,48), 'Medium', 'Launch story'),
 ('REGN', "Regeneron is up 22% in a month on pipeline news, at about 13x forward earnings.",
  "Pipeline readouts", "Eylea competition", (-18,8,26), 'Medium', 'Value with momentum'),
]
P[('long','hc','SGX')] = [
 ('Q0F.SI', "IHH runs hospitals across Asia; analysts see 37% upside.", "Q3 results Nov 25", "Currency swings", (-12,12,25), 'Medium', 'Regional leader'),
 ('C2PU.SI', "Parkway Life REIT: steady hospital and nursing-home rents, near its high.", "Dividend", "Higher rates", (-8,8,15), 'High', 'Income'),
 ('AP4.SI', "Riverstone makes cleanroom and medical gloves at about 14x earnings with 40% analyst upside.", "Q3 results (Nov)", "Glove price competition", (-15,12,30), 'Medium', 'Value'),
 ('BSL.SI', "Raffles Medical: Singapore hospital group, 21% off its high and rising this month.", "Results (Feb)", "Shrinking revenue (-7%)", (-10,8,18), 'Medium', 'Recovery'),
 ('H02.SI', "Haw Par (Tiger Balm) trades near 10x earnings with a large cash and investment pile.", "Results (Feb)", "Revenue down 8%", (-12,6,16), 'Medium', 'Value'),
]
P[('swing','hc','US')] = [
 ('LLY', "Defensive leader while tech de-risks; RSI 67, near its high.", "Money rotating out of chips", "Drug-price headlines", (-8,4,12), 'High', 'Relative strength'),
 ('JNJ', "Near its high with low volatility; a hiding place in a selloff.", "Rotation into defensives", "Talc litigation news", (-6,3,9), 'Medium', 'Relative strength'),
 ('GILD', "Up 14% in a month; HIV franchise plus lenacapavir launch.", "Rotation into defensives", "Overbought after the run", (-7,3,10), 'Medium', 'Trend'),
 ('CYTK', "Fell 14% after Q3 despite RBC calling a revenue inflection for its heart drug Myqorzo from 2027.", "Launch metrics", "Slow early sales", (-15,8,25), 'Speculative', 'Post-earnings dip'),
 ('ALNY', "Deeply oversold (RSI 15) and 67% off its high; analysts see 91% upside.", "Amvuttra script data", "Trend still down", (-15,8,24), 'Speculative', 'Oversold rebound'),
]
P[('swing','hc','SGX')] = [
 ('C2PU.SI', "Parkway Life REIT: lowest-volatility name in the group.", "Dividend", "Rates", (-4,2,6), 'High', 'Range'),
 ('BSL.SI', "Raffles Medical is in a mild uptrend (RSI 66).", "Momentum", "Low volume", (-5,2.5,8), 'Medium', 'Trend'),
 ('Q0F.SI', "IHH has drifted lower into Q3 results.", "Q3 results Nov 25", "Results miss", (-6,3,9), 'Medium', 'Pre-earnings'),
 ('AP4.SI', "Riverstone is near support with large analyst upside.", "Q3 results (Nov)", "Glove prices", (-8,3,10), 'Medium', 'Support'),
 ('H02.SI', "Haw Par is cheap and stable.", "None near term", "Slow drift", (-6,2,8), 'Medium', 'Value'),
]
P[('intraday','hc','US')] = [
 ('MRNA', "Reports Nov 6. Up 720% this year and trades far above analyst targets: expect a big move either way.",
  "Results", "Analysts see 43% downside to targets", (-10,0,10), 'Speculative', 'Earnings reaction'),
 ('CYTK', "Fell 14% on 3.3x volume after results; a reflex bounce is possible.", "Holding $54", "More selling", (-5,1,6), 'Speculative', 'Bounce watch'),
 ('LLY', "Fell only 3% on a crash day.", "Defensive bid", "Market-wide selling", (-2.5,0.4,2.5), 'Medium', 'Relative strength'),
 ('VRTX', "Near its high; low beta.", "Defensive bid", "Market-wide selling", (-2,0.3,2.5), 'Medium', 'Relative strength'),
 ('HIMS', "Fell 10%; reports Nov 9.", "Pre-earnings positioning", "High volatility", (-6,0.5,6), 'Speculative', 'Pre-earnings'),
]
P[('intraday','hc','SGX')] = [
 ('C2PU.SI', "Steady REIT.", "Next session", "Small range", (-1,0.2,1), 'Medium', 'Range'),
 ('BSL.SI', "Rose 1.8% on Nov 5.", "Next session", "Small range", (-1.5,0.3,1.5), 'Medium', 'Range'),
 ('H02.SI', "Rose 0.8% on Nov 5.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('Q0F.SI', "Flat.", "Next session", "Malaysia market swings", (-2,0.2,2), 'Medium', 'Range'),
 ('AP4.SI', "Slightly lower.", "Next session", "Thin trading", (-2,0.2,2), 'Medium', 'Range'),
]

# ---------- Finance ----------
P[('long','fin','US')] = [
 ('JPM', "Best-run US bank, 7% off its high at about 13x forward earnings.", "Q4 results Jan 14", "Credit cycle; market-wide selloff", (-15,8,22), 'High', 'Core holding'),
 ('V', "Visa: steady growth (+13%), near its high; little AI exposure.", "Holiday spending", "Regulation of card fees", (-12,6,18), 'High', 'Defensive growth'),
 ('GS', "Trading and deal-making boom, about 12x forward earnings, 25% off its high.", "Deal pipeline incl. big IPOs", "Market volatility hits deals", (-20,10,28), 'Medium', 'Cyclical value'),
 ('SE', "Sea (Shopee, Garena, Monee): revenue +48% at about 15x forward earnings, 52% off its high, RSI 24.", "Q3 results Nov 10", "Competition from TikTok Shop", (-30,28,65), 'Medium', 'Oversold growth'),
 ('NU', "Nubank: revenue +52% at about 10x forward earnings, 38% off its high.", "Q3 results Nov 12", "Brazil credit and currency", (-30,22,55), 'Medium', 'Growth at a discount'),
]
P[('long','fin','SGX')] = [
 ('D05.SI', "DBS missed Q3 (profit -5% on weaker trading) but kept its 81-cent dividend and says interest income has bottomed. The stock rose.",
  "Q4 results (Feb)", "Margins if rates fall; stronger SGD", (-10,7,15), 'High', 'Income leader'),
 ('O39.SI', "OCBC: about 14x earnings, 13% off its high.", "Q3 results Nov 6", "Margin squeeze like UOB's", (-10,7,15), 'Medium', 'Income'),
 ('U11.SI', "UOB fell to a four-month low after a Q3 miss; RSI 16 and 16% off its high.", "Recovery in fees", "More credit provisions", (-12,8,18), 'Medium', 'Oversold income'),
 ('AIY.SI', "iFAST: fintech platform, revenue +23%, 26% off its high with 41% analyst upside.", "Q3 results already out; HK pension business", "Market-driven volumes", (-18,18,38), 'Medium', 'Growth'),
 ('S68.SI', "SGX benefits from high trading volumes in volatile markets.", "Monthly volume data", "Already priced (25x earnings)", (-12,7,18), 'Medium', 'Volatility winner'),
]
P[('swing','fin','US')] = [
 ('GRAB', "Up 26% in five days after results; one of few names rising on Nov 5.", "Momentum", "Overbought (RSI 73)", (-10,4,14), 'Medium', 'Momentum'),
 ('SCHW', "Fell less than 1% on Nov 5; benefits from higher rates and heavy trading.", "Monthly trading metrics", "Rate cuts", (-8,4,12), 'Medium', 'Relative strength'),
 ('BAC', "About 10x earnings, 23% off its high, Strong Buy ratings.", "Rotation out of tech into value", "Credit worries", (-8,4,12), 'Medium', 'Value'),
 ('SE', "Oversold (RSI 24) into Q3 results.", "Results Nov 10", "Results gap", (-15,7,22), 'Medium', 'Pre-earnings'),
 ('HOOD', "Down 28% in a month (RSI 26) as crypto and retail trading cool.", "October trading data", "Bitcoin falling (~$76K)", (-18,6,22), 'Speculative', 'Oversold rebound'),
]
P[('swing','fin','SGX')] = [
 ('U11.SI', "UOB is the most oversold SGX bank (RSI 16).", "Rebound after the Q3 miss", "Further downgrades", (-5,3,8), 'Medium', 'Oversold rebound'),
 ('D05.SI', "DBS rose after results; RSI 21.", "Dividend support", "Margin worries", (-4,2.5,6), 'High', 'Oversold income'),
 ('O39.SI', "OCBC reports Nov 6; RSI 32.", "Results", "Margin squeeze", (-5,2,6), 'Medium', 'Pre-earnings'),
 ('AIY.SI', "iFAST rose 3% on Nov 5.", "Momentum", "Market-driven", (-8,3,10), 'Medium', 'Trend'),
 ('S68.SI', "SGX rose 2% on Nov 5; volatility lifts trading volumes.", "Volume data", "Valuation", (-5,2,7), 'Medium', 'Volatility winner'),
]
P[('intraday','fin','US')] = [
 ('AFRM', "Reported after the close; fell 8% during the day.", "Reaction to results", "Gap either way", (-8,0.5,8), 'Speculative', 'Earnings reaction'),
 ('JPM', "Fell 4%; banks often recover first after a tech-led drop.", "Jobs report", "Market-wide selling", (-2,0.4,2.5), 'Medium', 'Bounce watch'),
 ('GS', "Fell 6% with risk assets.", "Jobs report", "More volatility", (-3,0.5,3.5), 'Medium', 'Bounce watch'),
 ('COIN', "Bitcoin fell about 5% to ~$76K.", "Crypto bounce", "Further crypto selling", (-5,0,5), 'Speculative', 'Crypto beta'),
 ('GRAB', "Rose 3.6% against the market.", "Momentum continuation", "Profit-taking", (-3,0.5,4), 'Medium', 'Momentum'),
]
P[('intraday','fin','SGX')] = [
 ('O39.SI', "OCBC reports before the open on Nov 6.", "Results", "Margin miss like UOB", (-3,0.3,3), 'Medium', 'Earnings reaction'),
 ('D05.SI', "Rose after its Q3 miss: dividend support.", "Next session", "Market-wide risk-off", (-1.2,0.2,1.2), 'High', 'Range'),
 ('U11.SI', "Oversold.", "Next session", "Trend down", (-1.5,0.3,1.8), 'Medium', 'Bounce watch'),
 ('S68.SI', "Volatility helps SGX volumes.", "Next session", "Profit-taking", (-2,0.2,2), 'Medium', 'Range'),
 ('AIY.SI', "Rose 3% on Nov 5.", "Next session", "Risk-off", (-2.5,0.3,2.5), 'Medium', 'Momentum'),
]

# IPO tab (6-month view), all markets
P[('ipo','all','US')] = [
 ('SPCX', "SpaceX listed in June at $135 and now trades about 7% below that, 41% under its high. Analysts see large upside.",
  "xAI/GPU news; lock-up expiries", "Valuation, Musk headlines and data-centre policy; fell 8% on Nov 5", (-35,12,45), 'Medium', 'Mega-cap IPO'),
 ('CHYM', "Chime (IPO $27) trades about 11% above its IPO price and held flat on Nov 5.",
  "Member growth", "Fintech credit cycle", (-15,12,30), 'Medium', 'Post-IPO uptrend'),
 ('KLAR', "Klarna (IPO $40) is 66% below its IPO price at about 17x forward earnings; revenue +27%.",
  "Q3 results Nov 17", "Buy-now-pay-later credit losses", (-22,15,40), 'Speculative', 'Deep value'),
 ('FIG', "Figma: revenue +43% with AI products, but fell 16% after results and is 44% below its IPO price.",
  "AI product monetisation", "Software multiples falling", (-30,10,40), 'Speculative', 'Post-earnings dip'),
 ('ACCV', "Accelevation (IPO $18) makes electrical gear for data centres: revenue +80% at about 10x forward earnings, but 45% below its IPO price.",
  "First full quarter as a public company", "Data-centre policy risk; 8% daily swings", (-40,10,50), 'Speculative', 'Post-IPO value'),
]

# ---------- Power & grid (data-center power) ----------
P[('long','pwr','US')] = [
 ('GEV', "GE Vernova: gas turbines and grid gear sold out for years, revenue +27%. 34% off its high.", "Q4 results Jan 27", "Data-centre policy; valuation (30x)", (-25,15,40), 'High', 'Quality at a discount'),
 ('ETN', "Eaton: electrical gear for data centres and utilities, 29% off its high at about 20x earnings.", "Q4 results Feb 2", "Data-centre orders slowing", (-20,14,35), 'Medium', 'Quality at a discount'),
 ('PWR', "Quanta builds the grid: revenue +57%, 35% off its high after a 12% drop.", "Utility capex plans", "Data-centre policy", (-25,14,38), 'Medium', 'Grid builder'),
 ('VRT', "Vertiv: data-centre cooling and power, revenue +61% at about 18x forward earnings, 53% off its high.", "Order backlog updates", "Most exposed to data-centre slowdown", (-35,20,55), 'Medium', 'Oversold growth'),
 ('CEG', "Constellation: biggest US nuclear fleet, 37% off its high.", "Q3 results Nov 9", "Power-price regulation", (-25,14,38), 'Medium', 'Nuclear leader'),
]
P[('long','pwr','SGX')] = [
 ('BN4.SI', "Keppel: power, data centres and asset management, about 17x earnings with 28% analyst upside.", "Asset sales", "Execution", (-12,12,25), 'Medium', 'Value'),
 ('U96.SI', "Sembcorp: power and renewables at about 10x earnings.", "New contracts", "Power prices", (-12,6,18), 'Medium', 'Value'),
 ('AJBU.SI', "Keppel DC REIT: data-centre rents, near its high.", "Dividend", "Rates", (-10,8,18), 'Medium', 'Income'),
 ('DCRU.SI', "Digital Core REIT: US data-centre REIT, about 10x earnings with 47% analyst upside.", "Leasing news", "Tenant concentration", (-12,12,28), 'Medium', 'Deep value'),
 ('544.SI', "CSE Global: electrification and data-centre work, about 11x earnings, but fell 10% on Nov 5.", "New orders", "Small and volatile", (-30,18,50), 'Speculative', 'Recovery'),
]
P[('swing','pwr','US')] = [
 ('BE', "Bloom Energy fell 15% even as NTT DATA picked its fuel cells for 900 MW of data-centre power.", "New orders", "8% daily swings", (-20,8,28), 'Speculative', 'News vs price'),
 ('NEE', "NextEra rose this week (RSI 74); utilities are a safe spot in the selloff.", "Rotation into utilities", "Overbought", (-6,3,9), 'Medium', 'Relative strength'),
 ('VST', "Vistra is down 32% in a month (RSI 24) into results.", "Q3 results Nov 6", "Texas data-centre proposal", (-16,5,20), 'Speculative', 'Pre-earnings'),
 ('CEG', "Constellation is oversold into results.", "Q3 results Nov 9", "Regulation", (-14,5,18), 'Medium', 'Pre-earnings'),
 ('GEV', "GE Vernova fell 7%; RSI 36.", "Oversold bounce", "Data-centre news", (-15,5,20), 'Medium', 'Oversold rebound'),
]
P[('swing','pwr','SGX')] = [
 ('AJBU.SI', "Keppel DC REIT is in an uptrend (RSI 70).", "Momentum", "Rates", (-5,2,7), 'Medium', 'Trend'),
 ('BN4.SI', "Keppel flat on Nov 5.", "Asset-sale news", "Execution", (-4,2,6), 'Medium', 'Range'),
 ('U96.SI', "Sembcorp rose slightly.", "Contracts", "Power prices", (-5,2,6), 'Medium', 'Range'),
 ('DCRU.SI', "Digital Core REIT up 6% this month.", "Momentum", "Overbought (RSI 86)", (-6,2,8), 'Medium', 'Trend'),
 ('544.SI', "CSE Global fell 10%; oversold.", "Bounce", "Small cap", (-18,5,20), 'Speculative', 'Oversold rebound'),
]
P[('intraday','pwr','US')] = [
 ('VST', "Reports before the open Nov 6.", "Results", "Texas policy headlines", (-7,0.5,7), 'Speculative', 'Earnings reaction'),
 ('OKLO', "Reports Nov 6; down 84% from its high.", "Results", "Cash burn; no revenue", (-10,0,10), 'Speculative', 'Earnings reaction'),
 ('BE', "Fell 15% despite a 900 MW order.", "Bounce", "More selling", (-6,1,7), 'Speculative', 'Bounce watch'),
 ('NEE', "Held flat on a crash day.", "Defensive bid", "Market-wide selling", (-1.8,0.3,2), 'Medium', 'Relative strength'),
 ('GEV', "Fell 7%.", "Bounce", "Data-centre news", (-4,0.5,4.5), 'Medium', 'Bounce watch'),
]
P[('intraday','pwr','SGX')] = [
 ('AJBU.SI', "Rose 1.4% on Nov 5.", "Next session", "Small range", (-1.2,0.2,1.2), 'Medium', 'Range'),
 ('U96.SI', "Rose 0.5%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('BN4.SI', "Flat.", "Next session", "Small range", (-1.2,0.2,1.2), 'Medium', 'Range'),
 ('DCRU.SI', "Flat; US data-centre worries may weigh.", "Next session", "US tech selloff", (-1.5,0,1.5), 'Medium', 'Range'),
 ('544.SI', "Fell 10%.", "Next session", "Further selling", (-5,0,4), 'Speculative', 'Bounce watch'),
]

# ---------- Defence & industrials ----------
P[('long','def','US')] = [
 ('GE', "GE Aerospace: jet-engine services boom, revenue +16%, 18% off its high.", "Q4 results Jan 21", "Valuation (34x)", (-15,12,30), 'High', 'Quality'),
 ('RTX', "RTX: missiles and engines, revenue +11%, steady.", "Q4 results Jan 26", "Engine issues", (-12,10,24), 'High', 'Core defence'),
 ('LHX', "L3Harris: space and missile sensors, 32% off its high, 29% analyst upside.", "Golden Dome contracts", "Budget fights with a split government", (-15,13,32), 'Medium', 'Value'),
 ('HWM', "Howmet: jet-engine parts, revenue +29%, 31% off its high.", "Aerospace build rates", "Valuation", (-20,16,38), 'Medium', 'Growth at a discount'),
 ('NOC', "Northrop: B-21 and missile defence, about 18x earnings.", "Golden Dome contracts", "Budget fights", (-15,11,28), 'Medium', 'Value'),
]
P[('long','def','SGX')] = [
 ('S63.SI', "ST Engineering: defence and aerospace, revenue +11%; oversold (RSI 12).", "Contract wins", "Valuation (25x)", (-10,12,24), 'High', 'Quality'),
 ('BS6.SI', "Yangzijiang Shipbuilding: about 8x earnings, revenue +36%.", "New ship orders", "US port fees on Chinese ships", (-18,10,28), 'Medium', 'Value'),
 ('C52.SI', "ComfortDelGro: steady transport earnings, rising (RSI 73).", "Overseas contracts", "Slow growth", (-8,8,16), 'Medium', 'Steady'),
 ('S59.SI', "SIA Engineering: aircraft maintenance, 23% off its high, 33% analyst upside.", "Results already out", "Revenue falling (-11%)", (-10,12,25), 'Medium', 'Recovery'),
 ('H22.SI', "Hong Leong Asia: engines and building materials at about 9x earnings, 43% off its high.", "Results (Feb)", "China demand", (-25,22,50), 'Speculative', 'Deep value'),
]
P[('swing','def','US')] = [
 ('CAT', "Caterpillar is deeply oversold (RSI 18), down 32% in a month.", "Bounce", "Data-centre generator orders slowing", (-12,6,18), 'Medium', 'Oversold rebound'),
 ('NOC', "Defence held up on Nov 5.", "Budget news", "Split-government budget fights", (-8,3,10), 'Medium', 'Relative strength'),
 ('LMT', "Lockheed up 16% in a month.", "F-35 contracts", "Budget fights", (-8,3,10), 'Medium', 'Trend'),
 ('BA', "Boeing about 32% off its high; production recovering.", "Monthly deliveries", "Quality issues", (-10,5,15), 'Medium', 'Recovery'),
 ('KTOS', "Kratos reported after the close; down 74% from its high.", "Results reaction", "Volatile", (-25,5,25), 'Speculative', 'Earnings reaction'),
]
P[('swing','def','SGX')] = [
 ('S63.SI', "ST Engineering very oversold (RSI 12).", "Bounce", "Low volatility", (-4,3,8), 'High', 'Oversold rebound'),
 ('BS6.SI', "Yangzijiang fell 3%; RSI 26.", "Orders", "Trade fees", (-9,3,10), 'Medium', 'Oversold rebound'),
 ('C52.SI', "ComfortDelGro rose 2% (RSI 73).", "Momentum", "Overbought", (-4,1.5,5), 'Medium', 'Trend'),
 ('S59.SI', "SIA Engineering steady.", "Air travel", "Slow growth", (-6,2,7), 'Medium', 'Range'),
 ('H22.SI', "Hong Leong Asia oversold (RSI 26).", "Bounce", "China demand", (-10,4,12), 'Speculative', 'Oversold rebound'),
]
P[('intraday','def','US')] = [
 ('AXON', "Missed Q3 EPS by 19 cents (reported Nov 5) and fell 10%.", "Post-results follow-through", "Further downgrades", (-9,0,9), 'Speculative', 'Earnings reaction'),
 ('KTOS', "Reported after the close.", "Results reaction", "Volatile", (-8,0.5,9), 'Speculative', 'Earnings reaction'),
 ('LMT', "Fell 2.6%.", "Defensive bid", "Market-wide selling", (-2.5,0.4,2.8), 'Medium', 'Range'),
 ('GD', "Fell 1.9%; near its high.", "Defensive bid", "Market-wide selling", (-2,0.3,2.2), 'Medium', 'Relative strength'),
 ('RTX', "Fell 2.9%.", "Defensive bid", "Market-wide selling", (-2,0.3,2.2), 'Medium', 'Range'),
]
P[('intraday','def','SGX')] = [
 ('S63.SI', "Very oversold.", "Next session", "Small range", (-1,0.3,1.2), 'Medium', 'Bounce watch'),
 ('C52.SI', "Rising.", "Next session", "Small range", (-1,0.2,1), 'Medium', 'Momentum'),
 ('BS6.SI', "Fell 3%.", "Next session", "Risk-off", (-2.5,0.2,2.5), 'Medium', 'Range'),
 ('S59.SI', "Steady.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('H22.SI', "Oversold.", "Next session", "Thin trading", (-2.5,0.2,2.5), 'Speculative', 'Range'),
]

# ---------- Energy (oil and gas) ----------
P[('long','nrg','US')] = [
 ('CVX', "Chevron: revenue +35%, about 13x earnings, 9% off its high.", "Hess integration; buybacks", "Oil price drop if an Iran deal ends the war", (-15,9,25), 'High', 'Core energy'),
 ('XOM', "Exxon: steady cash flow, about 14x earnings.", "Buybacks", "Oil price drop", (-15,7,22), 'High', 'Core energy'),
 ('FANG', "Diamondback: low-cost Permian producer at about 9x earnings, 32% analyst upside.", "Buybacks", "Oil price drop", (-20,15,35), 'Medium', 'Value'),
 ('LNG', "Cheniere: US gas exports, steady contracts.", "New export capacity", "Gas price swings", (-15,9,26), 'Medium', 'Steady'),
 ('COP', "ConocoPhillips: about 13x earnings, revenue +36%.", "Results Nov 5", "Oil price drop", (-18,8,25), 'Medium', 'Value'),
]
P[('long','nrg','SGX')] = [
 ('5E2.SI', "Seatrium builds offshore rigs and wind platforms; 33% analyst upside.", "New orders", "Contract delays", (-15,12,28), 'Medium', 'Recovery'),
 ('BN4.SI', "Keppel: energy infrastructure and asset management.", "Asset sales", "Execution", (-12,10,22), 'Medium', 'Value'),
 ('RE4.SI', "Geo Energy: Indonesian coal at about 7x earnings.", "Coal prices", "Coal price drop", (-25,8,30), 'Speculative', 'Value'),
 ('5LY.SI', "Marco Polo Marine: offshore vessels, revenue +40% at about 10x earnings.", "Results (Nov)", "Thin trading", (-25,10,35), 'Speculative', 'Growth value'),
 ('5WH.SI', "Rex International is in a long downtrend; no setup.", "None", "Further losses", (-30,-5,20), 'Speculative', 'Avoid'),
]
P[('swing','nrg','US')] = [
 ('MPC', "Marathon Petroleum is oversold (RSI 20) after a strong year.", "Refining margins", "Margin drop", (-10,5,16), 'Medium', 'Oversold rebound'),
 ('PSX', "Phillips 66 oversold (RSI 24).", "Refining margins", "Margin drop", (-10,5,15), 'Medium', 'Oversold rebound'),
 ('DVN', "Devon oversold (RSI 25), about 8x earnings; reported Nov 5.", "Results reaction", "Oil price drop", (-11,5,16), 'Medium', 'Oversold rebound'),
 ('OXY', "Occidental oversold (RSI 27) into results.", "Results Nov 9", "Debt", (-9,4,13), 'Medium', 'Pre-earnings'),
 ('EOG', "EOG oversold (RSI 32); reported Nov 5.", "Results reaction", "Oil price drop", (-9,4,12), 'Medium', 'Oversold rebound'),
]
P[('swing','nrg','SGX')] = [
 ('5E2.SI', "Seatrium near support.", "Orders", "Delays", (-8,3,10), 'Medium', 'Support'),
 ('BN4.SI', "Keppel steady.", "Asset sales", "Execution", (-4,2,6), 'Medium', 'Range'),
 ('RE4.SI', "Geo Energy oversold.", "Coal prices", "Coal price drop", (-9,3,11), 'Speculative', 'Oversold rebound'),
 ('5LY.SI', "Marco Polo Marine near lows.", "Results", "Thin trading", (-10,3,12), 'Speculative', 'Support'),
 ('5WH.SI', "Rex International: no setup.", "None", "Further losses", (-12,-2,8), 'Speculative', 'Avoid'),
]
P[('intraday','nrg','US')] = [
 ('OXY', "Oil rebounded about 3% (WTI ~$91).", "Oil strength", "Iran-deal headlines", (-2,0.4,2.5), 'Medium', 'Oil bounce'),
 ('DVN', "Oversold; reported Nov 5.", "Results reaction", "Oil", (-3,0.5,3), 'Medium', 'Earnings reaction'),
 ('COP', "Reported Nov 5.", "Results reaction", "Oil", (-2.5,0.4,2.5), 'Medium', 'Earnings reaction'),
 ('MPC', "Very oversold.", "Bounce", "Margins", (-3,0.5,3.5), 'Medium', 'Bounce watch'),
 ('XOM', "Low volatility.", "Oil", "Market-wide selling", (-1.8,0.3,2), 'Medium', 'Range'),
]
P[('intraday','nrg','SGX')] = [
 ('5E2.SI', "Fell 2.6%.", "Next session", "Risk-off", (-2,0.3,2), 'Medium', 'Range'),
 ('BN4.SI', "Flat.", "Next session", "Small range", (-1.5,0.3,1.5), 'Medium', 'Range'),
 ('RE4.SI', "Fell 1.9%.", "Next session", "Coal prices", (-2.5,0.3,2.5), 'Speculative', 'Range'),
 ('5LY.SI', "Fell 2.7%.", "Next session", "Thin trading", (-2.5,0.2,2.5), 'Speculative', 'Range'),
 ('5WH.SI', "Penny stock in a downtrend; avoid.", "None", "Further losses", (-5,-1,4), 'Speculative', 'Avoid'),
]

IPO_LIST = [
 # sym, name, ipo_date, ipo_price, sector, status
 ('ANTHROPIC','Anthropic (not yet listed; roadshow may start week of Nov 9)','2026-10-26',None,'ai','Filed'),
 ('AGLT','Agility Robotics (merger listing with Churchill Capital XI)','2026-11-05',None,'ai','Expected'),
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
 ('2026-11-05T19:18','BE', "Via tracker: jokes that a new Google data centre running on Bloom fuel cells means the AI build-out is 'over', i.e. demand is still growing."),
 ('2026-11-05T07:12','COHR', "Via tracker: pushes back on doubts about Coherent's co-packaged optics, citing management saying laser demand shows no slowdown."),
 ('2026-11-05T05:12','NVDA MU', "Via tracker: argues fears about Democratic data-centre rules are overdone, since build-outs grew under Biden and AI support is bipartisan. Says he added leverage into the drop (not advice)."),
 ('2026-11-05T04:58','AAOI COHR LITE MRVL CRDO', "Via tracker: says laser and indium-phosphide supply stays tight, and smaller laser makers' 2028 sales could exceed today's market values."),
 ('2026-11-05T04:36','COHR LITE MRVL', "Via tracker: summarises Coherent's call: a $20B five-year contract, no laser oversupply expected in 2028, and pricing power."),
 ('2026-11-05T02:36','INTC MU TSM', "Via tracker: points to an SEC filing showing Intel's CEO bought about $9.7M of stock near $65 after the steep fall."),
 ('2026-11-05T01:40','AXTI COHR AAOI', "Via tracker: says AXT's backlog jumped in 90 days and that forced selling by funds is lumping strong and weak AI names together."),
]

EVENTS = [
 ('2026-11-04','Macro','Dow +3.0%, best post-midterm day in 44 years', "S&P +1.6%, Nasdaq +1.4%. Brent fell below $100; energy was the worst sector; defence and Nvidia slipped."),
 ('2026-11-04','Fin','UOB misses Q3 estimates', "Shares fell about 5% to a four-month low on a profit miss and margin pressure."),
 ('2026-11-04','AI','Coherent beats; Arm and Qualcomm report', "Coherent: record $2.37B revenue, EPS $2.09 vs $1.80, ~$20B five-year optics deal. Arm revenue +27%. Qualcomm phone-chip sales fell 26% as Apple business shrinks."),
 ('2026-11-05','Macro','AI meltdown: Nasdaq -5.5%, chip index -12%', "S&P -4.4% (worst day since April 2025), Dow -1,833 points, Nasdaq in correction, VIX ~28. Fears that the new Congress slows data-centre building plus hedge-fund de-grossing. Nvidia, AMD, Micron, Marvell fell 9-17%."),
 ('2026-11-05','AI','Microsoft data-centre delay chatter hits neoclouds', "Reports that Microsoft declined a Texas data-centre contract extension with Nscale. IREN -14%, Nebius -14%, CoreWeave -9%."),
 ('2026-11-05','Fin','DBS Q3 profit falls 5%, misses', "S$2.81B vs S$2.95B expected on weaker trading income; 81-cent dividend kept; says interest income has bottomed. Shares +0.6%."),
 ('2026-11-05','Macro','BoE hikes to 4%; Fed hike odds ease', "Markets now price ~70% odds of a Fed hike on Dec 9 (from 83%). WTI rose ~3% to about $91; bitcoin fell to ~$76K."),
 ('2026-11-05','Mixed','After the close: AAOI, IREN, Axon, Kratos, Affirm, Airbnb', "AAOI revenue +127% with a Q4 guide of $385-420M. IREN AI cloud revenue nearly tripled to ~$200M. Axon missed EPS by 19 cents."),
 ('2026-11-06','Macro','US October jobs report', "8:30 a.m. ET (9:30 p.m. SGT)."),
 ('2026-11-06','Fin','OCBC Q3 results', "Before the SGX open."),
 ('2026-11-06','Power','Vistra, Oklo, Moderna report', "Vistra is the most exposed to the Texas data-centre proposal."),
 ('2026-11-09','Mixed','Constellation, NRG, KKR, Occidental, Hims report', "Anthropic IPO roadshow may also begin this week (reported, not confirmed)."),
 ('2026-11-10','Mixed','CoreWeave and Sea report', "Nebius, Applied Materials and Nu follow on Nov 12."),
 ('2026-11-17','AI','Nvidia Q3 results', "The main AI-demand checkpoint this month. Klarna also reports."),
 ('2026-12-09','Macro','Fed rate decision', "Markets price a likely hike."),
]
