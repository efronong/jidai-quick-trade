# Analyst picks for 2026-10-26. Fields: sym, thesis, catalyst, risk, (low, base, high) % expected move, conviction, setup
# Horizons: long = 12 months, swing = ~4 weeks, intraday = rest of session (US) / next session (SGX), ipo = 6 months.
P = {}

P[('long','ai','US')] = [
 ('NVDA', "Trades near 13.5x forward earnings while revenue still roughly doubles. SpaceX's Apollo-led $40B financing is earmarked mainly for Nvidia GPUs in H1 2027.",
  "Big Tech capex guides Oct 28-29; Q3 results Nov 17", "Supply limits (Lam Research warned of constraints into 2027) can cap shipments; AI-bubble sentiment swings", (-15,28,55), 'High', 'Quality at a discount'),
 ('TSM', "Makes almost every leading AI chip. Revenue +51% with a forward P/E near 18: the steadiest way to own the build-out.",
  "October monthly sales (~Nov 10); Q4 results Jan 14", "Taiwan geopolitics and US tariff policy", (-12,22,40), 'High', 'Core holding'),
 ('MU', "Memory is the tightest link in AI servers: revenue +379%, forward P/E about 4. Amazon's CEO says the memory shortage does not end in 2027.",
  "HBM/DRAM contract prices; FQ1 results Dec 23", "Peak-cycle earnings: memory stocks fall hard when pricing turns", (-30,30,70), 'Medium', 'Cycle leader'),
 ('LITE', "Lasers and optical transceivers for AI clusters. Jensen Huang says scale-up optics volume goes about 15x; CW lasers are already short. Revenue +109%.",
  "Earnings Nov 5", "30% off its high and high beta; Chinese laser capacity ramps 2027-29", (-30,30,70), 'Medium', 'Bottleneck play'),
 ('AVGO', "Custom AI chips plus networking. Revenue +86% at ~17x forward earnings after a 32% drawdown on the CEO's capex comments.",
  "Q4 results Dec 9", "Lumpy custom-chip orders and customer concentration", (-15,25,50), 'Medium', 'Pullback in a leader'),
]
P[('long','ai','SGX')] = [
 ('AWX.SI', "AEM makes test handlers for AI and server chips. Up 350% this year yet 31% below its high; all 7 covering analysts rate it a buy.",
  "Q3 business update in November", "Heavy reliance on one large customer; very volatile", (-25,25,55), 'Medium', 'SGX AI leader'),
 ('558.SI', "UMS machines precision parts for chip-equipment makers. Up 85% in a year, now 29% off its high, with the equipment cycle still expanding.",
  "Q3 results mid-November", "Tied to Applied Materials spending; equipment supply limits", (-20,20,45), 'Medium', 'Equipment supplier'),
 ('E28.SI', "Frencken builds modules for semiconductor and medical equipment. 43% off its high with 8 buy ratings.",
  "Q3 business update (Nov)", "Flat revenue so far this year", (-20,18,40), 'Medium', 'Recovery'),
 ('V03.SI', "Venture builds electronics for chip-equipment, medical and AI-server makers. Steady, with a net cash balance sheet.",
  "Q3 business update (Nov)", "Flat revenue so far this year", (-10,10,22), 'Medium', 'Steady value'),
 ('MZH.SI', "Nanofilm makes coatings for consumer electronics and semis. Earnings expected to rebound strongly; heavy volume today (2x average).",
  "Q3 business update (Nov)", "Small company, thin trading; 50% off its high", (-25,15,45), 'Speculative', 'Turnaround'),
]
P[('swing','ai','US')] = [
 ('COHR', "Deeply oversold (RSI 14, 50% off high) right as Nvidia talks up a 15x optics ramp. Forward P/E about 15.",
  "Earnings Nov 4", "Optics names move 10%+ on earnings either way", (-15,15,30), 'Medium', 'Oversold rebound'),
 ('AMD', "Pulled back 20% from its high on the chip selloff while analysts still rate it Strong Buy. Revenue +50%.",
  "Earnings Nov 3", "Guidance on MI-series GPU ramps", (-10,10,20), 'Medium', 'Rebound into earnings'),
 ('AXTI', "Indium phosphide substrates, a named AI-optics bottleneck. Taiwan's VPEC says InP is 'seriously in short supply' (via @aleabitoreddit). Up 2.7% today.",
  "Earnings Oct 29", "Small cap, 61% off its high, swings 6% a day", (-25,18,45), 'Speculative', 'Catalyst trade'),
 ('STX', "Hard drives for AI data storage. Forward P/E about 11 and oversold (RSI 23) into results.",
  "Earnings Oct 27 (after US close)", "Gap risk on results", (-12,10,22), 'Medium', 'Earnings setup'),
 ('AMAT', "The most oversold large chip-equipment name (RSI 9, 47% off high). The supply warning hit the group, but demand is not the problem.",
  "Earnings Nov 12", "More equipment-maker supply warnings", (-10,12,25), 'Medium', 'Oversold rebound'),
]
P[('swing','ai','SGX')] = [
 ('5DD.SI', "Micro-Mechanics jumped 5.3% today on 4x normal volume, breaking out of a month-long drift.",
  "Q1 FY27 results (Nov)", "Small and thinly traded", (-8,8,18), 'Medium', 'Volume breakout'),
 ('558.SI', "UMS is very oversold (RSI 13) after a 23% monthly drop while analysts still rate it Strong Buy.",
  "Q3 results mid-November", "Chip-equipment sentiment", (-10,10,22), 'Medium', 'Oversold rebound'),
 ('E28.SI', "Frencken fell 23% this month (RSI 14). A rebound toward its 50-day average is about +10%.",
  "Q3 business update (Nov)", "No clear catalyst before results", (-10,9,20), 'Medium', 'Oversold rebound'),
 ('AWX.SI', "AEM dropped 13% over the last week but trend support from the 200-day average is holding.",
  "Q3 business update (Nov)", "High beta to US chip moves overnight", (-15,10,25), 'Speculative', 'Pullback buy'),
 ('V03.SI', "Venture is range-bound with low volatility; near the bottom of its range.",
  "Q3 business update (Nov)", "Flat revenue", (-6,5,10), 'Medium', 'Range trade'),
]
P[('intraday','ai','US')] = [
 ('LITE', "Leading the group (+4%) and trending up from the open after Jensen Huang's optics comments.",
  "Momentum: hold above the morning high", "Fades if chips roll over", (-3,1.5,4), 'Medium', 'Momentum long'),
 ('AXTI', "Up about 3% on InP shortage commentary; tends to extend on Serenity-flagged news days.",
  "Watch volume after the first hour", "Swings ±6% a day", (-4,1,5), 'Speculative', 'News momentum'),
 ('LRCX', "Bouncing 2.5% after last week's 9% drop on its own supply warning.",
  "Holding the opening range", "Bounce fails if the semis index turns red", (-2.5,0.8,3), 'Medium', 'Oversold bounce'),
 ('ARM', "RSI 15 going into today; up 2% on the Anthropic-led tech bid.", "Earnings Nov 4 ahead", "Weak trend since September", (-2.5,0.8,3.5), 'Medium', 'Oversold bounce'),
 ('NBIS', "Opened down but has reversed about 2% off the low; a stock readers are watching today.",
  "Reclaiming yesterday's close", "Down 35% this month; very volatile", (-3.5,1,4), 'Speculative', 'Reversal watch'),
]
P[('intraday','ai','SGX')] = [
 ('5DD.SI', "Closed +5.3% on 4x volume. Momentum stocks on this volume often follow through at the next open.",
  "Next session: hold above today's close", "Thin order book", (-2,1,3), 'Medium', 'Follow-through'),
 ('MZH.SI', "Volume at 2x average with a small gain; accumulation pattern.", "Next session open", "Tiny price steps (S$0.005) mean large % moves", (-2,0.8,3), 'Speculative', 'Accumulation'),
 ('AWX.SI', "Fell 2.6% today; watch whether US chips' Monday rally lifts it at Tuesday's open.",
  "Gap up on US chip strength", "Continues lower if US chips fade overnight", (-3,1,4), 'Medium', 'Gap watch'),
 ('558.SI', "Down 1.9% to an oversold reading; candidate for a reflex bounce.", "US chip close overnight", "Trend still down", (-2,0.8,3), 'Medium', 'Bounce watch'),
 ('V03.SI', "Low-volatility name near support; small range.", "Next session", "Little momentum", (-1.5,0.4,1.5), 'Medium', 'Range'),
]

