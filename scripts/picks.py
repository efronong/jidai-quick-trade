# Analyst picks for 2026-11-11 (snapshot: US close Nov 10, SGX close Nov 10). Fields: sym, thesis, catalyst, risk, (low, base, high) % expected move, conviction, setup
# Horizons: long = 12 months, swing = ~4 weeks, intraday = rest of session (US) / next session (SGX), ipo = 6 months.
# Context: Nov 10: October CPI +0.4% (core +0.3%), both above forecasts. 10-yr yield +14 bp to ~5.0%. Dec hike odds ~90% (CME, per WSJ); Waller says 50 bp should be considered.
# S&P -0.4% to 7,521, Nasdaq -0.7%, Dow -0.3%. Nvidia -5.5% (second day) on a shareholder lawsuit over the CEO's ties to a suspected spy and a report that $7.5B of its chips reached China.
# Hims -16.5% after cutting its EBITDA outlook. CoreWeave beat and raised after the close (~+2% late). TSMC October sales +60% y/y. STI +1.5% to 5,259 (AEM +10%, Yangzijiang +5.5%).
# Anthropic set its IPO range at $70-78 (825M shares, up to ~$64B). Nov 11 is Veterans Day: US stocks open, bond market shut.
P = {}

# ---------- AI & chips ----------
P[('long','ai','US')] = [
 ('TSM', "Makes almost every leading AI chip. October sales +60% y/y and +15% m/m; about 17x forward earnings, 18% below its high. Rose 2% while chips fell.",
  "November sales (~Dec 10); Q4 results Jan 14", "Taiwan geopolitics; AI capex cuts", (-18,18,40), 'High', 'Core holding'),
 ('NVDA', "Revenue +106% at about 10.5x forward earnings, the cheapest big AI chip stock. Down 18% in five days (RSI 19), but now carries legal and export-control risk, not just a headline.",
  "Q3 results Nov 17", "Shareholder lawsuit; report that $7.5B of chips reached China; board probe of the CEO", (-30,20,50), 'Medium', 'Quality at a discount, higher risk'),
 ('AVGO', "Custom AI chips plus networking: revenue +86% at about 17x forward earnings, 31% below its high. Rose 4% on a down day for chips.",
  "Q4 results Dec 9", "Lumpy custom-chip orders; customer concentration", (-22,20,45), 'Medium', 'Pullback in a leader'),
 ('MU', "Memory is still the tightest part of AI servers: revenue +379% at about 3.4x forward earnings, 40% off its high. New contracts carry price floors.",
  "FQ1 results Dec 23", "Peak-cycle earnings; memory falls hard when prices turn", (-38,22,62), 'Medium', 'Cycle leader'),
 ('COHR', "Record quarter and a ~$20B five-year optics deal; 50% below its high at about 13x forward earnings. Gave back 4.6% today.",
  "First $3B quarter targeted by FY27 end", "8% daily swings; capex keeps rising", (-32,24,62), 'Medium', 'Beat-and-sold'),
]
P[('long','ai','SGX')] = [
 ('AWX.SI', "AEM jumped 10% to S$6.85 as Singapore tech rebounded, but is still 39% below its high and up ~300% this year; analysts rate it Strong Buy.",
  "Q3 business update (Nov)", "One large customer; 7% daily swings", (-38,18,55), 'Medium', 'SGX AI leader'),
 ('558.SI', "UMS makes precision parts for chip-equipment makers: revenue +29%, 40% off its high, about 18x earnings. Rose 4% today.",
  "Q3 results mid-November; Applied Materials results Nov 12", "Tied to Applied Materials spending", (-30,15,45), 'Medium', 'Equipment supplier'),
 ('5DD.SI', "Micro-Mechanics makes precision tools for chip assembly and test: revenue +45%, 42% off its high.",
  "Q1 FY27 results (Nov)", "Small and thinly traded", (-24,14,36), 'Medium', 'Growth at a discount'),
 ('E28.SI', "Frencken builds modules for chip and medical equipment. 49% off its high at about 15x earnings.",
  "Q3 business update (Nov)", "Flat revenue so far this year", (-25,14,38), 'Medium', 'Recovery'),
 ('V03.SI', "Venture builds electronics for chip-equipment, medical and AI-server makers. Net cash, about 16x earnings, low volatility.",
  "Q3 business update (Nov)", "Slow growth (+7%)", (-12,10,22), 'Medium', 'Steady value'),
]
P[('swing','ai','US')] = [
 ('NVDA', "RSI 19 and down 18% in five days, a week before results. Oversold, but each new legal or China headline can push it lower first.",
  "Q3 results Nov 17", "More lawsuit or export-control news", (-18,6,20), 'Speculative', 'Oversold into earnings'),
 ('LITE', "Marvell is buying Lumentum for 4.5 Marvell shares each. At today's prices that is worth about 19% more than LITE's price.",
  "Spread narrows if MRVL recovers", "Regulatory delay (incl. China); MRVL falls again", (-15,7,20), 'Medium', 'Merger spread'),
 ('AVGO', "Rose 4% on a weak tape (RSI 48); the AI name least tied to the Nvidia story.",
  "Q4 results Dec 9", "Rates at 5% hit growth multiples", (-12,5,15), 'Medium', 'Relative strength'),
 ('CRDO', "Credo: revenue +115% at about 13x forward earnings, 57% off its high; analysts see 119% upside.",
  "Q2 results Nov 30", "Customer concentration; 8% daily swings", (-25,10,32), 'Speculative', 'Oversold growth'),
 ('CRWV', "CoreWeave beat Q3 (revenue $3.66B, smaller loss) and raised 2026 revenue guidance to $13.0-13.3B; 65% off its high.",
  "Post-results analyst updates", "Capex raised to $37-39B; heavy interest costs", (-25,8,30), 'Speculative', 'Beat and raise'),
]
P[('swing','ai','SGX')] = [
 ('AWX.SI', "AEM bounced 10% from oversold; still down 39% in a month.",
  "Q3 update; US chips stabilising", "Bounce fades if Nvidia keeps falling", (-20,6,26), 'Speculative', 'Oversold rebound'),
 ('558.SI', "UMS rose 4% (RSI 31); analysts see about 90% upside.", "Q3 results mid-November", "Chip-equipment sentiment", (-18,6,22), 'Speculative', 'Oversold rebound'),
 ('E28.SI', "Frencken rose 3.5% from RSI 30.", "Q3 business update (Nov)", "No clear catalyst before results", (-15,5,17), 'Speculative', 'Oversold rebound'),
 ('5DD.SI', "Micro-Mechanics rose 3.2%; RSI 36.", "Q1 FY27 results (Nov)", "Thin order book", (-12,4,14), 'Medium', 'Rebound'),
 ('V03.SI', "Venture is the least volatile SGX tech name (RSI 38).", "Q3 business update (Nov)", "Flat revenue", (-8,4,10), 'Medium', 'Range trade'),
]
P[('intraday','ai','US')] = [
 ('NVDA', "Fell 5.5% on 3x normal volume (RSI 19); briefly below $4T market value. Watch for a bounce or more lawsuit news.",
  "Oversold bounce", "More China-chip headlines", (-4,0.5,4.5), 'Speculative', 'Headline risk'),
 ('CRWV', "Beat and raised after the close; late trading swung between gains and losses.", "Results reaction", "Capex and debt worries", (-9,1,10), 'Speculative', 'Earnings reaction'),
 ('NBIS', "Fell 5.3%; reports Q3 on Nov 12. Rose ~2% late with CoreWeave.", "CoreWeave read-across", "Pre-earnings selling", (-6,0.5,6), 'Speculative', 'Read-across'),
 ('TSM', "October sales +60% y/y; rose 2% while chips fell.", "Follow-through", "Rates at 5%", (-2.5,0.5,3), 'Medium', 'Relative strength'),
 ('AVGO', "Rose 3.9% against the selloff.", "Follow-through", "Profit-taking", (-3,0.3,3), 'Medium', 'Relative strength'),
]
P[('intraday','ai','SGX')] = [
 ('AWX.SI', "Jumped 10% on Nov 10 but faded from a 12% intraday high; Nvidia fell 5.5% overnight.", "Holds the gap", "Gives back gains", (-6,0,5), 'Speculative', 'Gap-fade watch'),
 ('558.SI', "Rose 4%.", "Next session", "US chip weakness", (-4,0,3.5), 'Speculative', 'Follow-through check'),
 ('E28.SI', "Rose 3.5% from oversold.", "Next session", "Follows US chip equipment", (-3.5,0.3,3.5), 'Medium', 'Follow-through check'),
 ('5DD.SI', "Rose 3.2%.", "Next session", "Thin trading", (-3,0.3,3), 'Medium', 'Range'),
 ('V03.SI', "Rose 1.7%; low volatility.", "Next session", "Small range", (-1.8,0.3,1.8), 'Medium', 'Range'),
]

