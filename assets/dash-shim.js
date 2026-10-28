/* JIDAI Quick Trade — standalone data layer.
   Gives the page the same small `dash` API it uses inside Claude (data, onData, calc, setLink, colors),
   but reads the JSON files that GitHub Actions publishes next to the page in data/. */
(function () {
  const BASE = 'data/';
  const store = {};
  const calcs = {};
  const listeners = [];
  let queued = false;

  function notify() {
    if (queued) return;
    queued = true;
    requestAnimationFrame(() => {
      queued = false;
      for (const fn of listeners) { try { fn(); } catch (e) { console.error(e); } }
    });
  }

  async function load(id, force) {
    const cur = store[id];
    if (cur && !force) return;
    if (cur) cur.refreshing = true; else store[id] = { status: 'loading', data: [], columns: [], meta: [], refreshing: false };
    try {
      const r = await fetch(BASE + id + '.json?v=' + Date.now(), { cache: 'no-store' });
      if (!r.ok) throw new Error('HTTP ' + r.status);
      const d = await r.json();
      const rows = Array.isArray(d) ? d : (d.rows || d.data || d.results || []);
      store[id] = { status: 'ok', data: rows, columns: rows[0] ? Object.keys(rows[0]) : [], meta: [], refreshing: false };
    } catch (e) {
      store[id] = { status: cur && cur.status === 'ok' ? 'ok' : 'error', data: cur ? cur.data : [], columns: cur ? cur.columns : [], meta: [], message: String(e), refreshing: false };
    }
    for (const k in calcs) delete calcs[k].cache;
    notify();
  }

  function calcData(id) {
    const c = calcs[id];
    const ins = c.inputs.map((i) => window.dash.data(i));
    if (ins.some((x) => x.status === 'error')) return { status: 'error', data: [], meta: [] };
    if (ins.some((x) => x.status !== 'ok')) return { status: 'loading', data: [], meta: [] };
    if (!c.cache) {
      try { c.cache = { status: 'ok', data: c.fn(...ins.map((x) => x.data)), meta: [] }; }
      catch (e) { console.error(e); c.cache = { status: 'error', data: [], meta: [], message: String(e) }; }
    }
    return c.cache;
  }

  let rz;
  window.addEventListener('resize', () => { clearTimeout(rz); rz = setTimeout(notify, 150); });

  window.dash = {
    colors: ['#7048e8', '#0c8f80', '#d9480f', '#1971c2', '#c2255c', '#b7791f', '#2f9e44', '#868e96'],
    data(id) { if (calcs[id]) return calcData(id); if (!store[id]) load(id); return store[id]; },
    onData(fn) { listeners.push(fn); try { fn(); } catch (e) { console.error(e); } },
    calc(id, def) { calcs[id] = { inputs: def.inputs, fn: def.fn }; },
    loader() {},
    setLink(name) { try { history.replaceState(null, '', '#' + name); } catch (e) {} },
    params() { return {}; }, setParams() {}, resetParams() {},
    refresh(id) { return load(id, true); },
    /* re-fetch every file the page has opened (used by the Refresh button and the auto-refresh timer) */
    refreshAll() { return Promise.all(Object.keys(store).map((id) => load(id, true))); },
  };
})();
