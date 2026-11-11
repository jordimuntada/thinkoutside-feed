"""
make_fonts.py — Genera instancias estaticas de Raleway a partir de la variable font.

Salida en fonts/:
    Raleway-Light.ttf      (300)
    Raleway-Regular.ttf    (400)
    Raleway-Medium.ttf     (500)
    Raleway-SemiBold.ttf   (600)
    Raleway-Bold.ttf       (700)
    Raleway-Italic-*.ttf   (variante italic, 400/700)

Estas fuentes se instalan en el sistema para que Illustrator renderice
exactamente igual que el PNG exportado.
"""

import pathlib
import shutil

from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "tools" / "_fonts"
OUT = ROOT / "fonts"

WEIGHTS = {
    "Light": 300,
    "Regular": 400,
    "Medium": 500,
    "SemiBold": 600,
    "Bold": 700,
}


def make(src_name, out_name, weight, italic):
    font = TTFont(SRC / src_name)
    instancer.instantiateVariableFont(font, {"wght": weight}, inplace=True, updateFontNames=True)

    # flags de estilo: bit 0 = italic, bit 5 = bold, bit 6 = regular
    BOLD, ITALIC, REGULAR = 0x20, 0x01, 0x40
    fs = font["OS/2"]
    fs.usWeightClass = weight
    fs.fsSelection = 0
    if italic:
        fs.fsSelection |= ITALIC
    if weight >= 700:
        fs.fsSelection |= BOLD
    if not italic and weight < 700:
        fs.fsSelection |= REGULAR
    fs.fsSelection |= 0x40 if fs.fsSelection == 0 else 0
    font["head"].macStyle = (1 if weight >= 700 else 0) | (2 if italic else 0)

    OUT.mkdir(parents=True, exist_ok=True)
    font.save(OUT / out_name)
    print(f"OK  {out_name}  (wght {weight}{', italic' if italic else ''})  fsSelection=0x{fs.fsSelection:02X}")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, w in WEIGHTS.items():
        make("Raleway.ttf", f"Raleway-{name}.ttf", w, italic=False)
    for name in ("Regular", "Bold"):
        make("Raleway-Italic.ttf", f"Raleway-Italic-{name}.ttf", WEIGHTS[name], italic=True)
    # licencia
    lic = SRC / "OFL.txt"
    if lic.exists():
        shutil.copy(lic, OUT / "OFL.txt")
        print("OK  OFL.txt")


if __name__ == "__main__":
    main()
