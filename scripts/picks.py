# Analyst picks for 2026-11-10 (snapshot: US intraday Nov 9 ~3:05 pm ET, SGX close Nov 6; SGX shut Nov 9 for Deepavali). Fields: sym, thesis, catalyst, risk, (low, base, high) % expected move, conviction, setup
# Horizons: long = 12 months, swing = ~4 weeks, intraday = rest of session (US) / next session (SGX), ipo = 6 months.
# Context: Nov 6: S&P +0.3% (week -2.7%), chips +3.6%; jobs +165K vs ~65K expected, unemployment 4.1%; Dec hike odds ~78%. STI -2.2% to 5,179.
# Nov 9: relief rally. S&P +2.2%, Nasdaq-100 +3.1%, Dow +1,000, chip ETF +7%, VIX ~20.5. Nvidia -5% as its board probes reports that the CEO was targeted by foreign intelligence.
# Oil fell ~3.5% (WTI ~$88) after Trump said new strikes on Iran are unlikely while talks continue. 10-yr yield 4.88%. Citi cut US stocks to neutral.
P = {}

# ---------- AI & chips ----------
P[('long','ai','US')] = [
 ('NVDA', "Revenue +106% at about 11x forward earnings, now the cheapest big AI chip stock. Fell 5% on the CEO probe while every other chip rallied.",
  "Q3 results Nov 17", "Board probe and Congress briefing on the CEO; data-centre policy", (-25,22,50), 'High', 'Quality at a discount'),
 ('TSM', "Makes almost every leading AI chip. Revenue +51% at about 17x forward earnings, 20% below its high.",
  "October sales (~Nov 10); Q4 results Jan 14", "Taiwan geopolitics; AI capex cuts", (-18,18,40), 'High', 'Core holding'),
 ('AVGO', "Custom AI chips plus networking: revenue +86% at about 16x forward earnings, 33% below its high. Rose 9% on Nov 9.",
  "Q4 results Dec 9", "Lumpy custom-chip orders; customer concentration", (-22,20,45), 'Medium', 'Pullback in a leader'),
 ('COHR', "Record quarter and a ~$20B five-year optics deal. Jumped 18% on Nov 9 but is still 47% below its high at about 14x forward earnings.",
  "First $3B quarter targeted by FY27 end", "8% daily swings; capex keeps rising", (-32,24,62), 'Medium', 'Beat-and-sold'),
 ('MU', "Memory is still the tightest part of AI servers: revenue +379% at about 3.5x forward earnings, 40% off its high.",
  "FQ1 results Dec 23", "Peak-cycle earnings; memory falls hard when prices turn", (-38,22,62), 'Medium', 'Cycle leader'),
]
P[('long','ai','SGX')] = [
 ('AWX.SI', "AEM is 44% below its high after a 42% fall in a month, but still up 261% this year; analysts rate it Strong Buy.",
  "Q3 business update (Nov)", "One large customer; 6% daily swings", (-38,18,55), 'Medium', 'SGX AI leader'),
 ('558.SI', "UMS makes precision parts for chip-equipment makers: revenue +29%, 43% off its high. Applied Materials and Lam rose 9-12% on Nov 9.",
  "Q3 results mid-November", "Tied to Applied Materials spending", (-30,15,45), 'Medium', 'Equipment supplier'),
 ('5DD.SI', "Micro-Mechanics makes precision tools for chip assembly and test: revenue +45%, 43% off its high.",
  "Q1 FY27 results (Nov)", "Small and thinly traded", (-24,14,36), 'Medium', 'Growth at a discount'),
 ('E28.SI', "Frencken builds modules for chip and medical equipment. 51% off its high at about 15x earnings.",
  "Q3 business update (Nov)", "Flat revenue so far this year", (-25,14,38), 'Medium', 'Recovery'),
 ('V03.SI', "Venture builds electronics for chip-equipment, medical and AI-server makers. Net cash, about 15x earnings, low volatility.",
  "Q3 business update (Nov)", "Slow growth (+7%)", (-12,10,22), 'Medium', 'Steady value'),
]
P[('swing','ai','US')] = [
 ('NVDA', "RSI 27 and down 12% in five days, a week before results. The probe is a headline risk, not an earnings one; the board says no secrets were compromised.",
  "Q3 results Nov 17", "More probe news; Congress briefing", (-15,7,20), 'Medium', 'Oversold into earnings'),
 ('LITE', "Marvell is buying Lumentum for 4.5 Marvell shares each. At today's prices that is worth about 15% more than LITE's price.",
  "Spread narrows if MRVL keeps recovering", "Regulatory delay (incl. China); MRVL falls again", (-15,7,20), 'Medium', 'Merger spread'),
 ('AMD', "Rose 13% on Nov 9 after an Oppenheimer upgrade ($600 target). Revenue +45%; still 22% below its high.",
  "Analyst Day follow-through; MI-series orders", "29x forward earnings; 7% daily swings", (-18,6,20), 'Medium', 'Upgrade momentum'),
 ('CRDO', "Credo: revenue +115% at about 14x forward earnings, 56% off its high; analysts see 114% upside.",
  "Q2 results Nov 30", "Customer concentration; 8% daily swings", (-25,10,32), 'Speculative', 'Oversold growth'),
 ('COHR', "Up 18% on Nov 9 but RSI only 49; the relief rally has room if chips hold.",
  "Analyst target updates", "Gives back gains if the rally fades", (-18,6,22), 'Medium', 'Rebound follow-through'),
]
P[('swing','ai','SGX')] = [
 ('AWX.SI', "AEM is down 42% in a month (RSI 28). US chips jumped 7% while SGX was shut, so it reopens into better news.",
  "US chips stabilising; Q3 update", "Rally fades in the US", (-22,6,28), 'Speculative', 'Oversold rebound'),
 ('558.SI', "UMS is down 39% in a month (RSI 26); analysts still see about 100% upside.",
  "Q3 results mid-November", "Chip-equipment sentiment", (-20,6,24), 'Speculative', 'Oversold rebound'),
 ('E28.SI', "Frencken is down 32% in a month (RSI 23), the most oversold in the group.",
  "Q3 business update (Nov)", "No clear catalyst before results", (-16,5,18), 'Speculative', 'Oversold rebound'),
 ('5DD.SI', "Micro-Mechanics fell 7% on Nov 6; RSI 29 on twice normal volume.",
  "Q1 FY27 results (Nov)", "Thin order book", (-12,4,14), 'Medium', 'Oversold rebound'),
 ('V03.SI', "Venture is the least volatile SGX tech name and is oversold (RSI 32).",
  "Q3 business update (Nov)", "Flat revenue", (-8,4,10), 'Medium', 'Range trade'),
]
P[('intraday','ai','US')] = [
 ('NVDA', "Fell 5% on 3x normal volume on the CEO probe, against a 7% chip rally. Watch for more probe headlines.",
  "Any board or Congress update", "Further selling on headlines", (-4,0.5,4), 'Medium', 'Headline risk'),
 ('COHR', "Up 18% on Nov 9; watch whether it holds above the opening range the next day.",
  "Follow-through buying", "Profit-taking after a big day", (-6,0,6), 'Speculative', 'Momentum check'),
 ('AMD', "Up 13% on the Oppenheimer upgrade.", "Follow-through", "Profit-taking", (-5,0.3,5), 'Medium', 'Momentum check'),
 ('CRWV', "CoreWeave reports Nov 10, 64% off its high.", "Results", "Data-centre delay headlines", (-10,0,10), 'Speculative', 'Earnings reaction'),
 ('TSM', "October sales are due around Nov 10.", "Monthly sales", "Taiwan opens lower", (-3,0.5,3.5), 'Medium', 'Data point'),
]
P[('intraday','ai','SGX')] = [
 ('AWX.SI', "First session since US chips jumped 7% on Nov 9 (SGX shut for Deepavali).",
  "Gap up at the open", "Gap fades by the close", (-5,3,9), 'Speculative', 'Gap-up watch'),
 ('558.SI', "Applied Materials and Lam rose 9-12% while SGX was shut.", "Next session open", "Trend still down", (-4,2.5,7), 'Speculative', 'Gap-up watch'),
 ('E28.SI', "Fell 6.5% on Nov 6; most oversold (RSI 23).", "Next session open", "Follows US chip equipment", (-4,2,6), 'Medium', 'Bounce watch'),
 ('5DD.SI', "Fell 7% on Nov 6.", "Next session open", "Thin trading", (-3.5,1.5,5), 'Medium', 'Bounce watch'),
 ('MZH.SI', "Nanofilm is 54% off its high (RSI 29).", "Next session", "Thin trading", (-3,1,4), 'Speculative', 'Bounce watch'),
]

