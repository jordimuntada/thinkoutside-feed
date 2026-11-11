"""
send_pack.py — Envia las piezas de una carpeta por correo, adjuntas.

Por defecto envia el set catalan (creatives\\ca) a los dos destinatarios del
lanzamiento, carpeta a carpeta: 5 correos, uno por carpeta.

Uso:
    python tools\\send_pack.py
    python tools\\send_pack.py --from "Think Outside <hola@thinkoutside.es>" --to a@b.com
    python tools\\send_pack.py --dry

De donde saca la clave de Resend, por orden:
  1. variable de entorno RESEND_API_KEY
  2. ~/.claude.json  (clave guardada por el MCP de Resend)

REQUISITO: el dominio remitente debe estar VERIFICADO en la cuenta de Resend.
Sin dominio verificado solo se puede enviar a la direccion de la propia cuenta
usando onboarding@resend.dev.
"""

import argparse
import base64
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
HOME = pathlib.Path(os.environ.get("USERPROFILE", ""))
API = "https://api.resend.com"

# Cloudflare bloquea las llamadas sin User-Agent de navegador (error 1010).
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")

DEFAULT_TO = ["jordi.m@pdvwood.com", "hostmaster@thinkoutside.es"]
DEFAULT_FROM = "Think Outside <onboarding@resend.dev>"
DEFAULT_REPLY_TO = ["comercial@oitinstalaciones.com"]

# (etiqueta, carpeta, parte del cuerpo, descripcion)
FOLDERS = [
    ("01-svg-mestra", "creatives/ca", "1/5",
     "Los SVG maestros (21 piezas). Ficheros editables con texto vivo.\n\n"
     "  - Se abren en Inkscape, Figma, Illustrator o en el navegador.\n"
     "  - La tipografia es Raleway: si abres el fichero en Illustrator y no la\n"
     "    tienes instalada, instala los .ttf que van en la carpeta de fuentes.\n"
     "  - Todos miden 1080 x 1350 px (formato feed 4:5 de Instagram).\n\n"
     "  Las piezas 07, 08 y 09 llevan el marcador [ FOTO DE PROJECTE ] pendiente:\n"
     "  sustituidlo por una foto real antes de publicarlas."),
    ("02-png-final", "creatives/ca/png", "2/5",
     "Los PNG finales, 1080 x 1350 px, listos para subir a Instagram.\n\n"
     "  Mismos 21 nombres de fichero que los SVG. El PNG es la version\n"
     "  publicable; el SVG es el editable.\n\n"
     "  Aviso: 07, 08 y 09 son marcadores de posicion (aun necesitan foto)."),
    ("03-ai-svg", "creatives/ca/ai/svg", "3/5",
     "SVG limpios para Adobe Illustrator: texto vivo y font-family=\"Raleway\".\n\n"
     "  Necesitas la fuente Raleway instalada para editar el texto.\n"
     "  Si prefieres no depender de fuentes, usa la carpeta siguiente."),
    ("04-ai-outlined", "creatives/ca/ai/outlined", "4/5",
     "SVG con todo el texto convertido en trazados.\n\n"
     "  No dependen de ninguna fuente: se abren identicos al PNG en cualquier\n"
     "  equipo, sin avisos de fuentes ausentes. La entrega \"a prueba de todo\".\n"
     "  El texto ya no es editable, pero si todas las formas y colores."),
    ("05-ai-pdf", "creatives/ca/ai/pdf", "5/5",
     "PDF vectoriales con texto real y fuente incrustada.\n\n"
     "  Abrelos en Illustrator (Archivo > Abrir) y guardalos como .ai si los\n"
     "  necesitas en nativo. Es el formato de intercambio estandar: contiene\n"
     "  las mismas formas y el mismo texto que el PNG."),
]


def get_key():
    env = os.environ.get("RESEND_API_KEY")
    if env:
        return env
    cfg = HOME / ".claude.json"
    if cfg.exists():
        m = re.search(r"re_[A-Za-z0-9_\-]{32,}", cfg.read_text(encoding="utf-8", errors="ignore"))
        if m:
            return m.group(0)
    raise SystemExit("No hay clave de Resend. Exporta RESEND_API_KEY=re_... o anadela a ~/.claude.json")


def post(key, payload):
    req = urllib.request.Request(
        API + "/emails",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": "Bearer " + key,
            "Content-Type": "application/json",
            "User-Agent": UA,
            "Accept": "application/json",
        },
        method="POST",
    )
    try:
        r = urllib.request.urlopen(req, timeout=180)
        return json.loads(r.read())
    except urllib.error.HTTPError as e:
        return {"__error__": e.code, "body": e.read().decode("utf-8", "ignore")[:400]}


def build_body(label, rel, part, desc, to_list, forwarded):
    head = (
        "Hola,\n\n"
        f"Aqui os adjuntamos la carpeta {part} de los materiales graficos de "
        "Think Outside en catalan.\n\n"
        f"CARPETA: {rel}\n"
    )
    if forwarded:
        head += (
            "\nNOTA DE ENVIO: la cuenta de Resend de Think Outside todavia no tiene\n"
            "verificado ningun dominio, asi que este envio sale desde la direccion de\n"
            "la propia cuenta. Por favor, reenviad este correo a:\n"
            + "".join(f"  - {t}\n" for t in to_list)
            + "  (Responder a este correo llega a comercial@oitinstalaciones.com)\n\n"
        )
    return head + (
        "\nQue contiene:\n"
        "  - 01 a 12: piezas de lanzamiento (bienvenida, trayectoria, los 3\n"
        "    servicios, manifiesto, 3 proyectos, equipo, CTA y contacto).\n"
        "  - B1 a B6: piezas educativas que no necesitan ninguna foto.\n"
        "  - C1 a C3: piezas de captacion (calidad, oficio, perfil) con\n"
        "    formulario Typeform y el email unete@thinkoutside.es.\n\n"
        f"{desc}\n\n"
        "Van 5 correos en total, uno por carpeta. Este es el "
        f"{part[0]} de 5.\n\n"
        "Un saludo,\n"
        "Think Outside\n"
        "630 377 574 - thinkoutside.es\n"
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="sender", default=DEFAULT_FROM)
    ap.add_argument("--to", nargs="*", default=DEFAULT_TO)
    ap.add_argument("--reply-to", nargs="*", default=DEFAULT_REPLY_TO)
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()

    key = get_key()
    failed = 0
    for label, rel, part, desc in FOLDERS:
        folder = ROOT / rel
        files = sorted(p for p in folder.iterdir() if p.is_file())
        if not files:
            print(f"SKIP {label}: carpeta vacia")
            continue

        forwarded = "resend.dev" in args.sender
        subject = f"[Think Outside] Creatives en català — {part} · {label}"
        payload = {
            "from": args.sender,
            "to": args.to,
            "reply_to": args.reply_to,
            "subject": subject,
            "text": build_body(label, rel, part, desc, args.to, forwarded),
            "attachments": [
                {"filename": p.name,
                 "content": base64.b64encode(p.read_bytes()).decode("ascii")}
                for p in files
            ],
        }

        if args.dry:
            print(f"DRY  {subject}  ({len(files)} adjuntos, {len(payload['attachments'])})")
            continue

        res = post(key, payload)
        if "__error__" in res:
            print(f"ERROR {label}: HTTP {res['__error__']}  {res['body']}")
            failed += 1
            continue
        print(f"OK   {subject}  id={res.get('id')}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
