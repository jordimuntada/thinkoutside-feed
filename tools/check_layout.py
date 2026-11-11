"""
check_layout.py — Detecta problemas reales de maquetacion en los SVG.

Modelo de tinta (Raleway): para un texto con linea base B y tamano F,
la banda de tinta real es aproximadamente:
    arriba  = B - 0.78*F   (altura de mayuscula)
    abajo   = B + 0.22*F   (descendente)
Medir con getBoundingClientRect() no sirve: devuelve la caja em completa
(ascent/descent) y da falsos positivos en todos los titulares.

Detecta:
  - lineas/figuras decorativas que CRUZAN texto (el fallo clasico)
  - texto que se solapa con otro texto
  - texto fuera del lienzo o de la zona segura
  - texto que invade la zona del footer
  - numeros descentrados dentro de circulos o pills

Uso:
    python tools\\check_layout.py creatives\\es
    python tools\\check_layout.py creatives\\ca
"""

import base64
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.parse

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONT_DIR = ROOT / "tools" / "_fonts"
W, H = 1080, 1350
SAFE = 60          # margen minimo de seguridad
FOOTER_ZONE = 1230 # por debajo de esto ya hay footer

CAP = 0.78   # altura de mayuscula sobre la linea base
DESC = 0.22  # descendente bajo la linea base

JS = r"""
(function(){
  const svg = document.querySelector('svg');
  const r = svg.getBoundingClientRect();
  const sx = 1080 / r.width, sy = 1350 / r.height;
  const out = {texts:[], shapes:[]};

  function pt(el, i){
    const p = el.getStartPositionOfChar(i);
    const m = el.getScreenCTM();
    const q = svg.createSVGPoint(); q.x = p.x; q.y = p.y;
    const d = q.matrixTransform(m);
    return {x:(d.x - r.left)*sx, y:(d.y - r.top)*sy};
  }
  function endPt(el, i){
    const p = el.getEndPositionOfChar(i);
    const m = el.getScreenCTM();
    const q = svg.createSVGPoint(); q.x = p.x; q.y = p.y;
    const d = q.matrixTransform(m);
    return {x:(d.x - r.left)*sx, y:(d.y - r.top)*sy};
  }
  function box(el){
    const b = el.getBoundingClientRect();
    return {x:(b.left-r.left)*sx, y:(b.top-r.top)*sy, w:b.width*sx, h:b.height*sy};
  }

  const grpIds = new Map(); let gi = 0;
  document.querySelectorAll('text').forEach((el, i) => {
    const cs = getComputedStyle(el);
    const fs = parseFloat(cs.fontSize);
    const n = el.getNumberOfChars();
    const content = (el.textContent||'').trim();
    if (!n) { out.texts.push({i, content, empty:true}); return; }
    const b0 = pt(el, 0);
    const e0 = endPt(el, n-1);
    const x0 = Math.min(b0.x, e0.x), x1 = Math.max(b0.x, e0.x);
    const parent = el.parentNode;
    if (!grpIds.has(parent)) grpIds.set(parent, gi++);
    out.texts.push({
      i, content, fs, baseline: b0.y, grp: grpIds.get(parent),
      x:+x0.toFixed(1), x1:+x1.toFixed(1),
      y:+(b0.y - CAP*fs).toFixed(1),      // tope de tinta
      y2:+(b0.y + DESC*fs).toFixed(1),    // base de tinta
      w:+(x1-x0).toFixed(1),
      weight: cs.fontWeight,
      anchor: el.getAttribute('text-anchor') || 'start',
      family: cs.fontFamily.split(',')[0].replace(/["']/g,'')
    });
  });

  document.querySelectorAll('rect, circle, ellipse, line, path').forEach((el, i) => {
    const b = box(el);
    const tag = el.tagName.toLowerCase();
    const full = (tag === 'rect' && b.w > 1000 && b.h > 1000);
    out.shapes.push({
      i, tag, full,
      x:+b.x.toFixed(1), y:+b.y.toFixed(1), w:+b.w.toFixed(1), h:+b.h.toFixed(1),
      fill: el.getAttribute('fill'), stroke: el.getAttribute('stroke'),
      sw: parseFloat(el.getAttribute('stroke-width')||'0'),
      opacity: el.getAttribute('opacity')
    });
  });
  document.title = 'REPORT:' + encodeURIComponent(JSON.stringify(out));
})();
"""


def find_chrome():
    for c in CHROME_CANDIDATES:
        if pathlib.Path(c).exists():
            return c
    raise SystemExit("No se encuentra Chrome ni Edge.")


def font_b64(name):
    return base64.b64encode((FONT_DIR / name).read_bytes()).decode("ascii")


