# Analyst picks for 2026-11-12 (snapshot: US midday Nov 11 ~12:25 ET, SGX close Nov 11). Fields: sym, thesis, catalyst, risk, (low, base, high) % expected move, conviction, setup
# Horizons: long = 12 months, swing = ~4 weeks, intraday = rest of session (US) / next session (SGX), ipo = 6 months.
# Context: Nov 11: AI trade rebounded after CoreWeave's beat-and-raise (2026 revenue guide $13.0-13.3B, funding via prepayments and contract-backed debt, no unsecured debt).
# Close: S&P +1.3% to 7,619, Nasdaq +1.6% to 25,466 (erased post-election losses), Dow +0.5%. VIX 17.5. CoreWeave +24.7%; Nvidia +2.9% to $173.73 despite a Baird downgrade to Neutral.
# Memory, optics and storage led (Micron, Sandisk, Seagate, Lumentum up 10%+ midday). Bloom Energy +16%. Talen signed a 750 MW, $100M/yr capacity deal.
# Bond market shut (Veterans Day); 10-yr ~5.0%. Dec hike odds ~90% (CME); Goldman and UBS now expect hikes in Dec and March; Bowman says more hikes may be needed.
# STI +0.6% to 5,290; Venture +5.2% on a 22% Q3 profit rise. Anthropic launched its IPO roadshow ($70-78); pricing expected week of Nov 16. WTI ~$86.
P = {}

# ---------- AI & chips ----------
P[('long','ai','US')] = [
 ('TSM', "Makes almost every leading AI chip. October sales +60% y/y (record); about 18x forward earnings, 14% below its high. CEO says demand is still far above supply.",
  "November sales (~Dec 10); Q4 results Jan 14", "Taiwan geopolitics; overseas fabs dilute margins", (-18,17,38), 'High', 'Core holding'),
 ('NVDA', "Revenue +106% at about 11x forward earnings, the cheapest big AI chip stock. Bounced 2.9% on Nov 11 but is still 26% off its high; Baird cut it to Neutral on CEO and China uncertainty.",
  "Q3 results Nov 17", "Shareholder lawsuit; China-chip report; board probe of the CEO", (-30,20,50), 'Medium', 'Quality at a discount, higher risk'),
 ('AVGO', "Custom AI chips plus networking: revenue +86% at about 18x forward earnings, 26% below its high. Has held up best through the selloff.",
  "Q4 results Dec 9", "Lumpy custom-chip orders; customer concentration", (-22,18,42), 'Medium', 'Pullback in a leader'),
 ('MU', "Memory is still the tightest part of AI servers: revenue +379% at about 4x forward earnings, 32% off its high. Jumped ~14% on Nov 11; Goldman calls it a buy, BofA dropped it from its top picks.",
  "FQ1 results Dec 23", "Peak-cycle earnings; memory falls hard when prices turn", (-38,20,58), 'Medium', 'Cycle leader'),
 ('COHR', "Record quarter and a ~$20B five-year optics deal; 43% below its high at about 15x forward earnings. Up 24% in five days.",
  "First $3B quarter targeted by FY27 end", "8% daily swings; capex keeps rising", (-32,20,55), 'Medium', 'Optics rebound'),
]
P[('long','ai','SGX')] = [
 ('AWX.SI', "AEM is up ~300% this year but 37% below its high; analysts rate it Strong Buy with about 100% upside.",
  "Q3 business update (Nov)", "One large customer; 7% daily swings", (-38,18,55), 'Medium', 'SGX AI leader'),
 ('V03.SI', "Venture's Q3 profit rose 22% to S$67.8M; RHB raised its target to S$21.97 and DBS sees S$22.90. Net cash, about 16x earnings, low volatility.",
  "Analyst upgrades after Q3", "Slow revenue growth (+7%)", (-12,13,26), 'High', 'Steady value'),
 ('558.SI', "UMS makes precision parts for chip-equipment makers: revenue +61%, 35% off its high, about 19x earnings. Rose 9% on Nov 11 after a stronger quarter.",
  "Applied Materials results Nov 12", "Tied to Applied Materials spending", (-30,15,45), 'Medium', 'Equipment supplier'),
 ('5DD.SI', "Micro-Mechanics makes precision tools for chip assembly and test: revenue +45%, 39% off its high.",
  "Q1 FY27 results (Nov)", "Small and thinly traded", (-24,14,36), 'Medium', 'Growth at a discount'),
 ('E28.SI', "Frencken builds modules for chip and medical equipment. 47% off its high at about 16x earnings; rose 6% on Nov 11.",
  "Q3 business update (Nov)", "Flat revenue so far this year", (-25,13,36), 'Medium', 'Recovery'),
]
P[('swing','ai','US')] = [
 ('NVDA', "RSI 29 a week before results, on twice its normal volume. Lagged the Nov 11 rally, so the bad news may be largely priced; each new legal or China headline can still hit it.",
  "Q3 results Nov 17", "More lawsuit or export-control news; Baird downgrade", (-16,6,20), 'Speculative', 'Oversold into earnings'),
 ('CRWV', "CoreWeave rose ~25% after beating and raising; funding now leans on customer prepayments, with no new unsecured debt. Still 56% off its high.",
  "Analyst target updates; Nvidia results", "Capex $37-39B; 9% daily swings", (-25,8,32), 'Speculative', 'Beat and raise'),
 ('LITE', "Marvell is buying Lumentum for 4.5 Marvell shares each. At snapshot prices that is worth about 16% more than LITE's price.",
  "Spread narrows if the deal clears", "Regulatory delay (incl. China); MRVL falls again", (-15,7,20), 'Medium', 'Merger spread'),
 ('MU', "Up ~14% on Nov 11 on memory-shortage news; RSI only 48 after a 13% monthly drop.",
  "Price-floor contracts; FQ1 results Dec 23", "Fast reversal if AI capex fears return", (-15,7,22), 'Medium', 'Rebound'),
 ('CRDO', "Credo: revenue +115% at about 15x forward earnings, 51% off its high; analysts see ~90% upside. Rose 13% on Nov 11.",
  "Q2 results Dec 1", "Customer concentration; 8% daily swings", (-22,9,30), 'Speculative', 'Oversold growth'),
]
P[('swing','ai','SGX')] = [
 ('558.SI', "UMS rose 9% on very heavy volume after a stronger quarter; RSI 37.", "Applied Materials results Nov 12", "Chip-equipment sentiment", (-15,6,20), 'Medium', 'Earnings rebound'),
 ('V03.SI', "Venture jumped 5% on a Q3 profit beat and target raises.", "Analyst upgrades", "Low growth", (-6,4,10), 'High', 'Post-earnings drift'),
 ('AWX.SI', "AEM rose 3%; still down 35% in a month (RSI 36).",
  "Q3 update; US chips stabilising", "Bounce fades if Nvidia falls on results", (-20,6,26), 'Speculative', 'Oversold rebound'),
 ('E28.SI', "Frencken rose 6% from RSI 35.", "Q3 business update (Nov)", "No clear catalyst before results", (-14,5,16), 'Speculative', 'Oversold rebound'),
 ('5DD.SI', "Micro-Mechanics rose 4.4%; RSI 39.", "Q1 FY27 results (Nov)", "Thin order book", (-12,4,14), 'Medium', 'Rebound'),
]
P[('intraday','ai','US')] = [
 ('NBIS', "Reports Q3 before the open on Nov 12 after rising ~18% on CoreWeave's results.", "Results", "Sell-the-news after the run-up", (-10,0.5,10), 'Speculative', 'Earnings reaction'),
 ('AMAT', "Reports after the close on Nov 12; rose ~8% on Nov 11.", "Pre-results positioning", "China export rules", (-3,0.3,3), 'Medium', 'Pre-earnings'),
 ('CRWV', "Day-two follow-through after a ~25% jump.", "Analyst upgrades", "Profit-taking", (-8,0,8), 'Speculative', 'Momentum check'),
 ('NVDA', "Lagged the rally (+2.9% close) on a Baird downgrade.", "Catch-up bid", "CEO-probe headlines", (-3.5,0.5,4), 'Speculative', 'Headline risk'),
 ('SNDK', "Jumped ~16% midday on memory strength.", "Momentum", "Profit-taking; 8% daily swings", (-7,0,7), 'Speculative', 'Momentum check'),
]
P[('intraday','ai','SGX')] = [
 ('558.SI', "Rose 9% on heavy volume.", "Next session", "Gives back gains", (-4,0,4), 'Speculative', 'Follow-through check'),
 ('V03.SI', "Rose 5.2% to lead the STI after Q3.", "Next session", "Profit-taking", (-2,0.3,2.2), 'Medium', 'Follow-through check'),
 ('E28.SI', "Rose 6%.", "Next session", "Follows US chip equipment", (-3.5,0.2,3.5), 'Speculative', 'Follow-through check'),
 ('AWX.SI', "Rose 3%; US chips rallied overnight.", "Next session", "Gives back gains", (-5,0.5,5), 'Speculative', 'Gap watch'),
 ('5DD.SI', "Rose 4.4%.", "Next session", "Thin trading", (-3,0.2,3), 'Medium', 'Range'),
]

