# Analyst picks for 2026-11-13 (snapshot: US close Nov 12 ~15:55 ET, SGX close Nov 12). Fields: sym, thesis, catalyst, risk, (low, base, high) % expected move, conviction, setup
# Horizons: long = 12 months, swing = ~4 weeks, intraday = rest of session (US) / next session (SGX), ipo = 6 months.
# Context: Nov 12: Jensen Huang resigned as Nvidia CEO and director after reports of affairs; CFO Colette Kress is interim CEO. Nov 17 results still scheduled.
# NVDA fell as much as ~14% early, closed -4.3% at ~$166 on 4x normal volume. AMD +5.9%, Broadcom +5.6%, Arista +5.1% took the other side.
# Nebius -17%: Q3 revenue $981M (+571%) but a weaker 2026 outlook and bigger capex plans. CoreWeave -7%, Super Micro -11%.
# Close: S&P -0.35% to 7,592, Nasdaq -0.4% to 25,366, Dow -0.4%, Russell 2000 -1.7%. 10-yr 5.10% (30-yr 5.44%). Claims 200K. Daly: "further tightening will be needed".
# WTI ~$89 (+2.7%) on unverified Hormuz tanker reports; energy led. Bitcoin -3.7% to ~$71.5K. Applied Materials beat and guided Q1 above estimates after the close.
# STI -0.1% to 5,283; SGX tech fell (UMS -4%, AEM -3%), Geo Energy -6.5% despite a jump in Q3 profit. Anthropic IPO ~6x oversubscribed; Nasdaq debut expected Nov 19.
P = {}

# ---------- AI & chips ----------
P[('long','ai','US')] = [
 ('TSM', "Makes almost every leading AI chip, whoever designs it. October sales +60% y/y; about 17x forward earnings, 17% below its high. The Nvidia CEO change does not change TSMC's order book.",
  "November sales (~Dec 10); Q4 results Jan 14", "Taiwan geopolitics; overseas fabs dilute margins", (-18,17,38), 'High', 'Core holding'),
 ('AVGO', "Custom AI chips plus networking: revenue +86% at about 19x forward earnings, 24% below its high. Rose 5.6% on Nov 12 as buyers looked for AI exposure without Nvidia's leadership risk.",
  "Q4 results Dec 9", "Lumpy custom-chip orders; customer concentration", (-22,18,42), 'High', 'Leader, less key-person risk'),
 ('MU', "Memory is still the tightest part of AI servers: revenue +379% at about 4x forward earnings, 34% off its high. New contracts carry price floors.",
  "FQ1 results Dec 23", "Peak-cycle earnings; memory falls hard when prices turn", (-38,20,58), 'Medium', 'Cycle leader'),
 ('NVDA', "Revenue +106% at about 10x forward earnings, 31% off its high. Founder-CEO Jensen Huang resigned on Nov 12; CFO Colette Kress is interim CEO. The business is intact, but the stock now carries leadership risk, so the base case is cut.",
  "Q3 results Nov 17 (Kress's first call); permanent CEO choice", "Strategy and customer relationships without Huang; lawsuit; China", (-35,14,50), 'Speculative', 'Cheap, but leadership shock'),
 ('COHR', "Record quarter and a ~$20B five-year optics deal; 46% below its high at about 15x forward earnings.",
  "First $3B quarter targeted by FY27 end", "8% daily swings; capex keeps rising", (-32,20,55), 'Medium', 'Optics rebound'),
]
P[('long','ai','SGX')] = [
 ('AWX.SI', "AEM is up ~300% this year but 39% below its high; analysts see about 100% upside. Fell 3% with US chip names on Nov 12.",
  "Q3 business update (Nov)", "One large customer; 7% daily swings", (-38,18,55), 'Medium', 'SGX AI leader'),
 ('V03.SI', "Venture's Q3 profit rose 22%; RHB and DBS see S$22-23. Net cash, about 16x earnings, low volatility. Gave back 2.7% on Nov 12.",
  "Analyst upgrades after Q3", "Slow revenue growth (+7%)", (-12,13,26), 'High', 'Steady value'),
 ('558.SI', "UMS makes precision parts for chip-equipment makers: revenue +61%, 39% off its high, about 18x earnings. Applied Materials beat and guided higher on Nov 12.",
  "Applied Materials' upbeat outlook", "Tied to Applied Materials spending", (-30,16,45), 'Medium', 'Equipment supplier'),
 ('5DD.SI', "Micro-Mechanics makes precision tools for chip assembly and test: revenue +45%, 40% off its high.",
  "Q1 FY27 results (Nov)", "Small and thinly traded", (-24,14,36), 'Medium', 'Growth at a discount'),
 ('E28.SI', "Frencken builds modules for chip and medical equipment; 48% off its high at about 16x earnings.",
  "Q3 business update (Nov)", "Flat revenue so far this year", (-25,13,36), 'Medium', 'Recovery'),
]
P[('swing','ai','US')] = [
 ('AVGO', "Up 25% in five days and +5.6% on Nov 12 as money rotated out of Nvidia into other AI chip leaders; RSI 62, not yet stretched.",
  "Q4 results Dec 9", "Sharp reversal if AI spending fears return", (-12,6,18), 'Medium', 'Relative strength'),
 ('LITE', "Marvell is buying Lumentum for 4.5 Marvell shares each. At snapshot prices that is worth about 19% more than LITE's price.",
  "Spread narrows if the deal clears", "Regulatory delay (incl. China); MRVL falls again", (-15,8,22), 'Medium', 'Merger spread'),
 ('NVDA', "RSI 24 on 4x normal volume after the CEO resignation; recovered from -14% to -4% by the close. Results on Nov 17 are the next test.",
  "Q3 results Nov 17", "Weak guidance or more leadership news", (-18,6,22), 'Speculative', 'Oversold into earnings'),
 ('MU', "RSI 44 after a 13% monthly drop; memory shortage persists.",
  "Price-floor contracts; FQ1 results Dec 23", "Fast reversal if AI capex fears return", (-15,7,22), 'Medium', 'Rebound'),
 ('ANET', "Arista rose 5% to within 5% of its high; revenue +59%. AI networking gains when buyers spread spending away from Nvidia systems.",
  "AI networking orders", "About 34x earnings; profit-taking", (-10,5,14), 'Medium', 'Near-high momentum'),
]
P[('swing','ai','SGX')] = [
 ('558.SI', "UMS fell 4% (RSI 36), but its biggest customer Applied Materials beat and guided above estimates after the US close.", "Applied Materials results read-across", "Chip-equipment sentiment", (-15,6,20), 'Medium', 'Oversold with catalyst'),
 ('V03.SI', "Venture gave back 2.7% after its post-results jump; RSI 43.", "Analyst upgrades", "Low growth", (-6,4,10), 'High', 'Post-earnings drift'),
 ('AWX.SI', "AEM is down 32% in a month (RSI 38).",
  "Q3 update; US chips stabilising", "Bounce fades if Nvidia falls on results", (-20,6,26), 'Speculative', 'Oversold rebound'),
 ('E28.SI', "Frencken RSI 37 after a 2% drop.", "Q3 business update (Nov)", "No clear catalyst before results", (-14,5,16), 'Speculative', 'Oversold rebound'),
 ('5DD.SI', "Micro-Mechanics RSI 39.", "Q1 FY27 results (Nov)", "Thin order book", (-12,4,14), 'Medium', 'Rebound'),
]
P[('intraday','ai','US')] = [
 ('AMAT', "Record $10.41B revenue and EPS $4.16 beat; Q1 guide ~$11.1B vs ~$10.8B expected. Fell 3.5% before the report.", "Results reaction", "China export rules; options priced ~10%", (-6,1,7), 'Medium', 'Earnings reaction'),
 ('NVDA', "Day two after the CEO resignation; closed well off the lows on huge volume.", "Stabilisation bid", "New allegations or exits", (-6,0.5,6), 'Speculative', 'Headline risk'),
 ('NBIS', "Fell 17% on a weaker 2026 outlook and higher capex.", "Bounce after a flush", "Follow-through selling; analyst cuts", (-8,0,8), 'Speculative', 'Post-earnings flush'),
 ('AMD', "Rose 5.9% on 1.7x volume as the main Nvidia alternative.", "Momentum", "Profit-taking; up 173% this year", (-5,0,5), 'Speculative', 'Momentum check'),
 ('CRWV', "Fell 7% after a 25% jump; Nebius' outlook hurt neoclouds.", "Bounce", "Debt-funding worries", (-8,0,8), 'Speculative', 'Range'),
]
P[('intraday','ai','SGX')] = [
 ('558.SI', "Fell 4%; Applied Materials beat after the US close.", "Next session", "Read-across fades", (-4,0.5,4.5), 'Speculative', 'Gap watch'),
 ('AWX.SI', "Fell 3.3%.", "Next session", "US chips weak", (-5,0.3,5), 'Speculative', 'Bounce watch'),
 ('V03.SI', "Fell 2.7%.", "Next session", "Profit-taking", (-2,0.3,2.2), 'Medium', 'Range'),
 ('E28.SI', "Fell 2.1%.", "Next session", "Follows US chip equipment", (-3.5,0.3,3.5), 'Speculative', 'Bounce watch'),
 ('5DD.SI', "Fell 2.5%.", "Next session", "Thin trading", (-3,0.2,3), 'Medium', 'Range'),
]

