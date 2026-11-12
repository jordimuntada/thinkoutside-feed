"""
strip_emoji.py — Elimina els emojis dels captions.

Processa els blocs de caption dels .md (``` després d'una línia "Caption...")
i també tools/build_site.py (les seves cadenes són captions).

Conserva deliberadament:
  - les fletxes (→) del copy
  - el punt volat (·)
  - els guillemets («»)

Uso: python tools\\strip_emoji.py
"""

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent

# rangs d'emoji (sense fletxes U+2190-21FF ni · U+00B7)
EMOJI = re.compile(
    "["
    "\U0001F000-\U0001FAFF"   # pictogrames, emoticones, símbols
    "\U00002600-\U000027BF"   # símbols diversos i dingbats (✅ ❌ ...)
    "\U0000FE00-\U0000FE0F"   # selectors de variació
    "\U0001F1E6-\U0001F1FF"   # banderes
    "\u200d"                  # zero width joiner
    "\u20e3"                  # enclosing keycap
    "\u2b00-\u2bff"           # estrelles i fletxes decoratives
    "\u3030\u303d\u3297\u3299"
    "]+"
)

KEYCAPS = {i: f"{i}." for i in "1234567890"}


def neteja(text):
    # 1️ / 2️ ... (digit + VS16 + U+20E3) -> "1." etc.
    for d in KEYCAPS:
        text = text.replace(f"{d}\ufe0f\u20e3", f"{d}.")
        text = text.replace(f"{d}\u20e3", f"{d}.")
    # resta d'emojis
    text = EMOJI.sub("", text)

    out = []
    for line in text.splitlines():
        line = re.sub(r"[ \t]{2,}", " ", line).rstrip()
        out.append(line)
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def processa_md(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    out = []
    dins = False
    pendent = False
    canvis = 0

    for line in lines:
        s = line.strip()

        if not dins and not pendent and re.match(r"^(\*\*|#{1,6}\s)?caption\b", s, re.I):
            pendent = True
            out.append(line)
            continue

        if pendent and s.startswith("```"):
            dins = True
            pendent = False
            out.append(line)
            continue

        if dins and s.startswith("```"):
            dins = False
            out.append(line)
            continue

        if dins:
            nou = neteja(line)
            if nou != line:
                canvis += 1
            out.append(nou)
        else:
            out.append(line)

    path.write_text("\n".join(out) + ("\n" if lines else ""), encoding="utf-8")
    return canvis


def processa_py(path):
    t = path.read_text(encoding="utf-8")
    nou = neteja(t)
    if nou != t:
        path.write_text(nou, encoding="utf-8")
        return True
    return False


def main():
    mds = [
        "POSTS_CONTENT_PLAN.md",
        "INSTAGRAM_LAUNCH_BRIEF.md",
        "INSTAGRAM_BATCH_EDU_BRIEF.md",
        "INSTAGRAM_CONTRATACION_BRIEF.md",
        "INSTAGRAM_INSTALLADORS_BRIEF.md",
    ]
    for name in mds:
        p = ROOT / name
        if p.exists():
            n = processa_md(p)
            print(f"{name}: {n} línies de caption netejades")

    py = ROOT / "tools" / "build_site.py"
    if py.exists():
        print("build_site.py:", "actualitzat" if processa_py(py) else "sense canvis")


if __name__ == "__main__":
    main()