# ---------- Health ----------
P[('long','hc','US')] = [
 ('LLY', "Obesity-drug leader: revenue +39%, at its high (+33% this year). Little analyst upside left, so the base case is modest.",
  "Orforglipron launch; Q4 results (Feb)", "Drug-price policy under the new Congress", (-16,8,25), 'High', 'Defensive growth'),
 ('ARGX', "argenx: revenue +52% from its immune-disease drug Vyvgart, 8% off its high, 17% analyst upside.",
  "New indications in 2027", "Competition in myasthenia gravis", (-15,10,28), 'Medium', 'Growth leader'),
 ('MDGL', "Madrigal's liver drug Rezdiffra is growing fast (revenue +50%); 28% off its high with 59% analyst upside.",
  "Script data; EU rollout", "Competition from GLP-1 drugs", (-22,20,45), 'Medium', 'Oversold growth'),
 ('INSM', "Insmed's lung drug launch drives revenue +268%; up 23% in a month but still 44% off its high, 63% analyst upside.",
  "Brensocatib launch numbers", "Expensive on near-term earnings", (-30,18,48), 'Medium', 'Launch story'),
 ('ALNY', "Alnylam is 67% off its high at about 14x forward earnings (RSI 17); analysts see 91% upside.",
  "Amvuttra script data", "Trend still down", (-30,18,50), 'Speculative', 'Deep value'),
]
P[('long','hc','SGX')] = [
 ('Q0F.SI', "IHH runs hospitals across Asia; analysts see 37% upside.", "Q3 results Nov 25", "Currency swings", (-12,12,25), 'Medium', 'Regional leader'),
 ('C2PU.SI', "Parkway Life REIT: steady hospital and nursing-home rents, 6% off its high.", "Dividend", "Rates near 5% in the US", (-8,7,15), 'High', 'Income'),
 ('AP4.SI', "Riverstone makes cleanroom and medical gloves at about 14x earnings with 38% analyst upside.", "Q3 results (Nov)", "Glove price competition", (-15,11,28), 'Medium', 'Value'),
 ('BSL.SI', "Raffles Medical: Singapore hospital group, 21% off its high and in a mild uptrend (RSI 65).", "Results (Feb)", "Shrinking revenue (-7%)", (-10,8,18), 'Medium', 'Recovery'),
 ('H02.SI', "Haw Par (Tiger Balm) trades near 10x earnings with a large cash and investment pile.", "Results (Feb)", "Revenue down 8%", (-12,6,16), 'Medium', 'Value'),
]
P[('swing','hc','US')] = [
 ('ALNY', "Deeply oversold (RSI 17), 67% off its high; rose 3.5% on Nov 11.", "Amvuttra script data", "Trend still down", (-15,7,22), 'Speculative', 'Oversold rebound'),
 ('MDGL', "Up 8.5% in five days; 59% analyst upside.", "Script data", "Rotation back to tech", (-12,6,18), 'Medium', 'Rebound'),
 ('INSM', "Up 23% in a month (RSI 76).", "Launch numbers", "Overbought", (-10,3,13), 'Medium', 'Momentum'),
 ('LLY', "At its high; steady leader while growth stocks swing.", "Orforglipron news", "Money rotating back into chips", (-8,3,10), 'High', 'Relative strength'),
 ('CYTK', "Cytokinetics' heart drug launch is starting (revenue from a near-zero base); 33% off its high, 87% analyst upside. Rose 4% on Nov 11.", "Launch numbers", "Launch slower than hoped", (-14,6,20), 'Speculative', 'Launch rebound'),
]
P[('swing','hc','SGX')] = [
 ('C2PU.SI', "Parkway Life REIT: lowest-volatility name in the group.", "Dividend", "Rates", (-4,2,6), 'High', 'Range'),
 ('BSL.SI', "Raffles Medical is in a mild uptrend (RSI 65).", "Momentum", "Low volume", (-5,2.5,8), 'Medium', 'Trend'),
 ('Q0F.SI', "IHH ahead of Q3 results.", "Q3 results Nov 25", "Results miss", (-6,3,9), 'Medium', 'Pre-earnings'),
 ('AP4.SI', "Riverstone rose 2.8%; large analyst upside.", "Q3 results (Nov)", "Glove prices", (-8,3,10), 'Medium', 'Support'),
 ('QC7.SI', "Q&M Dental is very oversold (RSI 15).", "Bounce", "Small cap", (-8,3,10), 'Speculative', 'Oversold rebound'),
]
P[('intraday','hc','US')] = [
 ('HIMS', "Bounced ~6% after a 24% weekly drop, but the FTC widened its lawsuit and KeyBanc calls 2027 a transition year.", "Oversold (RSI 30)", "Legal headlines; downgrades", (-7,0,7), 'Speculative', 'Post-earnings flush'),
 ('ALNY', "Rose 3.5% from RSI 17.", "Bounce", "Trend down", (-4,0.3,4), 'Speculative', 'Bounce watch'),
 ('MRNA', "Fell 2.3%; still far above analyst targets.", "Dip buying", "Analysts see 37% downside to targets", (-6,0,6), 'Speculative', 'Extended'),
 ('CYTK', "Rose 4% with biotech.", "Momentum", "Profit-taking", (-3.5,0.3,3.5), 'Speculative', 'Momentum check'),
 ('LLY', "Flat near its high.", "Defensive bid", "Rotation into tech", (-2.2,0.2,2.2), 'Medium', 'Range'),
]
P[('intraday','hc','SGX')] = [
 ('C2PU.SI', "Steady REIT.", "Next session", "Small range", (-1,0.2,1), 'Medium', 'Range'),
 ('BSL.SI', "Rose 1.2%; mild uptrend.", "Next session", "Small range", (-1.5,0.3,1.5), 'Medium', 'Relative strength'),
 ('AP4.SI', "Rose 2.8%.", "Next session", "Thin trading", (-2,0.2,2), 'Medium', 'Follow-through check'),
 ('H02.SI', "Rose 0.8%.", "Next session", "Small range", (-1.5,0.3,1.5), 'Medium', 'Range'),
 ('Q0F.SI', "Rose 0.4%.", "Next session", "Malaysia market swings", (-2,0.2,2), 'Medium', 'Range'),
]