P[('long','hc','US')] = [
 ('LLY', "Leader in obesity and diabetes drugs: revenue +48% and shares at a record. The biotech sector is in a broad innovation rally.",
  "Q3 results Oct 29", "Drug-pricing policy; high expectations already priced", (-10,15,30), 'High', 'Quality compounder'),
 ('ARGX', "argenx: revenue +52% and earnings +51% from its autoimmune franchise, 17% off its high.",
  "Q3 reported Oct 22; pipeline readouts", "Competition in FcRn drugs", (-15,20,40), 'Medium', 'Growth at a discount'),
 ('ALNY', "Alnylam: RNA drugs with revenue +67% and a forward P/E near 19, yet 52% below its high.",
  "Q3 results Oct 29", "Sentiment on its heart-disease drug launch", (-20,25,55), 'Medium', 'Recovery'),
 ('ISRG', "Intuitive Surgical's robots: up 13% this month as it recovers from a weak start to the year.",
  "Q4 results Jan 21", "Hospital capital spending; valuation (37x forward)", (-12,15,30), 'Medium', 'Trend recovery'),
 ('VRTX', "Vertex: steady cystic-fibrosis cash flow funding new pain and kidney drugs; 7% off its high.",
  "Q3 results Nov 2", "Pipeline setbacks", (-10,12,25), 'High', 'Defensive growth'),
]
P[('long','hc','SGX')] = [
 ('Q0F.SI', "IHH Healthcare: the region's largest hospital group, earnings +29% and a 35% gap to analyst targets.", "Q3 results Nov 25", "Currency swings (MYR, TRY)", (-10,12,25), 'Medium', 'Regional leader'),
 ('C2PU.SI', "Parkway Life REIT: hospital and nursing-home landlord with long leases. A defensive income holding; all 7 analysts rate it Strong Buy.", "Q3 update (Nov)", "Interest rates", (-8,10,18), 'High', 'Defensive income'),
 ('QC7.SI', "Q&M Dental: Singapore's largest dental chain, about 40% below analyst targets.", "Q3 results (Nov)", "Small and illiquid", (-15,10,30), 'Speculative', 'Value'),
 ('BSL.SI', "Raffles Medical is 24% off its high; China hospital losses are narrowing.", "Q3 update (Nov)", "Earnings still falling (-9%)", (-12,8,22), 'Medium', 'Turnaround'),
 ('H02.SI', "Haw Par (Tiger Balm) holds a large stake in UOB, so it trades below its asset value.", "UOB results Nov 4", "Slow growth", (-8,8,18), 'Medium', 'Value'),
]
P[('swing','hc','US')] = [
 ('ALNY', "Up about 3% today, deeply discounted, and reports Oct 29.", "Earnings Oct 29", "Gap risk on results", (-12,10,25), 'Medium', 'Rebound into earnings'),
 ('BIIB', "Biogen is breaking out at a 52-week high (RSI 77) going into results.", "Earnings Oct 28", "Overbought; earnings fell 85% last quarter", (-8,5,12), 'Medium', 'Breakout'),
 ('GILD', "Gilead is at a record with steady momentum (RSI 70).", "Earnings Oct 29", "Pulls back if guidance is flat", (-7,5,10), 'Medium', 'Breakout'),
 ('MDGL', "Madrigal's liver drug launch is growing revenue 71%, yet the stock is oversold (RSI 28).", "Earnings Nov 3", "Launch-pace scrutiny", (-15,10,25), 'Speculative', 'Oversold rebound'),
 ('AMGN', "Amgen is at a record before its results.", "Earnings Nov 3", "Analysts' average target is below the price", (-7,4,10), 'Medium', 'Momentum'),
]
P[('swing','hc','SGX')] = [
 ('AP4.SI', "Riverstone (cleanroom gloves for chip fabs) is oversold (RSI 26).", "Q3 results (Nov)", "Glove pricing", (-6,5,12), 'Medium', 'Oversold rebound'),
 ('Q0F.SI', "IHH is holding steady near support ahead of results.", "Q3 results Nov 25", "Currency", (-5,4,9), 'Medium', 'Pre-earnings'),
 ('C2PU.SI', "Parkway Life REIT is up 1.5% this month while the market fell, a sign of defensive buying.", "Q3 update (Nov)", "Rate moves after the Fed", (-4,3,7), 'High', 'Defensive'),
 ('H02.SI', "Haw Par tracks UOB, which reports Nov 4.", "UOB results Nov 4", "Bank results miss", (-5,3,8), 'Medium', 'Read-through'),
 ('BSL.SI', "Raffles Medical is flat and near support.", "Q3 update (Nov)", "No momentum", (-5,3,8), 'Medium', 'Range'),
]
P[('intraday','hc','US')] = [
 ('BOLT', "Up 8% today and 86% this month on heavy momentum. Speculative.", "Momentum continuation", "Can reverse 10%+ quickly", (-8,2,10), 'Speculative', 'Momentum long'),
 ('RXRX', "Recursion is up 3% with the AI-biotech bid.", "Holding above the open", "Volatile (7% daily swings)", (-4,1,5), 'Speculative', 'Momentum long'),
 ('ALNY', "Up 3% and steady from the open ahead of Thursday's results.", "Earnings Oct 29", "Fades into the close", (-2,0.8,3), 'Medium', 'Steady trend'),
 ('JNJ', "Up 2% in a low-volatility megacap; an orderly trend day.", "Holding the morning gains", "Small range", (-1.5,0.5,2), 'High', 'Trend day'),
 ('TEM', "Tempus AI is down 3% and below its open. A weak-relative name to avoid or fade.", "Below the open = weak", "Bounces sharply on AI news", (-4,-1,3), 'Medium', 'Fade / avoid'),
]
P[('intraday','hc','SGX')] = [
 ('AP4.SI', "Riverstone closed slightly higher and oversold.", "Next session", "Thin trading", (-2,0.5,2), 'Medium', 'Bounce watch'),
 ('C2PU.SI', "A defensive bid continues.", "Next session", "Small range", (-1,0.3,1.2), 'High', 'Range'),
 ('Q0F.SI', "IHH fell 2% on light volume.", "Next session", "Ringgit moves", (-1.5,0.3,1.5), 'Medium', 'Range'),
 ('QC7.SI', "Q&M fell 2.9%; watch for stabilisation.", "Next session", "Illiquid", (-2,0.5,2.5), 'Speculative', 'Bounce watch'),
 ('BSL.SI', "Raffles Medical is flat with no catalyst.", "Next session", "None", (-1,0.2,1), 'Medium', 'Range'),
]