# ---------- Health ----------
P[('long','hc','US')] = [
 ('LLY', "Obesity-drug leader: revenue +39%, at a new high (+32% this year). Little analyst upside left, so the base case is modest.",
  "Orforglipron launch; Q4 results (Feb)", "Drug-price policy under the new Congress", (-16,8,25), 'High', 'Defensive growth'),
 ('ARGX', "argenx: revenue +52% from its immune-disease drug Vyvgart, 9% off its high, 19% analyst upside.",
  "New indications in 2027", "Competition in myasthenia gravis", (-15,11,30), 'Medium', 'Growth leader'),
 ('MDGL', "Madrigal's liver drug Rezdiffra is growing fast (revenue +50%); 29% off its high with 60% analyst upside. Rose 8% on Nov 9.",
  "Script data; EU rollout", "Competition from GLP-1 drugs", (-22,20,45), 'Medium', 'Oversold growth'),
 ('INSM', "Insmed's lung drug launch drives revenue +268%; 46% off its high with 70% analyst upside.",
  "Brensocatib launch numbers", "Expensive on near-term earnings", (-30,18,48), 'Medium', 'Launch story'),
 ('ALNY', "Alnylam is 67% off its high at about 15x forward earnings (RSI 14); analysts see 94% upside.",
  "Amvuttra script data", "Trend still down", (-30,18,50), 'Speculative', 'Deep value'),
]
P[('long','hc','SGX')] = [
 ('Q0F.SI', "IHH runs hospitals across Asia; analysts see 37% upside.", "Q3 results Nov 25", "Currency swings", (-12,12,25), 'Medium', 'Regional leader'),
 ('C2PU.SI', "Parkway Life REIT: steady hospital and nursing-home rents, 6% off its high.", "Dividend", "Higher rates", (-8,8,15), 'High', 'Income'),
 ('AP4.SI', "Riverstone makes cleanroom and medical gloves at about 14x earnings with 43% analyst upside.", "Q3 results (Nov)", "Glove price competition", (-15,12,30), 'Medium', 'Value'),
 ('BSL.SI', "Raffles Medical: Singapore hospital group, 21% off its high and in a mild uptrend (RSI 65).", "Results (Feb)", "Shrinking revenue (-7%)", (-10,8,18), 'Medium', 'Recovery'),
 ('H02.SI', "Haw Par (Tiger Balm) trades near 10x earnings with a large cash and investment pile.", "Results (Feb)", "Revenue down 8%", (-12,6,16), 'Medium', 'Value'),
]
P[('swing','hc','US')] = [
 ('MDGL', "Bounced 8% on Nov 9 from RSI 35; 60% analyst upside.", "Script data", "Rotation back to tech", (-12,6,18), 'Medium', 'Oversold rebound'),
 ('ALNY', "Deeply oversold (RSI 14) and 67% off its high.", "Amvuttra script data", "Trend still down", (-15,7,22), 'Speculative', 'Oversold rebound'),
 ('ARGX', "Up 10% in five days (RSI 69).", "Momentum", "Overbought", (-8,4,12), 'Medium', 'Trend'),
 ('CYTK', "Down 10% in five days after Q3 (RSI 30); RBC sees a revenue step-up for Myqorzo from 2027.", "Launch metrics", "Slow early sales", (-15,7,22), 'Speculative', 'Post-earnings dip'),
 ('LLY', "At a new high; leadership through the selloff.", "Orforglipron news", "Money rotating back into chips", (-8,3,10), 'High', 'Relative strength'),
]
P[('swing','hc','SGX')] = [
 ('C2PU.SI', "Parkway Life REIT: lowest-volatility name in the group.", "Dividend", "Rates", (-4,2,6), 'High', 'Range'),
 ('BSL.SI', "Raffles Medical is in a mild uptrend (RSI 65).", "Momentum", "Low volume", (-5,2.5,8), 'Medium', 'Trend'),
 ('Q0F.SI', "IHH traded nearly 8x normal volume on Nov 6 ahead of Q3 results.", "Q3 results Nov 25", "Results miss", (-6,3,9), 'Medium', 'Pre-earnings'),
 ('AP4.SI', "Riverstone is near support with large analyst upside.", "Q3 results (Nov)", "Glove prices", (-8,3,10), 'Medium', 'Support'),
 ('QC7.SI', "Q&M Dental is very oversold (RSI 17).", "Bounce", "Small cap", (-8,3,10), 'Speculative', 'Oversold rebound'),
]
P[('intraday','hc','US')] = [
 ('HIMS', "Fell 9% on 3x volume before reporting Q3 after the close on Nov 9.", "Reaction to results", "High short interest; gap either way", (-10,0,10), 'Speculative', 'Earnings reaction'),
 ('MRNA', "At a new high (+835% this year) and far above analyst targets after raising its 2026 outlook.", "Momentum", "Analysts see 44% downside to targets", (-6,0,6), 'Speculative', 'Extended'),
 ('TEM', "Tempus rose 12% to near its high.", "Momentum", "Profit-taking", (-5,0.3,5), 'Speculative', 'Momentum check'),
 ('VKTX', "Rose 8%; analysts see over 200% upside.", "Obesity-drug news", "Volatile", (-5,0.3,5), 'Speculative', 'Momentum check'),
 ('LLY', "New high on Nov 9.", "Momentum", "Rotation into tech", (-2.5,0.3,2.5), 'Medium', 'Relative strength'),
]
P[('intraday','hc','SGX')] = [
 ('C2PU.SI', "Steady REIT.", "Next session", "Small range", (-1,0.2,1), 'Medium', 'Range'),
 ('BSL.SI', "Rose 0.6% on Nov 6 against a 2% STI drop.", "Next session", "Small range", (-1.5,0.3,1.5), 'Medium', 'Relative strength'),
 ('H02.SI', "Fell 2.8% on Nov 6.", "Next session", "Small range", (-1.5,0.3,1.5), 'Medium', 'Range'),
 ('Q0F.SI', "Heavy volume on Nov 6.", "Next session", "Malaysia market swings", (-2,0.2,2), 'Medium', 'Range'),
 ('AP4.SI', "Slightly lower.", "Next session", "Thin trading", (-2,0.2,2), 'Medium', 'Range'),
]

