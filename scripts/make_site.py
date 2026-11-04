"""Wrap the dashboard page (page.html: the same <style>+markup+<script> the Claude dashboard uses) into a standalone index.html."""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
page = (root / 'page.html').read_text()
fonts = {'985a07612c31de3a2714640dd348a4ec': '400', '054c4ccdcd285428e5b39df0e1f90725': '500', 'a4e543e5fa1372544446dbb06322b828': '700'}
for blob, w in fonts.items():
    page = page.replace(f'url(/_blob/{blob})', f'url(assets/fonts/roboto-latin-{w}-normal.woff2)')

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#0f1117">
<title>JIDAI Quick Trade</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700;9..40,800&display=swap" rel="stylesheet">
<style>
/* Theme tokens (the Claude dashboard supplies these; here we define them for light and dark) */
:root { color-scheme: light;
  --color-bg: #f6f7fb; --color-panel: rgba(255,255,255,.84); --color-fg: #14161f; --color-fg-muted: #5f6475; --color-border-line: #e2e5ee;
  --color-ok: #1f9d55; --color-bad: #d63a3a; --color-warn: #b7791f;
  --cds-surface-popover: #ffffff; --cds-border: #dfe3ec; --cds-shadow-popover: 0 8px 24px rgba(20,22,31,.14); --cds-text-secondary: #5f6475;
  --cds-chart-grid: #eceff5; --cds-chart-axis: #b9bfcc; --cds-chart-reference: #9aa1b1;
  --cds-radius: 10px; --cds-gap-sm: 8px; --cds-gap-md: 14px; --cds-gap-lg: 22px;
  --cds-pad-xs: 4px; --cds-pad-sm: 8px; --cds-pad-lg: 16px; --cds-pad-xl: 24px;
  --cds-font-size-caption: 12.5px; --cds-font-size-body: 14.5px; --cds-font-size-heading: 16px; --cds-font-weight-medium: 600;
  --cds-dur-slow: 320ms; --cds-ease-out: cubic-bezier(.2,.8,.2,1);
  --font-anthropic-sans: 'DM Sans', system-ui, -apple-system, 'Segoe UI', sans-serif; --font-anthropic-serif: 'DM Sans', system-ui, sans-serif; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { color-scheme: dark;
  --color-bg: #0f1117; --color-panel: rgba(23,26,35,.8); --color-fg: #eef0f6; --color-fg-muted: #9aa0b2; --color-border-line: #272b38;
  --color-ok: #3ccf7a; --color-bad: #ff6b6b; --color-warn: #f0b429;
  --cds-surface-popover: #1d2130; --cds-border: #2e3344; --cds-shadow-popover: 0 8px 24px rgba(0,0,0,.5); --cds-text-secondary: #9aa0b2;
  --cds-chart-grid: #222634; --cds-chart-axis: #3a4052; --cds-chart-reference: #586078; } }
:root[data-theme="dark"] { color-scheme: dark;
  --color-bg: #0f1117; --color-panel: rgba(23,26,35,.8); --color-fg: #eef0f6; --color-fg-muted: #9aa0b2; --color-border-line: #272b38;
  --color-ok: #3ccf7a; --color-bad: #ff6b6b; --color-warn: #f0b429;
  --cds-surface-popover: #1d2130; --cds-border: #2e3344; --cds-shadow-popover: 0 8px 24px rgba(0,0,0,.5); --cds-text-secondary: #9aa0b2;
  --cds-chart-grid: #222634; --cds-chart-axis: #3a4052; --cds-chart-reference: #586078; }
html, body { margin: 0; background: var(--color-bg); color: var(--color-fg); font-family: var(--font-anthropic-sans); font-size: 14px; -webkit-text-size-adjust: 100%; }
#dash-root { max-width: 1280px; margin: 0 auto; padding: max(12px, env(safe-area-inset-top, 0px)) max(14px, env(safe-area-inset-right, 0px)) 40px max(14px, env(safe-area-inset-left, 0px)); }
[hidden] { display: none !important; }
.dash-skeleton { color: transparent !important; background: linear-gradient(90deg, var(--color-border-line), var(--color-panel), var(--color-border-line)); background-size: 200% 100%; border-radius: 6px; animation: sk 1.4s linear infinite; }
@keyframes sk { to { background-position: -200% 0; } }
/* Background artwork: rising red trend line, fixed behind the page */
body::before { content: ""; position: fixed; inset: auto 0 0 0; height: 70vh; z-index: 0; pointer-events: none;
  background: url(assets/bg-trend.webp) no-repeat right bottom / min(1500px, 115vw) auto; opacity: .38; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) body::before { opacity: .7; } }
:root[data-theme="dark"] body::before { opacity: .7; }
@media (max-width: 640px) { body::before { height: 55vh; background-size: 230vw auto; background-position: 65% bottom; } }
#dash-root { position: relative; z-index: 1; }
.live-bar { display: flex; align-items: center; justify-content: space-between; gap: 10px; flex-wrap: wrap; margin-bottom: 10px; font-size: 12.5px; color: var(--color-fg-muted); }
.live-bar .dot { display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: var(--color-ok); margin-right: 6px; vertical-align: middle; }
.live-bar .dot.stale { background: var(--color-warn); }
.live-bar button { font: inherit; font-weight: 700; border: 1px solid var(--color-border-line); background: var(--color-panel); color: var(--color-fg); border-radius: 99px; padding: 7px 14px; cursor: pointer; display: inline-flex; gap: 6px; align-items: center; }
.live-bar button:disabled { opacity: .6; }
.live-bar button .spin { display: inline-block; }
.live-bar button.busy .spin { animation: rot 0.9s linear infinite; }
@keyframes rot { to { transform: rotate(360deg); } }
.live-bar .tg { display: inline-flex; gap: 6px; align-items: center; }
</style>
<script src="assets/d3.min.js"></script>
<script src="assets/dash-shim.js"></script>
</head>
<body>
<div id="dash-root">
<div class="live-bar" id="live-bar">
  <span><span class="dot" id="live-dot"></span><span id="live-text">Loading prices…</span></span>
  <span class="tg"><button id="live-refresh" type="button" aria-label="Refresh prices"><span class="spin">⟳</span> Refresh</button></span>
</div>
"""
TAIL = """
</div>
<script>
(() => {
  // Auto-refresh: re-read the data files every 2 minutes while the page is open; the Refresh button does it now.
  const btn = document.getElementById('live-refresh'), txt = document.getElementById('live-text'), dot = document.getElementById('live-dot');
  const fmt = new Intl.DateTimeFormat('en-SG', { timeZone: 'Asia/Singapore', weekday: 'short', day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit', hourCycle: 'h23' });
  function stamp() {
    const s = window.dash.data('stocks');
    if (s.status !== 'ok' || !s.data.length) return;
    const t = new Date(s.data[0].updated_utc + ':00Z'); const age = (Date.now() - t) / 6e4;
    dot.classList.toggle('stale', age > 30);
    txt.textContent = `Prices from ${fmt.format(t)} SGT · ${age < 1 ? 'just now' : Math.round(age) + ' min ago'} · updates every 10 min in market hours`;
  }
  window.dash.onData(stamp);
  async function refresh() { btn.disabled = true; btn.classList.add('busy'); try { await window.dash.refreshAll(); } finally { btn.disabled = false; btn.classList.remove('busy'); stamp(); } }
  btn.addEventListener('click', refresh);
  setInterval(() => { if (!document.hidden) refresh(); }, 120000);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) refresh(); });
  setInterval(stamp, 30000);
})();
</script>
</body>
</html>
"""
out = HEAD + page + TAIL
(root / 'site').mkdir(exist_ok=True)
(root / 'site' / 'index.html').write_text(out)
print('site/index.html', len(out))