# ---------- Health ----------
P[('long','hc','US')] = [
 ('LLY', "Obesity-drug leader: revenue +39%, at a new high (+33% this year). Little analyst upside left, so the base case is modest.",
  "Orforglipron launch; Q4 results (Feb)", "Drug-price policy under the new Congress", (-16,8,25), 'High', 'Defensive growth'),
 ('ARGX', "argenx: revenue +52% from its immune-disease drug Vyvgart, 8% off its high, 18% analyst upside.",
  "New indications in 2027", "Competition in myasthenia gravis", (-15,11,30), 'Medium', 'Growth leader'),
 ('MDGL', "Madrigal's liver drug Rezdiffra is growing fast (revenue +50%); 28% off its high with 59% analyst upside.",
  "Script data; EU rollout", "Competition from GLP-1 drugs", (-22,20,45), 'Medium', 'Oversold growth'),
 ('INSM', "Insmed's lung drug launch drives revenue +268%; up 21% in a month but still 44% off its high, 63% analyst upside.",
  "Brensocatib launch numbers", "Expensive on near-term earnings", (-30,18,48), 'Medium', 'Launch story'),
 ('ALNY', "Alnylam is 68% off its high at about 14x forward earnings (RSI 15); analysts see 98% upside.",
  "Amvuttra script data", "Trend still down", (-30,18,50), 'Speculative', 'Deep value'),
]
P[('long','hc','SGX')] = [
 ('Q0F.SI', "IHH runs hospitals across Asia; analysts see 37% upside.", "Q3 results Nov 25", "Currency swings", (-12,12,25), 'Medium', 'Regional leader'),
 ('C2PU.SI', "Parkway Life REIT: steady hospital and nursing-home rents, 6% off its high.", "Dividend", "Rates near 5% in the US", (-8,7,15), 'High', 'Income'),
 ('AP4.SI', "Riverstone makes cleanroom and medical gloves at about 14x earnings with 42% analyst upside.", "Q3 results (Nov)", "Glove price competition", (-15,12,30), 'Medium', 'Value'),
 ('BSL.SI', "Raffles Medical: Singapore hospital group, 21% off its high and in a mild uptrend (RSI 65).", "Results (Feb)", "Shrinking revenue (-7%)", (-10,8,18), 'Medium', 'Recovery'),
 ('H02.SI', "Haw Par (Tiger Balm) trades near 10x earnings with a large cash and investment pile.", "Results (Feb)", "Revenue down 8%", (-12,6,16), 'Medium', 'Value'),
]
P[('swing','hc','US')] = [
 ('INSM', "Up 14% in five days and rose 3% on a down day (RSI 77).", "Launch numbers", "Overbought", (-10,4,14), 'Medium', 'Momentum'),
 ('MDGL', "Up 9% in five days; 59% analyst upside.", "Script data", "Rotation back to tech", (-12,6,18), 'Medium', 'Rebound'),
 ('ALNY', "Deeply oversold (RSI 15) and 68% off its high.", "Amvuttra script data", "Trend still down", (-15,7,22), 'Speculative', 'Oversold rebound'),
 ('LLY', "At a new high again; leadership while growth stocks sell off.", "Orforglipron news", "Money rotating back into chips", (-8,3,10), 'High', 'Relative strength'),
 ('ARGX', "Up 8% in five days (RSI 67).", "Momentum", "Overbought", (-8,4,12), 'Medium', 'Trend'),
]
P[('swing','hc','SGX')] = [
 ('C2PU.SI', "Parkway Life REIT: lowest-volatility name in the group.", "Dividend", "Rates", (-4,2,6), 'High', 'Range'),
 ('BSL.SI', "Raffles Medical is in a mild uptrend (RSI 65).", "Momentum", "Low volume", (-5,2.5,8), 'Medium', 'Trend'),
 ('Q0F.SI', "IHH ahead of Q3 results.", "Q3 results Nov 25", "Results miss", (-6,3,9), 'Medium', 'Pre-earnings'),
 ('AP4.SI', "Riverstone rose 1.4%; large analyst upside.", "Q3 results (Nov)", "Glove prices", (-8,3,10), 'Medium', 'Support'),
 ('QC7.SI', "Q&M Dental is very oversold (RSI 7).", "Bounce", "Small cap", (-8,3,10), 'Speculative', 'Oversold rebound'),
]
P[('intraday','hc','US')] = [
 ('HIMS', "Fell 16.5% on almost 5x volume after cutting its 2026 EBITDA outlook, though revenue rose 49%.", "Oversold bounce (RSI 26)", "Analyst downgrades", (-8,0.5,8), 'Speculative', 'Post-earnings flush'),
 ('CRSP', "Fell 9.8% on 3x volume.", "Bounce", "More selling", (-6,0.3,6), 'Speculative', 'Bounce watch'),
 ('MRNA', "Fell 6.8% from near its high; still far above analyst targets.", "Dip buying", "Analysts see 38% downside to targets", (-6,0,6), 'Speculative', 'Extended'),
 ('INSM', "Rose 3% against the market (RSI 77).", "Momentum", "Profit-taking", (-3.5,0.3,3.5), 'Medium', 'Momentum check'),
 ('LLY', "New high on Nov 10.", "Momentum", "Rotation into tech", (-2.5,0.3,2.5), 'Medium', 'Relative strength'),
]
P[('intraday','hc','SGX')] = [
 ('C2PU.SI', "Steady REIT.", "Next session", "Small range", (-1,0.2,1), 'Medium', 'Range'),
 ('BSL.SI', "Flat; mild uptrend.", "Next session", "Small range", (-1.5,0.3,1.5), 'Medium', 'Relative strength'),
 ('H02.SI', "Steady.", "Next session", "Small range", (-1.5,0.3,1.5), 'Medium', 'Range'),
 ('Q0F.SI', "Rose 0.8%.", "Next session", "Malaysia market swings", (-2,0.2,2), 'Medium', 'Range'),
 ('AP4.SI', "Rose 1.4%.", "Next session", "Thin trading", (-2,0.2,2), 'Medium', 'Range'),
]