P[('long','fin','US')] = [
 ('GS', "The IPO wave (SpaceX in June, Anthropic filing today) and an M&A rebound feed Goldman's fee engine. Forward P/E about 12.",
  "Anthropic IPO pricing; Q4 results Jan 19", "Capital markets slow if AI stocks sell off", (-15,18,35), 'High', 'IPO-cycle winner'),
 ('APO', "Apollo is leading SpaceX's $40B chip financing; private credit is funding the AI build-out. Forward P/E about 11, 24% off its high.",
  "Q3 results Nov 3", "Private-credit quality worries", (-18,22,45), 'Medium', 'AI financing'),
 ('JPM', "The best-run US bank: forward P/E 13, 8% off its high.", "Q4 results Jan 14", "Credit cycle; rate cuts squeezing margins", (-10,12,22), 'High', 'Core holding'),
 ('V', "Visa: a payments toll road at a record, with revenue +14%.", "Earnings Oct 27 (after US close)", "Rich valuation (27x forward)", (-8,12,22), 'High', 'Quality compounder'),
 ('HOOD', "Robinhood: revenue +32% but 37% off its high. Retail trading, crypto and prediction markets give it upside.",
  "Earnings Oct 27 (after US close)", "Crypto and retail activity are cyclical", (-25,25,55), 'Speculative', 'High-beta growth'),
]
P[('long','fin','SGX')] = [
 ('AIY.SI', "iFAST: wealth platform with revenue +35% and a UK digital bank; about 50% below analyst targets.", "Q3 results today (Oct 26)", "Bank-unit losses", (-20,20,45), 'Medium', 'Growth'),
 ('D05.SI', "DBS: Singapore's best-run bank and a dividend compounder, 6% off its high.", "Q3 results Nov 5", "Falling SGD rates hit margins", (-10,10,20), 'High', 'Core holding'),
 ('S68.SI', "SGX is gaining from higher trading volumes and derivatives growth.", "Q1 FY27 update", "Volumes fade", (-10,12,25), 'Medium', 'Market-volume play'),
 ('O39.SI', "OCBC is up 73% in a year with strong insurance and wealth fees; the weakest RSI in the group (13) gives a better entry.", "Q3 results Nov 6", "Rate cuts", (-12,8,20), 'Medium', 'Pullback buy'),
 ('U11.SI', "UOB is the cheapest of the three local banks (11.5x forward).", "Q3 results Nov 4", "ASEAN credit costs", (-10,8,18), 'Medium', 'Value'),
]
P[('swing','fin','US')] = [
 ('HOOD', "Oversold (RSI 28) into results tomorrow; results have moved the stock 10%+ before.", "Earnings Oct 27", "Gap risk both ways", (-15,10,25), 'Speculative', 'Earnings setup'),
 ('SOFI', "Down 54% from its high and reporting tomorrow with revenue +43%.", "Earnings Oct 27", "Credit-quality worries", (-15,10,25), 'Speculative', 'Earnings setup'),
 ('APO', "Up 3% today; the SpaceX financing headlines keep it in focus.", "Earnings Nov 3", "Private-credit headlines", (-8,8,16), 'Medium', 'Catalyst trade'),
 ('MS', "Up 2% today on the IPO-wave story; Morgan Stanley is a lead bank for big listings.", "Anthropic IPO process", "Market selloff", (-6,6,12), 'Medium', 'Theme momentum'),
 ('CHYM', "Chime is in an uptrend (+30% over 3 months) with 22 analysts at Strong Buy.", "Earnings Nov 4", "Newer stock, lock-up supply", (-10,8,18), 'Medium', 'Trend'),
]
P[('swing','fin','SGX')] = [
 ('AIY.SI', "iFAST reports today; a beat could break the 3-month downtrend.", "Q3 results Oct 26", "Bank-unit losses", (-10,8,18), 'Medium', 'Earnings setup'),
 ('D05.SI', "DBS is oversold (RSI 24) two weeks before results.", "Q3 results Nov 5", "Margin guidance", (-6,5,10), 'High', 'Pre-earnings'),
 ('U11.SI', "UOB reports Nov 4 and is 8% off its high.", "Q3 results Nov 4", "Credit costs", (-6,5,10), 'Medium', 'Pre-earnings'),
 ('O39.SI', "OCBC's RSI of 13 is the most oversold reading among the banks.", "Q3 results Nov 6", "Rate cuts", (-6,5,11), 'Medium', 'Oversold rebound'),
 ('G07.SI', "Great Eastern is up 4.7% this week on 1.5x volume.", "OCBC results Nov 6", "Thin float", (-5,4,9), 'Medium', 'Momentum'),
]
P[('intraday','fin','US')] = [
 ('NU', "Down about 20% after Lula's surprise re-election hit Brazilian stocks; it has bounced about 3% off the open. High-risk reversal trade only.",
  "Brazil market and BRL moves", "Further de-risking of Brazil", (-6,1.5,8), 'Speculative', 'Reversal watch'),
 ('APO', "Up 3% with SpaceX-financing headlines; trending above its open.", "Holding the morning gain", "Market-wide fade", (-2,0.8,3), 'Medium', 'Momentum long'),
 ('MS', "Up 2% on the IPO-wave story with steady buying.", "Anthropic IPO headlines", "Bank group fades", (-1.5,0.6,2.5), 'Medium', 'Theme momentum'),
 ('CRCL', "Circle is down 7% and below its open: relative weakness.", "Below the open = weak", "Short squeezes on crypto news", (-4,-1,3), 'Speculative', 'Fade / avoid'),
 ('HOOD', "Down 3% ahead of tomorrow's results; pre-earnings positioning.", "Earnings Oct 27", "Big moves into the print", (-3,0,3), 'Speculative', 'Pre-earnings watch'),
]
P[('intraday','fin','SGX')] = [
 ('AIY.SI', "iFAST results land today; expect a large move at Tuesday's open.", "Q3 results reaction", "Miss sends it lower", (-5,1,6), 'Speculative', 'Results reaction'),
 ('G07.SI', "Great Eastern's volume is at 1.5x average with a small gain.", "Next session", "Thin float", (-1.5,0.5,2), 'Medium', 'Accumulation'),
 ('D05.SI', "DBS is flat; banks drift with US yields after the Fed.", "Next session", "Small range", (-1,0.3,1.2), 'High', 'Range'),
 ('U11.SI', "UOB is down 0.7%, near support.", "Next session", "Small range", (-1,0.3,1.2), 'Medium', 'Range'),
 ('S68.SI', "SGX is flat; volumes are rising with volatility.", "Next session", "Small range", (-1,0.3,1.2), 'Medium', 'Range'),
]