# ---------- Health ----------
P[('long','hc','US')] = [
 ('LLY', "Obesity-drug leader: revenue +39%, at its high (+33% this year). Little analyst upside left, so the base case is modest.",
  "Orforglipron launch; Q4 results (Feb)", "Drug-price policy under the new Congress", (-16,8,25), 'High', 'Defensive growth'),
 ('ARGX', "argenx: revenue +52% from its immune-disease drug Vyvgart, 7% off its high, 17% analyst upside.",
  "New indications in 2027", "Competition in myasthenia gravis", (-15,10,28), 'Medium', 'Growth leader'),
 ('MDGL', "Madrigal's liver drug Rezdiffra is growing fast (revenue +50%); 30% off its high with 62% analyst upside.",
  "Script data; EU rollout", "Competition from GLP-1 drugs", (-22,20,45), 'Medium', 'Oversold growth'),
 ('INSM', "Insmed's lung drug launch drives revenue +268%; up 21% in a month but still 44% off its high, 65% analyst upside.",
  "Brensocatib launch numbers", "Expensive on near-term earnings", (-30,18,48), 'Medium', 'Launch story'),
 ('ALNY', "Alnylam is 67% off its high at about 15x forward earnings (RSI 19); analysts see 92% upside.",
  "Amvuttra script data", "Trend still down", (-30,18,50), 'Speculative', 'Deep value'),
]
P[('long','hc','SGX')] = [
 ('Q0F.SI', "IHH runs hospitals across Asia; analysts see 38% upside. Oversold (RSI 24) before results.", "Q3 results Nov 25", "Currency swings", (-12,12,25), 'Medium', 'Regional leader'),
 ('C2PU.SI', "Parkway Life REIT: steady hospital and nursing-home rents, 6% off its high.", "Dividend", "US 10-yr yield above 5%", (-8,7,15), 'High', 'Income'),
 ('AP4.SI', "Riverstone makes cleanroom and medical gloves at about 14x earnings with 38% analyst upside.", "Q3 results (Nov)", "Glove price competition", (-15,11,28), 'Medium', 'Value'),
 ('BSL.SI', "Raffles Medical: Singapore hospital group, 21% off its high and in a mild uptrend (RSI 72).", "Results (Feb)", "Shrinking revenue (-7%)", (-10,8,18), 'Medium', 'Recovery'),
 ('H02.SI', "Haw Par (Tiger Balm) trades near 10x earnings with a large cash and investment pile.", "Results (Feb)", "Revenue down 8%", (-12,6,16), 'Medium', 'Value'),
]
P[('swing','hc','US')] = [
 ('ALNY', "Deeply oversold (RSI 19), 67% off its high; fell 2% on Nov 12.", "Amvuttra script data", "Trend still down", (-15,7,22), 'Speculative', 'Oversold rebound'),
 ('MDGL', "Pulled back 2% after a 6% weekly gain; 62% analyst upside.", "Script data", "Rotation back to tech", (-12,6,18), 'Medium', 'Rebound'),
 ('LLY', "Near its high; steady leader while AI stocks swing on Nvidia news.", "Orforglipron news", "Money rotating back into chips", (-8,3,10), 'High', 'Relative strength'),
 ('REGN', "Regeneron is up 22% in a month to near its high, at about 14x forward earnings with revenue +36%.", "Pipeline updates", "Overbought (RSI 73)", (-9,3,11), 'Medium', 'Trend'),
 ('CYTK', "Cytokinetics' heart drug launch is starting; 36% off its high, 95% analyst upside. Fell 4% on Nov 12 (RSI 39).", "Launch numbers", "Launch slower than hoped", (-14,6,20), 'Speculative', 'Launch rebound'),
]
P[('swing','hc','SGX')] = [
 ('C2PU.SI', "Parkway Life REIT: lowest-volatility name in the group.", "Dividend", "Rates", (-4,2,6), 'High', 'Range'),
 ('BSL.SI', "Raffles Medical rose again (RSI 72).", "Momentum", "Low volume; overbought", (-5,2,7), 'Medium', 'Trend'),
 ('Q0F.SI', "IHH is oversold (RSI 24) ahead of Q3 results.", "Q3 results Nov 25", "Results miss", (-6,3,9), 'Medium', 'Pre-earnings'),
 ('AP4.SI', "Riverstone steady (RSI 61); large analyst upside.", "Q3 results (Nov)", "Glove prices", (-8,3,10), 'Medium', 'Support'),
 ('QC7.SI', "Q&M Dental is very oversold (RSI 17).", "Bounce", "Small cap", (-8,3,10), 'Speculative', 'Oversold rebound'),
]
P[('intraday','hc','US')] = [
 ('MRNA', "Fell 7% as gene and vaccine names were sold; still far above analyst targets.", "Dip buying", "Analysts see ~30% downside to targets", (-6,0,6), 'Speculative', 'Extended'),
 ('CRSP', "Fell 6.8% on 1.6x normal volume (RSI 37).", "Bounce", "Small-cap risk-off (Russell -1.7%)", (-5,0.3,5), 'Speculative', 'Bounce watch'),
 ('HIMS', "Fell 5% to RSI 32; FTC lawsuit still weighs.", "Oversold", "Legal headlines", (-7,0,7), 'Speculative', 'Bounce watch'),
 ('ALNY', "RSI 19.", "Bounce", "Trend down", (-4,0.3,4), 'Speculative', 'Bounce watch'),
 ('LLY', "Flat near its high.", "Defensive bid", "Rotation into tech", (-2.2,0.2,2.2), 'Medium', 'Range'),
]
P[('intraday','hc','SGX')] = [
 ('C2PU.SI', "Flat; steady REIT.", "Next session", "Small range", (-1,0.2,1), 'Medium', 'Range'),
 ('BSL.SI', "Rose 0.6%; mild uptrend.", "Next session", "Small range", (-1.5,0.3,1.5), 'Medium', 'Relative strength'),
 ('AP4.SI', "Flat.", "Next session", "Thin trading", (-2,0.2,2), 'Medium', 'Range'),
 ('H02.SI', "Fell 0.6%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('Q0F.SI', "RSI 24.", "Next session", "Malaysia market swings", (-2,0.3,2), 'Medium', 'Bounce watch'),
]

# ---------- Finance ----------
P[('long','fin','US')] = [
 ('JPM', "Best-run US bank, 6% off its high at about 13.5x forward earnings. Higher rates (10-yr 5.1%) support interest income.", "Q4 results Jan 14", "Credit cycle", (-15,8,22), 'High', 'Core holding'),
 ('V', "Visa: steady growth (+13%), near its high; little AI exposure.", "Holiday spending", "Regulation of card fees", (-12,6,18), 'High', 'Defensive growth'),
 ('GS', "Trading and deal-making boom, about 12.4x forward earnings, 21% off its high. Co-leads Anthropic's IPO, now about six times oversubscribed.",
  "Anthropic IPO (debut expected Nov 19)", "Market volatility hits deals", (-20,10,28), 'Medium', 'Cyclical value'),
 ('NU', "Nubank: revenue +52% at about 11x forward earnings, 37% off its high (RSI 22).", "Q3 results (due Nov 12)", "Brazil credit and currency", (-30,18,50), 'Medium', 'Growth at a discount'),
 ('SE', "Sea: Q3 revenue +43%; $1B buyback. About 15x forward earnings, 49% off its high; held up on Nov 12.",
  "Q4 results (Mar)", "Rising credit costs at Monee; competition", (-30,20,52), 'Medium', 'Oversold growth'),
]
P[('long','fin','SGX')] = [
 ('D05.SI', "DBS kept its 81-cent quarterly dividend and says interest income has bottomed; 10% off its high.",
  "Q4 results (Feb)", "Margins if rates fall; stronger SGD", (-10,8,16), 'High', 'Income leader'),
 ('O39.SI', "OCBC was the only local bank to beat in Q3 and raised loan-growth guidance.",
  "Q4 results (Feb)", "Margin fell 18 bp to 1.66%", (-10,7,15), 'Medium', 'Income'),
 ('U11.SI', "UOB missed Q3 and cut its margin guidance; RSI 18, 16% off its high.", "Recovery in fees", "More credit provisions", (-12,8,18), 'Medium', 'Oversold income'),
 ('AIY.SI', "iFAST: fintech platform, revenue +23%, 27% off its high with 42% analyst upside.", "HK pension business", "Market-driven volumes", (-18,17,36), 'Medium', 'Growth'),
 ('S68.SI', "SGX benefits from high trading volumes; from Jan 2027 its RegCo takes over IPO prospectus reviews.", "Monthly volume data", "Already priced (25x earnings)", (-12,7,18), 'Medium', 'Volatility winner'),
]
P[('swing','fin','US')] = [
 ('NU', "Oversold (RSI 22) and fell 4% into its Q3 report.", "Results reaction", "Brazil credit", (-15,6,20), 'Speculative', 'Earnings reaction'),
 ('GS', "Anthropic IPO is ~6x oversubscribed with a Nasdaq debut expected Nov 19.", "Deal fees", "Volatility", (-8,4,12), 'Medium', 'Deal pipeline'),
 ('HOOD', "RSI 33 after a 3.8% drop with bitcoin; retail access to the Anthropic IPO runs partly through Robinhood.", "Anthropic IPO demand", "Crypto weakness; higher rates", (-16,6,22), 'Speculative', 'Oversold rebound'),
 ('IBKR', "Up 12% in five days; 17% off its high, about 25x forward earnings.", "Monthly brokerage metrics", "Rates and crypto swings", (-10,4,13), 'Medium', 'Relative strength'),
 ('SE', "Holding after a revenue beat and EPS miss; $1B buyback.", "Buyback; analyst updates", "Credit costs", (-12,5,16), 'Medium', 'Post-earnings'),
]
P[('swing','fin','SGX')] = [
 ('D05.SI', "DBS is oversold (RSI 24) and flat on a weak day.", "Dividend support", "Margin worries", (-4,3,7), 'High', 'Oversold income'),
 ('U11.SI', "UOB RSI 18 after its Q3 miss; rose 0.6%.", "Rebound", "Further downgrades", (-5,3,8), 'Medium', 'Oversold rebound'),
 ('O39.SI', "OCBC eased 0.4%.", "Post-results recovery", "Margin squeeze", (-4,2,6), 'Medium', 'Range'),
 ('AIY.SI', "iFAST is holding up (RSI 52).", "Momentum", "Market-driven", (-8,3,10), 'Medium', 'Range'),
 ('S68.SI', "SGX benefits when markets are volatile.", "Volume data", "Valuation", (-5,2,7), 'Medium', 'Volatility winner'),
]
P[('intraday','fin','US')] = [
 ('NU', "First session after Q3 results; RSI 22 going in.", "Results", "Brazil credit", (-8,0.5,8), 'Speculative', 'Earnings reaction'),
 ('COIN', "Fell 4% as bitcoin dropped below $72K (RSI 28).", "Crypto bounce", "More crypto selling", (-5,0,5), 'Speculative', 'Crypto beta'),
 ('HOOD', "Fell 3.8% (RSI 33).", "Anthropic IPO interest", "Crypto weakness", (-4,0.3,4), 'Speculative', 'Bounce watch'),
 ('GS', "Fell 1.4%; Anthropic book strong.", "IPO fees", "Market risk-off", (-2,0.2,2), 'Medium', 'Range'),
 ('JPM', "Little changed; banks steady.", "Higher rates", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
]
P[('intraday','fin','SGX')] = [
 ('D05.SI', "Flat; RSI 24.", "Next session", "Market-wide risk-off", (-1.2,0.3,1.4), 'High', 'Bounce watch'),
 ('U11.SI', "Rose 0.6%; still oversold.", "Next session", "Trend down", (-1.5,0.3,1.6), 'Medium', 'Bounce watch'),
 ('G07.SI', "Great Eastern rose 1.4% on above-normal volume.", "Next session", "Thin trading", (-1.5,0.2,1.5), 'Medium', 'Momentum check'),
 ('O39.SI', "Fell 0.4%.", "Next session", "Small range", (-1.3,0.2,1.3), 'Medium', 'Range'),
 ('S68.SI', "Flat.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
]

# IPO tab (6-month view), all markets
P[('ipo','all','US')] = [
 ('SPCX', "SpaceX listed in June at $135 and trades about 4% above that, 34% under its high. Reports of merger talks with Tesla; analysts see large upside.",
  "xAI/GPU news; NASA lunar awards; lock-up expiries", "Valuation, Musk headlines and data-centre policy", (-35,12,45), 'Medium', 'Mega-cap IPO'),
 ('CHYM', "Chime (IPO $27) trades about 22% above its IPO price, near its high (RSI 71).",
  "Member growth", "Fintech credit cycle", (-15,10,28), 'Medium', 'Post-IPO uptrend'),
 ('ACCV', "Accelevation (IPO $18) makes electrical gear for data centres: revenue +80% at about 13x forward earnings, 33% below its IPO price. Up 22% in five days.",
  "First results as a public company (due Nov 12)", "Data-centre policy risk; 9% daily swings", (-40,12,55), 'Speculative', 'Post-IPO value'),
 ('KLAR', "Klarna (IPO $40) is 68% below its IPO price at about 16x forward earnings; revenue +27%. Fell 5.7% on Nov 12.",
  "Q3 results Nov 17", "Buy-now-pay-later credit losses", (-22,15,40), 'Speculative', 'Deep value'),
 ('FIG', "Figma: revenue +43% with AI products, but 43% below its IPO price (RSI 26).",
  "AI product monetisation", "Software multiples falling; Anthropic's new office tools", (-30,8,38), 'Speculative', 'Post-earnings dip'),
]

# ---------- Power & grid (data-center power) ----------
P[('long','pwr','US')] = [
 ('GEV', "GE Vernova: gas turbines and grid gear sold out for years, revenue +27%. 30% off its high with 44% analyst upside.", "Q4 results Jan 27", "Data-centre policy; valuation (32x)", (-25,15,40), 'High', 'Quality at a discount'),
 ('CEG', "Constellation beat Q3 and raised 2026 guidance; up 18% in five days and +2.8% on Nov 12, still 25% off its high.", "Buyback update; new long-term power deals", "Data-centre politics; PJM rules", (-22,14,34), 'High', 'Beat and raise'),
 ('ETN', "Eaton: electrical gear for data centres and utilities, 22% off its high at about 22x earnings.", "Q4 results Feb 2", "Data-centre orders slowing", (-20,13,33), 'Medium', 'Quality at a discount'),
 ('VRT', "Vertiv: data-centre cooling and power, revenue +61% at about 22x forward earnings, 44% off its high. Rose 1.5% on a weak day for AI.", "Order backlog updates", "Most exposed to a data-centre slowdown", (-35,18,52), 'Medium', 'Oversold growth'),
 ('PWR', "Quanta builds the grid: revenue +57%, 23% off its high.", "Utility capex plans", "Data-centre policy", (-25,12,34), 'Medium', 'Grid builder'),
]
P[('long','pwr','SGX')] = [
 ('BN4.SI', "Keppel: power, data centres and asset management, about 16x earnings with 29% analyst upside.", "Asset sales", "Execution", (-12,12,25), 'Medium', 'Value'),
 ('U96.SI', "Sembcorp: power and renewables at about 9x earnings.", "New contracts", "Power prices", (-12,7,18), 'Medium', 'Value'),
 ('DCRU.SI', "Digital Core REIT: US data-centre REIT, about 9x earnings with 55% analyst upside. Fell 3.3% on heavy volume.", "Leasing news", "Tenant concentration; US rates above 5%", (-14,12,28), 'Medium', 'Deep value'),
 ('AJBU.SI', "Keppel DC REIT: data-centre rents, 10% off its high.", "Dividend", "Rates", (-10,7,17), 'Medium', 'Income'),
 ('544.SI', "CSE Global: electrification and data-centre work, about 11x earnings, 50% off its high.", "New orders", "Small and volatile", (-30,18,50), 'Speculative', 'Recovery'),
]
P[('swing','pwr','US')] = [
 ('TLN', "Talen's new 750 MW capacity deal keeps it rising: +22% in five days, about 12.5x forward earnings.", "Analyst target updates", "Overbought after the jump (RSI 67)", (-12,5,16), 'Medium', 'New-contract momentum'),
 ('CEG', "Up 18% in five days and rose again on a down day for the market.", "Analyst target updates", "Data-centre politics; higher yields", (-12,6,18), 'Medium', 'Post-earnings drift'),
 ('NRG', "Strong Q3 and a $4B asset sale; about 10x earnings with 68% analyst upside. Up 22% in five days.", "Analyst updates", "Texas data-centre proposal", (-15,6,20), 'Medium', 'Post-earnings drift'),
 ('VRT', "Held gains (+1.5%) while AI hardware sold off.", "Order updates", "Rates; 7% daily swings", (-15,6,20), 'Medium', 'Relative strength'),
 ('VST', "Raised its 2026 outlook on Nov 6; up 19% in five days, 51% analyst upside.", "Analyst updates", "Texas data-centre proposal", (-14,6,20), 'Medium', 'Post-earnings drift'),
]
P[('swing','pwr','SGX')] = [
 ('544.SI', "CSE Global gave back 3.3% (RSI 47).", "New orders", "Small cap", (-15,5,18), 'Speculative', 'Rebound'),
 ('BN4.SI', "Keppel eased 0.5% (RSI 45).", "Asset-sale news", "Execution", (-5,3,8), 'Medium', 'Range'),
 ('U96.SI', "Sembcorp RSI 36.", "Contracts", "Power prices", (-5,2,7), 'Medium', 'Oversold rebound'),
 ('DCRU.SI', "Digital Core REIT fell 3.3% on 2.6x normal volume.", "Support", "US data-centre worries", (-7,2,8), 'Medium', 'Dip'),
 ('AJBU.SI', "Keppel DC REIT steady near overbought (RSI 70).", "Momentum", "Overbought", (-5,1,6), 'Medium', 'Trend'),
]
P[('intraday','pwr','US')] = [
 ('CEG', "Rose 2.8%; up 18% in five days.", "Momentum", "Profit-taking", (-3,0.3,3), 'Medium', 'Momentum check'),
 ('SMR', "Fell 8% with small caps.", "Bounce", "Cash burn; rate-sensitive", (-7,0,7), 'Speculative', 'Bounce watch'),
 ('OKLO', "Fell 5.5% after a 27% weekly run.", "Bounce", "Rate-sensitive", (-7,0,7), 'Speculative', 'Range'),
 ('BE', "Fell 3.6% after a big week.", "Momentum", "8% daily swings", (-6,0,6), 'Speculative', 'Range'),
 ('TLN', "Rose 2.1%.", "Follow-through", "Profit-taking", (-3.5,0.3,3.5), 'Medium', 'Momentum check'),
]
P[('intraday','pwr','SGX')] = [
 ('DCRU.SI', "Fell 3.3% on heavy volume.", "Next session", "More selling", (-2,0.3,2), 'Medium', 'Bounce watch'),
 ('544.SI', "Fell 3.3%.", "Next session", "Small cap", (-4,0.2,4), 'Speculative', 'Range'),
 ('BN4.SI', "Fell 0.5%.", "Next session", "Small range", (-1.6,0.2,1.6), 'Medium', 'Range'),
 ('U96.SI', "Fell 0.9%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('AJBU.SI', "Flat.", "Next session", "Small range", (-1.2,0.2,1.2), 'Medium', 'Range'),
]

# ---------- Defence & industrials ----------
P[('long','def','US')] = [
 ('GE', "GE Aerospace: jet-engine services boom, revenue +16%, 13% off its high after a 3.5% drop on Nov 12.", "Q4 results Jan 21", "Valuation (36x)", (-15,10,26), 'High', 'Quality'),
 ('RTX', "RTX: missiles and engines, revenue +11%, steady.", "Q4 results Jan 26", "Engine issues", (-12,10,24), 'High', 'Core defence'),
 ('LHX', "L3Harris: space and missile sensors, 28% off its high, 24% analyst upside.", "Golden Dome contracts", "Budget fights with a split government", (-15,12,30), 'Medium', 'Value'),
 ('HWM', "Howmet: jet-engine parts, revenue +29%, 24% off its high.", "Aerospace build rates", "Valuation (34x)", (-20,14,34), 'Medium', 'Growth at a discount'),
 ('NOC', "Northrop: B-21 and missile defence, about 18x earnings, 29% off its high.", "Golden Dome contracts", "Budget fights", (-15,11,28), 'Medium', 'Value'),
]
P[('long','def','SGX')] = [
 ('S63.SI', "ST Engineering: defence and aerospace, revenue +11%; oversold (RSI 36) and 15% off its high.", "Contract wins", "Valuation (25x)", (-10,12,24), 'High', 'Quality'),
 ('BS6.SI', "Yangzijiang Shipbuilding: about 7x earnings, revenue +36%, 26% analyst upside. Fell 4.3% on Nov 12.", "New ship orders", "US port fees on Chinese ships", (-18,13,32), 'Medium', 'Value'),
 ('S59.SI', "SIA Engineering: aircraft maintenance, 22% off its high, 27% analyst upside; rose 2.8%.", "Air travel", "Revenue falling (-11%)", (-10,11,24), 'Medium', 'Recovery'),
 ('C52.SI', "ComfortDelGro: steady transport earnings at about 14x.", "Overseas contracts", "Slow growth", (-8,8,16), 'Medium', 'Steady'),
 ('H22.SI', "Hong Leong Asia: engines and building materials at about 8.5x earnings, 47% off its high.", "Results (Feb)", "China demand", (-25,22,50), 'Speculative', 'Deep value'),
]
P[('swing','def','US')] = [
 ('CAT', "Caterpillar is 43% off its high (RSI 36); rose 0.6% on a down day.", "Rebound", "Data-centre generator orders slowing", (-12,6,18), 'Medium', 'Oversold rebound'),
 ('AXON', "Down 20% in five days after a Q3 miss (RSI 21); 76% analyst upside.", "Analyst updates", "More downgrades", (-18,6,22), 'Speculative', 'Post-earnings dip'),
 ('LMT', "Up 16% in a month; steady defence bid.", "Contracts", "Budget fights", (-7,3,9), 'Medium', 'Trend'),
 ('BA', "Boeing 32% off its high (RSI 33); production recovering.", "Monthly deliveries", "Quality issues; staff cuts", (-10,5,15), 'Medium', 'Recovery'),
 ('AVAV', "AeroVironment 69% off its high; up 18% in five days.", "Drone orders; results Dec 2", "Volatile", (-18,6,22), 'Speculative', 'Rebound'),
]
P[('swing','def','SGX')] = [
 ('S63.SI', "ST Engineering oversold (RSI 36).", "Bounce", "Low volatility", (-4,3,8), 'High', 'Oversold rebound'),
 ('BS6.SI', "Yangzijiang fell 4.3% to RSI 33; about 7x earnings.", "Orders", "Trade fees", (-8,4,12), 'Medium', 'Oversold rebound'),
 ('H22.SI', "Hong Leong Asia fell 4.2% to RSI 26.", "Bounce", "China demand", (-10,4,12), 'Speculative', 'Oversold rebound'),
 ('S59.SI', "SIA Engineering rose 2.8% on above-normal volume.", "Air travel", "Slow growth", (-6,2,7), 'Medium', 'Rebound'),
 ('C52.SI', "ComfortDelGro steady (RSI 60).", "Support", "Slow growth", (-4,1.5,5), 'Medium', 'Range'),
]
P[('intraday','def','US')] = [
 ('GE', "Fell 3.5% from near its high.", "Dip buying", "More profit-taking", (-2.5,0.3,2.5), 'Medium', 'Dip watch'),
 ('KTOS', "Fell 5.3%.", "Drone contracts", "Volatile", (-4.5,0,4.5), 'Speculative', 'Bounce watch'),
 ('AXON', "Fell 2.6% to RSI 21.", "Bounce", "More selling", (-5,0.3,5), 'Speculative', 'Bounce watch'),
 ('CAT', "Rose 0.6% (RSI 36).", "Bounce", "Rotation back to tech", (-3,0.3,3), 'Medium', 'Range'),
 ('LMT', "Fell 1%.", "Defence bid", "Rotation into tech", (-2.2,0.2,2.2), 'Medium', 'Range'),
]
P[('intraday','def','SGX')] = [
 ('BS6.SI', "Fell 4.3%.", "Next session", "Trade fees", (-2.5,0.3,2.8), 'Medium', 'Bounce watch'),
 ('H22.SI', "Fell 4.2%.", "Next session", "Thin trading", (-3,0.3,3), 'Speculative', 'Bounce watch'),
 ('S59.SI', "Rose 2.8%.", "Next session", "Gives back gains", (-1.5,0.2,1.5), 'Medium', 'Follow-through check'),
 ('S63.SI', "Rose 0.3%.", "Next session", "Small range", (-1.5,0.3,1.8), 'Medium', 'Range'),
 ('C52.SI', "Flat.", "Next session", "Small range", (-1,0.2,1), 'Medium', 'Range'),
]

# ---------- Energy (oil and gas) ----------
P[('long','nrg','US')] = [
 ('CVX', "Chevron: revenue +35%, about 13x earnings, 8% off its high.", "Hess integration; buybacks", "Oil falls if Gulf tensions ease", (-16,8,24), 'High', 'Core energy'),
 ('XOM', "Exxon: steady cash flow, about 13.6x earnings.", "Buybacks", "Oil price drop", (-15,7,21), 'High', 'Core energy'),
 ('FANG', "Diamondback: low-cost Permian producer at about 8x earnings, 30% analyst upside.", "Buybacks", "Oil price drop", (-22,13,33), 'Medium', 'Value'),
 ('LNG', "Cheniere: US gas exports on long contracts; less tied to oil. Up 11% in a month.", "New export capacity", "Gas price swings", (-15,9,26), 'Medium', 'Steady'),
 ('COP', "ConocoPhillips: about 12x earnings, revenue +29%.", "Buybacks", "Oil price drop", (-18,8,24), 'Medium', 'Value'),
]
P[('long','nrg','SGX')] = [
 ('5E2.SI', "Seatrium builds offshore rigs and wind platforms; 38% analyst upside.", "New orders", "Contract delays", (-15,12,28), 'Medium', 'Recovery'),
 ('BN4.SI', "Keppel: energy infrastructure and asset management.", "Asset sales", "Execution", (-12,10,22), 'Medium', 'Value'),
 ('RE4.SI', "Geo Energy: Indonesian coal at about 7x earnings. Q3 profit rose to $20.6M from $3.2M, yet the stock fell 6.5%.", "Coal prices", "Coal price drop", (-25,10,32), 'Speculative', 'Value'),
 ('5LY.SI', "Marco Polo Marine: offshore vessels, revenue +40% at about 11x earnings.", "Results (Nov)", "Thin trading", (-25,10,35), 'Speculative', 'Growth value'),
 ('5WH.SI', "Rex International is in a long downtrend (-62% this year); no setup.", "None", "Further losses", (-30,-5,20), 'Speculative', 'Avoid'),
]
P[('swing','nrg','US')] = [
 ('OXY', "Occidental rose 2% on 1.8x normal volume from RSI 29 as oil jumped.", "Oil near $89", "Debt; oil price", (-10,5,14), 'Medium', 'Oversold rebound'),
 ('DVN', "Devon rose 2.9% from RSI 34; about 9x earnings, 32% analyst upside.", "Buybacks; oil", "Oil price drop", (-12,5,15), 'Medium', 'Oversold rebound'),
 ('MPC', "Marathon Petroleum rose 2.5% from RSI 38.", "Refining margins", "Costlier crude squeezes margins", (-10,4,14), 'Medium', 'Oversold rebound'),
 ('FANG', "Diamondback oversold (RSI 27).", "Buybacks; oil", "Oil price drop", (-11,4,13), 'Medium', 'Oversold rebound'),
 ('CVX', "Chevron oversold (RSI 30) with oil rising on Gulf risk.", "Oil", "Gulf calm returns", (-7,3,9), 'Medium', 'Oversold rebound'),
]
P[('swing','nrg','SGX')] = [
 ('RE4.SI', "Geo Energy fell 6.5% despite a much higher Q3 profit.", "Coal prices; results digestion", "Profit-taking", (-10,4,14), 'Speculative', 'Post-results dip'),
 ('5E2.SI', "Seatrium fell 2% toward support.", "Orders", "Delays", (-8,3,10), 'Medium', 'Support'),
 ('BN4.SI', "Keppel eased 0.5%.", "Asset sales", "Execution", (-5,3,8), 'Medium', 'Range'),
 ('5LY.SI', "Marco Polo Marine fell 4%.", "Results", "Thin trading", (-10,3,12), 'Speculative', 'Range'),
 ('5WH.SI', "Rex International: no setup.", "None", "Further losses", (-12,-2,8), 'Speculative', 'Avoid'),
]
P[('intraday','nrg','US')] = [
 ('DVN', "Rose 2.9%.", "Oil follow-through", "Oil reversal", (-3,0.3,3), 'Medium', 'Momentum check'),
 ('OXY', "Rose 2% on heavy volume.", "Oil", "Oil reversal", (-2.5,0.3,2.5), 'Medium', 'Momentum check'),
 ('MPC', "Rose 2.5%.", "Momentum", "Margins", (-3,0.2,3), 'Medium', 'Momentum check'),
 ('XOM', "Rose 1.8%; WTI near $89.", "Oil", "Hormuz reports prove false", (-2,0.2,2), 'Medium', 'Range'),
 ('HAL', "Flat; lagged oil.", "Catch-up", "Oil reversal", (-2.5,0.2,2.5), 'Medium', 'Range'),
]
P[('intraday','nrg','SGX')] = [
 ('RE4.SI', "Fell 6.5% after results.", "Next session", "More selling", (-3,0.3,3.5), 'Speculative', 'Bounce watch'),
 ('5LY.SI', "Fell 4.2%.", "Next session", "Thin trading", (-4,0,4), 'Speculative', 'Range'),
 ('5E2.SI', "Fell 2.2%.", "Next session", "Small range", (-2,0.2,2), 'Medium', 'Range'),
 ('BN4.SI', "Fell 0.5%.", "Next session", "Small range", (-1.6,0.2,1.6), 'Medium', 'Range'),
 ('5WH.SI', "Penny stock in a downtrend; avoid.", "None", "Further losses", (-5,-1,4), 'Speculative', 'Avoid'),
]

IPO_LIST = [
 # sym, name, ipo_date, ipo_price, sector, status
 ('ANT','Anthropic (Nasdaq: ANT; range $70-78, 825M shares, up to ~$64B; ~6x oversubscribed per Bloomberg; trading expected Nov 19)','2026-11-19',None,'ai','Roadshow'),
 ('BIAI','Bitari','2026-11-30',7.00,'ai','Expected'),
 ('FBLLU','Football Manager SPAC','2026-11-23',10.00,'fin','Expected'),
 ('YNTE','Primagrove ($4-6 range)','2026-11-16',None,'fin','Expected'),
 ('VVVV','vVardis ($21-24 range, ~$214M; dental tech; NYSE)','2026-11-13',None,'hc','Expected'),
 ('WWB','Windward Bio ($16-18 range, ~$175M; Nasdaq)','2026-11-13',None,'hc','Expected'),
 ('RZRA','Rezera ($11-13 range, ~$200M; Nasdaq)','2026-11-12',None,'hc','Expected'),
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
 ('2026-11-12T13:56','NVDA', "Via search excerpt: notes Jensen Huang has resigned despite strong support from staff and fans, calling it the end of an era for Nvidia."),
 ('2026-11-12T08:38','NVDA TSLA', "Via search excerpt: argues Huang is close to irreplaceable, comparing it to Tesla without Musk; credits him with the early CUDA bet and building the neocloud ecosystem."),
 ('2026-11-11T23:20','NVDA', "Via search excerpt: hopes Nvidia's board stands by Huang despite media and political pressure; says the AI trade won't end over this."),
 ('2026-11-11T05:42','CRWV NBIS', "Via search excerpt: reads CoreWeave's results as good news for Nebius and other neoclouds, quoting '10x as much qualified demand as available capacity'."),
 ('2026-11-10T10:50','GE', "Via search excerpt: highlights SoftBank's CFO denying it defaulted on turbine orders, as had been claimed online."),
 ('2026-11-09T14:59','LITE NBIS', "Via search excerpt: surprised that everything in the AI trade, from Lumentum to Nebius, rallied on the same day."),
 ('2026-11-08T17:35','COHR LITE POET', "Via tracker: calls the 'AI bubble' label lazy. Memory makers with price floors and optical firms near net cash look cheap; leveraged neoclouds are more bubble-prone."),
 ('2026-11-08T01:11','MU', "Via tracker: says Micron's new memory deals carry price floors and binding commitments, so old renegotiation fears don't apply."),
]

EVENTS = [
 ('2026-11-11','Macro','AI rally: S&P +1.3%, Nasdaq +1.6%', "S&P 7,619; Nasdaq 25,466. CoreWeave +25% after beating and raising. Bond market shut for Veterans Day."),
 ('2026-11-11','SGX','STI +0.6% to 5,290', "Venture +5.2% on a 22% Q3 profit rise; UMS +9%."),
 ('2026-11-12','AI','Jensen Huang resigns as Nvidia CEO', "Followed reports of affairs. CFO Colette Kress is interim CEO. NVDA fell as much as ~14%, closed -4.3% at ~$166. AMD +5.9%, Broadcom +5.6%."),
 ('2026-11-12','AI','Nebius -17% on weaker outlook', "Q3 revenue $981M (+571%), but a softer 2026 outlook and higher capex. CoreWeave -7%, Super Micro -11%."),
 ('2026-11-12','Macro','S&P -0.35%, Nasdaq -0.4%; 10-yr 5.10%', "S&P 7,592; Russell 2000 -1.7%. Jobless claims 200K. Fed's Daly: further tightening needed. Bitcoin below $72K."),
 ('2026-11-12','Energy','WTI ~$89 on Hormuz tanker reports', "Iran claims more tanker blasts (unverified). Energy stocks led the S&P."),
 ('2026-11-12','AI','Applied Materials beats', "Record Q4 revenue $10.41B; EPS $4.16 vs ~$4.06 expected. Q1 revenue guide ~$11.1B vs ~$10.8B expected. Cisco also reported after the close."),
 ('2026-11-12','SGX','STI -0.1% to 5,283', "Tech fell (UMS -4%, AEM -3%). Geo Energy -6.5% despite Q3 profit of $20.6M vs $3.2M a year ago."),
 ('2026-11-13','Macro','US PPI and more Fed speakers', "Markets price a Dec hike; two Fed officials have floated 50 bp."),
 ('2026-11-17','AI','Nvidia Q3 results', "First call under interim CEO Kress; the main AI-demand checkpoint. Klarna also reports."),
 ('2026-11-19','IPO','Anthropic expected to start trading (Nasdaq: ANT)', "Range $70-78; book ~6x oversubscribed per Bloomberg. Existing backers to get priority."),
 ('2026-11-25','SGX','IHH Q3 results', ""),
 ('2026-11-26','Macro','US Thanksgiving', "US stock market closed."),
 ('2026-12-01','AI','Marvell and Credo results', ""),
 ('2026-12-09','Macro','Fed rate decision (Dec 8-9)', "A hike is widely expected. Broadcom reports the same day."),
]
