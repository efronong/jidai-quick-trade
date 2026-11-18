# Analyst picks for 2026-11-19 SGT (snapshot: US Wed Nov 18 ~13:15 ET, SGX close Nov 18). Fields: sym, thesis, catalyst, risk, (low, base, high) % expected move, conviction, setup
# Horizons: long = 12 months, swing = ~4 weeks, intraday = rest of session (US) / next session (SGX), ipo = 6 months.
# Context: Wed Nov 18 close: Dow -561 (-1.1%), S&P -0.2% (fifth straight drop), Nasdaq +0.4%. Dollar at a 19-month high.
# FOMC minutes (Oct): almost all officials see further hikes as likely appropriate; a couple open to more than 25 bp in December.
# Nvidia gave up a pre-market gain and closed -2.9% the day after its beat and raise. AAOI -9.8% after filing a $550M at-the-market share sale.
# Health insurers sank on CMS's proposed "CRUSH" Medicare Advantage audit rule (extrapolated clawbacks back to 2018; comments to Jan 19, 2027):
# UNH -10.2%, HUM -13%, ELV -7.6%, CNC -7.1%. Energy weakest sector: WTI -4% to ~$82 on bigger-than-expected US crude and gasoline builds.
# Anthropic priced its IPO at $83 (above the $70-78 range): ~$68.5B plus a $26B private placement, ~$1.5T fully diluted; trades Thu Nov 19 (ANT).
# SGX: STI -1.06% to 5,054.89. Riverstone -4% (new CEO from Dec 1), ST Engineering -2.8%; AEM +3.3%, UMS +2.4%; Geo Energy +9% on ~30x normal volume.
P = {}

# ---------- AI & chips ----------
P[('long','ai','US')] = [
 ('TSM', "Makes almost every leading AI chip, whoever designs it. Revenue +51% at about 15x forward earnings, 26% below its high (RSI 33). Nvidia's $130B guide is a direct read-across for TSMC wafers.",
  "November sales (~Dec 10); Q4 results Jan 14", "Taiwan geopolitics; new US chip-access rules", (-20,16,38), 'High', 'Core holding'),
 ('AVGO', "Custom AI chips plus networking: revenue +86% at about 18x forward earnings, 27% below its high. Rose 2.7% while the market fell; results Dec 9.",
  "Q4 results Dec 9", "Lumpy custom-chip orders; AI financing worries", (-24,17,42), 'High', 'Leader, less key-person risk'),
 ('MU', "Memory is still the tightest part of AI servers: revenue +379% at about 3.4x forward earnings, 42% off its high. Nvidia's supply commitments jumped to $390B, mostly multi-year memory buying.",
  "FQ1 results Dec 23", "DRAM lawsuit; memory falls hard when prices turn", (-40,18,58), 'Medium', 'Cycle leader'),
 ('NVDA', "Beat and raised (Q3 revenue $115.8B, Q4 guide $130B, $150B more buyback) but the stock still closed 2.9% lower. About 9x forward earnings, 37% off its high. No permanent CEO yet.",
  "Post-earnings estimate upgrades; CEO search", "Leadership vacuum; SEC disclosure probe; China rules", (-30,14,50), 'Medium', 'Cheap leader, leadership risk'),
 ('COHR', "Coherent: record quarter and a ~$20B five-year optics deal; 50% below its high at about 13x forward earnings. Held up (+0.7%) while optics peers fell.",
  "Optics orders; FQ2 results (Feb)", "8% daily swings; policy headlines cut both ways", (-35,18,55), 'Medium', 'Optics rebound'),
]
P[('long','ai','SGX')] = [
 ('AWX.SI', "AEM rose 3.3% on a down day for the STI; up ~280% this year but 42% below its high, with about 100% analyst upside.",
  "Q3 business update (Nov); Nvidia beat", "One large customer; 7% daily swings", (-40,16,55), 'Medium', 'SGX AI leader'),
 ('V03.SI', "Venture: net cash, about 15x earnings, low volatility; analysts see about 28% upside. Rose 0.6% on a weak day.",
  "Analyst upgrades after Q3", "Slow revenue growth (+7%)", (-12,12,25), 'High', 'Steady value'),
 ('558.SI', "UMS makes precision parts for chip-equipment makers: revenue +61%, 41% off its high, about 17x earnings. Rose 2.4%.",
  "Chip-equipment spending outlook", "Tied to Applied Materials spending", (-32,15,45), 'Medium', 'Equipment supplier'),
 ('5DD.SI', "Micro-Mechanics makes precision tools for chip assembly and test: revenue +45%, 40% off its high. Rose 2.2%.",
  "Q1 FY27 results (Nov)", "Small and thinly traded", (-24,13,36), 'Medium', 'Growth at a discount'),
 ('E28.SI', "Frencken builds modules for chip and medical equipment; 52% off its high at about 14x earnings (RSI 28).",
  "Q3 business update (Nov)", "Flat revenue so far this year", (-26,12,36), 'Medium', 'Recovery'),
]
P[('swing','ai','US')] = [
 ('AVGO', "Strongest big chip name this week (+1.6% in five days, RSI 52); results on Dec 9 fall inside the swing window.",
  "Q4 results Dec 9", "AI financing worries", (-13,5,17), 'Medium', 'Relative strength into results'),
 ('LITE', "Marvell is buying Lumentum for 4.5 Marvell shares each. At snapshot prices that is worth about 17% more than LITE's price.",
  "Spread narrows if the deal clears", "Regulatory delay (incl. China); MRVL falls again", (-15,8,22), 'Medium', 'Merger spread'),
 ('TSM', "RSI 33 after a 13% five-day drop; Nvidia's guide points to more TSMC wafer demand.", "November sales (~Dec 10)", "Chip-rule headlines", (-10,5,14), 'Medium', 'Oversold leader'),
 ('MU', "RSI 31; about 3.4x forward earnings, and Nvidia's call pointed to multi-year memory buying.",
  "FQ1 results Dec 23", "Lawsuit news; AI capex fears", (-16,7,22), 'Medium', 'Rebound'),
 ('NVDA', "RSI 16, the most oversold big chip name; but the market sold the beat, so the bounce needs proof.",
  "Analyst target raises; Anthropic debut mood", "Leadership or SEC headlines", (-14,6,20), 'Speculative', 'Oversold, post-beat'),
]
P[('swing','ai','SGX')] = [
 ('AWX.SI', "AEM bounced 3.3% (RSI 34) after a 27% one-month drop.", "Q3 update; Nvidia read-across", "US chip curbs", (-20,6,26), 'Speculative', 'Oversold rebound'),
 ('558.SI', "UMS rose 2.4% from RSI 31.", "Chip-equipment read-across", "Chip-equipment sentiment", (-15,5,18), 'Medium', 'Oversold with catalyst'),
 ('V03.SI', "Venture rose 0.6% (RSI 41); the steadiest name in the group.", "Analyst upgrades", "Low growth", (-6,3,9), 'High', 'Range'),
 ('5DD.SI', "Micro-Mechanics rose 2.2% (RSI 36).", "Q1 FY27 results", "Thin trading", (-10,4,12), 'Medium', 'Support'),
 ('E28.SI', "Frencken RSI 28 after a 10% five-day drop.", "Bounce", "Flat revenue", (-12,4,14), 'Speculative', 'Oversold rebound'),
]
P[('intraday','ai','US')] = [
 ('AVGO', "Up 2.7% while the Dow fell.", "Momentum", "Chip selling returns", (-3,0.5,3.5), 'Medium', 'Relative strength'),
 ('ANET', "Up 2.6%; networking demand in Nvidia's guide.", "Sympathy move", "Gives back gains", (-3.5,0.4,4), 'Medium', 'Momentum'),
 ('AMD', "Up 2.2%; an Anthropic cornerstone investor.", "Anthropic debut mood", "Chip-rule headlines", (-4,0.5,4.5), 'Speculative', 'Momentum'),
 ('NBIS', "Up 1.5% after a 30% five-day drop (RSI 31).", "AI cloud bounce", "9% daily swings", (-6,0.5,7), 'Speculative', 'Bounce watch'),
 ('NVDA', "Down 2.4-2.9% after the beat (RSI 16).", "Dip buying", "More post-earnings selling", (-3.5,0.3,3.5), 'Speculative', 'Oversold watch'),
]
P[('intraday','ai','SGX')] = [
 ('AWX.SI', "Rose 3.3% against the STI.", "Next session", "US chips weak again", (-5,0.8,6), 'Speculative', 'Follow-through check'),
 ('558.SI', "Rose 2.4%.", "Next session", "Follows US chip equipment", (-4,0.5,4.5), 'Speculative', 'Follow-through check'),
 ('5DD.SI', "Rose 2.2%.", "Next session", "Thin trading", (-3,0.2,3), 'Medium', 'Range'),
 ('V03.SI', "Rose 0.6% on a weak day.", "Next session", "Small range", (-2,0.3,2.2), 'Medium', 'Range'),
 ('MZH.SI', "Nanofilm RSI 20 after an 11% five-day drop.", "Next session", "Thin trading", (-3,0.3,3), 'Speculative', 'Bounce watch'),
]