# IPO tab (6-month view), all markets
P[('ipo','all','US')] = [
 ('SPCX', "SpaceX listed in June at $135 (the largest IPO on record) and trades about 9% above that, below its first-day close. The $40B GPU financing makes it an AI-infrastructure story too.",
  "Lock-up expiries; xAI news", "Valuation and Musk headline risk", (-25,15,45), 'Medium', 'Mega-cap IPO'),
 ('CHYM', "Chime (IPO June 2025 at $27) is up 30% in 3 months with a 35% gap to analyst targets.", "Earnings Nov 4", "Fintech credit cycle", (-15,18,40), 'Medium', 'Post-IPO uptrend'),
 ('CRCL', "Circle (IPO June 2025 at $31) is a stablecoin issuer 44% off its high; earnings ride interest rates and USDC growth.", "Earnings Nov 4", "Rate cuts shrink its interest income", (-25,15,45), 'Speculative', 'Recovery'),
 ('LYCA', "Lycia Therapeutics priced at $18 on Oct 23 and is up over 50%: a hot biotech debut in a strong sector.", "First analyst coverage (~25 days after IPO)", "Fresh IPOs often fade from the first-week high", (-30,10,50), 'Speculative', 'New listing'),
 ('RTSN', "Retension Pharmaceuticals is up about 25% from its $12 IPO price (Oct 9).", "Analyst initiations", "Small float, high volatility", (-30,10,45), 'Speculative', 'New listing'),
]