# ---------- Finance ----------
P[('long','fin','US')] = [
 ('JPM', "Best-run US bank, 6% off its high at about 13x forward earnings. Higher rates support interest income.", "Q4 results Jan 14", "Credit cycle", (-15,8,22), 'High', 'Core holding'),
 ('V', "Visa: steady growth (+13%), near its high; little AI exposure.", "Holiday spending", "Regulation of card fees", (-12,6,18), 'High', 'Defensive growth'),
 ('GS', "Trading and deal-making boom, about 12x forward earnings, 21% off its high. A record Anthropic IPO (up to ~$64B) would be a big fee win.",
  "Anthropic IPO (Goldman co-leads)", "Market volatility hits deals", (-20,10,28), 'Medium', 'Cyclical value'),
 ('SE', "Sea: Q3 revenue +43% to $8.6B beat, but EPS missed on higher loan-loss provisions; new $1B buyback. About 16x forward earnings, 50% off its high.",
  "Q4 results (Mar)", "Rising credit costs at Monee; competition", (-30,22,55), 'Medium', 'Oversold growth'),
 ('NU', "Nubank: revenue +52% at about 11x forward earnings, 36% off its high.", "Q3 results Nov 12", "Brazil credit and currency", (-30,22,55), 'Medium', 'Growth at a discount'),
]
P[('long','fin','SGX')] = [
 ('D05.SI', "DBS kept its 81-cent quarterly dividend and says interest income has bottomed; 10% off its high.",
  "Q4 results (Feb)", "Margins if rates fall; stronger SGD", (-10,8,16), 'High', 'Income leader'),
 ('O39.SI', "OCBC was the only local bank to beat in Q3 and raised loan-growth guidance; rose 3.3% today.",
  "Q4 results (Feb)", "Margin fell 18 bp to 1.66%", (-10,7,15), 'Medium', 'Income'),
 ('U11.SI', "UOB missed Q3 and cut its margin guidance; RSI 18, 17% off its high.", "Recovery in fees", "More credit provisions", (-12,8,18), 'Medium', 'Oversold income'),
 ('AIY.SI', "iFAST: fintech platform, revenue +23%, 27% off its high with 43% analyst upside.", "HK pension business", "Market-driven volumes", (-18,18,38), 'Medium', 'Growth'),
 ('S68.SI', "SGX benefits from high trading volumes; from Jan 2027 its RegCo takes over IPO prospectus reviews.", "Monthly volume data", "Already priced (25x earnings)", (-12,7,18), 'Medium', 'Volatility winner'),
]
P[('swing','fin','US')] = [
 ('NU', "Oversold (RSI 25) into Q3 results Nov 12.", "Results", "Brazil credit", (-15,6,20), 'Medium', 'Pre-earnings'),
 ('SE', "Fell only 1.5% after a revenue beat and EPS miss; new $1B buyback.", "Buyback; analyst updates", "Credit costs", (-12,5,16), 'Medium', 'Post-earnings'),
 ('GS', "Anthropic set an IPO range of $70-78; pricing is expected next week.", "Deal fees", "Volatility", (-8,4,12), 'Medium', 'Deal pipeline'),
 ('HOOD', "Down 26% in a month (RSI 25); retail access to the Anthropic IPO runs partly through Robinhood.", "Anthropic IPO demand; October data", "Crypto weakness; higher rates", (-18,6,22), 'Speculative', 'Oversold rebound'),
 ('KKR', "Rose 2.8% to an RSI of 68; up 10% in a month.", "Momentum", "Private-credit worries", (-8,3,10), 'Medium', 'Trend'),
]
P[('swing','fin','SGX')] = [
 ('D05.SI', "DBS is oversold (RSI 23) and rose 1.3%.", "Dividend support", "Margin worries", (-4,3,7), 'High', 'Oversold income'),
 ('U11.SI', "UOB RSI 18 after its Q3 miss.", "Rebound", "Further downgrades", (-5,3,8), 'Medium', 'Oversold rebound'),
 ('O39.SI', "OCBC rose 3.3% as banks bounced.", "Post-results recovery", "Margin squeeze", (-4,2,6), 'Medium', 'Rebound'),
 ('AIY.SI', "iFAST is holding up (RSI 51).", "Momentum", "Market-driven", (-8,3,10), 'Medium', 'Range'),
 ('S68.SI', "SGX benefits when markets are volatile.", "Volume data", "Valuation", (-5,2,7), 'Medium', 'Volatility winner'),
]
P[('intraday','fin','US')] = [
 ('SE', "Fell 1.5% after Q3 (revenue beat, EPS miss).", "Buyback support", "Credit-cost worries", (-5,0.5,5), 'Medium', 'Earnings reaction'),
 ('UPST', "Fell 8.3% as yields rose to 5%.", "Bounce", "Rate-sensitive lender", (-6,0,6), 'Speculative', 'Rate sensitivity'),
 ('HOOD', "Fell 2.4% (RSI 25).", "Anthropic IPO interest", "Crypto weakness", (-4,0.3,4), 'Speculative', 'Bounce watch'),
 ('COIN', "Fell 2.9% (RSI 22).", "Crypto bounce", "More crypto selling", (-5,0,5), 'Speculative', 'Crypto beta'),
 ('JPM', "Flat; banks held up as yields rose.", "Higher rates", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
]
P[('intraday','fin','SGX')] = [
 ('D05.SI', "Rose 1.3% from RSI 23.", "Next session", "Market-wide risk-off", (-1.2,0.3,1.4), 'High', 'Follow-through check'),
 ('U11.SI', "Rose 1%; still oversold.", "Next session", "Trend down", (-1.5,0.3,1.6), 'Medium', 'Bounce watch'),
 ('O39.SI', "Rose 3.3%.", "Next session", "Profit-taking", (-1.5,0,1.2), 'Medium', 'Follow-through check'),
 ('S68.SI', "Rose 0.5%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('AIY.SI', "Rose 1.3%.", "Next session", "Risk-off", (-2,0.3,2), 'Medium', 'Range'),
]

# IPO tab (6-month view), all markets
P[('ipo','all','US')] = [
 ('SPCX', "SpaceX listed in June at $135 and trades about 6% above that, 32% under its high. Analysts see large upside.",
  "xAI/GPU news; NASA lunar awards; lock-up expiries", "Valuation, Musk headlines and data-centre policy", (-35,12,45), 'Medium', 'Mega-cap IPO'),
 ('CHYM', "Chime (IPO $27) trades about 20% above its IPO price, near its high, up 15% in five days.",
  "Member growth", "Fintech credit cycle", (-15,10,28), 'Medium', 'Post-IPO uptrend'),
 ('KLAR', "Klarna (IPO $40) is 67% below its IPO price at about 17x forward earnings; revenue +27%.",
  "Q3 results Nov 17", "Buy-now-pay-later credit losses", (-22,15,40), 'Speculative', 'Deep value'),
 ('ACCV', "Accelevation (IPO $18) makes electrical gear for data centres: revenue +80% at about 10x forward earnings. Fell 12% today to 41% below its IPO price.",
  "First results as a public company Nov 12", "Data-centre policy risk; 9% daily swings", (-40,10,50), 'Speculative', 'Post-IPO value'),
 ('FIG', "Figma: revenue +43% with AI products, but 44% below its IPO price after a weak reaction to results.",
  "AI product monetisation", "Software multiples falling; Anthropic's new office tools", (-30,8,38), 'Speculative', 'Post-earnings dip'),
]

# ---------- Power & grid (data-center power) ----------
P[('long','pwr','US')] = [
 ('GEV', "GE Vernova: gas turbines and grid gear sold out for years, revenue +27%. 32% off its high; fell 3.9% today.", "Q4 results Jan 27", "Data-centre policy; valuation (30x)", (-25,15,40), 'High', 'Quality at a discount'),
 ('CEG', "Constellation beat Q3 and raised 2026 guidance to $12.50-12.80; still 29% off its high.", "Buyback update; new long-term power deals", "Data-centre politics; PJM rules", (-22,16,38), 'High', 'Beat and raise'),
 ('ETN', "Eaton: electrical gear for data centres and utilities, 23% off its high at about 21x earnings.", "Q4 results Feb 2", "Data-centre orders slowing", (-20,13,33), 'Medium', 'Quality at a discount'),
 ('PWR', "Quanta builds the grid: revenue +57%, 26% off its high.", "Utility capex plans", "Data-centre policy", (-25,13,36), 'Medium', 'Grid builder'),
 ('VRT', "Vertiv: data-centre cooling and power, revenue +61% at about 19x forward earnings, 48% off its high. CoreWeave raised capex to $37-39B.", "Order backlog updates", "Most exposed to a data-centre slowdown", (-35,20,55), 'Medium', 'Oversold growth'),
]
P[('long','pwr','SGX')] = [
 ('BN4.SI', "Keppel: power, data centres and asset management, about 16x earnings with 30% analyst upside; rose 3.4% today.", "Asset sales", "Execution", (-12,12,25), 'Medium', 'Value'),
 ('U96.SI', "Sembcorp: power and renewables at about 9x earnings.", "New contracts", "Power prices", (-12,7,18), 'Medium', 'Value'),
 ('DCRU.SI', "Digital Core REIT: US data-centre REIT, about 10x earnings with 52% analyst upside.", "Leasing news", "Tenant concentration; US rates at 5%", (-12,12,28), 'Medium', 'Deep value'),
 ('AJBU.SI', "Keppel DC REIT: data-centre rents, 10% off its high.", "Dividend", "Rates", (-10,7,17), 'Medium', 'Income'),
 ('544.SI', "CSE Global: electrification and data-centre work, about 10x earnings, 52% off its high; rose 4% today.", "New orders", "Small and volatile", (-30,18,50), 'Speculative', 'Recovery'),
]
P[('swing','pwr','US')] = [
 ('CEG', "Beat-and-raise last week; FY consensus still sits below the new guidance. Fell 3% today with power names.", "Analyst target updates", "Data-centre politics; higher yields", (-12,6,18), 'Medium', 'Post-earnings drift'),
 ('NRG', "Strong Q3 and a $4B asset sale; about 10x earnings with 71% analyst upside.", "Analyst updates", "Texas data-centre proposal", (-15,7,22), 'Medium', 'Post-earnings drift'),
 ('VST', "Raised its 2026 outlook on Nov 6; 30% off its high (RSI 36).", "Analyst updates", "Texas data-centre proposal", (-14,6,20), 'Medium', 'Post-earnings drift'),
 ('GEV', "Down 13% in five days on 1.5x volume (RSI 38).", "Rebound", "Rates; data-centre politics", (-12,5,16), 'Medium', 'Oversold quality'),
 ('BE', "Bloom: down 13% in five days (RSI 37) despite new Google fuel-cell work.", "New orders", "7% daily swings", (-20,7,26), 'Speculative', 'News vs price'),
]
P[('swing','pwr','SGX')] = [
 ('BN4.SI', "Keppel rose 3.4% from RSI 30.", "Asset-sale news", "Execution", (-5,3,8), 'Medium', 'Rebound'),
 ('U96.SI', "Sembcorp rose 1%; RSI 35.", "Contracts", "Power prices", (-5,2,7), 'Medium', 'Range'),
 ('544.SI', "CSE Global rose 4% but faded from a 5% intraday gain.", "Bounce", "Small cap", (-18,5,20), 'Speculative', 'Oversold rebound'),
 ('DCRU.SI', "Digital Core REIT fell 2.2% (RSI 56).", "Support", "US data-centre worries", (-6,2,8), 'Medium', 'Range'),
 ('AJBU.SI', "Keppel DC REIT is in an uptrend (RSI 77).", "Momentum", "Overbought", (-5,1,6), 'Medium', 'Trend'),
]
P[('intraday','pwr','US')] = [
 ('OKLO', "Fell 6.7%.", "Bounce", "Cash burn; rate-sensitive", (-7,0,7), 'Speculative', 'Momentum check'),
 ('GEV', "Fell 3.9% on 1.5x volume.", "Bounce", "More selling", (-3.5,0.3,3.5), 'Medium', 'Bounce watch'),
 ('BE', "Fell 4.4%.", "Bounce", "7% daily swings", (-6,0,6), 'Speculative', 'Momentum check'),
 ('CEG', "Fell 3%.", "Bounce", "Higher yields", (-3,0.3,3), 'Medium', 'Bounce watch'),
 ('NEE', "Dipped 0.7% as yields rose (RSI 74).", "Defensive bid", "Rates at 5%", (-1.8,0,1.8), 'Medium', 'Range'),
]
P[('intraday','pwr','SGX')] = [
 ('BN4.SI', "Rose 3.4%.", "Next session", "Profit-taking", (-1.8,0.2,1.8), 'Medium', 'Follow-through check'),
 ('U96.SI', "Rose 1%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('544.SI', "Rose 4%.", "Next session", "Gives back gains", (-5,0,5), 'Speculative', 'Follow-through check'),
 ('AJBU.SI', "Rose 0.9%.", "Next session", "Small range", (-1.2,0.2,1.2), 'Medium', 'Range'),
 ('DCRU.SI', "Fell 2.2%.", "Next session", "Small range", (-1.5,0.3,1.5), 'Medium', 'Bounce watch'),
]

# ---------- Defence & industrials ----------
P[('long','def','US')] = [
 ('GE', "GE Aerospace: jet-engine services boom, revenue +16%, 11% off its high.", "Q4 results Jan 21", "Valuation (36x)", (-15,11,28), 'High', 'Quality'),
 ('RTX', "RTX: missiles and engines, revenue +11%, steady; rose 2% today.", "Q4 results Jan 26", "Engine issues", (-12,10,24), 'High', 'Core defence'),
 ('LHX', "L3Harris: space and missile sensors, 27% off its high, 22% analyst upside.", "Golden Dome contracts", "Budget fights with a split government", (-15,12,30), 'Medium', 'Value'),
 ('HWM', "Howmet: jet-engine parts, revenue +29%, 25% off its high.", "Aerospace build rates", "Valuation (33x)", (-20,15,36), 'Medium', 'Growth at a discount'),
 ('NOC', "Northrop: B-21 and missile defence, about 18x earnings, 29% off its high; NASA lunar award.", "Golden Dome contracts", "Budget fights", (-15,11,28), 'Medium', 'Value'),
]
P[('long','def','SGX')] = [
 ('S63.SI', "ST Engineering: defence and aerospace, revenue +11%; oversold (RSI 22) and 17% off its high.", "Contract wins", "Valuation (25x)", (-10,12,24), 'High', 'Quality'),
 ('BS6.SI', "Yangzijiang Shipbuilding: about 8x earnings, revenue +36%; top STI gainer today (+5.5%).", "New ship orders", "US port fees on Chinese ships", (-18,12,30), 'Medium', 'Value'),
 ('S59.SI', "SIA Engineering: aircraft maintenance, 24% off its high, 30% analyst upside.", "Air travel", "Revenue falling (-11%)", (-10,11,24), 'Medium', 'Recovery'),
 ('C52.SI', "ComfortDelGro: steady transport earnings at about 14x.", "Overseas contracts", "Slow growth", (-8,8,16), 'Medium', 'Steady'),
 ('H22.SI', "Hong Leong Asia: engines and building materials at about 8x earnings, 46% off its high.", "Results (Feb)", "China demand", (-25,22,50), 'Speculative', 'Deep value'),
]
P[('swing','def','US')] = [
 ('CAT', "Caterpillar is 45% off its high (RSI 26) and fell 2.4% today.", "Rebound", "Data-centre generator orders slowing", (-12,6,18), 'Medium', 'Oversold rebound'),
 ('AXON', "Down 27% in five days after a Q3 miss (RSI 24); 79% analyst upside.", "Analyst updates", "More downgrades", (-18,6,22), 'Speculative', 'Post-earnings dip'),
 ('LMT', "Rose 2.5% as money moved to defensives; NASA lunar award.", "Contracts", "Budget fights", (-7,3,9), 'Medium', 'Defensive bid'),
 ('BA', "Boeing 31% off its high (RSI 31); production recovering.", "Monthly deliveries", "Quality issues; staff cuts", (-10,5,15), 'Medium', 'Recovery'),
 ('AVAV', "AeroVironment 69% off its high; RSI 54.", "Drone and counter-drone orders", "Volatile; results Dec 2", (-18,6,22), 'Speculative', 'Rebound'),
]
P[('swing','def','SGX')] = [
 ('S63.SI', "ST Engineering rose 2.8% from extreme oversold.", "Bounce", "Low volatility", (-4,3,8), 'High', 'Oversold rebound'),
 ('BS6.SI', "Yangzijiang rose 5.5%.", "Orders", "Trade fees", (-8,4,12), 'Medium', 'Rebound'),
 ('H22.SI', "Hong Leong Asia rose 3% from RSI 24.", "Bounce", "China demand", (-10,4,12), 'Speculative', 'Oversold rebound'),
 ('S59.SI', "SIA Engineering steady.", "Air travel", "Slow growth", (-6,2,7), 'Medium', 'Range'),
 ('C52.SI', "ComfortDelGro steady (RSI 63).", "Support", "Slow growth", (-4,1.5,5), 'Medium', 'Range'),
]
P[('intraday','def','US')] = [
 ('HII', "Rose 3.1% (RSI 67).", "Defence bid", "Profit-taking", (-2.5,0.3,2.5), 'Medium', 'Momentum check'),
 ('LMT', "Rose 2.5%.", "Defence bid", "Rotation into tech", (-2.5,0.3,2.5), 'Medium', 'Range'),
 ('CAT', "Fell 2.4% (RSI 26).", "Bounce", "More selling", (-3,0.3,3), 'Medium', 'Bounce watch'),
 ('AXON', "Flat at RSI 24.", "Bounce", "More selling", (-5,0.5,5), 'Speculative', 'Bounce watch'),
 ('KTOS', "Fell 2.6%.", "Drone contracts", "Volatile", (-5,0,5), 'Speculative', 'Range'),
]
P[('intraday','def','SGX')] = [
 ('BS6.SI', "Rose 5.5% to lead the STI.", "Next session", "Profit-taking", (-2.5,0.2,2.5), 'Medium', 'Follow-through check'),
 ('S63.SI', "Rose 2.8%.", "Next session", "Small range", (-1.5,0.3,1.8), 'Medium', 'Follow-through check'),
 ('H22.SI', "Rose 3%.", "Next session", "Thin trading", (-3,0.3,3), 'Speculative', 'Bounce watch'),
 ('C52.SI', "Flat.", "Next session", "Small range", (-1,0.2,1), 'Medium', 'Range'),
 ('S59.SI', "Flat.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
]

# ---------- Energy (oil and gas) ----------
P[('long','nrg','US')] = [
 ('CVX', "Chevron: revenue +35%, about 13x earnings, 10% off its high.", "Hess integration; buybacks", "Oil drops further if an Iran deal is reached", (-16,8,24), 'High', 'Core energy'),
 ('XOM', "Exxon: steady cash flow, about 13x earnings.", "Buybacks", "Oil price drop", (-15,7,21), 'High', 'Core energy'),
 ('FANG', "Diamondback: low-cost Permian producer at about 8x earnings, 34% analyst upside.", "Buybacks", "Oil price drop (WTI ~$85)", (-22,13,33), 'Medium', 'Value'),
 ('LNG', "Cheniere: US gas exports on long contracts; less tied to oil. Rose 3% today.", "New export capacity", "Gas price swings", (-15,9,26), 'Medium', 'Steady'),
 ('COP', "ConocoPhillips: about 12x earnings, revenue +29%.", "Buybacks", "Oil price drop", (-18,8,24), 'Medium', 'Value'),
]
P[('long','nrg','SGX')] = [
 ('5E2.SI', "Seatrium builds offshore rigs and wind platforms; 35% analyst upside.", "New orders", "Contract delays", (-15,12,28), 'Medium', 'Recovery'),
 ('BN4.SI', "Keppel: energy infrastructure and asset management.", "Asset sales", "Execution", (-12,10,22), 'Medium', 'Value'),
 ('RE4.SI', "Geo Energy: Indonesian coal at about 7x earnings; jumped 9% today.", "Coal prices", "Coal price drop", (-25,8,30), 'Speculative', 'Value'),
 ('5LY.SI', "Marco Polo Marine: offshore vessels, revenue +40% at about 10x earnings.", "Results (Nov)", "Thin trading", (-25,10,35), 'Speculative', 'Growth value'),
 ('5WH.SI', "Rex International is in a long downtrend (-62% this year); no setup.", "None", "Further losses", (-30,-5,20), 'Speculative', 'Avoid'),
]
P[('swing','nrg','US')] = [
 ('MPC', "Marathon Petroleum is oversold (RSI 27); refiners gain when crude falls.", "Refining margins", "Margin drop", (-10,5,16), 'Medium', 'Oversold rebound'),
 ('PSX', "Phillips 66 oversold (RSI 29); also helped by cheaper crude.", "Refining margins", "Margin drop", (-10,5,15), 'Medium', 'Oversold rebound'),
 ('DVN', "Devon rose 2.4% from RSI 29; about 8x earnings, 42% analyst upside.", "Buybacks", "Oil price drop", (-12,4,15), 'Medium', 'Oversold rebound'),
 ('OXY', "Occidental rose 2% on 1.8x volume after results (RSI 29).", "Results follow-through", "Debt; oil price", (-10,4,13), 'Medium', 'Post-earnings'),
 ('FANG', "Diamondback oversold (RSI 30).", "Buybacks", "Oil price drop", (-11,4,13), 'Medium', 'Oversold rebound'),
]
P[('swing','nrg','SGX')] = [
 ('5E2.SI', "Seatrium rose 3.3%.", "Orders", "Delays", (-8,3,10), 'Medium', 'Support'),
 ('BN4.SI', "Keppel rose 3.4%.", "Asset sales", "Execution", (-5,3,8), 'Medium', 'Rebound'),
 ('RE4.SI', "Geo Energy jumped 9.3%.", "Coal prices", "Profit-taking", (-10,2,10), 'Speculative', 'Momentum'),
 ('5LY.SI', "Marco Polo Marine rose 3.8% near lows.", "Results", "Thin trading", (-10,3,12), 'Speculative', 'Support'),
 ('5WH.SI', "Rex International: no setup.", "None", "Further losses", (-12,-2,8), 'Speculative', 'Avoid'),
]
P[('intraday','nrg','US')] = [
 ('OXY', "Rose 2% on 1.8x volume after results.", "Follow-through", "Iran-deal headlines", (-3,0.3,3), 'Medium', 'Earnings follow-through'),
 ('DVN', "Rose 2.4%.", "Follow-through", "Oil", (-3,0.3,3), 'Medium', 'Momentum check'),
 ('LNG', "Rose 3%.", "Gas exports", "Profit-taking", (-3,0.2,3), 'Medium', 'Momentum check'),
 ('XOM', "Flat; WTI near $85.", "Oil", "More Iran-deal hopes", (-2,0.2,2), 'Medium', 'Range'),
 ('MPC', "RSI 27.", "Cheaper crude", "Margins", (-3,0.4,3), 'Medium', 'Bounce watch'),
]
P[('intraday','nrg','SGX')] = [
 ('RE4.SI', "Jumped 9.3%.", "Next session", "Profit-taking", (-4,0,3), 'Speculative', 'Follow-through check'),
 ('5E2.SI', "Rose 3.3%.", "Next session", "Profit-taking", (-2,0.2,2), 'Medium', 'Follow-through check'),
 ('BN4.SI', "Rose 3.4%.", "Next session", "Small range", (-1.8,0.2,1.8), 'Medium', 'Follow-through check'),
 ('5LY.SI', "Rose 3.8%.", "Next session", "Thin trading", (-3,0.2,3), 'Speculative', 'Range'),
 ('5WH.SI', "Penny stock in a downtrend; avoid.", "None", "Further losses", (-5,-1,4), 'Speculative', 'Avoid'),
]

IPO_LIST = [
 # sym, name, ipo_date, ipo_price, sector, status
 ('ANT','Anthropic (Nasdaq: ANT; range $70-78, 825M shares, up to ~$64B; pricing expected week of Nov 16)','2026-11-19',None,'ai','Roadshow'),
 ('BIAI','Bitari','2026-11-30',7.00,'ai','Expected'),
 ('FBLLU','Football Manager SPAC','2026-11-23',10.00,'fin','Expected'),
 ('YNTE','Primagrove ($4-6 range)','2026-11-16',None,'fin','Expected'),
 ('VVVV','vVardis ($21-24 range, ~$214M; dental tech; this week)','2026-11-13',None,'hc','Expected'),
 ('WWB','Windward Bio ($16-18 range)','2026-11-13',None,'hc','Expected'),
 ('RZRA','Rezera ($11-13 range, ~$200M)','2026-11-12',None,'hc','Expected'),
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
 ('2026-11-09T15:12','NVDA TSM', "Via tracker: notes Taiwan's index jumped about 5% as AI stocks rebounded, joking that markets were impressed by Jensen Huang's energy."),
 ('2026-11-09T11:28','NVDA', "Via tracker: backs Nvidia and Huang through the personal scrutiny, saying many public figures have faced similar attention."),
 ('2026-11-08T23:52','AMD ARM QCOM LITE IREN', "Via tracker: rounds up executive comments from the selloff and argues AI demand is delayed by how fast data centres can be built, not disappearing."),
 ('2026-11-08T17:35','COHR LITE POET', "Via tracker: calls the 'AI bubble' label lazy. Memory makers with price floors and optical firms near net cash look cheap; leveraged neoclouds and AI-lab valuations are more bubble-prone."),
 ('2026-11-08T01:11','MU', "Via tracker: says old memory contract renegotiations don't apply now, since Micron's new deals carry price floors and binding commitments."),
 ('2026-11-08T00:10','NVDA', "Via tracker: on the CEO/China rumour, says Nvidia wanted China sales anyway, doubts the impact and will wait for more news."),
 ('2026-11-07T22:40','NBIS CRWV IREN', "Via tracker: contrarian on neoclouds; thinks players with contracted capacity and sound financing win if funding and permits tighten."),
 ('2026-11-07T20:23','AAOI', "Via tracker: memory longs went from ~+450% to ~+50-100%; tax-loss harvested some AAOI but remains long and expects a better 2027."),
]

EVENTS = [
 ('2026-11-09','AI','Nvidia -5% on CEO probe', "Board-led investigation into reports that Jensen Huang was targeted by foreign intelligence; board says no secrets compromised."),
 ('2026-11-09','Power','Constellation beats and raises', "2026 guide $12.50-12.80. NRG +11% on results and a $4B asset sale."),
 ('2026-11-10','Macro','Hot CPI: +0.4% (core +0.3%)', "Both above forecasts. 10-yr yield ~5.0%; Dec hike odds ~90% (CME, per WSJ). Waller says 50 bp should be considered. S&P -0.4%, Nasdaq -0.7%."),
 ('2026-11-10','AI','Nvidia -5.5% on shareholder lawsuit', "Suit says investors were misled about the CEO's ties to a suspected spy; a report says her network moved $7.5B of Nvidia chips to China. Down 18% in five days."),
 ('2026-11-10','Health','Hims & Hers -16.5%', "Q3 revenue +49% to $890M, but 2026 adjusted EBITDA outlook cut to $257-277M."),
 ('2026-11-10','AI','CoreWeave beats and raises', "Q3 revenue $3.66B; 2026 revenue guide $13.0-13.3B; capex $37-39B. TSMC October sales +60% y/y."),
 ('2026-11-10','Fin','Sea: revenue beat, EPS miss', "Revenue +43% to $8.6B; EPS $0.78 vs $0.97 on higher loan-loss provisions; $1B buyback. Stock -1.5%."),
 ('2026-11-10','SGX','STI +1.5% to 5,259', "AEM +10%, Yangzijiang +5.5% (top STI gainer), OCBC +3.1%, UMS +3.6%."),
 ('2026-11-10','IPO','Anthropic sets IPO range $70-78', "825M shares, up to ~$64B raised and ~$1.4T value at the top. Pricing expected week of Nov 16."),
 ('2026-11-11','Macro','Veterans Day', "US stock market open; bond market closed."),
 ('2026-11-12','Mixed','Nebius, Applied Materials, Nu, Accelevation report', "Rezera IPO ($11-13) expected; Windward Bio ($16-18) and vVardis ($21-24) also this week."),
 ('2026-11-17','AI','Nvidia Q3 results', "The main AI-demand checkpoint, now with a lawsuit and the CEO probe in the background. Klarna also reports."),
 ('2026-11-18','IPO','Anthropic IPO pricing (reported)', "Reported pricing around Nov 18, trading Nov 19 on Nasdaq as ANT; not confirmed by the company."),
 ('2026-11-25','SGX','IHH Q3 results', ""),
 ('2026-12-09','Macro','Fed rate decision (Dec 8-9)', "A 25 bp hike is ~90% priced after the hot CPI; ~10% odds of 50 bp."),
]
