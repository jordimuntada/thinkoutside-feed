# CLAUDE.md — thinkoutside.es · Instagram

Contexto para Claude (y cualquier agente) que trabaje en este repositorio.

## Qué es este proyecto

Material de producción para el perfil de Instagram de **Think Outside**
(razón social: Outside Instalaciones y Técnicos S.L.) — carpintería de madera:
instalación, reparación y mantenimiento. Sede en Terrassa, Barcelona.

**No es una web app.** No hay build, ni servidor, ni tests. El "output" son
piezas gráficas (SVG → PNG) y documentos de estrategia. La comprobación de
calidad es **visual**: abrir el PNG y mirar que se ve bien.

## Datos de la empresa

| Campo | Valor |
|---|---|
| Marca | **Think Outside** |
| Razón social | Outside Instalaciones y Técnicos S.L. |
| Web | thinkoutside.es |
| **Teléfono de contacto** | **630 377 574** (móvil ES · formato internacional `+34 630 377 574`) |
| Email comercial | comercial@oitinstalaciones.com |
| Email selección / CV | unete@thinkoutside.es (ES) · uneixte@thinkoutside.es (CA) |
| Captación de candidatos | Typeform (ver `creatives/es/10-unete-equipo.svg`) |
| Sede | Carrer Apol·lo 10 · 08228 Terrassa, Barcelona |
| Experiencia | **9 años** (fundada en 2017) |
| Mercados | Residencial, hoteles, edificios corporativos, hospitales, retail, industrial |

> Si el usuario da un dato nuevo de contacto (teléfono, email, web), actualízalo
> **en los tres sitios**: los ficheros `BRANDING.md` + briefs, el SVG de la pieza
> correspondiente, y los ficheros de reglas de este repo.

## Estructura

```
posts-thinkoutside\
├── BRANDING.md                  Identidad de marca (paleta, tipografía, voz)
├── INSTAGRAM_LAUNCH_BRIEF.md    Batch A · 12 posts de lanzamiento (copy + captions)
├── INSTAGRAM_BATCH_EDU_BRIEF.md Batch B · 6 posts educativos sin fotos
├── INSTAGRAM_CONTRATACION_BRIEF.md  Batch C · 3 posts de captación (C1–C3)
├── POSTS_CONTENT_PLAN.md        Plan de contenido: calendario + copy de cada post
├── POSTS_CONTENT_PLAN.txt       El mismo plan en texto plano
├── CLAUDE.md / AGENTS.md / RULES.md
├── README.md
├── creatives\                    21 piezas POR IDIOMA
│   ├── es\                      español (feed principal)
│   │   ├── 01-bienvenida.svg … 12-tarjeta-contacto.svg
│   │   ├── B1-cuidados-invierno.svg … B6-sabias-que.svg
│   │   ├── C1-calidad.svg … C3-perfil.svg
│   │   ├── png\                 export a 1080×1350
│   │   └── ai\                  entregables Illustrator (svg / outlined / pdf)
│   └── ca\                      catalán (mismos nombres de fichero)
│       ├── *.svg
│       ├── png\
│       └── ai\
├── fonts\                       Raleway estática (300/400/500/600/700) + OFL.txt
└── tools\
    ├── svg2png.py               SVG → PNG 1080×1350 (Chrome headless + Raleway)
    ├── export_ai.py             SVG → SVG limpio / SVG outlined / PDF vectorial
    ├── make_fonts.py            genera las estáticas desde la variable font
    ├── make_ca.py               genera la versión catalana desde la española
    ├── check_layout.py          detecta colisiones de texto y saltos de línea
    ├── send_pack.py             envía las piezas por correo, carpeta a carpeta
    └── _fonts\                  Raleway variable (se descarga sola)
```

**21 piezas por idioma** (12 del Batch A + 6 del Batch B + 3 de captación C1-C3). Las únicas
bloqueadas por falta de foto: **ninguna**. Las `07`, `08` y `09` ya llevan las
fotos incrustadas en el SVG.

## Comandos

```powershell
# 1. Editar el SVG maestro (siempre en creatives\es\ o creatives\ca\)
# 2. Reexportar PNG
python tools\svg2png.py creatives\es creatives\es\png
python tools\svg2png.py creatives\ca creatives\ca\png

# 3. Reexportar entregables Illustrator
python tools\export_ai.py creatives\es
python tools\export_ai.py creatives\ca

# 4. Comprobar maquetación (debe dar 0 avisos)
python tools\check_layout.py creatives\es
python tools\check_layout.py creatives\ca

# 5. (solo si cambia el español) regenerar el catalán
python tools\make_ca.py

# 6. (solo si cambian las fuentes) regenerar las TTF estáticas
python tools\make_fonts.py
```

Requisitos: Python 3.8+ (`pip install pymupdf pillow`) y Google Chrome o Edge.
La primera ejecución descarga Raleway en `tools\_fonts\`.

## Convenciones

- **Formato único:** 1080 × 1350 px (feed 4:5), sRGB, 60 px de margen por borde.
- **Tipografía:** Raleway. En los SVG maestros el `font-family` es
  `Raleway, ui-sans-serif, system-ui, sans-serif`; en `ai/svg/` se deja solo
  `Raleway` porque Illustrator no resuelve el stack CSS.
- **Paleta** (solo estos): `#54453A` `#D4A373` `#FAF8F3` `#EFE6DA` `#36332F`
  `#DED3C4` `#FFFFFF`. Los verdes `#E9EDC9` `#CCD5AE` son estados internos, nunca
  en piezas públicas.
- **Radios:** 8 px (cards), 6 px (botones), 22–32 px (píldoras).
- **Idioma:** español peninsular. Copy de las piezas y captions en español.
- **Numeración de ficheros:** Batch A `01-`…`12-`; Batch B `B1-`…`B6-`;
  Batch C `C1-`…`C3-`. No renumerar: los briefs referencian los nombres de fichero.
- **Salto de línea en captions:** mantener el ancho de ~30–40 caracteres para
  que se lea bien en móvil.

## Cómo verificar el trabajo

1. Exporta el PNG.
2. **Abre el PNG y míralo.** Es la única comprobación que importa. Cuidado
   con: texto que se sale del lienzo, líneas de base cortadas, textos que se
   solapan, colores fuera de la paleta.
3. Comprueba que el PNG mide exactamente 1080 × 1350.
4. Ejecuta `python tools\check_layout.py creatives\es` y `…\ca`: debe dar
   **0 avisos**. Detecta lo que el ojo no ve: una línea decorativa que cruza
   una tilde, un rótulo 40 px del borde, un número descentrado en un círculo.
5. Si tocaste un SVG maestro, actualiza también el brief correspondiente y,
   si tocaste el español, regenera el catalán con `python tools\make_ca.py`.

## Referencias

- `BRANDING.md` — paleta, tipografía, iconografía, voz de marca, fotos (Pexels).
- `INSTAGRAM_LAUNCH_BRIEF.md` — Batch A pieza a pieza + calendario de 13 días.
- `INSTAGRAM_BATCH_EDU_BRIEF.md` — Batch B pieza a pieza + calendario.
- `INSTAGRAM_CONTRATACION_BRIEF.md` — Batch C (C1–C3) pieza a pieza, ES + CA.
- `POSTS_CONTENT_PLAN.md` — **qué publicar, cuándo y con qué texto** (10 semanas).
- `RULES.md` — reglas duras. Lelas antes de tocar nada.