# ---------- Power & grid (data-center power) ----------
P[('long','pwr','US')] = [
 ('GEV', "GE Vernova's gas turbines and grid gear are sold out for years as AI data centers race for power. Up 4.5% today, 27% off its high.", "Earnings Oct 28", "Rich valuation (34x forward)", (-18,25,45), 'High', 'Power bottleneck'),
 ('VRT', "Vertiv supplies power and liquid cooling for AI data centers. 47% off its high after the chip selloff; analysts see 66% upside.", "Earnings Oct 28", "Moves with AI capex sentiment", (-20,30,60), 'Medium', 'Pullback in a leader'),
 ('PWR', "Quanta builds the grid lines and substations that connect data centers. Revenue +41%.", "Earnings Oct 29", "Labour and project timing", (-15,22,40), 'High', 'Grid build-out'),
 ('ETN', "Eaton's electrical equipment (switchgear, transformers) is in short supply. Revenue +21% at 23x forward.", "Earnings Nov 3", "Industrial slowdown", (-12,18,32), 'High', 'Quality compounder'),
 ('TLN', "Talen sells nuclear power directly to Amazon data centers. Revenue +111% at 11x forward.", "Earnings Nov 3", "Power-price and regulatory risk", (-20,25,50), 'Medium', 'Nuclear power for AI'),
]
P[('long','pwr','SGX')] = [
 ('AJBU.SI', "Keppel DC REIT owns data centers in Asia and Europe. 16 analysts rate it Strong Buy; you also collect a steady dividend.", "Q3 update (Nov)", "Interest rates", (-8,14,25), 'High', 'Data-center income'),
 ('BN4.SI', "Keppel runs infrastructure, data-center and renewables funds. Oversold (RSI 18) with 27% analyst upside.", "Q3 update Oct 29", "Asset-sale timing", (-12,15,30), 'Medium', 'Infrastructure manager'),
 ('U96.SI', "Sembcorp: power generation and renewables at under 10x forward earnings; revenue +28%.", "Results (Feb)", "Fell 2.8% today on heavy volume", (-10,12,25), 'Medium', 'Cheap utility'),
 ('544.SI', "CSE Global wires data centers and utilities. 48% off its high; 7 analysts see it doubling.", "Q3 update (Nov)", "Small and volatile", (-25,25,55), 'Speculative', 'Recovery'),
 ('DCRU.SI', "Digital Core REIT owns US data centers leased to big tech, 21% off its high.", "Q3 update (Nov)", "Tenant concentration", (-15,15,35), 'Speculative', 'Data-center income'),
]
P[('swing','pwr','US')] = [
 ('VRT', "Very oversold (RSI 18) into earnings in two days.", "Earnings Oct 28", "Gap risk on results", (-12,12,25), 'Medium', 'Rebound into earnings'),
 ('GEV', "Up 4.5% today, leading the group into its results.", "Earnings Oct 28", "High expectations", (-10,10,20), 'Medium', 'Momentum into earnings'),
 ('PWR', "Bouncing 4% from an oversold reading (RSI 20).", "Earnings Oct 29", "Gap risk on results", (-10,10,22), 'Medium', 'Oversold rebound'),
 ('BE', "Bloom Energy jumped 7.5% today after an 11% drop on Friday; fuel cells power data centers off-grid.", "Momentum", "Swings 6% a day", (-18,12,30), 'Speculative', 'Volatile rebound'),
 ('CEG', "Constellation (largest US nuclear fleet) is oversold (RSI 27) and 37% off its high.", "Earnings Nov 9", "Power-price rules", (-10,8,18), 'Medium', 'Oversold rebound'),
]
P[('swing','pwr','SGX')] = [
 ('544.SI', "CSE Global is deeply oversold (RSI 17) after a 26% monthly drop.", "Q3 update (Nov)", "Thin trading", (-12,12,25), 'Speculative', 'Oversold rebound'),
 ('BN4.SI', "Keppel is oversold (RSI 18) three days before its Q3 update.", "Q3 update Oct 29", "Update disappoints", (-6,6,12), 'Medium', 'Pre-results'),
 ('U96.SI', "Sembcorp dipped 2.8% on 2x volume; watch for a bounce at support.", "Next sessions", "Further selling", (-6,5,11), 'Medium', 'Pullback buy'),
 ('AJBU.SI', "Keppel DC REIT is holding steady near support.", "Q3 update (Nov)", "Rates", (-4,4,8), 'High', 'Range'),
 ('DCRU.SI', "Digital Core REIT is flat at a low level.", "Q3 update (Nov)", "No momentum", (-5,4,9), 'Speculative', 'Range'),
]
P[('intraday','pwr','US')] = [
 ('BE', "Up 7.5%, the strongest move in the group today.", "Momentum continuation", "Can reverse fast", (-5,1.5,6), 'Speculative', 'Momentum long'),
 ('GEV', "Up 4.5% with steady buying before earnings.", "Hold above the morning high", "Fades into the close", (-3,1,4), 'Medium', 'Momentum long'),
 ('PWR', "Up 4.3%, recovering with chips.", "Hold above the open", "Group fade", (-3,1,4), 'Medium', 'Rebound'),
 ('TLN', "Up 4.3% with the nuclear-power names.", "Momentum", "Volatile", (-4,1,4.5), 'Medium', 'Momentum long'),
 ('VRT', "Up 3% from an oversold level.", "Hold above the open", "Fades if chips turn", (-3,0.8,3.5), 'Medium', 'Oversold bounce'),
]
P[('intraday','pwr','SGX')] = [
 ('U96.SI', "Fell 2.8% on 2.1x normal volume; watch for a bounce or follow-through at the open.", "Next session open", "More selling", (-2,0.5,2.5), 'Medium', 'Volume watch'),
 ('BN4.SI', "Up 0.9% from an oversold level ahead of results.", "Next session", "Small range", (-1.5,0.5,2), 'Medium', 'Bounce'),
 ('544.SI', "Oversold small cap; may track US power stocks' rally.", "Gap up on US strength", "Thin trading", (-2.5,1,3.5), 'Speculative', 'Gap watch'),
 ('AJBU.SI', "Small dip; defensive range.", "Next session", "Small range", (-1,0.3,1.2), 'High', 'Range'),
 ('DCRU.SI', "Flat; low activity.", "Next session", "None", (-1.5,0.2,1.5), 'Speculative', 'Range'),
]

