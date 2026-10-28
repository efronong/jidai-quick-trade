// JIDAI Quick Trade collector: run on a finance.yahoo.com page in the browser.
// Stores one JSON string in window.__jidai: {fetchedAt, U, q:{sym:{meta,fund,news,intra,ser}}}; returns its size.
// Then read it in chunks: javascript_exec `window.__jidai.slice(k*120000, (k+1)*120000)` for k = 0..chunks-1, and join the chunk texts in order.
(async () => {
const U = {
 ai: ['NVDA','AMD','AVGO','TSM','MU','MRVL','ARM','INTC','COHR','LITE','AAOI','AXTI','SNDK','AEHR','TSEM','POET','NBIS','SMCI','ASML','AMAT','LRCX','KLAC','QCOM','CRDO','ALAB','ANET','PLTR','CIEN','GLW','WDC','STX','IREN','CRWV','ORCL','AWX.SI','558.SI','E28.SI','V03.SI','MZH.SI','5DD.SI'],
 hc: ['LLY','NVO','MRNA','VRTX','REGN','AMGN','ISRG','ABBV','UNH','GILD','BIIB','CRSP','VKTX','MDGL','ALNY','ARGX','INSM','TEM','HIMS','RXRX','NTLA','BEAM','DXCM','BOLT','CYTK','SRPT','PFE','MRK','JNJ','BSL.SI','Q0F.SI','AP4.SI','H02.SI','QC7.SI','C2PU.SI','A50.SI'],
 fin: ['JPM','GS','MS','BAC','C','WFC','V','MA','AXP','PYPL','XYZ','HOOD','SOFI','COIN','AFRM','UPST','NU','SCHW','BLK','KKR','APO','IBKR','CRCL','CHYM','KLAR','SE','GRAB','D05.SI','O39.SI','U11.SI','S68.SI','AIY.SI','G07.SI'],
 pwr: ['VRT','GEV','ETN','PWR','CEG','VST','NRG','TLN','OKLO','SMR','BE','CCJ','NEE','U96.SI','BN4.SI','544.SI','AJBU.SI','DCRU.SI'],
 def: ['LMT','RTX','NOC','GD','LHX','GE','HWM','AXON','KTOS','AVAV','BA','CAT','HII','S63.SI','BS6.SI','S59.SI','C52.SI','H22.SI'],
 nrg: ['XOM','CVX','COP','OXY','EOG','SLB','LNG','HAL','DVN','FANG','MPC','PSX','RE4.SI','5WH.SI','NO4.SI','5LY.SI','5E2.SI'],
 ipo: ['SPCX','LYCA','CTY','AMRO','IAM','RTSN','TRXB','ACCV','ADRX','ASBH','ETRA','OIG','FIG','CRWV','CRCL','CHYM','KLAR']
};
const syms = [...new Set(Object.values(U).flat())];
const crumb = encodeURIComponent(await (await fetch('https://query1.finance.yahoo.com/v1/test/getcrumb',{credentials:'include'})).text());
const v = x => x?.raw ?? null;
const J = async u => (await fetch(u,{credentials:'include'})).json();
const q = {};
async function one(s){
  const o = {};
  try {
    const r = (await J(`https://query1.finance.yahoo.com/v8/finance/chart/${encodeURIComponent(s)}?range=5y&interval=1d`)).chart.result[0];
    const m = r.meta; o.meta = {name:m.longName||m.shortName, ex:m.fullExchangeName, cur:m.currency, px:m.regularMarketPrice, chg:m.regularMarketChangePercent, time:m.regularMarketTime, vol:m.regularMarketVolume, hi52:m.fiftyTwoWeekHigh, lo52:m.fiftyTwoWeekLow, pc:m.chartPreviousClose};
    const t=[],c=[],vv=[]; const Q=r.indicators.quote[0];
    for(let i=0;i<r.timestamp.length;i++) if(Q.close[i]!=null){t.push(Math.round(r.timestamp[i]/86400)); c.push(Q.close[i]); vv.push(Q.volume[i]||0);}
    const last=c[c.length-1], n=c.length, cut=Math.max(0,n-252), wi=[]; for(let i=0;i<cut;i+=5) wi.push(i);
    const di=[]; for(let i=cut;i<n;i++) di.push(i);
    const enc=idx=>idx.map(i=>Math.round(c[i]/last*1000)).join(',');
    const dd=idx=>idx.map((i,k)=>k===0?t[i]:t[i]-t[idx[k-1]]).join(',');
    o.ser = {last, wd:dd(wi), wc:enc(wi), dd:dd(di), dc:enc(di), v20: vv.slice(-21,-1).reduce((a,b)=>a+b,0)/20, vLast: vv[vv.length-1]};
  } catch(e) { o.err = String(e); }
  try {
    const r = (await J(`https://query1.finance.yahoo.com/v8/finance/chart/${encodeURIComponent(s)}?range=1d&interval=5m`)).chart.result[0];
    const iq=r.indicators.quote[0]||{};
    o.intra = {t0:r.timestamp?.[0]||null, c:(iq.close||[]).map(x=>x==null?null:+x.toPrecision(5)), open:(iq.open||[]).find(x=>x!=null)??null, high:r.meta.regularMarketDayHigh??null, low:r.meta.regularMarketDayLow??null, pc:r.meta.chartPreviousClose??r.meta.previousClose??null, time:r.meta.regularMarketTime??null};
  } catch(e) {}
  try {
    const x = (await J(`https://query2.finance.yahoo.com/v10/finance/quoteSummary/${encodeURIComponent(s)}?modules=financialData,calendarEvents,summaryDetail,assetProfile&crumb=${crumb}`)).quoteSummary.result[0];
    const fd=x.financialData||{}, sd=x.summaryDetail||{};
    o.fund = {tgt:v(fd.targetMeanPrice),tHi:v(fd.targetHighPrice),tLo:v(fd.targetLowPrice),rec:fd.recommendationKey||null,nA:v(fd.numberOfAnalystOpinions),rg:v(fd.revenueGrowth),eg:v(fd.earningsGrowth),fpe:v(sd.forwardPE),mcap:v(sd.marketCap),beta:v(sd.beta),ind:x.assetProfile?.industry||null,earn:(x.calendarEvents?.earnings?.earningsDate||[]).map(e=>e.fmt)[0]||null};
  } catch(e) {}
  try {
    const n = await J(`https://query1.finance.yahoo.com/v1/finance/search?q=${encodeURIComponent(s)}&newsCount=4&quotesCount=0`);
    o.news = (n.news||[]).map(a=>({t:a.title,p:a.publisher,d:new Date(a.providerPublishTime*1000).toISOString().slice(0,16),u:a.link}));
  } catch(e) {}
  q[s] = o;
}
for(let i=0;i<syms.length;i+=8) await Promise.all(syms.slice(i,i+8).map(one));
window.__jidai = JSON.stringify({fetchedAt:new Date().toISOString(), U, q});
return {chars: window.__jidai.length, chunks: Math.ceil(window.__jidai.length / 120000), failed: Object.keys(q).filter(k => !q[k].ser)};
})()