# ---------- Health ----------
P[('long','hc','US')] = [
 ('LLY', "Obesity-drug leader: revenue +39%, 3% off its high (+30% this year). Little analyst upside left, so the base case is modest. Not exposed to the Medicare Advantage audit rule.",
  "Orforglipron launch; Q4 results (Feb)", "Drug-price policy", (-16,8,25), 'High', 'Defensive growth'),
 ('ARGX', "argenx: revenue +52% from its immune-disease drug Vyvgart, 11% off its high, 22% analyst upside.",
  "New indications in 2027", "Competition in myasthenia gravis", (-15,10,28), 'Medium', 'Growth leader'),
 ('MDGL', "Madrigal's liver drug Rezdiffra is growing fast (revenue +50%); 32% off its high with 69% analyst upside. Fell 3.4%.",
  "Script data; EU rollout", "Competition from GLP-1 drugs", (-22,20,45), 'Medium', 'Oversold growth'),
 ('INSM', "Insmed's lung drug launch drives revenue +268%; up 26% in a month, still 43% off its high.",
  "Brensocatib launch numbers", "High valuation; volatile", (-30,16,45), 'Medium', 'Launch story'),
 ('VRTX', "Vertex: steady growth (+12%), 4% off its high, about 27x earnings; rose on a weak day.",
  "Pain-drug launch; kidney data", "Valuation", (-14,9,22), 'Medium', 'Steady growth'),
]
P[('long','hc','SGX')] = [
 ('Q0F.SI', "IHH runs hospitals across Asia; analysts see 35% upside. Flat ahead of Q3 results.", "Q3 results Nov 25", "Currency swings", (-12,11,24), 'Medium', 'Regional leader'),
 ('C2PU.SI', "Parkway Life REIT: steady hospital and nursing-home rents, 7% off its high.", "Dividend", "US rates and a strong dollar", (-8,7,15), 'High', 'Income'),
 ('AP4.SI', "Riverstone makes cleanroom and medical gloves at about 14x earnings with 33% analyst upside; fell 4% after naming a new CEO from Dec 1.", "Q3 results (Nov)", "Glove price competition; management change", (-15,10,26), 'Medium', 'Value'),
 ('BSL.SI', "Raffles Medical: Singapore hospital group, 22% off its high, steady (RSI 59).", "Results (Feb)", "Shrinking revenue (-7%)", (-10,8,18), 'Medium', 'Recovery'),
 ('H02.SI', "Haw Par (Tiger Balm) trades near 10x earnings with a large cash and investment pile; 33% off its high.", "Results (Feb)", "Revenue down 8%", (-12,6,16), 'Medium', 'Value'),
]
P[('swing','hc','US')] = [
 ('LLY', "Near its high; no Medicare Advantage exposure while insurers sell off.", "Orforglipron news", "Money rotating into chips", (-8,3,10), 'High', 'Relative strength'),
 ('VRTX', "Rose 0.7% on a weak day (RSI 49), 4% off its high.", "Pipeline news", "Rotation out of defensives", (-6,2,7), 'Medium', 'Relative strength'),
 ('MDGL', "RSI 39 after a 3.4% drop; 69% analyst upside.", "Script data", "Biotech risk-off", (-12,6,18), 'Medium', 'Rebound'),
 ('ALNY', "Oversold (RSI 32), 68% off its high; 89% analyst upside.", "Amvuttra script data", "Trend still down", (-15,7,22), 'Speculative', 'Oversold rebound'),
 ('UNH', "Down 12% in five days on the CMS audit proposal; now about 15x forward earnings (RSI 25). The rule is only a proposal and legal challenges are expected.",
  "2027 outlook before year-end; comment period", "Rule finalised as written; more insurer selling", (-15,4,18), 'Speculative', 'Policy-shock rebound'),
]
P[('intraday','hc','US')] = [
 ('UNH', "Fell 9-10% on the CMS audit proposal (RSI 25).", "Dip buying", "More insurer selling", (-4,0.3,4), 'Speculative', 'Bounce watch'),
 ('CRSP', "Up 3.2% (RSI 22).", "Gene-editing bounce", "Gives back gains", (-4,0.3,4), 'Speculative', 'Momentum'),
 ('VRTX', "Rose 0.7% against the market.", "Momentum", "Small range", (-1.8,0.2,2), 'Medium', 'Relative strength'),
 ('MRNA', "Fell 3%; down 19% in five days.", "Bounce", "6% daily swings", (-6,0,6), 'Speculative', 'Bounce watch'),
 ('LLY', "Eased 1.5% near its high.", "Defensive bid", "Rotation into tech", (-2.2,0.2,2.2), 'Medium', 'Range'),
]
P[('swing','hc','SGX')] = [
 ('Q0F.SI', "IHH flat (RSI 42) ahead of Q3 results.", "Q3 results Nov 25", "Results miss", (-6,3,9), 'Medium', 'Pre-earnings'),
 ('C2PU.SI', "Parkway Life REIT: lowest-volatility name in the group.", "Dividend", "Rates", (-4,2,6), 'High', 'Range'),
 ('BSL.SI', "Raffles Medical holding up (RSI 59); +1.8% in a month.", "Momentum", "Low volume", (-5,2,6), 'Medium', 'Trend'),
 ('AP4.SI', "Riverstone fell 4% on the CEO change (RSI 39); large analyst upside.", "Q3 results (Nov)", "Glove prices; management change", (-8,3,10), 'Medium', 'Pullback'),
 ('QC7.SI', "Q&M Dental is very oversold (RSI 9).", "Bounce", "Small cap", (-8,3,10), 'Speculative', 'Oversold rebound'),
]
P[('intraday','hc','SGX')] = [
 ('AP4.SI', "Fell 4% on the CEO change.", "Next session", "More selling", (-2.5,0.4,2.5), 'Medium', 'Bounce watch'),
 ('Q0F.SI', "Flat.", "Next session", "Malaysia market swings", (-2,0.3,2), 'Medium', 'Range'),
 ('C2PU.SI', "Eased 0.8%.", "Next session", "Small range", (-1,0.2,1), 'Medium', 'Range'),
 ('BSL.SI', "Eased 0.6%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('H02.SI', "Eased 0.7% (RSI 27).", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
]

# ---------- Finance ----------
P[('long','fin','US')] = [
 ('JPM', "Best-run US bank, 11% off its high at about 13x forward earnings. Higher rates support interest income; a December hike is widely expected.", "Q4 results Jan 14", "Credit cycle; AI-spending worries", (-15,8,22), 'High', 'Core holding'),
 ('V', "Visa: steady growth (+13%), 5% off its high; flat on a weak day and little AI exposure.", "Holiday spending", "Regulation of card fees", (-12,6,18), 'High', 'Defensive growth'),
 ('GS', "Trading and deal-making boom, about 12x forward earnings, 24% off its high. Co-lead on Anthropic, which priced above range at $83 in a record ~$68B IPO.",
  "Anthropic debut Nov 19; Q4 results Jan 19", "Market volatility hits deals", (-20,10,28), 'Medium', 'Cyclical value'),
 ('NU', "Nubank: revenue +34% at about 11x forward earnings, 35% off its high; 47% analyst upside.", "Q4 results (Feb)", "Brazil credit and currency; strong dollar", (-30,16,48), 'Medium', 'Growth at a discount'),
 ('SE', "Sea: revenue +43%; $1B buyback. About 15x forward earnings, 53% off its high.",
  "Q4 results (Mar)", "Rising credit costs at Monee; competition", (-30,18,50), 'Medium', 'Oversold growth'),
]
P[('long','fin','SGX')] = [
 ('D05.SI', "DBS kept its 81-cent quarterly dividend and says interest income has bottomed; 15% off its high (RSI 16) after another 1.1% drop.",
  "Q4 results (Feb)", "Margins if rates fall; stronger SGD", (-10,8,16), 'High', 'Income leader'),
 ('O39.SI', "OCBC was the only local bank to beat in Q3 and raised loan-growth guidance.",
  "Q4 results (Feb)", "Margin fell 18 bp to 1.66%", (-10,7,15), 'Medium', 'Income'),
 ('U11.SI', "UOB missed Q3 and cut its margin guidance; RSI 13, 20% off its high.", "Recovery in fees", "More credit provisions", (-12,7,17), 'Medium', 'Oversold income'),
 ('AIY.SI', "iFAST: fintech platform, revenue +23%, 29% off its high with 47% analyst upside.", "HK pension business", "Market-driven volumes", (-18,16,36), 'Medium', 'Growth'),
 ('S68.SI', "SGX benefits from high trading volumes; from Jan 2027 its RegCo takes over IPO prospectus reviews.", "Monthly volume data", "Already priced (24x earnings)", (-12,7,18), 'Medium', 'Volatility winner'),
]
P[('swing','fin','US')] = [
 ('GS', "Anthropic priced above range at $83 and trades Nov 19; fees and follow-on deals help.", "Deal fees", "Volatility", (-9,4,12), 'Medium', 'Deal pipeline'),
 ('KLAR', "Klarna up 9% in five days after Q3 (RSI 59), still 55% below its high.", "Holiday volumes", "Credit losses", (-12,6,18), 'Speculative', 'Post-results momentum'),
 ('SCHW', "Schwab rose on a weak day (RSI 60); about 12x forward earnings, 26% analyst upside.", "Monthly client metrics", "Rates and market swings", (-8,3,10), 'Medium', 'Relative strength'),
 ('MA', "Mastercard 4% off its high (RSI 53).", "Holiday spending data", "Rotation out of defensives", (-6,2,7), 'High', 'Steady'),
 ('HOOD', "RSI 25 after a 19% five-day drop; retail access to the Anthropic IPO runs partly through Robinhood.", "Anthropic debut demand", "More crypto weakness", (-18,6,24), 'Speculative', 'Oversold rebound'),
]
P[('swing','fin','SGX')] = [
 ('D05.SI', "DBS is oversold (RSI 16).", "Dividend support", "Margin worries", (-4,3,7), 'High', 'Oversold income'),
 ('U11.SI', "UOB RSI 13.", "Rebound", "Further downgrades", (-5,3,8), 'Medium', 'Oversold rebound'),
 ('O39.SI', "OCBC fell 1.2% (RSI 32).", "Post-results recovery", "Margin squeeze", (-4,2,6), 'Medium', 'Pullback'),
 ('AIY.SI', "iFAST RSI 43.", "Momentum", "Market-driven", (-8,3,10), 'Medium', 'Range'),
 ('S68.SI', "SGX benefits when markets are volatile.", "Volume data", "Valuation", (-5,2,7), 'Medium', 'Volatility winner'),
]
P[('intraday','fin','US')] = [
 ('KLAR', "Up 2.8%; momentum since Q3.", "Follow-through", "Gives back gains", (-3.5,0.3,3.5), 'Speculative', 'Momentum'),
 ('HOOD', "RSI 25; Anthropic starts trading.", "Anthropic debut interest", "Crypto weakness", (-5,0.5,5.5), 'Speculative', 'Bounce watch'),
 ('GS', "Anthropic priced above range.", "IPO fees", "Market risk-off", (-2.5,0.3,2.5), 'Medium', 'Range'),
 ('COIN', "Fell 2.5% (RSI 22).", "Crypto bounce", "More crypto selling", (-5,0,5), 'Speculative', 'Crypto beta'),
 ('JPM', "Fell 1.5%.", "Dip buying", "Bank weakness", (-2,0.3,2), 'Medium', 'Dip watch'),
]
P[('intraday','fin','SGX')] = [
 ('D05.SI', "Fell 1.1%; RSI 16.", "Next session", "Market-wide risk-off", (-1.3,0.4,1.5), 'High', 'Bounce watch'),
 ('U11.SI', "Fell 1.5%; RSI 13.", "Next session", "Trend down", (-1.5,0.3,1.6), 'Medium', 'Bounce watch'),
 ('O39.SI', "Fell 1.2%.", "Next session", "Small range", (-1.3,0.3,1.4), 'Medium', 'Bounce watch'),
 ('S68.SI', "Eased 0.6%.", "Next session", "Small range", (-1.3,0.2,1.3), 'Medium', 'Range'),
 ('AIY.SI', "Fell 1.7%.", "Next session", "Small range", (-1.8,0.2,1.8), 'Medium', 'Range'),
]

# IPO tab (6-month view), all markets
P[('ipo','all','US')] = [
 ('SPCX', "SpaceX listed in June at $135 and trades about 7% above that, 32% under its high; rose 1.8% on a weak day.",
  "Starship progress; lock-up expiries", "Valuation and Musk headlines", (-35,12,45), 'Medium', 'Mega-cap IPO'),
 ('KLAR', "Klarna (IPO $40) is 63% below its IPO price at about 20x forward earnings. Back to profit in Q3; up 9% in five days.",
  "Holiday volumes; Q4 results", "Buy-now-pay-later credit losses", (-25,14,40), 'Speculative', 'Deep value'),
 ('CHYM', "Chime (IPO $27) trades about 18% above its IPO price, 8% off its high after a 3.3% dip.",
  "Member growth", "Fintech credit cycle", (-18,8,25), 'Medium', 'Post-IPO uptrend'),
 ('IAM', "Iambic (IPO $16, AI drug discovery) rose 4% to about $14.8, still just below its IPO price; 84% analyst upside.",
  "Pipeline data; partnerships", "Cash burn; 10% daily swings", (-40,12,55), 'Speculative', 'Post-IPO rebound'),
 ('ACCV', "Accelevation (IPO $18) makes electrical gear for data centres: revenue +66% at about 9x forward earnings. Bounced 5.9% but is 38% below its IPO price.",
  "Order updates", "Data-centre slowdown; 9% daily swings", (-40,10,50), 'Speculative', 'Post-IPO value'),
]

# ---------- Power & grid (data-center power) ----------
P[('long','pwr','US')] = [
 ('GEV', "GE Vernova: gas turbines and grid gear sold out for years, revenue +27%. 34% off its high with 50% analyst upside.", "Q4 results Jan 27", "Data-centre policy; valuation (30x)", (-25,15,40), 'High', 'Quality at a discount'),
 ('CEG', "Constellation beat Q3 and raised 2026 guidance; 30% off its high.", "New long-term power deals", "Data-centre politics; PJM rules", (-22,13,32), 'High', 'Beat and raise'),
 ('ETN', "Eaton: electrical gear for data centres and utilities, 26% off its high at about 21x earnings; rose 1%.", "Q4 results Feb 2", "Data-centre orders slowing", (-20,13,33), 'Medium', 'Quality at a discount'),
 ('VRT', "Vertiv: data-centre cooling and power, revenue +61% at about 20x forward earnings, 48% off its high. Rose 2.1%.", "Order backlog updates", "Most exposed to a data-centre slowdown", (-35,18,52), 'Medium', 'Oversold growth'),
 ('PWR', "Quanta builds the grid: revenue +57%, 23% off its high; rose 1.3%.", "Utility capex plans", "Data-centre policy", (-25,12,34), 'Medium', 'Grid builder'),
]
P[('long','pwr','SGX')] = [
 ('BN4.SI', "Keppel: power, data centres and asset management, about 15x earnings with 39% analyst upside. Fell 1.6% (RSI 29).", "Asset sales", "Execution", (-13,12,25), 'Medium', 'Value'),
 ('U96.SI', "Sembcorp: power and renewables at about 9x earnings.", "New contracts", "Power prices", (-12,7,18), 'Medium', 'Value'),
 ('DCRU.SI', "Digital Core REIT: US data-centre REIT, about 9x earnings with 55% analyst upside.", "Leasing news", "Tenant concentration; US rates", (-14,11,27), 'Medium', 'Deep value'),
 ('AJBU.SI', "Keppel DC REIT: data-centre rents, 10% off its high.", "Dividend", "Rates", (-10,7,17), 'Medium', 'Income'),
 ('544.SI', "CSE Global: electrification and data-centre work, about 9x earnings, 58% off its high; flat after last week's slide.", "New orders", "Small and volatile", (-30,14,45), 'Speculative', 'Recovery'),
]
P[('swing','pwr','US')] = [
 ('NEE', "NextEra rose on a weak day (RSI 61); regulated utility earnings.", "Renewables deals", "Higher yields", (-6,3,8), 'Medium', 'Defensive'),
 ('VRT', "Vertiv rose 2.1% (RSI 34); the most direct power play on Nvidia's guide.", "Order news", "AI hardware selling", (-16,7,22), 'Speculative', 'Oversold rebound'),
 ('GEV', "GE Vernova RSI 37, down 13% in a month.", "Order news", "AI capex fears", (-14,6,20), 'Medium', 'Oversold rebound'),
 ('TLN', "Talen rose 2.1% (RSI 53); new 750 MW capacity deal, about 12x forward earnings.", "Analyst target updates", "Data-centre politics", (-13,5,16), 'Medium', 'New-contract momentum'),
 ('VST', "Vistra RSI 41 after a 15% monthly drop; 56% analyst upside.", "Analyst updates", "Texas data-centre proposal", (-14,6,20), 'Medium', 'Oversold rebound'),
]
P[('swing','pwr','SGX')] = [
 ('AJBU.SI', "Keppel DC REIT eased 0.9% (RSI 64).", "Momentum", "Rates", (-5,1.5,6), 'Medium', 'Trend'),
 ('BN4.SI', "Keppel fell 1.6% to RSI 29.", "Asset-sale news", "Execution", (-6,3,9), 'Medium', 'Oversold rebound'),
 ('U96.SI', "Sembcorp RSI 34.", "Contracts", "Power prices", (-5,2,7), 'Medium', 'Oversold'),
 ('DCRU.SI', "Digital Core REIT flat (RSI 50).", "Support", "US data-centre worries", (-7,2,8), 'Medium', 'Range'),
 ('544.SI', "CSE Global flat after an 18% five-day drop.", "New orders", "No floor yet", (-15,3,16), 'Speculative', 'Base building'),
]
P[('intraday','pwr','US')] = [
 ('VRT', "Up 2.1%.", "Momentum", "AI hardware selling", (-5,0.6,6), 'Speculative', 'Momentum'),
 ('NRG', "Up 2.3%.", "Momentum", "Gives back gains", (-4,0.3,4), 'Medium', 'Momentum'),
 ('TLN', "Up 2.1%.", "Momentum", "Data-centre politics", (-4,0.3,4), 'Medium', 'Momentum'),
 ('OKLO', "Fell 2.2%; down 15% in five days.", "Bounce", "Cash burn", (-7,0,7), 'Speculative', 'Bounce watch'),
 ('NEE', "Up 0.6% on a weak day.", "Defensive bid", "Small range", (-1.8,0.2,1.8), 'Medium', 'Range'),
]
P[('intraday','pwr','SGX')] = [
 ('BN4.SI', "Fell 1.6% (RSI 29).", "Next session", "More selling", (-1.8,0.4,2), 'Medium', 'Bounce watch'),
 ('544.SI', "Flat after a sharp slide.", "Next session", "Small cap", (-4,0.2,4), 'Speculative', 'Range'),
 ('U96.SI', "Eased 0.5%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('AJBU.SI', "Eased 0.9%.", "Next session", "Small range", (-1.2,0.2,1.2), 'Medium', 'Range'),
 ('DCRU.SI', "Flat.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
]

# ---------- Defence & industrials ----------
P[('long','def','US')] = [
 ('GE', "GE Aerospace: jet-engine services boom, revenue +16%, 14% off its high; rose on a weak day.", "Q4 results Jan 21", "Valuation (35x)", (-15,10,26), 'High', 'Quality'),
 ('RTX', "RTX: missiles and engines, revenue +11%, steady; 16% analyst upside.", "Q4 results Jan 26", "Engine issues", (-12,10,24), 'High', 'Core defence'),
 ('HWM', "Howmet: jet-engine parts, revenue +29%, 24% off its high with 34% analyst upside; rose 2.8%.", "Aerospace build rates", "Valuation (33x)", (-20,14,34), 'Medium', 'Growth at a discount'),
 ('LHX', "L3Harris: space and missile sensors, 32% off its high, 31% analyst upside.", "Golden Dome contracts", "Budget fights with a split government", (-15,12,30), 'Medium', 'Value'),
 ('NOC', "Northrop: B-21 and missile defence, about 18x earnings, 29% off its high.", "Golden Dome contracts", "Budget fights", (-15,10,27), 'Medium', 'Value'),
]
P[('long','def','SGX')] = [
 ('S63.SI', "ST Engineering: record S$37.7B order book and nine-month revenue +10%. Fell another 2.8% to S$8.61 (RSI 21); 34% analyst upside.", "Contract wins; FY results (Feb)", "Selling pressure; valuation (22x)", (-12,12,26), 'High', 'Quality on a dip'),
 ('BS6.SI', "Yangzijiang Shipbuilding: about 7x earnings, revenue +36%; rose 2.1% on a weak day.", "New ship orders", "US port fees on Chinese ships", (-18,14,32), 'Medium', 'Value'),
 ('S59.SI', "SIA Engineering: aircraft maintenance, 25% off its high, 32% analyst upside.", "Air travel", "Revenue falling (-11%)", (-10,10,24), 'Medium', 'Recovery'),
 ('C52.SI', "ComfortDelGro: steady transport earnings at about 13x; flat on a weak day.", "Overseas contracts", "Slow growth", (-8,7,15), 'Medium', 'Steady'),
 ('H22.SI', "Hong Leong Asia: engines and building materials at about 8x earnings, 49% off its high.", "Results (Feb)", "China demand", (-25,20,50), 'Speculative', 'Deep value'),
]
P[('swing','def','US')] = [
 ('HWM', "Howmet rose 2.8% (RSI 58), up 5% in a month.", "Aerospace data", "Valuation", (-8,4,11), 'Medium', 'Relative strength'),
 ('CAT', "Caterpillar is 48% off its high (RSI 32).", "Rebound", "Data-centre generator orders slowing", (-12,6,18), 'Medium', 'Oversold rebound'),
 ('AXON', "RSI 14 after a Q3 miss; 82% analyst upside.", "Analyst updates", "More downgrades", (-18,6,22), 'Speculative', 'Post-earnings dip'),
 ('NOC', "Northrop RSI 39; steady over the month.", "Golden Dome contracts", "Budget fights", (-7,3,9), 'Medium', 'Support'),
 ('BA', "Boeing 35% off its high (RSI 35); production recovering.", "Monthly deliveries", "Quality issues", (-10,5,15), 'Medium', 'Recovery'),
]
P[('swing','def','SGX')] = [
 ('S63.SI', "ST Engineering RSI 21 after a 12% five-day drop.", "Bounce; contract wins", "Large holder selling; downgrade", (-6,4,10), 'Medium', 'Oversold rebound'),
 ('BS6.SI', "Yangzijiang rose 2.1%.", "Orders", "Trade fees", (-8,4,12), 'Medium', 'Rebound'),
 ('H22.SI', "Hong Leong Asia RSI 21.", "Bounce", "China demand", (-10,4,12), 'Speculative', 'Oversold rebound'),
 ('S59.SI', "SIA Engineering RSI 35.", "Air travel", "Slow growth", (-6,2,7), 'Medium', 'Range'),
 ('C52.SI', "ComfortDelGro steady (RSI 39).", "Support", "Slow growth", (-4,1.5,5), 'Medium', 'Range'),
]
P[('intraday','def','US')] = [
 ('HWM', "Up 2.8%.", "Momentum", "Gives back gains", (-2.5,0.3,3), 'Medium', 'Relative strength'),
 ('GE', "Up 0.8% on a weak day.", "Momentum", "Small range", (-2,0.2,2.2), 'Medium', 'Relative strength'),
 ('AXON', "RSI 14.", "Bounce", "More selling", (-4,0.3,4), 'Speculative', 'Bounce watch'),
 ('KTOS', "Down 17% in five days.", "Drone contracts", "Volatile", (-4.5,0,4.5), 'Speculative', 'Bounce watch'),
 ('AVAV', "Fell 2.3%; results Dec 2.", "Bounce", "Volatile", (-5,0,5), 'Speculative', 'Bounce watch'),
]
P[('intraday','def','SGX')] = [
 ('S63.SI', "Fell 2.8% (RSI 21).", "Next session", "More selling", (-2.5,0.5,3), 'Medium', 'Bounce watch'),
 ('BS6.SI', "Rose 2.1%.", "Next session", "Gives back gains", (-2.5,0.3,2.5), 'Medium', 'Follow-through check'),
 ('H22.SI', "Fell 2% (RSI 21).", "Next session", "Thin trading", (-3,0.3,3), 'Speculative', 'Bounce watch'),
 ('S59.SI', "Eased 0.7%.", "Next session", "Small range", (-1.5,0.2,1.5), 'Medium', 'Range'),
 ('C52.SI', "Flat.", "Next session", "Small range", (-1.2,0.2,1.2), 'Medium', 'Range'),
]

# ---------- Energy (oil and gas) ----------
P[('long','nrg','US')] = [
 ('CVX', "Chevron: revenue +35%, about 12.5x earnings, 13% off its high after a 4.7% drop as WTI fell 4%.", "Hess integration; buybacks", "Oil falls further on stock builds or Gulf calm", (-16,8,24), 'High', 'Core energy'),
 ('XOM', "Exxon: steady cash flow, about 13x earnings, 15% analyst upside; fell 3.8% with oil.", "Buybacks", "Oil price drop", (-15,7,21), 'High', 'Core energy'),
 ('LNG', "Cheniere: US gas exports on long contracts; less tied to oil. 10% off its high.", "New export capacity", "Gas price swings", (-15,8,24), 'Medium', 'Steady'),
 ('FANG', "Diamondback: low-cost Permian producer at about 8x earnings, 37% analyst upside (RSI 22).", "Buybacks", "Oil price drop", (-22,12,32), 'Medium', 'Value'),
 ('EOG', "EOG: about 9x earnings, revenue +43%, 9% off its high.", "Buybacks", "Oil price drop", (-16,7,22), 'Medium', 'Value'),
]
P[('long','nrg','SGX')] = [
 ('5E2.SI', "Seatrium builds offshore rigs and wind platforms; 47% analyst upside.", "New orders", "Contract delays", (-15,12,28), 'Medium', 'Recovery'),
 ('BN4.SI', "Keppel: energy infrastructure and asset management.", "Asset sales", "Execution", (-13,10,22), 'Medium', 'Value'),
 ('5LY.SI', "Marco Polo Marine: offshore vessels, revenue +40% at about 10x earnings.", "Results (Nov)", "Thin trading", (-25,10,35), 'Speculative', 'Growth value'),
 ('RE4.SI', "Geo Energy rebounded 9% to S$0.415 on about 30x normal volume after saying it had no new Indonesian mining directive. About 6x earnings; still 23% down in five days.", "Q3 update; trading settles", "Indonesian policy risk", (-35,8,40), 'Speculative', 'Wait'),
 ('5WH.SI', "Rex International is in a long downtrend (-65% this year); no setup.", "None", "Further losses", (-30,-5,20), 'Speculative', 'Avoid'),
]
P[('swing','nrg','US')] = [
 ('LNG', "Cheniere held up better than oil names (RSI 40); gas exports, not crude.", "Export capacity", "Gas price swings", (-8,3,10), 'Medium', 'Relative strength'),
 ('FANG', "Diamondback oversold (RSI 22); about 8x earnings.", "Buybacks", "Oil price drop", (-11,4,13), 'Medium', 'Oversold rebound'),
 ('SLB', "SLB oversold (RSI 24), 19% off its high; 29% analyst upside.", "Offshore orders", "Oil price drop", (-10,4,12), 'Medium', 'Oversold rebound'),
 ('CVX', "Chevron RSI 25 after a 4.7% drop.", "Buybacks", "More inventory builds", (-8,3,9), 'Medium', 'Oversold'),
 ('DVN', "Devon RSI 27; about 8x earnings, 42% analyst upside.", "Buybacks", "Oil price drop", (-12,4,14), 'Medium', 'Oversold rebound'),
]
P[('intraday','nrg','US')] = [
 ('CVX', "Fell 4.7% as WTI dropped 4%.", "Bounce", "Oil keeps falling", (-2.5,0.3,2.5), 'Medium', 'Bounce watch'),
 ('MPC', "Fell 5.1%.", "Margins", "Gasoline stock build", (-3,0.2,3), 'Speculative', 'Bounce watch'),
 ('XOM', "Fell 3.8% (RSI 25).", "Bounce", "Oil keeps falling", (-2,0.2,2), 'Medium', 'Bounce watch'),
 ('OXY', "Fell 4.6%.", "Bounce", "Oil keeps falling", (-3,0.2,3), 'Speculative', 'Bounce watch'),
 ('LNG', "Fell 1.8%, less than oil names.", "Gas exports", "Small range", (-2.5,0.2,2.5), 'Medium', 'Range'),
]
P[('swing','nrg','SGX')] = [
 ('5E2.SI', "Seatrium eased 0.6% (RSI 38).", "Orders", "Delays", (-8,3,10), 'Medium', 'Support'),
 ('BN4.SI', "Keppel fell 1.6% to RSI 29.", "Asset sales", "Execution", (-6,3,9), 'Medium', 'Oversold rebound'),
 ('RE4.SI', "Geo Energy bounced 9% on heavy volume after the company's clarification.", "Follow-through", "Policy risk; bounce fades", (-25,4,25), 'Speculative', 'Rebound'),
 ('5LY.SI', "Marco Polo Marine fell 3.8% (RSI 37).", "Results", "Thin trading", (-10,3,12), 'Speculative', 'Range'),
 ('5WH.SI', "Rex International: no setup.", "None", "Further losses", (-12,-2,8), 'Speculative', 'Avoid'),
]
P[('intraday','nrg','SGX')] = [
 ('RE4.SI', "Rose 9% on about 30x normal volume.", "Next session", "Bounce fades", (-8,0.5,8), 'Speculative', 'Follow-through check'),
 ('5E2.SI', "Eased 0.6%.", "Next session", "Oil weakness", (-2,0.2,2), 'Medium', 'Range'),
 ('BN4.SI', "Fell 1.6%.", "Next session", "Small range", (-1.8,0.4,2), 'Medium', 'Bounce watch'),
 ('5LY.SI', "Fell 3.8%.", "Next session", "Thin trading", (-4,0,4), 'Speculative', 'Range'),
 ('5WH.SI', "Penny stock in a downtrend; avoid.", "None", "Further losses", (-5,-1,4), 'Speculative', 'Avoid'),
]

IPO_LIST = [
 # sym, name, ipo_date, ipo_price, sector, status
 ('ANT','Anthropic (Nasdaq: ANT; priced Nov 18 at $83, above the $70-78 range; ~$68.5B raised plus a $26B private placement; ~$1.5T fully diluted; trading Nov 19)','2026-11-19',83.00,'ai','Priced'),
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
 ('2026-11-17T23:34','NVDA MU', "On X: reads Nvidia's call as 'demand far exceeds supply'; notes supply commitments rose from $279B to $390B, mostly multi-year memory buying, which he calls good for Micron and Samsung."),
 ('2026-11-17T00:22','NVDA', "On X: says DeepSeek is rationing users for lack of compute, and argues compute shortages are a bullish sign for AI infrastructure demand."),
 ('2026-11-15T23:01','NVDA', "Via tracker: backs Jensen Huang as '1 of 1' and shares a petition for his return."),
 ('2026-11-15T19:19','NVDA', "On X: shares the FT report that Huang is discussing a comeback and calls it his 'redemption arc'."),
 ('2026-11-15T19:03','AXTI', "Via tracker: says his AXT thesis is narrow, using indium phosphide substrate capacity as an example of an AI bottleneck."),
 ('2026-11-15T18:47','NVDA', "Via tracker: expects buying of bottleneck parts to speed up through 2027, naming laminates, ABF substrates, PCBs and optical parts."),
 ('2026-11-15T06:27','NVDA', "On X: says Western media coverage of Nvidia and Huang has gone too far."),
 ('2026-11-14T08:16','NVDA', "Via tracker: shares a letter from Altimeter and Atreides to Nvidia's board."),
 ('2026-11-14T04:25','LITE MU', "Via tracker: argues demand stays supply-limited for optics and memory even if AI capex slows."),
 ('2026-11-14T01:07','TSM', "Via tracker: calls rumours of TSMC capacity cuts hypothetical; says they have not happened."),
 ('2026-11-13T21:21','AXTI COHR LITE', "Via tracker: still bullish on AXT, citing backlog growth and visibility on customers."),
]

EVENTS = [
 ('2026-11-17','Macro','S&P -1.0%, Dow -1.6%, Nasdaq -0.7%', "Fourth straight drop; ~9 in 10 S&P stocks fell; VIX ~26. October retail sales +0.2% (control group beat)."),
 ('2026-11-17','AI','Nvidia beats and raises', "Q3 revenue $115.8B (+103%) vs ~$109B expected; Q4 guide $130B +/-3%; $150B added to buyback. Board says it doesn't intend to reinstate Huang."),
 ('2026-11-17','Finance','Klarna Q3: revenue +12%, back to profit', "KLAR +3%. JPMorgan names a new CFO for 2027; banks -2 to -3%."),
 ('2026-11-17','SGX','STI -1.4% to ~5,110', "Selling on US chip-curb worries. AEM -5%, Frencken -5%, CSE Global -7.4%. Geo Energy says no new Indonesian mining directive."),
 ('2026-11-18','Macro','Dow -561 (-1.1%), S&P -0.2%, Nasdaq +0.4%', "S&P's fifth straight drop. FOMC minutes: almost all officials see further hikes as likely appropriate; a couple open to more than 25 bp in December. Dollar at a 19-month high. WTI -4% to ~$82 on bigger US crude and gasoline builds."),
 ('2026-11-18','Health','CMS audit proposal hits insurers', "Proposed 'CRUSH' rule would extrapolate Medicare Advantage audit findings and claw back overpayments to 2018. UNH -10%, HUM -13%, ELV -7.6%, CNC -7%. Open for comment until Jan 19, 2027; legal challenges expected."),
 ('2026-11-18','AI','Nvidia gives up early gain, closes -2.9%', "Chips faded after a strong pre-market. AAOI -9.8% after filing a $550M at-the-market share sale."),
 ('2026-11-18','IPO','Anthropic prices at $83, above range', "Range was $70-78. About $68.5B raised plus a $26B private placement (>$94B total); ~$1.5T fully diluted."),
 ('2026-11-18','SGX','STI -1.06% to 5,054.89', "Riverstone -4% (new CEO from Dec 1); ST Engineering -2.8%; AEM +3.3%, UMS +2.4%; Geo Energy +9% on heavy volume."),
 ('2026-11-19','IPO','Anthropic starts trading (Nasdaq: ANT)', "Largest IPO on record; Goldman Sachs and Morgan Stanley lead."),
 ('2026-11-19','Macro','Weekly US jobless claims', ""),
 ('2026-11-23','IPO','Tracx Logis and Football Manager SPAC expected', ""),
 ('2026-11-25','SGX','IHH Q3 results', ""),
 ('2026-11-26','Macro','US Thanksgiving', "US stock market closed; early close (1pm ET) on Nov 27."),
 ('2026-12-01','AI','Marvell and Credo results', ""),
 ('2026-12-02','Defence','AeroVironment results', ""),
 ('2026-12-09','Macro','Fed rate decision (Dec 8-9)', "A hike is widely expected after hawkish minutes. Broadcom reports the same day."),
 ('2026-12-10','AI','Ciena results; TSMC November sales', ""),
 ('2026-12-23','AI','Micron FQ1 results', ""),
]