# ---------- Defence & industrials ----------
P[('long','def','US')] = [
 ('RTX', "Raytheon (missiles, air defence) and Pratt engines with a record backlog; revenue +11%, 13% off its high.", "Q4 results Jan", "Defence budget timing", (-10,15,28), 'High', 'Record backlog'),
 ('HWM', "Howmet makes jet-engine parts; revenue +24%. 34% off its high with 68% analyst upside.", "Earnings Oct 29", "Aircraft delivery delays", (-18,25,45), 'Medium', 'Pullback in a leader'),
 ('GE', "GE Aerospace earns on every flight hour from its engines; 24% off its high, Strong Buy.", "Q4 results Jan 21", "Airline demand", (-12,18,32), 'High', 'Quality compounder'),
 ('AXON', "Axon (Tasers, body cameras, police software): revenue +35% but 44% below its high.", "Earnings Nov 5", "Valuation (40x forward)", (-20,25,50), 'Medium', 'Growth at a discount'),
 ('KTOS', "Kratos makes drones and hypersonic test vehicles; revenue +30%, 69% off its high.", "Earnings Nov 5", "Very volatile; contract timing", (-30,30,70), 'Speculative', 'Drone warfare'),
]
P[('long','def','SGX')] = [
 ('S63.SI', "ST Engineering: defence, aerospace and smart-city tech with a steady order book.", "Q3 update (Nov)", "Valuation near the top of its range", (-10,12,25), 'High', 'Defence leader'),
 ('BS6.SI', "Yangzijiang Shipbuilding: full order book, revenue +36%, only 8x forward earnings.", "Q3 update (Nov)", "Shipping cycle", (-15,18,35), 'Medium', 'Cheap growth'),
 ('S59.SI', "SIA Engineering maintains aircraft for 80+ airlines; 22% off its high.", "Results Nov 3", "Flat revenue", (-12,14,28), 'Medium', 'Recovery'),
 ('H22.SI', "Hong Leong Asia makes power generators and building materials; 4 analysts see big upside.", "Q3 update (Nov)", "China property exposure", (-20,20,45), 'Speculative', 'Value'),
 ('C52.SI', "ComfortDelGro: taxis, buses and rail; a steady dividend payer.", "Q3 update (Nov)", "Slow growth", (-8,10,20), 'Medium', 'Defensive'),
]
P[('swing','def','US')] = [
 ('HWM', "Oversold (RSI 22) and up 4% today going into results.", "Earnings Oct 29", "Gap risk on results", (-10,10,22), 'Medium', 'Rebound into earnings'),
 ('CAT', "Caterpillar is the most oversold large industrial (RSI 11) before results; it also sells data-center generators.", "Earnings Oct 29", "Weak construction demand", (-10,10,22), 'Medium', 'Oversold rebound'),
 ('BA', "Boeing reports tomorrow; production-rate guidance can move it 5-10%.", "Earnings Oct 27", "Delivery problems", (-10,8,18), 'Speculative', 'Earnings setup'),
 ('HII', "Huntington Ingalls (warships) is trending up (RSI 66) into results.", "Earnings Oct 29", "Shipyard cost overruns", (-8,6,14), 'Medium', 'Momentum'),
 ('GE', "GE Aerospace is near oversold (RSI 30) with no earnings until January.", "Sector rotation", "Slow catalyst", (-8,7,15), 'Medium', 'Pullback buy'),
]
P[('swing','def','SGX')] = [
 ('S63.SI', "ST Engineering is oversold (RSI 19) after a 6% monthly dip.", "Q3 update (Nov)", "No near-term catalyst", (-5,5,10), 'High', 'Oversold rebound'),
 ('S59.SI', "SIA Engineering reports Nov 3 near its lows (RSI 31).", "Results Nov 3", "Weak margins", (-6,6,12), 'Medium', 'Pre-results'),
 ('BS6.SI', "Yangzijiang is pulling back to support within an uptrend.", "Q3 update (Nov)", "Shipping cycle", (-7,6,14), 'Medium', 'Pullback buy'),
 ('H22.SI', "Hong Leong Asia fell 15% this month; rebound candidate.", "Q3 update (Nov)", "China property", (-8,7,15), 'Speculative', 'Rebound'),
 ('C52.SI', "ComfortDelGro is steady in a narrow range.", "Q3 update (Nov)", "Little momentum", (-4,3,7), 'Medium', 'Range'),
]
P[('intraday','def','US')] = [
 ('HWM', "Up 4% from an oversold level.", "Hold above the open", "Fades with the market", (-3,1,4), 'Medium', 'Oversold bounce'),
 ('KTOS', "Up 3.7%; drone names are bouncing.", "Momentum", "Volatile", (-3.5,1,4), 'Speculative', 'Momentum long'),
 ('LMT', "Up 3.2% to new highs on defence demand from the Iran conflict.", "Record-high breakout", "Very overbought (RSI 86)", (-2.5,0.6,3), 'Medium', 'Breakout'),
 ('HII', "Up 2.2% ahead of Thursday's results.", "Hold gains", "Small range", (-2,0.5,2.5), 'Medium', 'Momentum'),
 ('RTX', "Up 2.1% in a steady trend.", "Hold gains", "Small range", (-2,0.5,2.5), 'High', 'Trend day'),
]
P[('intraday','def','SGX')] = [
 ('C52.SI', "Up 0.8% on near-normal volume.", "Next session", "Small range", (-1,0.3,1.2), 'Medium', 'Range'),
 ('S63.SI', "Oversold with normal volume; may follow US defence strength.", "Next session open", "Small range", (-1.2,0.4,1.5), 'High', 'Bounce watch'),
 ('BS6.SI', "Dipped 1%; watch for buyers at support.", "Next session", "Shipping news", (-2,0.5,2.5), 'Medium', 'Bounce watch'),
 ('H22.SI', "Fell 1.7%; weak.", "Next session", "Further selling", (-2.5,0,2.5), 'Speculative', 'Fade / avoid'),
 ('S59.SI', "Flat ahead of results next week.", "Next session", "None", (-1.2,0.2,1.2), 'Medium', 'Range'),
]