# ---------- Finance ----------
P[('long','fin','US')] = [
 ('JPM', "Best-run US bank, 6% off its high at about 13x forward earnings. Higher rates support interest income.", "Q4 results Jan 14", "Credit cycle", (-15,8,22), 'High', 'Core holding'),
 ('V', "Visa: steady growth (+13%), near its high; little AI exposure.", "Holiday spending", "Regulation of card fees", (-12,6,18), 'High', 'Defensive growth'),
 ('GS', "Trading and deal-making boom, about 12.5x forward earnings, 19% off its high. Co-leads Anthropic's IPO, whose roadshow launched this week.",
  "Anthropic IPO (pricing week of Nov 16)", "Market volatility hits deals", (-20,10,28), 'Medium', 'Cyclical value'),
 ('NU', "Nubank: revenue +52% at about 11x forward earnings, 35% off its high.", "Q3 results Nov 12", "Brazil credit and currency", (-30,20,52), 'Medium', 'Growth at a discount'),
 ('SE', "Sea: Q3 revenue +43% beat but EPS missed on loan-loss provisions; $1B buyback. About 15x forward earnings, 49% off its high.",
  "Q4 results (Mar)", "Rising credit costs at Monee; competition", (-30,20,52), 'Medium', 'Oversold growth'),
]
P[('long','fin','SGX')] = [
 ('D05.SI', "DBS kept its 81-cent quarterly dividend and says interest income has bottomed; 10% off its high.",
  "Q4 results (Feb)", "Margins if rates fall; stronger SGD", (-10,8,16), 'High', 'Income leader'),
 ('O39.SI', "OCBC was the only local bank to beat in Q3 and raised loan-growth guidance.",
  "Q4 results (Feb)", "Margin fell 18 bp to 1.66%", (-10,7,15), 'Medium', 'Income'),
 ('U11.SI', "UOB missed Q3 and cut its margin guidance; RSI 17, 16% off its high.", "Recovery in fees", "More credit provisions", (-12,8,18), 'Medium', 'Oversold income'),
 ('AIY.SI', "iFAST: fintech platform, revenue +23%, 27% off its high with 42% analyst upside.", "HK pension business", "Market-driven volumes", (-18,17,36), 'Medium', 'Growth'),
 ('S68.SI', "SGX benefits from high trading volumes; from Jan 2027 its RegCo takes over IPO prospectus reviews.", "Monthly volume data", "Already priced (25x earnings)", (-12,7,18), 'Medium', 'Volatility winner'),
]
P[('swing','fin','US')] = [
 ('NU', "Oversold (RSI 27) into Q3 results on Nov 12.", "Results", "Brazil credit; MercadoLibre's margin miss", (-15,6,20), 'Medium', 'Pre-earnings'),
 ('HOOD', "Rose 5% from oversold; retail access to the Anthropic IPO runs partly through Robinhood.", "Anthropic IPO demand", "Crypto weakness; higher rates", (-16,6,22), 'Speculative', 'Oversold rebound'),
 ('GS', "Anthropic roadshow is under way ($70-78); pricing expected next week.", "Deal fees", "Volatility", (-8,4,12), 'Medium', 'Deal pipeline'),
 ('IBKR', "Rose ~8% midday with the market rebound; 15% off its high, about 25x forward earnings.", "Monthly brokerage metrics", "Rates and crypto swings", (-10,4,13), 'Medium', 'Relative strength'),
 ('SE', "Holding after a revenue beat and EPS miss; $1B buyback.", "Buyback; analyst updates", "Credit costs", (-12,5,16), 'Medium', 'Post-earnings'),
]
P[('swing','fin','SGX')] = [
 ('D05.SI', "DBS is oversold (RSI 25); rose 1% on Nov 11.", "Dividend support", "Margin worries", (-4,3,7), 'High', 'Oversold income'),
 ('U11.SI', "UOB RSI 17 after its Q3 miss.", "Rebound", "Further downgrades", (-5,3,8), 'Medium', 'Oversold rebound'),
 ('O39.SI', "OCBC rose 1% as banks firmed.", "Post-results recovery", "Margin squeeze", (-4,2,6), 'Medium', 'Rebound'),
 ('AIY.SI', "iFAST is holding up (RSI 48).", "Momentum", "Market-driven", (-8,3,10), 'Medium', 'Range'),
 ('S68.SI', "SGX benefits when markets are volatile.", "Volume data", "Valuation", (-5,2,7), 'Medium', 'Volatility winner'),
]
P[('intraday','fin','US')] = [
 ('NU', "Reports Q3 on Nov 12 (RSI 27).", "Results", "Brazil credit", (-8,0.5,8), 'Speculative', 'Earnings reaction'),
 ('IBKR', "Rose ~8% midday.", "Momentum", "Profit-taking", (-3,0.2,3), 'Medium', 'Momentum check'),
 ('HOOD', "Rose 5%.", "Anthropic IPO interest", "Crypto weakness", (-4,0.3,4), 'Speculative', 'Follow-through check'),
 ('COIN', "Rose 4.5% as bitcoin firmed near $74K.", "Crypto bounce", "More crypto selling", (-5,0,5), 'Speculative', 'Crypto beta'),
 ('JPM', "Little changed; banks steady.", "Higher rates", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
]
P[('intraday','fin','SGX')] = [
 ('D05.SI', "Rose 1% from RSI 25.", "Next session", "Market-wide risk-off", (-1.2,0.3,1.4), 'High', 'Follow-through check'),
 ('U11.SI', "Rose 0.9%; still oversold.", "Next session", "Trend down", (-1.5,0.3,1.6), 'Medium', 'Bounce watch'),
 ('O39.SI', "Rose 1%.", "Next session", "Small range", (-1.3,0.2,1.3), 'Medium', 'Range'),
 ('S68.SI', "Rose 0.4%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('AIY.SI', "Rose 0.8%.", "Next session", "Risk-off", (-2,0.3,2), 'Medium', 'Range'),
]

# IPO tab (6-month view), all markets
P[('ipo','all','US')] = [
 ('SPCX', "SpaceX listed in June at $135 and trades about 7% above that, 32% under its high. Analysts see large upside.",
  "xAI/GPU news; NASA lunar awards; lock-up expiries", "Valuation, Musk headlines and data-centre policy", (-35,12,45), 'Medium', 'Mega-cap IPO'),
 ('CHYM', "Chime (IPO $27) trades about 22% above its IPO price, near its high, up 11% in five days.",
  "Member growth", "Fintech credit cycle", (-15,10,28), 'Medium', 'Post-IPO uptrend'),
 ('ACCV', "Accelevation (IPO $18) makes electrical gear for data centres: revenue +80% at about 12x forward earnings. Rose ~16% midday with AI infrastructure, still 31% below its IPO price.",
  "First results as a public company Nov 12", "Data-centre policy risk; 9% daily swings", (-40,12,55), 'Speculative', 'Post-IPO value'),
 ('KLAR', "Klarna (IPO $40) is 66% below its IPO price at about 16x forward earnings; revenue +27%.",
  "Q3 results Nov 17", "Buy-now-pay-later credit losses", (-22,15,40), 'Speculative', 'Deep value'),
 ('FIG', "Figma: revenue +43% with AI products, but 42% below its IPO price after a weak reaction to results (RSI 30).",
  "AI product monetisation", "Software multiples falling; Anthropic's new office tools", (-30,8,38), 'Speculative', 'Post-earnings dip'),
]

# ---------- Power & grid (data-center power) ----------
P[('long','pwr','US')] = [
 ('GEV', "GE Vernova: gas turbines and grid gear sold out for years, revenue +27%. 30% off its high with 44% analyst upside.", "Q4 results Jan 27", "Data-centre policy; valuation (32x)", (-25,15,40), 'High', 'Quality at a discount'),
 ('CEG', "Constellation beat Q3 and raised 2026 guidance to $12.50-12.80; still 27% off its high.", "Buyback update; new long-term power deals", "Data-centre politics; PJM rules", (-22,15,36), 'High', 'Beat and raise'),
 ('ETN', "Eaton: electrical gear for data centres and utilities, 20% off its high at about 22x earnings.", "Q4 results Feb 2", "Data-centre orders slowing", (-20,13,33), 'Medium', 'Quality at a discount'),
 ('VRT', "Vertiv: data-centre cooling and power, revenue +61% at about 21x forward earnings, 44% off its high. CoreWeave's results eased spending fears.", "Order backlog updates", "Most exposed to a data-centre slowdown", (-35,18,52), 'Medium', 'Oversold growth'),
 ('PWR', "Quanta builds the grid: revenue +57%, 21% off its high.", "Utility capex plans", "Data-centre policy", (-25,12,34), 'Medium', 'Grid builder'),
]
P[('long','pwr','SGX')] = [
 ('BN4.SI', "Keppel: power, data centres and asset management, about 16x earnings with 29% analyst upside.", "Asset sales", "Execution", (-12,12,25), 'Medium', 'Value'),
 ('U96.SI', "Sembcorp: power and renewables at about 9x earnings.", "New contracts", "Power prices", (-12,7,18), 'Medium', 'Value'),
 ('DCRU.SI', "Digital Core REIT: US data-centre REIT, about 10x earnings with 52% analyst upside.", "Leasing news", "Tenant concentration; US rates at 5%", (-12,12,28), 'Medium', 'Deep value'),
 ('AJBU.SI', "Keppel DC REIT: data-centre rents, 11% off its high.", "Dividend", "Rates", (-10,7,17), 'Medium', 'Income'),
 ('544.SI', "CSE Global: electrification and data-centre work, about 11x earnings, 48% off its high; rose 8% on Nov 11.", "New orders", "Small and volatile", (-30,18,50), 'Speculative', 'Recovery'),
]
P[('swing','pwr','US')] = [
 ('TLN', "Talen signed a seven-year 750 MW capacity deal worth ~$100M a year; up 17% in five days, about 12.5x forward earnings.", "Analyst target updates", "Overbought after the jump", (-12,6,18), 'Medium', 'New-contract momentum'),
 ('CEG', "Beat-and-raise last week; up 12% in five days.", "Analyst target updates", "Data-centre politics; higher yields", (-12,6,18), 'Medium', 'Post-earnings drift'),
 ('NRG', "Strong Q3 and a $4B asset sale; about 10x earnings with 66% analyst upside. Up 20% in five days.", "Analyst updates", "Texas data-centre proposal", (-15,6,20), 'Medium', 'Post-earnings drift'),
 ('VRT', "Rose ~9% midday as CoreWeave's results revived data-centre spending hopes.", "Order updates", "Rates; 7% daily swings", (-15,6,20), 'Medium', 'Rebound'),
 ('VST', "Raised its 2026 outlook on Nov 6; up 13% in five days, 49% analyst upside.", "Analyst updates", "Texas data-centre proposal", (-14,6,20), 'Medium', 'Post-earnings drift'),
]
P[('swing','pwr','SGX')] = [
 ('544.SI', "CSE Global rose 8% on heavy volume (RSI 47).", "New orders", "Small cap", (-15,5,18), 'Speculative', 'Rebound'),
 ('BN4.SI', "Keppel rose 1.1% from RSI 42.", "Asset-sale news", "Execution", (-5,3,8), 'Medium', 'Rebound'),
 ('U96.SI', "Sembcorp rose 1%; RSI 36.", "Contracts", "Power prices", (-5,2,7), 'Medium', 'Range'),
 ('DCRU.SI', "Digital Core REIT flat (RSI 63).", "Support", "US data-centre worries", (-6,2,8), 'Medium', 'Range'),
 ('AJBU.SI', "Keppel DC REIT eased 1.4% from overbought (RSI 69).", "Momentum", "Overbought", (-5,1,6), 'Medium', 'Trend'),
]
P[('intraday','pwr','US')] = [
 ('BE', "Rose ~16% as CoreWeave's results lifted AI power names.", "Momentum", "Profit-taking; 8% daily swings", (-7,0,7), 'Speculative', 'Momentum check'),
 ('VRT', "Rose ~9% midday.", "Follow-through", "Profit-taking", (-4,0.3,4), 'Medium', 'Follow-through check'),
 ('TLN', "Rose ~6% on a new 750 MW capacity deal.", "Analyst updates", "Profit-taking", (-3.5,0.3,3.5), 'Medium', 'News follow-through'),
 ('OKLO', "Rose 6.5%; up 21% in five days.", "Momentum", "Cash burn; rate-sensitive", (-7,0,7), 'Speculative', 'Momentum check'),
 ('GEV', "Rose 2.8%; lagged other power names.", "Catch-up", "Higher yields", (-3,0.3,3), 'Medium', 'Range'),
]
P[('intraday','pwr','SGX')] = [
 ('544.SI', "Rose 8%.", "Next session", "Gives back gains", (-4,0,4), 'Speculative', 'Follow-through check'),
 ('BN4.SI', "Rose 1.1%.", "Next session", "Small range", (-1.6,0.2,1.6), 'Medium', 'Range'),
 ('U96.SI', "Rose 1%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('AJBU.SI', "Fell 1.4%.", "Next session", "Small range", (-1.2,0.2,1.2), 'Medium', 'Bounce watch'),
 ('DCRU.SI', "Flat.", "Next session", "Small range", (-1.5,0.3,1.5), 'Medium', 'Range'),
]

# ---------- Defence & industrials ----------
P[('long','def','US')] = [
 ('GE', "GE Aerospace: jet-engine services boom, revenue +16%, 10% off its high.", "Q4 results Jan 21", "Valuation (37x)", (-15,10,26), 'High', 'Quality'),
 ('RTX', "RTX: missiles and engines, revenue +11%, steady.", "Q4 results Jan 26", "Engine issues", (-12,10,24), 'High', 'Core defence'),
 ('LHX', "L3Harris: space and missile sensors, 27% off its high, 22% analyst upside.", "Golden Dome contracts", "Budget fights with a split government", (-15,12,30), 'Medium', 'Value'),
 ('HWM', "Howmet: jet-engine parts, revenue +29%, 23% off its high.", "Aerospace build rates", "Valuation (34x)", (-20,14,34), 'Medium', 'Growth at a discount'),
 ('NOC', "Northrop: B-21 and missile defence, about 18x earnings, 29% off its high; NASA lunar award.", "Golden Dome contracts", "Budget fights", (-15,11,28), 'Medium', 'Value'),
]
P[('long','def','SGX')] = [
 ('S63.SI', "ST Engineering: defence and aerospace, revenue +11%; oversold (RSI 33) and 15% off its high.", "Contract wins", "Valuation (25x)", (-10,12,24), 'High', 'Quality'),
 ('BS6.SI', "Yangzijiang Shipbuilding: about 8x earnings, revenue +36%, 22% analyst upside.", "New ship orders", "US port fees on Chinese ships", (-18,12,30), 'Medium', 'Value'),
 ('S59.SI', "SIA Engineering: aircraft maintenance, 24% off its high, 30% analyst upside.", "Air travel", "Revenue falling (-11%)", (-10,11,24), 'Medium', 'Recovery'),
 ('C52.SI', "ComfortDelGro: steady transport earnings at about 14x.", "Overseas contracts", "Slow growth", (-8,8,16), 'Medium', 'Steady'),
 ('H22.SI', "Hong Leong Asia: engines and building materials at about 9x earnings, 44% off its high.", "Results (Feb)", "China demand", (-25,22,50), 'Speculative', 'Deep value'),
]
P[('swing','def','US')] = [
 ('CAT', "Caterpillar is 43% off its high (RSI 34); Evercore ISI still sees ~40% upside. Rose 3.5% midday.", "Rebound", "Data-centre generator orders slowing", (-12,6,18), 'Medium', 'Oversold rebound'),
 ('AXON', "Down 25% in five days after a Q3 miss (RSI 25); 71% analyst upside. Rose 4.5% midday.", "Analyst updates", "More downgrades", (-18,6,22), 'Speculative', 'Post-earnings dip'),
 ('LMT', "Up 20% in a month; NASA lunar award.", "Contracts", "Budget fights", (-7,3,9), 'Medium', 'Trend'),
 ('BA', "Boeing 31% off its high (RSI 35); production recovering.", "Monthly deliveries", "Quality issues; staff cuts", (-10,5,15), 'Medium', 'Recovery'),
 ('AVAV', "AeroVironment 68% off its high; up 11% in five days.", "Drone and counter-drone orders", "Volatile; results Dec 2", (-18,6,22), 'Speculative', 'Rebound'),
]
P[('swing','def','SGX')] = [
 ('S63.SI', "ST Engineering rose 2.2% from oversold.", "Bounce", "Low volatility", (-4,3,8), 'High', 'Oversold rebound'),
 ('H22.SI', "Hong Leong Asia rose 3.4% from RSI 26.", "Bounce", "China demand", (-10,4,12), 'Speculative', 'Oversold rebound'),
 ('BS6.SI', "Yangzijiang rose 0.9% (RSI 37).", "Orders", "Trade fees", (-8,4,12), 'Medium', 'Support'),
 ('S59.SI', "SIA Engineering oversold (RSI 31).", "Air travel", "Slow growth", (-6,2,7), 'Medium', 'Oversold rebound'),
 ('C52.SI', "ComfortDelGro steady (RSI 56).", "Support", "Slow growth", (-4,1.5,5), 'Medium', 'Range'),
]
P[('intraday','def','US')] = [
 ('AXON', "Rose 4.5% from a 52-week low.", "Bounce", "More selling", (-5,0.5,5), 'Speculative', 'Bounce watch'),
 ('CAT', "Rose 3.5% (RSI 34).", "Bounce", "Rotation back to tech", (-3,0.3,3), 'Medium', 'Follow-through check'),
 ('HWM', "Rose 2.8% (RSI 65).", "Momentum", "Profit-taking", (-3,0.2,3), 'Medium', 'Momentum check'),
 ('KTOS', "Rose 1.4%.", "Drone contracts", "Volatile", (-4.5,0,4.5), 'Speculative', 'Range'),
 ('LMT', "Rose 0.7%.", "Defence bid", "Rotation into tech", (-2.2,0.2,2.2), 'Medium', 'Range'),
]
P[('intraday','def','SGX')] = [
 ('H22.SI', "Rose 3.4%.", "Next session", "Thin trading", (-3,0.3,3), 'Speculative', 'Bounce watch'),
 ('S63.SI', "Rose 2.2%.", "Next session", "Small range", (-1.5,0.3,1.8), 'Medium', 'Follow-through check'),
 ('BS6.SI', "Rose 0.9%.", "Next session", "Trade fees", (-2.5,0.2,2.5), 'Medium', 'Range'),
 ('C52.SI', "Fell 0.8%.", "Next session", "Small range", (-1,0.2,1), 'Medium', 'Range'),
 ('S59.SI', "Flat.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
]

# ---------- Energy (oil and gas) ----------
P[('long','nrg','US')] = [
 ('CVX', "Chevron: revenue +35%, about 13x earnings, 10% off its high.", "Hess integration; buybacks", "Oil drops further if an Iran deal is reached", (-16,8,24), 'High', 'Core energy'),
 ('XOM', "Exxon: steady cash flow, about 13x earnings.", "Buybacks", "Oil price drop", (-15,7,21), 'High', 'Core energy'),
 ('FANG', "Diamondback: low-cost Permian producer at about 8x earnings, 33% analyst upside.", "Buybacks", "Oil price drop (WTI ~$86)", (-22,13,33), 'Medium', 'Value'),
 ('LNG', "Cheniere: US gas exports on long contracts; less tied to oil. Up 5% in a month.", "New export capacity", "Gas price swings", (-15,9,26), 'Medium', 'Steady'),
 ('COP', "ConocoPhillips: about 12x earnings, revenue +29%.", "Buybacks", "Oil price drop", (-18,8,24), 'Medium', 'Value'),
]
P[('long','nrg','SGX')] = [
 ('5E2.SI', "Seatrium builds offshore rigs and wind platforms; 35% analyst upside.", "New orders", "Contract delays", (-15,12,28), 'Medium', 'Recovery'),
 ('BN4.SI', "Keppel: energy infrastructure and asset management.", "Asset sales", "Execution", (-12,10,22), 'Medium', 'Value'),
 ('RE4.SI', "Geo Energy: Indonesian coal at about 7x earnings.", "Coal prices", "Coal price drop", (-25,8,30), 'Speculative', 'Value'),
 ('5LY.SI', "Marco Polo Marine: offshore vessels, revenue +40% at about 12x earnings; jumped 9% on Nov 11.", "Results (Nov)", "Thin trading", (-25,10,35), 'Speculative', 'Growth value'),
 ('5WH.SI', "Rex International is in a long downtrend (-62% this year); no setup.", "None", "Further losses", (-30,-5,20), 'Speculative', 'Avoid'),
]
P[('swing','nrg','US')] = [
 ('MPC', "Marathon Petroleum is oversold (RSI 32); refiners gain when crude falls.", "Refining margins", "Margin drop", (-10,5,16), 'Medium', 'Oversold rebound'),
 ('PSX', "Phillips 66 oversold (RSI 35); also helped by cheaper crude.", "Refining margins", "Margin drop", (-10,5,15), 'Medium', 'Oversold rebound'),
 ('DVN', "Devon rose 2.7% from RSI 36; about 8.5x earnings, 38% analyst upside.", "Buybacks", "Oil price drop", (-12,4,15), 'Medium', 'Oversold rebound'),
 ('OXY', "Occidental oversold (RSI 30) after results.", "Results follow-through", "Debt; oil price", (-10,4,13), 'Medium', 'Post-earnings'),
 ('FANG', "Diamondback oversold (RSI 34).", "Buybacks", "Oil price drop", (-11,4,13), 'Medium', 'Oversold rebound'),
]
P[('swing','nrg','SGX')] = [
 ('5E2.SI', "Seatrium flat near support.", "Orders", "Delays", (-8,3,10), 'Medium', 'Support'),
 ('BN4.SI', "Keppel rose 1.1%.", "Asset sales", "Execution", (-5,3,8), 'Medium', 'Rebound'),
 ('5LY.SI', "Marco Polo Marine jumped 9.3%.", "Results", "Thin trading", (-10,3,12), 'Speculative', 'Momentum'),
 ('RE4.SI', "Geo Energy rose 1.9%.", "Coal prices", "Profit-taking", (-10,2,10), 'Speculative', 'Range'),
 ('5WH.SI', "Rex International: no setup.", "None", "Further losses", (-12,-2,8), 'Speculative', 'Avoid'),
]
P[('intraday','nrg','US')] = [
 ('HAL', "Rose 3.2% with oil services.", "Follow-through", "Oil", (-2.5,0.2,2.5), 'Medium', 'Momentum check'),
 ('DVN', "Rose 2.7%.", "Follow-through", "Oil", (-3,0.3,3), 'Medium', 'Momentum check'),
 ('LNG', "Rose 2.7%.", "Gas exports", "Profit-taking", (-3,0.2,3), 'Medium', 'Momentum check'),
 ('XOM', "Rose 0.8%; WTI near $86.", "Oil", "Iran-deal headlines", (-2,0.2,2), 'Medium', 'Range'),
 ('MPC', "RSI 32.", "Cheaper crude", "Margins", (-3,0.4,3), 'Medium', 'Bounce watch'),
]
P[('intraday','nrg','SGX')] = [
 ('5LY.SI', "Jumped 9.3%.", "Next session", "Profit-taking", (-4,0,4), 'Speculative', 'Follow-through check'),
 ('RE4.SI', "Rose 1.9%.", "Next session", "Small range", (-3,0.2,3), 'Speculative', 'Range'),
 ('BN4.SI', "Rose 1.1%.", "Next session", "Small range", (-1.6,0.2,1.6), 'Medium', 'Range'),
 ('5E2.SI', "Flat.", "Next session", "Small range", (-2,0.2,2), 'Medium', 'Range'),
 ('5WH.SI', "Penny stock in a downtrend; avoid.", "None", "Further losses", (-5,-1,4), 'Speculative', 'Avoid'),
]

IPO_LIST = [
 # sym, name, ipo_date, ipo_price, sector, status
 ('ANT','Anthropic (Nasdaq: ANT; roadshow launched Nov 10, range $70-78, 825M shares, up to ~$64B; pricing expected week of Nov 16)','2026-11-19',None,'ai','Roadshow'),
 ('BIAI','Bitari','2026-11-30',7.00,'ai','Expected'),
 ('FBLLU','Football Manager SPAC','2026-11-23',10.00,'fin','Expected'),
 ('YNTE','Primagrove ($4-6 range)','2026-11-16',None,'fin','Expected'),
 ('VVVV','vVardis ($21-24 range, ~$214M; dental tech; NYSE, this week)','2026-11-13',None,'hc','Expected'),
 ('WWB','Windward Bio ($16-18 range, ~$175M; Nasdaq, this week)','2026-11-13',None,'hc','Expected'),
 ('RZRA','Rezera ($11-13 range, ~$200M; Nasdaq, this week)','2026-11-12',None,'hc','Expected'),
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
 ('2026-11-11T05:42','CRWV NBIS', "Via search excerpt: reads CoreWeave's results as good news for Nebius and other neoclouds, quoting '10x as much qualified demand as available capacity', strong interest in 2028 capacity and several price rises this year."),
 ('2026-11-10T10:50','GE', "Via search excerpt: highlights SoftBank's CFO denying it defaulted on turbine orders, as had been claimed online, and says this matches what GE's management has said."),
 ('2026-11-09T15:12','NVDA TSM', "Via tracker: notes Taiwan's index jumped about 5% as AI stocks rebounded, joking that markets were impressed by Jensen Huang's energy."),
 ('2026-11-09T11:28','NVDA', "Via tracker: backs Nvidia and Huang through the personal scrutiny, saying many public figures have faced similar attention."),
 ('2026-11-08T17:35','COHR LITE POET', "Via tracker: calls the 'AI bubble' label lazy. Memory makers with price floors and optical firms near net cash look cheap; leveraged neoclouds and AI-lab valuations are more bubble-prone."),
 ('2026-11-08T01:11','MU', "Via tracker: says old memory contract renegotiations don't apply now, since Micron's new deals carry price floors and binding commitments."),
 ('2026-11-07T11:36','POET', "Via search excerpt: says the market hit 'extreme dislocation', with POET trading about $98M below its net cash, and argues some bottleneck suppliers keep demand visibility even if hyperscaler capex is cut."),
 ('2026-11-06T07:24','NBIS SPCX', "Via search excerpt: says everyone is a long-term investor until volatility hits; still thinks Rocket Lab could be the next SpaceX and Nebius the next hyperscaler."),
]

EVENTS = [
 ('2026-11-10','Macro','Hot CPI: +0.4% (core +0.3%)', "Both above forecasts. 10-yr yield ~5.0%; Dec hike odds ~90% (CME). S&P -0.4%, Nasdaq -0.7%."),
 ('2026-11-10','AI','Nvidia -5.5% on shareholder lawsuit', "Suit over the CEO's ties to a suspected spy and a report that $7.5B of chips reached China. Down 18% in five days."),
 ('2026-11-10','AI','CoreWeave beats and raises', "Q3 revenue $3.66B (+168%); 2026 revenue guide $13.0-13.3B; capex $37-39B. TSMC October sales +60% y/y."),
 ('2026-11-10','IPO','Anthropic launches IPO roadshow', "Range $70-78, 825M shares, up to ~$64B raised and ~$1.4T value at the top."),
 ('2026-11-11','Macro','AI rally: S&P +1.3%, Nasdaq +1.6%', "S&P 7,619; Nasdaq 25,466 erased its post-election losses. VIX 17.5. Bond market shut for Veterans Day. Fed's Bowman says more hikes may be needed."),
 ('2026-11-11','AI','CoreWeave +25%; chips, memory and optics rebound', "Nvidia +2.9% to $173.73 despite a Baird downgrade to Neutral; Micron, Sandisk, Seagate, Lumentum up 10%+ midday."),
 ('2026-11-11','Power','Bloom +16%; Talen signs 750 MW deal', "Talen's seven-year capacity deal is worth ~$100M a year. AI power names rallied with CoreWeave."),
 ('2026-11-11','SGX','STI +0.6% to 5,290', "Venture +5.2% on a 22% Q3 profit rise (RHB target S$21.97); UMS +9%; DBS +0.9%, OCBC +0.8%."),
 ('2026-11-12','Mixed','Nebius, Applied Materials, Cisco, Nu, Accelevation report', "Nebius before the open; Applied Materials and Cisco after the close. US jobless claims 8:30 ET. Rezera, Windward Bio and vVardis IPOs expected this week."),
 ('2026-11-17','AI','Nvidia Q3 results', "The main AI-demand checkpoint, with a lawsuit, the CEO probe and a Baird downgrade in the background. Klarna also reports."),
 ('2026-11-18','IPO','Anthropic IPO pricing (expected)', "Pricing expected the week of Nov 16, trading on Nasdaq as ANT; exact date not confirmed."),
 ('2026-11-25','SGX','IHH Q3 results', ""),
 ('2026-11-26','Macro','US Thanksgiving', "US stock market closed."),
 ('2026-12-09','Macro','Fed rate decision (Dec 8-9)', "A 25 bp hike is ~90% priced; Goldman and UBS expect another in March."),
]