# ---------- Finance ----------
P[('long','fin','US')] = [
 ('JPM', "Best-run US bank, 6% off its high at about 13x forward earnings.", "Q4 results Jan 14", "Credit cycle", (-15,8,22), 'High', 'Core holding'),
 ('V', "Visa: steady growth (+13%), near its high; little AI exposure.", "Holiday spending", "Regulation of card fees", (-12,6,18), 'High', 'Defensive growth'),
 ('GS', "Trading and deal-making boom, about 12x forward earnings, 21% off its high. A record Anthropic IPO would be a big fee win.",
  "Anthropic IPO (Goldman co-leads)", "Market volatility hits deals", (-20,10,28), 'Medium', 'Cyclical value'),
 ('SE', "Sea (Shopee, Garena, Monee): revenue +48% at about 15x forward earnings, 50% off its high.", "Q3 results Nov 10", "Competition from TikTok Shop", (-30,26,62), 'Medium', 'Oversold growth'),
 ('NU', "Nubank: revenue +52% at about 11x forward earnings, 34% off its high.", "Q3 results Nov 12", "Brazil credit and currency", (-30,22,55), 'Medium', 'Growth at a discount'),
]
P[('long','fin','SGX')] = [
 ('D05.SI', "DBS missed Q3 but kept its 81-cent dividend and says interest income has bottomed. RSI 11 after a 5% slide.",
  "Q4 results (Feb)", "Margins if rates fall; stronger SGD", (-10,8,16), 'High', 'Income leader'),
 ('O39.SI', "OCBC was the only local bank to beat in Q3 (profit +3%) and raised loan-growth guidance to low double digits.",
  "Q4 results (Feb)", "Margin fell 18 bp to 1.66%", (-10,7,15), 'Medium', 'Income'),
 ('U11.SI', "UOB missed Q3 and cut its margin guidance; RSI 13, 18% off its high.", "Recovery in fees", "More credit provisions", (-12,8,18), 'Medium', 'Oversold income'),
 ('AIY.SI', "iFAST: fintech platform, revenue +23%, 28% off its high with 45% analyst upside.", "HK pension business", "Market-driven volumes", (-18,18,38), 'Medium', 'Growth'),
 ('S68.SI', "SGX benefits from high trading volumes; from Jan 2027 its RegCo takes over IPO prospectus reviews.", "Monthly volume data", "Already priced (25x earnings)", (-12,7,18), 'Medium', 'Volatility winner'),
]
P[('swing','fin','US')] = [
 ('SE', "Reports Q3 on Nov 10, 50% off its high.", "Results", "Results gap", (-15,7,22), 'Medium', 'Pre-earnings'),
 ('NU', "Oversold (RSI 26) into Q3 results Nov 12.", "Results", "Brazil credit", (-15,6,20), 'Medium', 'Pre-earnings'),
 ('HOOD', "Down 22% in a month (RSI 35); 52% analyst upside.", "October trading data", "Bitcoin weak (~$75K); crypto rules after the election", (-18,6,22), 'Speculative', 'Oversold rebound'),
 ('GS', "Rose 5% on Nov 9; IPO pipeline (Anthropic) is building.", "Deal fees", "Volatility", (-8,4,12), 'Medium', 'Deal pipeline'),
 ('GRAB', "Up 21% in five days after raising guidance (RSI 73).", "Momentum", "Overbought", (-10,3,12), 'Medium', 'Momentum'),
]
P[('swing','fin','SGX')] = [
 ('D05.SI', "DBS is the most oversold SGX bank (RSI 11).", "Dividend support", "Margin worries", (-4,3,7), 'High', 'Oversold income'),
 ('U11.SI', "UOB RSI 13 after its Q3 miss.", "Rebound", "Further downgrades", (-5,3,8), 'Medium', 'Oversold rebound'),
 ('O39.SI', "OCBC beat but still slipped (RSI 30).", "Post-results recovery", "Margin squeeze", (-4,2.5,6), 'Medium', 'Oversold income'),
 ('AIY.SI', "iFAST is holding up (RSI 45).", "Momentum", "Market-driven", (-8,3,10), 'Medium', 'Range'),
 ('S68.SI', "SGX benefits when markets are volatile.", "Volume data", "Valuation", (-5,2,7), 'Medium', 'Volatility winner'),
]
P[('intraday','fin','US')] = [
 ('SE', "Reports Q3 on Nov 10.", "Results", "Gap either way", (-9,0.5,9), 'Speculative', 'Earnings reaction'),
 ('KKR', "Reported Nov 9; rose 2.4%.", "Follow-through", "Private-credit worries", (-3,0.3,3), 'Medium', 'Earnings reaction'),
 ('COIN', "Bitcoin is near $75K on fears of tougher crypto rules after the election.", "Crypto bounce", "More crypto selling", (-5,0,5), 'Speculative', 'Crypto beta'),
 ('HOOD', "Rose 4.6% with the market.", "Risk-on", "Crypto weakness", (-4,0.3,4), 'Speculative', 'Momentum check'),
 ('GS', "Rose 5% on Nov 9.", "Risk-on", "Profit-taking", (-2.5,0.3,2.5), 'Medium', 'Momentum check'),
]
P[('intraday','fin','SGX')] = [
 ('D05.SI', "RSI 11; first session after a strong US rally.", "Next session", "Market-wide risk-off", (-1.2,0.5,1.5), 'High', 'Bounce watch'),
 ('U11.SI', "Oversold.", "Next session", "Trend down", (-1.5,0.4,1.8), 'Medium', 'Bounce watch'),
 ('O39.SI', "Beat in Q3 but fell with peers.", "Next session", "Small range", (-1.2,0.3,1.4), 'Medium', 'Bounce watch'),
 ('S68.SI', "Fell 2.4% on Nov 6.", "Next session", "Profit-taking", (-2,0.3,2), 'Medium', 'Range'),
 ('AIY.SI', "Fell 2.8% on Nov 6.", "Next session", "Risk-off", (-2.5,0.4,2.5), 'Medium', 'Range'),
]