# ---------- Energy (oil & gas) ----------
P[('long','nrg','US')] = [
 ('LNG', "Cheniere exports US gas on 20-year contracts. Europe and Asia buy more US gas while the Strait of Hormuz is disrupted.", "Earnings Oct 29", "At a record already", (-12,10,22), 'High', 'Steady contracts'),
 ('SLB', "SLB (oilfield services) has lagged the oil rally; 13% off its high with 20% analyst upside.", "Q4 results Jan 22", "Oil price falls if Hormuz reopens", (-15,15,30), 'Medium', 'Laggard catch-up'),
 ('DVN', "Devon: revenue +64% at under 10x earnings; Strong Buy with 19% upside.", "Earnings Nov 5", "Oil price reversal", (-18,12,30), 'Medium', 'Cheap producer'),
 ('FANG', "Diamondback: a low-cost Permian producer at about 10x earnings.", "Earnings Nov 2", "Oil price reversal", (-18,12,28), 'Medium', 'Cheap producer'),
 ('XOM', "ExxonMobil: the most defensive oil stock with a dividend. Analysts see little upside after a 52% rally this year.", "Earnings Oct 30", "Oil falls if the conflict ends", (-15,5,18), 'High', 'Defensive income'),
]
P[('long','nrg','SGX')] = [
 ('5E2.SI', "Seatrium builds offshore rigs and wind platforms; 27% off its high with 38% analyst upside.", "Q3 update (Nov)", "Project cost overruns", (-20,18,40), 'Medium', 'Offshore recovery'),
 ('5LY.SI', "Marco Polo Marine runs offshore vessels for wind farms and oil; revenue +40%.", "Results (Nov)", "Penny stock, thin trading", (-25,18,45), 'Speculative', 'Offshore growth'),
 ('RE4.SI', "Geo Energy mines Indonesian coal at about 7x earnings.", "Q3 update (Nov)", "Coal price swings; ESG pressure", (-25,15,40), 'Speculative', 'Cheap commodity'),
 ('BN4.SI', "Keppel also owns offshore and energy infrastructure assets, giving it a steadier way into energy.", "Q3 update Oct 29", "Asset-sale timing", (-12,12,25), 'Medium', 'Diversified'),
 ('5WH.SI', "Rex International is a tiny oil explorer, down 71% in a year. Shown for completeness; avoid unless trading.", "Drilling results", "Losses; very small", (-40,0,40), 'Speculative', 'Avoid'),
]
P[('swing','nrg','US')] = [
 ('MPC', "Refiners are earning record margins; Marathon is up 2.7% today.", "Earnings Nov 3", "Margins fall if crude drops", (-10,6,15), 'Medium', 'Trend'),
 ('PSX', "Phillips 66 reports in two days with refining margins near records.", "Earnings Oct 28", "Gap risk on results", (-10,6,15), 'Medium', 'Earnings setup'),
 ('SLB', "SLB dipped 1.7% today in an uptrend; a pullback entry.", "Oil stays above $100", "Hormuz reopening", (-8,7,15), 'Medium', 'Pullback buy'),
 ('HAL', "Halliburton is trending up (RSI 67) with room to its high.", "Oil prices", "Oil reversal", (-8,6,14), 'Medium', 'Trend'),
 ('OXY', "Occidental tracks oil closely; overbought (RSI 81) but still trending.", "Earnings Nov 9", "Overbought", (-10,5,14), 'Medium', 'Momentum'),
]
P[('swing','nrg','SGX')] = [
 ('5E2.SI', "Seatrium is oversold (RSI 29) on 1.3x volume.", "Q3 update (Nov)", "Contract delays", (-8,8,16), 'Medium', 'Oversold rebound'),
 ('5LY.SI', "Marco Polo is oversold (RSI 24) and up 1.9% today.", "Results (Nov)", "Thin trading", (-10,10,22), 'Speculative', 'Rebound'),
 ('RE4.SI', "Geo Energy is oversold (RSI 27).", "Coal prices", "Coal price drop", (-10,8,18), 'Speculative', 'Rebound'),
 ('BN4.SI', "Keppel is oversold before its Oct 29 update.", "Q3 update Oct 29", "Weak update", (-6,6,12), 'Medium', 'Pre-results'),
 ('5WH.SI', "Rex is in a downtrend; no setup.", "None", "Further losses", (-15,0,15), 'Speculative', 'Avoid'),
]
P[('intraday','nrg','US')] = [
 ('MPC', "Up 2.7%, leading energy today.", "Hold above the open", "Crude drops", (-2.5,0.8,3), 'Medium', 'Momentum long'),
 ('PSX', "Up 2.1% before results.", "Hold gains", "Crude drops", (-2.5,0.6,3), 'Medium', 'Momentum long'),
 ('LNG', "Up 1.2% at a record high.", "Breakout", "Overbought", (-2,0.5,2.5), 'High', 'Breakout'),
 ('SLB', "Down 1.7%, weaker than peers.", "Below the open = weak", "Sharp reversals", (-3,-0.5,2), 'Medium', 'Fade / avoid'),
 ('CVX', "Flat at a record; Brent is easing toward $110 today.", "Oil moves", "Oil drops", (-1.5,0,1.5), 'High', 'Range'),
]
P[('intraday','nrg','SGX')] = [
 ('5LY.SI', "Up 1.9% from an oversold level.", "Next session", "Thin trading", (-2.5,1,3.5), 'Speculative', 'Bounce'),
 ('5E2.SI', "Up 0.6% on 1.3x volume.", "Next session", "Small range", (-2,0.5,2.5), 'Medium', 'Accumulation'),
 ('RE4.SI', "Up 1%, oversold.", "Next session", "Coal prices", (-2,0.5,2.5), 'Speculative', 'Bounce'),
 ('BN4.SI', "Small gain before results.", "Next session", "Small range", (-1.5,0.5,2), 'Medium', 'Range'),
 ('5WH.SI', "Down 2%; avoid.", "None", "Further losses", (-5,-1,4), 'Speculative', 'Avoid'),
]

