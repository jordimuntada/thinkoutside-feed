"""
export_ai.py — Genera entregables editables en Adobe Illustrator.

Por cada SVG fuente produce tres formatos:

  ai/svg/<name>.svg        SVG limpio: texto vivo, font-family="Raleway" (sin el stack CSS)
  ai/outlined/<name>.svg   SVG con TODO el texto convertido en trazados (0 fuentes necesarias)
  ai/pdf/<name>.pdf        PDF vectorial con texto real e incrustado

Notas:
  - El PDF y el SVG "outlined" se generan pasando el SVG por Chrome en modo
    impresión (PDF vectorial) y reinterpretando el resultado con PyMuPDF.
  - El SVG "outlined" no depende de ninguna fuente: se abre en Illustrator
    identico al PNG, aunque no tengas Raleway instalada.
  - El SVG "svg" mantiene el texto editable, pero necesita Raleway instalada
    (los .ttf estan en fonts/). Si en Illustrator sale una aviso de fuente
    ausente, instalalos o usa la version "outlined".

Uso (desde la raiz del proyecto):

    python tools\\export_ai.py creatives\\es
    python tools\\export_ai.py creatives\\ca
    python tools\\export_ai.py creatives
"""

import base64
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

import pymupdf  # PyMuPDF

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONT_DIR = ROOT / "fonts"
W, H = 1080, 1350
PT_W, PT_H = W * 72 / 96, H * 72 / 96  # 810 x 1012.5 pt

# peso -> fichero TTF estatico. Usar estaticas (en vez de la variable) hace que
# Chrome incruste la fuente como TrueType real y no como Type3, que Illustrator
# maneja de forma mucho mas.native.
STATIC_FONTS = [
    ("Raleway-Light.ttf", 300),
    ("Raleway-Regular.ttf", 400),
    ("Raleway-Medium.ttf", 500),
    ("Raleway-SemiBold.ttf", 600),
    ("Raleway-Bold.ttf", 700),
]


def find_chrome():
    for c in CHROME_CANDIDATES:
        if pathlib.Path(c).exists():
            return c
    raise SystemExit("No se encuentra Chrome ni Edge.")


def font_b64(name):
    return base64.b64encode((FONT_DIR / name).read_bytes()).decode("ascii")


def print_html(svg_text, fonts):
    """HTML con tamano de pagina exacto para Chrome print-to-pdf."""
    faces = "\n".join(
        f"@font-face{{font-family:'Raleway';src:url(data:font/ttf;base64,{fonts[fn]}) format('truetype');font-weight:{w};font-style:normal;font-display:block;}}"
        for fn, w in STATIC_FONTS
    )
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
{faces}
@page{{size:{PT_W:g}pt {PT_H:g}pt;margin:0;}}
html,body{{margin:0;padding:0;width:{W}px;height:{H}px;overflow:hidden;background:#fff;}}
svg{{position:absolute;top:0;left:0;display:block;width:{W}px;height:{H}px;}}
*{{-webkit-print-color-adjust:exact;print-color-adjust:exact;}}
</style></head><body>
{svg_text}
</body></html>"""


def clean_for_ai(svg_text):
    """Quita el stack CSS que Illustrator no resuelve y deja solo 'Raleway'."""
    s = re.sub(r'font-family="[^"]*"', 'font-family="Raleway"', svg_text)
    # Illustrator no entiende estos genericos CSS
    s = s.replace("ui-sans-serif", "sans-serif").replace("system-ui", "sans-serif")
    return s


def to_pdf(svg_path, out_pdf, chrome, fonts, tmp):
    html = tmp / (svg_path.stem + ".print.html")
    html.write_text(print_html(svg_path.read_text(encoding="utf-8"), fonts), encoding="utf-8")
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--no-pdf-header-footer",
        "--print-to-pdf-no-header",
        "--virtual-time-budget=5000",
        f"--print-to-pdf={out_pdf}",
        html.as_uri(),
    ]
    subprocess.run(cmd, capture_output=True, text=True, timeout=120)


def pdf_to_outlined_svg(pdf_path, out_svg):
    """Convierte el PDF a SVG con el texto convertido en trazados."""
    doc = pymupdf.open(pdf_path)
    page = doc[0]
    svg = page.get_svg_image(text_as_path=True)
    doc.close()

    # Normaliza el tamano a 1080 x 1350 px manteniendo la viewBox en puntos
    m = re.search(r'viewBox="([^"]+)"', svg)
    if m:
        _, _, vw, vh = [float(x) for x in m.group(1).split()]
        svg = re.sub(r'viewBox="[^"]+"', f'viewBox="0 0 {vw:g} {vh:g}"', svg)
        svg = re.sub(r'width="[^"]*"\s+height="[^"]*"', f'width="{W}" height="{H}"', svg, count=1)
    out_svg.write_text(svg, encoding="utf-8")


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    src = pathlib.Path(sys.argv[1])
    out_root = src / "ai"
    dirs = {k: out_root / k for k in ("svg", "outlined", "pdf")}
    for d in dirs.values():
        d.mkdir(parents=True, exist_ok=True)

    chrome = find_chrome()
    fonts = {fn: font_b64(fn) for fn, _ in STATIC_FONTS}
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="ai_export_"))
    try:
        for svg in sorted(src.glob("*.svg")):
            # 1) SVG limpio (texto vivo, font-family="Raleway")
            (dirs["svg"] / svg.name).write_text(clean_for_ai(svg.read_text(encoding="utf-8")), encoding="utf-8")

            # 2) PDF vectorial
            pdf_path = dirs["pdf"] / (svg.stem + ".pdf")
            to_pdf(svg, pdf_path, chrome, fonts, tmp)

            # 3) SVG outlined (texto -> trazados)
            out_svg = dirs["outlined"] / svg.name
            if pdf_path.exists():
                pdf_to_outlined_svg(pdf_path, out_svg)
            print(f"OK  {svg.name}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