def measure(svg_path, chrome, fonts, tmp):
    html = tmp / (svg_path.stem + ".check.html")
    html.write_text(
        f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Raleway';src:url(data:font/ttf;base64,{fonts}) format('truetype');font-weight:100 900;font-display:block;}}
html,body{{margin:0;padding:0;}}
svg{{display:block;width:{W}px;height:{H}px;}}
</style></head><body>{svg_path.read_text(encoding='utf-8')}
<script>const CAP={CAP}, DESC={DESC};</script>
<script>{JS}</script></body></html>""",
        encoding="utf-8",
    )
    res = subprocess.run(
        [chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars",
         "--allow-file-access-from-files", "--force-device-scale-factor=1",
         "--virtual-time-budget=5000", "--dump-dom", html.as_uri()],
        capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120,
    )
    m = re.search(r"REPORT:(.*?)</title>", res.stdout or "", re.S)
    if not m:
        return None
    return json.loads(urllib.parse.unquote(m.group(1)))


def hit(a, b):
    """solape entre dos rectangulos {x,y,x1,y2}"""
    ox = min(a["x1"], b["x1"]) - max(a["x"], b["x"])
    oy = min(a["y2"], b["y2"]) - max(a["y"], b["y"])
    return (ox, oy) if ox > 0.5 and oy > 0.5 else None


def analyse(data):
    issues = []
    texts = [t for t in data["texts"] if not t.get("empty")]
    shapes = data["shapes"]

    def tbox(t):
        return {"x": t["x"], "x1": t["x1"], "y": t["y"], "y2": t["y2"]}

    # 1. texto vs texto
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            a, b = texts[i], texts[j]
            r = hit(tbox(a), tbox(b))
            if r:
                issues.append(
                    f"TEXTO  «{a['content'][:28]}» ↔ «{b['content'][:28]}»  solapa {r[0]:.0f}x{r[1]:.0f}px")

    # 2. figuras decorativas cruzando texto
    for s in shapes:
        if s["full"]:
            continue
        if s["tag"] == "path":
            continue
        # Chrome no incluye el trazo en el bbox de <line>: lo expandimos
        sw = (s.get("sw") or 0) / 2.0
        sbox = {"x": s["x"] - sw, "x1": s["x"] + s["w"] + sw,
                "y": s["y"] - sw, "y2": s["y"] + s["h"] + sw}
        for t in texts:
            tb = tbox(t)
            # la figura CONTIENE el texto -> es su contenedor (card, pill, circulo)
            if (tb["x"] >= sbox["x"] - 2 and tb["x1"] <= sbox["x1"] + 2
                    and tb["y"] >= sbox["y"] - 2 and tb["y2"] <= sbox["y2"] + 2):
                continue
            r = hit(sbox, tb)
            if r and r[0] > 2 and r[1] > 1:
                issues.append(
                    f"CRUZA  <{s['tag']}> en y={s['y']:.0f} atraviesa «{t['content'][:30]}» ({r[0]:.0f}x{r[1]:.0f}px)")

    # 3. fuera del lienzo
    for t in texts:
        if t["x"] < -0.5 or t["x1"] > W + 0.5 or t["y"] < -0.5 or t["y2"] > H + 0.5:
            issues.append(f"FUERA  «{t['content'][:40]}»  x={t['x']}..{t['x1']} y={t['y']}..{t['y2']}")

    # el footer: textos del mismo grupo que el que lleva "EXPERTOS EN INSTALACIONES"
    footer_groups = {t["grp"] for t in texts if "EXPERTOS EN INSTALACIONES" in t["content"]}
    footer_top = min((t["y"] for t in texts if t["grp"] in footer_groups), default=None)

    # 4. invade la zona del footer
    if footer_top is not None:
        for t in texts:
            if t["grp"] in footer_groups:
                continue
            if t["y2"] > footer_top:
                issues.append(f"FOOTER «{t['content'][:38]}» llega a y={t['y2']:.0f} (footer empieza en {footer_top:.0f})")

    # 5. fuera de la zona segura
    for t in texts:
        if t["grp"] in footer_groups:
            continue
        if t["x"] < SAFE - 1 or t["x1"] > W - SAFE + 1:
            issues.append(f"SEGURA «{t['content'][:38]}» x={t['x']:.0f}..{t['x1']:.0f} (margen {SAFE})")

    # 6. circulos: el texto debe estar centrado
    for t in texts:
        for s in shapes:
            if s["tag"] != "circle":
                continue
            cx, cy = s["x"] + s["w"] / 2, s["y"] + s["h"] / 2
            tcx = (t["x"] + t["x1"]) / 2
            tcy = (t["y"] + t["y2"]) / 2
            if abs(tcx - cx) < s["w"] / 2 and abs(tcy - cy) < s["h"] / 2:
                dv, dh = tcy - cy, tcx - cx
                if abs(dv) > s["h"] * 0.10:
                    issues.append(f"VERT   «{t['content'][:14]}» descentrado {dv:+.0f}px en circulo r={s['w']/2:.0f}")
                if abs(dh) > s["w"] * 0.10:
                    issues.append(f"HORIZ  «{t['content'][:14]}» descentrado {dh:+.0f}px en circulo")

    return issues


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    src = pathlib.Path(sys.argv[1])
    chrome = find_chrome()
    fonts = font_b64("Raleway.ttf")
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="check_"))
    total = 0
    try:
        for svg in sorted(src.glob("*.svg")):
            data = measure(svg, chrome, fonts, tmp)
            if data is None:
                print(f"?? {svg.name}: no se pudo medir")
                continue
            issues = analyse(data)
            if issues:
                print(f"\n=== {svg.name}  ({len(issues)}) ===")
                for i in issues:
                    print("   " + i)
                total += len(issues)
            else:
                print(f"OK   {svg.name}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print(f"\n--- {total} avisos en total ---")


if __name__ == "__main__":
    main()