IPO_LIST = [
 # sym, name, ipo_date, ipo_price, sector, status
 ('ANTHROPIC','Anthropic (not yet listed)','2026-10-26',None,'ai','Filed'),
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

SERENITY = {'NVDA','SPCX','AXTI','LITE','COHR','NBIS','MU','AVGO','AAOI','AEHR','GLW','SNDK','POET','IREN','TSEM','MRVL','AMD','ARM','INTC','TSM'}

X_POSTS = [
 ('2026-10-26T01:26','SPCX NVDA AXTI', "Says SpaceX's $40B financing will mostly fund Nvidia GPU purchases in H1 2027, lifting demand for memory and networking. Quotes VPEC that indium phosphide substrates are 'seriously in short supply' (AXTI); Morgan Stanley sees InP, EML and CW lasers as the main bottlenecks. Concludes any slowdown seems unlikely."),
 ('2026-10-25T22:00','NVDA AVGO', "Criticises X's owner for amplifying collapse narratives about companies that compete with SpaceX and Tesla, asking how people would feel if Jensen Huang owned Meta and amplified stories of Broadcom failing."),
 ('2026-10-25T12:00','NVDA LITE COHR', "Quotes Jensen Huang that moving scale-up to optics is 'going to be, well, 15x' aggregate volume. Argues the CW-laser bottleneck can't be met at that scale and expects allocation wars and price hikes for lasers."),
 ('2026-10-25T08:00','NBIS MU', "Highlights Amazon CEO Andy Jassy: the memory shortage won't end in 2027 and AWS capacity is largely sold out through 2027. Reads it as validating the neocloud model (Nebius)."),
 ('2026-10-25T04:00','LITE COHR AAOI', "Lists Chinese laser-capacity expansions (Source Photonics, Shijia, Yunling, Ligent, Yuanjie, Hongchen) and argues most full capacity arrives only around 2029, so claims of an H2 2026 laser flood are overstated."),
]

EVENTS = [
 ('2026-10-26','AI','Anthropic files for its IPO', "First listing by a standalone frontier-AI lab; Q2 sales $11.6B vs $787M a year earlier. Lifted chip stocks at the open."),
 ('2026-10-26','Fin','Lula wins Brazil election', "Brazilian stocks fell sharply: NU about -20%, MercadoLibre and Petrobras lower."),
 ('2026-10-26','AI','Meta plans up to $95B raise for AI infrastructure', "Another large AI capex funding round; Meta shares fell."),
 ('2026-10-28','Macro','FOMC rate decision', "2:00 PM New York time (02:00 Thu in Singapore). Markets mostly expect a hold."),
 ('2026-10-26','Energy','Brent near $110 on Strait of Hormuz disruption', "The Iran conflict keeps oil and defence stocks near records; a reopening deal is the main downside risk for both."),
 ('2026-10-28','AI','Microsoft, Alphabet, Meta earnings', "After the US close: AI capex guidance drives chips."),
 ('2026-11-01','Macro','US clocks change', "Daylight saving ends: from Nov 2, NYSE/Nasdaq open at 22:30 Singapore time instead of 21:30."),
]
