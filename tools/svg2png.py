r"""
svg2png.py — Exporta los SVG de Instagram a PNG 1080x1350 usando Chrome headless.

Uso (desde la raíz del proyecto):

    python tools\svg2png.py creatives\es creatives\es\png
    python tools\svg2png.py creatives\ca creatives\ca\png
    python tools\svg2png.py creatives creatives\png

Renderiza con Raleway real (variable font embebida en base64 dentro de un HTML
temporal), así que el PNG sale idéntico al diseño, sin depender de que la fuente
esté instalada en el sistema.

Requisitos: Python 3.8+, Google Chrome instalado. La primera ejecución descarga
la variable font de Raleway en tools\_fonts\ (solo una vez).
"""

import base64
import pathlib
import shutil
import subprocess
import sys
import tempfile
import urllib.request

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

FONT_URLS = {
    "normal": "https://raw.githubusercontent.com/google/fonts/main/ofl/raleway/Raleway%5Bwght%5D.ttf",
    "italic": "https://raw.githubusercontent.com/google/fonts/main/ofl/raleway/Raleway-Italic%5Bwght%5D.ttf",
}

W, H = 1080, 1350
TOOLS_DIR = pathlib.Path(__file__).resolve().parent
FONT_DIR = TOOLS_DIR / "_fonts"


def find_chrome():
    for c in CHROME_CANDIDATES:
        if pathlib.Path(c).exists():
            return c
    raise SystemExit("No se encuentra Chrome ni Edge. Instala Google Chrome o editra CHROME_CANDIDATES.")


def ensure_fonts():
    FONT_DIR.mkdir(parents=True, exist_ok=True)
    out = {}
    for style, url in FONT_URLS.items():
        path = FONT_DIR / ("Raleway.ttf" if style == "normal" else "Raleway-Italic.ttf")
        if not path.exists():
            print(f"Descargando Raleway ({style})...")
            urllib.request.urlretrieve(url, path)
        out[style] = base64.b64encode(path.read_bytes()).decode("ascii")
    return out


def build_html(svg_text, fonts):
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Raleway';src:url(data:font/ttf;base64,{fonts['normal']}) format('truetype');font-weight:100 900;font-style:normal;font-display:block;}}
@font-face{{font-family:'Raleway';src:url(data:font/ttf;base64,{fonts['italic']}) format('truetype');font-weight:100 900;font-style:italic;font-display:block;}}
html,body{{margin:0;padding:0;background:#fff;overflow:hidden;}}
svg{{position:absolute;top:0;left:0;display:block;width:{W}px;height:{H}px;}}
</style></head><body>
{svg_text}
</body></html>"""


def crop_to_canvas(path):
    from PIL import Image

    with Image.open(path) as im:
        if im.size != (W, H):
            im.crop((0, 0, W, H)).save(path)


def render(svg_path, out_path, chrome, fonts, tmp):
    html_path = tmp / (svg_path.stem + ".html")
    html_path.write_text(build_html(svg_path.read_text(encoding="utf-8"), fonts), encoding="utf-8")
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--allow-file-access-from-files",
        "--force-device-scale-factor=1",
        "--virtual-time-budget=5000",
        f"--window-size={W + 200},{H + 200}",
        f"--screenshot={out_path}",
        html_path.as_uri(),
    ]
    subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    crop_to_canvas(out_path)


def main():
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    src_dirs = [pathlib.Path(p) for p in sys.argv[1:-1]]
    out_dir = pathlib.Path(sys.argv[-1])
    out_dir.mkdir(parents=True, exist_ok=True)

    chrome = find_chrome()
    fonts = ensure_fonts()
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="svg2png_"))
    try:
        for d in src_dirs:
            for svg in sorted(d.glob("*.svg")):
                out = out_dir / (svg.stem + ".png")
                render(svg, out, chrome, fonts, tmp)
                ok = out.exists() and out.stat().st_size > 0
                print(f"{'OK  ' if ok else 'FAIL'} {svg.name} -> {out.name} ({out.stat().st_size if out.exists() else 0} bytes)")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