# IPO tab (6-month view), all markets
P[('ipo','all','US')] = [
 ('SPCX', "SpaceX listed in June at $135 and trades about 5% above that, 33% under its high. Analysts see large upside.",
  "xAI/GPU news; lock-up expiries", "Valuation, Musk headlines and data-centre policy", (-35,12,45), 'Medium', 'Mega-cap IPO'),
 ('CHYM', "Chime (IPO $27) trades about 22% above its IPO price, near its high, up 15% in five days.",
  "Member growth", "Fintech credit cycle", (-15,10,28), 'Medium', 'Post-IPO uptrend'),
 ('KLAR', "Klarna (IPO $40) is 66% below its IPO price at about 17x forward earnings; revenue +27%.",
  "Q3 results Nov 17", "Buy-now-pay-later credit losses", (-22,15,40), 'Speculative', 'Deep value'),
 ('ACCV', "Accelevation (IPO $18) makes electrical gear for data centres: revenue +80% at about 12x forward earnings, 35% below its IPO price.",
  "First results as a public company Nov 12", "Data-centre policy risk; 8% daily swings", (-40,10,50), 'Speculative', 'Post-IPO value'),
 ('FIG', "Figma: revenue +43% with AI products, but 41% below its IPO price after a weak reaction to results.",
  "AI product monetisation", "Software multiples falling", (-30,10,40), 'Speculative', 'Post-earnings dip'),
]

# ---------- Power & grid (data-center power) ----------
P[('long','pwr','US')] = [
 ('GEV', "GE Vernova: gas turbines and grid gear sold out for years, revenue +27%. 29% off its high.", "Q4 results Jan 27", "Data-centre policy; valuation (32x)", (-25,15,40), 'High', 'Quality at a discount'),
 ('CEG', "Constellation beat Q3 (EPS $5.06 vs $3.72) and raised 2026 guidance to $12.50-12.80; still 28% off its high.", "Buyback update; new long-term power deals", "Data-centre politics; PJM rules", (-22,16,38), 'High', 'Beat and raise'),
 ('ETN', "Eaton: electrical gear for data centres and utilities, 21% off its high at about 22x earnings.", "Q4 results Feb 2", "Data-centre orders slowing", (-20,13,33), 'Medium', 'Quality at a discount'),
 ('PWR', "Quanta builds the grid: revenue +57%, 24% off its high.", "Utility capex plans", "Data-centre policy", (-25,13,36), 'Medium', 'Grid builder'),
 ('VRT', "Vertiv: data-centre cooling and power, revenue +61% at about 20x forward earnings, 47% off its high.", "Order backlog updates", "Most exposed to a data-centre slowdown", (-35,20,55), 'Medium', 'Oversold growth'),
]
P[('long','pwr','SGX')] = [
 ('BN4.SI', "Keppel: power, data centres and asset management, about 16x earnings with 34% analyst upside; fell 4.6% on Nov 6.", "Asset sales", "Execution", (-12,12,25), 'Medium', 'Value'),
 ('U96.SI', "Sembcorp: power and renewables at about 9x earnings.", "New contracts", "Power prices", (-12,7,18), 'Medium', 'Value'),
 ('DCRU.SI', "Digital Core REIT: US data-centre REIT, about 10x earnings with 50% analyst upside.", "Leasing news", "Tenant concentration", (-12,12,28), 'Medium', 'Deep value'),
 ('AJBU.SI', "Keppel DC REIT: data-centre rents, 10% off its high.", "Dividend", "Rates", (-10,7,17), 'Medium', 'Income'),
 ('544.SI', "CSE Global: electrification and data-centre work, about 10x earnings, 54% off its high after an 8% drop on Nov 6.", "New orders", "Small and volatile", (-30,18,50), 'Speculative', 'Recovery'),
]
P[('swing','pwr','US')] = [
 ('CEG', "Beat-and-raise on Nov 9 (+10%); FY consensus still sits below the new guidance, so estimates should rise.", "Analyst target updates", "Data-centre politics", (-12,6,18), 'Medium', 'Post-earnings drift'),
 ('NRG', "Strong Q3 and a $4B asset sale; rose 11% and trades at about 9x earnings with 71% analyst upside.", "Analyst updates", "Texas data-centre proposal", (-15,7,22), 'Medium', 'Post-earnings drift'),
 ('VST', "Raised its 2026 outlook on Nov 6 (+11%); still 30% off its high.", "Analyst updates", "Texas data-centre proposal", (-14,6,20), 'Medium', 'Post-earnings drift'),
 ('BE', "Bloom rose 13% as investors re-rated two fuel-cell contract wins; RSI 44.", "New orders", "8% daily swings", (-20,7,26), 'Speculative', 'News vs price'),
 ('OKLO', "Rose 15% on a narrower-than-expected Q3 loss, but is still 76% off its high.", "Licensing news", "Cash burn; no revenue", (-25,5,28), 'Speculative', 'Rebound'),
]
P[('swing','pwr','SGX')] = [
 ('BN4.SI', "Keppel fell 4.6% on Nov 6 (RSI 30).", "Asset-sale news", "Execution", (-5,3,8), 'Medium', 'Oversold rebound'),
 ('U96.SI', "Sembcorp fell 3%; RSI 38.", "Contracts", "Power prices", (-5,2,7), 'Medium', 'Range'),
 ('544.SI', "CSE Global fell 8% on 2.4x volume.", "Bounce", "Small cap", (-18,5,20), 'Speculative', 'Oversold rebound'),
 ('DCRU.SI', "Digital Core REIT is in an uptrend (RSI 67).", "Momentum", "US data-centre worries", (-6,2,8), 'Medium', 'Trend'),
 ('AJBU.SI', "Keppel DC REIT is in an uptrend (RSI 72).", "Momentum", "Overbought", (-5,1.5,6), 'Medium', 'Trend'),
]
P[('intraday','pwr','US')] = [
 ('CEG', "Beat and raised on Nov 9 (+10%).", "Follow-through", "Profit-taking", (-4,0.5,4.5), 'Medium', 'Earnings follow-through'),
 ('NRG', "Rose 11% on results and a $4B asset sale.", "Follow-through", "Profit-taking", (-4,0.5,4.5), 'Medium', 'Earnings follow-through'),
 ('BE', "Rose 13% on contract wins.", "Momentum", "Profit-taking; 8% daily swings", (-7,0,7), 'Speculative', 'Momentum check'),
 ('OKLO', "Rose 15% after results.", "Momentum", "Profit-taking", (-8,0,8), 'Speculative', 'Momentum check'),
 ('NEE', "Lagged the rally (+0.4%) as money left defensives (RSI 74).", "Defensive bid", "Rotation into growth", (-1.8,0,1.8), 'Medium', 'Range'),
]
P[('intraday','pwr','SGX')] = [
 ('BN4.SI', "Fell 4.6% on Nov 6.", "Next session", "Small range", (-1.5,0.5,2), 'Medium', 'Bounce watch'),
 ('U96.SI', "Fell 3%.", "Next session", "Small range", (-1.5,0.4,1.8), 'Medium', 'Bounce watch'),
 ('544.SI', "Fell 8%.", "Next session", "Further selling", (-5,1,5), 'Speculative', 'Bounce watch'),
 ('AJBU.SI', "Fell 0.9%.", "Next session", "Small range", (-1.2,0.2,1.2), 'Medium', 'Range'),
 ('DCRU.SI', "Fell 2.2%.", "Next session", "Small range", (-1.5,0.3,1.5), 'Medium', 'Range'),
]

# ---------- Defence & industrials ----------
P[('long','def','US')] = [
 ('GE', "GE Aerospace: jet-engine services boom, revenue +16%, 12% off its high.", "Q4 results Jan 21", "Valuation (36x)", (-15,11,28), 'High', 'Quality'),
 ('RTX', "RTX: missiles and engines, revenue +11%, steady.", "Q4 results Jan 26", "Engine issues", (-12,10,24), 'High', 'Core defence'),
 ('LHX', "L3Harris: space and missile sensors, 28% off its high, 23% analyst upside.", "Golden Dome contracts", "Budget fights with a split government", (-15,12,30), 'Medium', 'Value'),
 ('HWM', "Howmet: jet-engine parts, revenue +29%, 26% off its high.", "Aerospace build rates", "Valuation (33x)", (-20,15,36), 'Medium', 'Growth at a discount'),
 ('NOC', "Northrop: B-21 and missile defence, about 18x earnings, 30% off its high.", "Golden Dome contracts", "Budget fights", (-15,11,28), 'Medium', 'Value'),
]
P[('long','def','SGX')] = [
 ('S63.SI', "ST Engineering: defence and aerospace, revenue +11%; extremely oversold (RSI 7) after a 5% drop on Nov 6.", "Contract wins", "Valuation (24x)", (-10,12,24), 'High', 'Quality'),
 ('BS6.SI', "Yangzijiang Shipbuilding: about 7x earnings, revenue +36%; fell 6% on Nov 6.", "New ship orders", "US port fees on Chinese ships", (-18,12,30), 'Medium', 'Value'),
 ('S59.SI', "SIA Engineering: aircraft maintenance, 24% off its high, 30% analyst upside.", "Air travel", "Revenue falling (-11%)", (-10,11,24), 'Medium', 'Recovery'),
 ('C52.SI', "ComfortDelGro: steady transport earnings at about 14x.", "Overseas contracts", "Slow growth", (-8,8,16), 'Medium', 'Steady'),
 ('H22.SI', "Hong Leong Asia: engines and building materials at about 8x earnings, 48% off its high.", "Results (Feb)", "China demand", (-25,22,50), 'Speculative', 'Deep value'),
]
P[('swing','def','US')] = [
 ('CAT', "Caterpillar rose 7% to lead the Dow but is still 44% off its high (RSI 30).", "Rebound", "Data-centre generator orders slowing", (-12,6,18), 'Medium', 'Oversold rebound'),
 ('AXON', "Down 29% in five days after a Q3 miss (RSI 28); 79% analyst upside.", "Analyst updates", "More downgrades", (-18,6,22), 'Speculative', 'Post-earnings dip'),
 ('AVAV', "AeroVironment rose 13.5% (RSI 57) but is 67% off its high.", "Drone and counter-drone orders", "Volatile; results Dec 2", (-18,6,22), 'Speculative', 'Rebound'),
 ('BA', "Boeing 31% off its high (RSI 33); production recovering.", "Monthly deliveries", "Quality issues; staff cuts", (-10,5,15), 'Medium', 'Recovery'),
 ('KTOS', "Kratos rose 8% after results; 71% off its high.", "Drone contracts", "Volatile", (-20,5,24), 'Speculative', 'Rebound'),
]
P[('swing','def','SGX')] = [
 ('S63.SI', "ST Engineering extremely oversold (RSI 7).", "Bounce", "Low volatility", (-4,3,8), 'High', 'Oversold rebound'),
 ('BS6.SI', "Yangzijiang fell 6% (RSI 22).", "Orders", "Trade fees", (-9,4,12), 'Medium', 'Oversold rebound'),
 ('H22.SI', "Hong Leong Asia fell 9% (RSI 18).", "Bounce", "China demand", (-10,4,12), 'Speculative', 'Oversold rebound'),
 ('S59.SI', "SIA Engineering steady.", "Air travel", "Slow growth", (-6,2,7), 'Medium', 'Range'),
 ('C52.SI', "ComfortDelGro fell 3% on 4x volume.", "Support", "Slow growth", (-4,1.5,5), 'Medium', 'Range'),
]
P[('intraday','def','US')] = [
 ('AVAV', "Rose 13.5% on Nov 9.", "Follow-through", "Profit-taking", (-6,0,6), 'Speculative', 'Momentum check'),
 ('KTOS', "Rose 8%.", "Follow-through", "Profit-taking", (-5,0,5), 'Speculative', 'Momentum check'),
 ('CAT', "Rose 7%; led the Dow.", "Follow-through", "Profit-taking", (-3,0.3,3.5), 'Medium', 'Momentum check'),
 ('AXON', "Fell 3% against the rally; RSI 28.", "Bounce", "More selling", (-5,0.5,5), 'Speculative', 'Bounce watch'),
 ('LMT', "Rose 3.7%.", "Defence bid", "Rotation into tech", (-2.5,0.3,2.5), 'Medium', 'Range'),
]
P[('intraday','def','SGX')] = [
 ('S63.SI', "RSI 7; first session after a strong US rally.", "Next session", "Small range", (-1,0.6,1.8), 'Medium', 'Bounce watch'),
 ('BS6.SI', "Fell 6%.", "Next session", "Risk-off", (-2.5,0.6,3), 'Medium', 'Bounce watch'),
 ('H22.SI', "Fell 9%.", "Next session", "Thin trading", (-3,0.5,3.5), 'Speculative', 'Bounce watch'),
 ('C52.SI', "Fell 3%.", "Next session", "Small range", (-1,0.3,1.2), 'Medium', 'Range'),
 ('S59.SI', "Steady.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
]

# ---------- Energy (oil and gas) ----------
P[('long','nrg','US')] = [
 ('CVX', "Chevron: revenue +35%, about 13x earnings, 11% off its high.", "Hess integration; buybacks", "Oil drops further if an Iran deal is reached", (-16,8,24), 'High', 'Core energy'),
 ('XOM', "Exxon: steady cash flow, about 13x earnings.", "Buybacks", "Oil price drop", (-15,7,21), 'High', 'Core energy'),
 ('FANG', "Diamondback: low-cost Permian producer at about 8x earnings, 36% analyst upside.", "Buybacks", "Oil price drop", (-22,14,34), 'Medium', 'Value'),
 ('LNG', "Cheniere: US gas exports on long contracts; less tied to oil.", "New export capacity", "Gas price swings", (-15,9,26), 'Medium', 'Steady'),
 ('COP', "ConocoPhillips: about 12x earnings, revenue +29%.", "Buybacks", "Oil price drop", (-18,8,24), 'Medium', 'Value'),
]
P[('long','nrg','SGX')] = [
 ('5E2.SI', "Seatrium builds offshore rigs and wind platforms; 39% analyst upside.", "New orders", "Contract delays", (-15,12,28), 'Medium', 'Recovery'),
 ('BN4.SI', "Keppel: energy infrastructure and asset management.", "Asset sales", "Execution", (-12,10,22), 'Medium', 'Value'),
 ('RE4.SI', "Geo Energy: Indonesian coal at about 7x earnings.", "Coal prices", "Coal price drop", (-25,8,30), 'Speculative', 'Value'),
 ('5LY.SI', "Marco Polo Marine: offshore vessels, revenue +40% at about 10x earnings.", "Results (Nov)", "Thin trading", (-25,10,35), 'Speculative', 'Growth value'),
 ('5WH.SI', "Rex International is in a long downtrend (-63% this year); no setup.", "None", "Further losses", (-30,-5,20), 'Speculative', 'Avoid'),
]
P[('swing','nrg','US')] = [
 ('MPC', "Marathon Petroleum is oversold (RSI 24); refiners gain when crude falls.", "Refining margins", "Margin drop", (-10,5,16), 'Medium', 'Oversold rebound'),
 ('PSX', "Phillips 66 oversold (RSI 27); also helped by cheaper crude.", "Refining margins", "Margin drop", (-10,5,15), 'Medium', 'Oversold rebound'),
 ('DVN', "Devon oversold (RSI 23), about 8x earnings, 46% analyst upside.", "Buybacks", "Oil price drop", (-12,4,15), 'Medium', 'Oversold rebound'),
 ('OXY', "Occidental oversold (RSI 22); reported Nov 9.", "Results reaction", "Debt; oil price", (-10,4,13), 'Medium', 'Post-earnings'),
 ('FANG', "Diamondback oversold (RSI 29).", "Buybacks", "Oil price drop", (-11,4,13), 'Medium', 'Oversold rebound'),
]
P[('swing','nrg','SGX')] = [
 ('5E2.SI', "Seatrium fell 4.8% on Nov 6.", "Orders", "Delays", (-8,3,10), 'Medium', 'Support'),
 ('BN4.SI', "Keppel oversold (RSI 30).", "Asset sales", "Execution", (-5,3,8), 'Medium', 'Oversold rebound'),
 ('RE4.SI', "Geo Energy fell 4.9%.", "Coal prices", "Coal price drop", (-9,3,11), 'Speculative', 'Oversold rebound'),
 ('5LY.SI', "Marco Polo Marine near lows.", "Results", "Thin trading", (-10,3,12), 'Speculative', 'Support'),
 ('5WH.SI', "Rex International: no setup.", "None", "Further losses", (-12,-2,8), 'Speculative', 'Avoid'),
]
P[('intraday','nrg','US')] = [
 ('OXY', "Reported Nov 9; fell 1.6% as oil slid.", "Results reaction", "Iran-deal headlines", (-3,0.3,3), 'Medium', 'Earnings reaction'),
 ('MPC', "Rose 3% as crude fell; RSI 24.", "Cheaper crude", "Margins", (-3,0.5,3.5), 'Medium', 'Bounce watch'),
 ('XOM', "Fell 1.5% with oil (WTI ~$88).", "Oil", "More Iran-deal hopes", (-2,0.2,2), 'Medium', 'Range'),
 ('CVX', "Fell 1.5%.", "Oil", "More Iran-deal hopes", (-2,0.2,2), 'Medium', 'Range'),
 ('DVN', "RSI 23.", "Bounce", "Oil", (-3,0.4,3), 'Medium', 'Bounce watch'),
]
P[('intraday','nrg','SGX')] = [
 ('5E2.SI', "Fell 4.8% on Nov 6.", "Next session", "Risk-off", (-2,0.4,2.5), 'Medium', 'Bounce watch'),
 ('BN4.SI', "Fell 4.6%.", "Next session", "Small range", (-1.5,0.5,2), 'Medium', 'Bounce watch'),
 ('RE4.SI', "Fell 4.9%.", "Next session", "Coal prices", (-2.5,0.3,2.5), 'Speculative', 'Range'),
 ('5LY.SI', "Fell 1.9%.", "Next session", "Thin trading", (-2.5,0.2,2.5), 'Speculative', 'Range'),
 ('5WH.SI', "Penny stock in a downtrend; avoid.", "None", "Further losses", (-5,-1,4), 'Speculative', 'Avoid'),
]

IPO_LIST = [
 # sym, name, ipo_date, ipo_price, sector, status
 ('ANT','Anthropic (Nasdaq: ANT; roadshow from Nov 10, pricing reported for Nov 18, raise reported at $75-100B)','2026-11-19',None,'ai','Roadshow'),
 ('BIAI','Bitari','2026-11-30',7.00,'ai','Expected'),
 ('FBLLU','Football Manager SPAC','2026-11-23',10.00,'fin','Expected'),
 ('YNTE','Primagrove ($4-6 range)','2026-11-16',None,'fin','Expected'),
 ('WWB','Windward Bio ($16-18 range)','2026-11-13',None,'hc','Expected'),
 ('RZRA','Rezera ($11-13 range)','2026-11-12',None,'hc','Expected'),
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
 ('2026-11-06T07:24','NBIS SPCX', "Via search snippet: says everyone is a long-term investor until volatility hits; still thinks Nebius could become the next hyperscaler and Rocket Lab the next SpaceX."),
 ('2026-11-05T20:52','IREN NBIS', "Via search snippet: highlights Galaxy's CEO buying more stock after pushing back on Texas data-centre worries, as a sign colocation executives see value."),
 ('2026-11-05T19:18','BE', "Via tracker: jokes that a new Google data centre running on Bloom fuel cells means the AI build-out is 'over', i.e. demand is still growing."),
 ('2026-11-05T09:19','NVDA AVGO MU', "Via search snippet: contrasts Citadel calling AI a bubble in October with saying 'the setup has improved' in November, as earnings beat and AI valuations compress."),
 ('2026-11-05T07:12','COHR', "Via tracker: pushes back on doubts about Coherent's co-packaged optics, citing management saying laser demand shows no slowdown."),
 ('2026-11-05T05:12','NVDA MU', "Via tracker: argues fears about Democratic data-centre rules are overdone, since build-outs grew under Biden and AI support is bipartisan. Says he added leverage into the drop (not advice)."),
 ('2026-11-05T04:58','AAOI COHR LITE MRVL CRDO', "Via tracker: says laser and indium-phosphide supply stays tight, and smaller laser makers' 2028 sales could exceed today's market values."),
 ('2026-11-05T02:36','INTC MU TSM', "Via tracker: points to an SEC filing showing Intel's CEO bought about $9.7M of stock near $65 after the steep fall."),
]

EVENTS = [
 ('2026-11-06','Macro','October jobs: +165K vs ~65K expected', "Unemployment 4.1%, wages +0.4%; Aug-Sep revised up 84K. Dec hike odds rose to ~78%. S&P +0.3% (week -2.7%), chips +3.6%."),
 ('2026-11-06','Fin','OCBC beats; STI falls 2.2%', "OCBC Q3 profit +3% to S$2.04B and loan-growth guidance raised. STI fell 117 points to 5,179 on the global chip selloff."),
 ('2026-11-06','Power','Vistra raises outlook; Moderna lifts guide', "Vistra +11% on a higher 2026 profit midpoint. Moderna +5% on 15-25% revenue growth guidance. IREN +20%."),
 ('2026-11-09','SGX','SGX shut for Deepavali', "SGX prices are from the Nov 6 close; first session after the US rebound is Nov 10."),
 ('2026-11-09','Macro','Relief rally: S&P +2.2%, Nasdaq-100 +3.1%', "Chip ETF +7% (AMD +12%, Coherent +18%), Dow +1,000, VIX ~20.5. WTI -3.5% to ~$88 after Trump said new Iran strikes are unlikely. Citi cut US stocks to neutral."),
 ('2026-11-09','AI','Nvidia -5% on CEO probe', "Board-led investigation into reports that Jensen Huang was targeted by foreign intelligence; board says no secrets compromised. House chairs asked for a briefing."),
 ('2026-11-09','Power','Constellation beats and raises', "Adj. EPS $5.06 vs $3.72; 2026 guide $12.50-12.80. NRG +11% on results and a $4B asset sale; Oklo +15% on a smaller loss."),
 ('2026-11-09','Mixed','After the close: Hims & Hers, Amaero', "Occidental and KKR also reported."),
 ('2026-11-10','Mixed','CoreWeave and Sea report; Anthropic roadshow starts', "TSMC October sales due around now."),
 ('2026-11-12','Mixed','Nebius, Applied Materials, Nu, Accelevation report', "Rezera IPO ($11-13) expected; Windward Bio ($16-18) on Nov 13."),
 ('2026-11-17','AI','Nvidia Q3 results', "The main AI-demand checkpoint this month, now with the CEO probe in the background. Klarna also reports."),
 ('2026-11-18','IPO','Anthropic IPO pricing (reported)', "Reported pricing after the close Nov 18, trading Nov 19 on Nasdaq as ANT; not confirmed by the company."),
 ('2026-11-25','SGX','IHH Q3 results', ""),
 ('2026-12-09','Macro','Fed rate decision', "Markets price a likely hike (~78% after the jobs report)."),
]
