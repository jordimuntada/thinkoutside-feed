# thinkoutside.es · Instagram

Material preparado para el perfil de Instagram de **Think Outside** (Outside Instalaciones y Técnicos S.L.).

| Contacto | |
|---|---|
| **Teléfono** | **630 377 574** · internacional `+34 630 377 574` |
| Email comercial (clientes) | comercial@oitinstalaciones.com |
| Email selección / CV | unete@thinkoutside.es (ES) · uneixte@thinkoutside.es (CA) — captación principal vía Typeform |
| Web | thinkoutside.es |
| Sede | Carrer Apol·lo 10 · 08228 Terrassa, Barcelona |

## Estructura

```
posts-thinkoutside\
├── CLAUDE.md                          Contexto del proyecto para agentes
├── AGENTS.md                          Instrucciones de trabajo para agentes
├── RULES.md                           Reglas duras (lo que no se toca)
├── POSTS_CONTENT_PLAN.md              Plan de contenido: copy, captions, calendario
├── POSTS_CONTENT_PLAN.txt             El mismo plan en texto plano (copiar y pegar)
├── BRANDING.md                        Identidad de marca extraída del sitio web
├── INSTAGRAM_LAUNCH_BRIEF.md          Batch A · 12 posts de lanzamiento (copy, hashtags)
├── INSTAGRAM_BATCH_EDU_BRIEF.md       Batch B · 6 posts educativos SIN fotos (copy, hashtags)
├── INSTAGRAM_CONTRATACION_BRIEF.md    Batch C · 3 posts de captación (C1–C3)
├── INSTAGRAM_INSTALLADORS_BRIEF.md    Variante CA · captación de instal·ladors i muntadors
├── README.md                          Este archivo
├── creatives\
│   ├── es\                            ESPAÑOL — 21 piezas
│   │   ├── 01-bienvenida.svg … 12-tarjeta-contacto.svg
│   │   ├── B1-cuidados-invierno.svg … B6-sabias-que.svg
│   │   ├── C1-calidad.svg … C3-perfil.svg
│   │   ├── png\                        PNG 1080 × 1350 listos para publicar
│   │   └── ai\                         Illustrator: svg/ · outlined/ · pdf/
│   ├── ca\                            CATALÁN — las mismas 21 piezas
│   │   ├── 01-bienvenida.svg … 12-tarjeta-contacto.svg
│   │   ├── B1-cuidados-invierno.svg … B6-sabias-que.svg
│   │   ├── C1-calidad.svg … C3-perfil.svg
│   │   ├── png\
│   │   └── ai\
│   └── ca-installadors\               CATALÁN — duplicado con rol «instal·ladors i muntadors»
│       ├── 01-bienvenida.svg … 12-tarjeta-contacto.svg
│       ├── B1-cuidados-invierno.svg … B6-sabias-que.svg
│       ├── C1-calidad.svg … C3-perfil.svg
│       ├── png\
│       ├── ai\
│       └── sense-text\                plantillas SIN texto (solo fondos y formas)
│           ├── svg\
│           ├── png\
│           └── ai\
├── site\                              Web de muestra: simulación del feed (estática)
├── render.yaml                        Blueprint de despliegue en Render
├── fonts\                             Raleway estática 300/400/500/600/700 (+ OFL.txt)
└── tools\
    ├── svg2png.py                      exportador SVG → PNG 1080 × 1350 (Chrome headless)
    ├── export_ai.py                    exportador SVG → SVG limpio / outlined / PDF
    ├── make_fonts.py                   genera las TTF estáticas desde la variable font
    ├── make_ca.py                      genera la versión catalana desde la española
    ├── check_layout.py                 detecta colisiones de texto y saltos de línea
    ├── send_pack.py                    envía las piezas por correo, carpeta a carpeta
    ├── build_site.py                   genera site/ (feed de mostra) desde los PNG
    └── _fonts\                         Raleway variable (se descarga sola la 1ª vez)
```

### Las carpetas de piezas

| Carpeta | Contenido | ¿Publicable ya? |
|---|---|---|
| `creatives/es/` y `creatives/ca/` | 21 piezas por idioma: 12 del Batch A + 6 del Batch B + 3 de captación | **Sí**, salvo la **09**, que sigue con placeholder `[ FOTO ... ]` y necesita fotos reales |
| `creatives/ca-installadors/` | Duplicado del set catalán (21 piezas) con el rol **instal·ladors i muntadors** en vez de fusters | **Sí**, con el mismo aviso de la pieza 09 y del Typeform |
| `creatives/ca-installadors/sense-text/` | Las mismas 21 piezas **sin ningún texto**: solo fondos, tarjetas, botones y formas | **Plantilla** — pensada para maquetar texto propio encima |

> La pieza **09** (antes/después) es la única bloqueada por falta de foto. Mientras
> tanto, sustitúyela el mismo día por una educational (B1, B3, B5) — ver
> `POSTS_CONTENT_PLAN.md` §2. Las **07** y **08** ya llevan foto real.

### Publicar

Todo lo necesario para llenar un perfil vacío está en:

- **`POSTS_CONTENT_PLAN.md`** — setup (bio, highlights), estrategia, calendario de
  10 semanas y el contenido completo de cada post: copy, caption ES, caption CA,
  hashtags y alt-text.
- **`POSTS_CONTENT_PLAN.txt`** — el mismo plan en texto plano, listo para copiar y
  pegar.

## Especificaciones de las creatividades

- **Formato:** 1080 × 1350 px (feed portrait 4:5), sRGB.
- **Tipografía:** Raleway (300/400/500/600/700). Los PNG se exportan con la fuente embebida, así que el resultado es idéntico al diseño.
- **Paleta:** `#54453A` · `#D4A373` · `#FAF8F3` · `#EFE6DA` · `#36332F` · `#DED3C4` · `#FFFFFF`.
- **Radios:** 8 px (cards), 6 px (botones), 22–32 px (píldoras).
- **Idiomas:** español (feed principal) y catalán (1 de cada 3 posts). Mismos nombres de fichero en ambos.

## Exportar a PNG (recomendado)

Desde la raíz del proyecto:

```
python tools\svg2png.py creatives\es creatives\es\png
python tools\svg2png.py creatives\ca creatives\ca\png
```

Renderiza con Chrome headless y **Raleway real embebida** (no hace falta instalar la fuente en el sistema). Requiere Python 3.8+ y Chrome o Edge. La primera ejecución descarga la variable font en `tools\_fonts\`.

Alternativas manuales:

- **Inkscape** (gratis): `File → Export PNG Image` → 1080 × 1350.
- **Figma** (gratis): `File → Import` → `Export` → PNG 2× (2160 × 2700).
- **Navegador**: extensión "SVG Export" → 1080 × 1350 (cargar antes Raleway desde Google Fonts).

> ⚠️ Si exportas desde un navegador sin instalar Raleway, el texto saldrá con una fuente genérica (serif o sans del sistema). Revisa siempre la primera pieza exportada.

## Comprobar la maquetación

```
python tools\check_layout.py creatives\es
python tools\check_layout.py creatives\ca
```

Mide la caja real de tinta de cada texto y avisa de: líneas o figuras que
**cruzan las letras**, texto que se solapa con otro texto, texto fuera del
lienzo o de la zona segura de 60 px, invasion de la zona del footer y números
descentrados dentro de círculos. Debe salir **0 avisos** en ambos idiomas.

## Entregables para Adobe Illustrator

```
python tools\export_ai.py creatives\es
python tools\export_ai.py creatives\ca
```

Genera tres versiones de cada pieza en `creatives\<idioma>\ai\`:

| Carpeta | Contenido | Editable | Necesita Raleway |
|---|---|---|---|
| `ai/svg/` | SVG limpio (`font-family="Raleway"`, sin el stack CSS) | texto y formas | **Sí** |
| `ai/outlined/` | SVG con todo el texto convertido en trazados | formas (el texto son paths) | No |
| `ai/pdf/` | PDF vectorial, texto real, fuente incrustada (Type0/TrueType) | texto y formas | No |

Cómo usarlos:

- **Editas el texto** → `ai/svg/`. Instala antes las fuentes de `fonts\`
  (doble clic en cada `.ttf` → *Instalar*) o Illustrator sustituirá la tipografía
  y el texto se recolocará.
- **No quieres depender de fuentes** → `ai/outlined/`. Se abre idéntico al PNG
  en cualquier máquina, sin avisos de fuentes ausentes.
- **Quiero un PDF para abrir en Illustrator y guardar como .ai** → `ai/pdf/`.
  Ábrelo con *Archivo → Abrir* y guárdalo como `.ai` si lo necesitas.
- Todos los formatos van a caja de **1080 × 1350 px**.

> `.ai` nativo no se puede generar sin Illustrator; el PDF vectorial es el
> formato de intercambio estándar y contiene las mismas formas y el mismo texto.

## Traducir o retocar el catalán

`creatives\ca\` se genera automáticamente desde `creatives\es\`:

```
python tools\make_ca.py
```

El diccionario es → ca está en `tools\make_ca.py` (regla `T`). Si añades texto
nuevo en español, añádelo también al diccionario y vuelve a ejecutar el script:
así el catalán nunca se queda desactualizado.

## Enviar las piezas por correo

```
python tools\send_pack.py
```

Manda las 5 carpetas del set catalán en 5 correos a los destinatarios de
lanzamiento. Opciones: `--from`, `--to`, `--reply-to`, `--dry`.

> **Requisito:** el dominio remitente debe estar **verificado** en la cuenta de
> Resend. Sin dominio verificado, Resend solo permite enviar a la dirección de
> la propia cuenta (`onboarding@resend.dev`). Verifica `thinkoutside.es` en
> <https://resend.com/domains> y luego:
> ```
> python tools\send_pack.py --from "Think Outside <hola@thinkoutside.es>"
> ```

## Previsualizar y editar

- **Previsualización rápida**: doble clic sobre cualquier `.svg` para abrirlo en el navegador.
- **Edición**: Inkscape, Figma, Illustrator o Affinity Designer importan el SVG directamente.

## Reemplazar placeholders (pieza 09)

Sustituye los rectángulos `[ FOTO DE PROJECTE ]` / `[ FOTO ABANS ]` /
`[ FOTO DESPRÉS ]` por fotos reales con el mismo aspect ratio (1:1) antes de publicar, y vuelve a exportarlas.

## Orden de publicación recomendado

Ver **`POSTS_CONTENT_PLAN.md`**: 10 semanas de calendario con las 42 piezas
(21 ES + 21 CA) asignadas a fechas concretas.

- **Batch A (lanzamiento):** `INSTAGRAM_LAUNCH_BRIEF.md` §1 — cadencia diaria la primera semana.
- **Batch B (educativo, sin fotos):** `INSTAGRAM_BATCH_EDU_BRIEF.md` §1 — 6 piezas para mantener el feed activo.
- **Batch C (captación, ES + CA):** `INSTAGRAM_CONTRATACION_BRIEF.md` — 3 piezas de contratación (C1, C2, C3) para publicar cuando el perfil ya tiene peso.
- **Ritmo recomendado tras el lanzamiento:** 1 pieza con foto + 2 educativas por semana.

## Recordatorios antes de publicar

- Verificar que la primera exportación usa Raleway y no una fuente fallback.
- Revisar ortografía en cada exportación.
- Mantener el orden de los posts tal como están diseñados (alternan fondos claros y oscuros para romper monotonía en el grid).
- Si se sube en horario distinto al plan, ajustar `alt-text` y ubicación en cada post.
- En la pieza `10-unete-equipo` y en las piezas `C1-calidad`, `C2-oficio` y `C3-perfil`, sustituir la URL de Typeform `https://typeform.com/to/thinkoutside-unete` por el ID real del formulario (en el SVG **y** en el caption del brief, en los dos idiomas).
- Teléfono en las piezas: **630 377 574** (`+34 630 377 574`). El antiguo `+34 93 012 95 73` está obsoleto.

---

## Web de mostra (simulació del feed)

Dins `site\` hi ha una pàgina estàtica d'una sola plana que **simula el perfil
d'Instagram** amb les 21 creativitats catalanes del set `creatives\ca-installadors\`.

```
site\
├── index.html          el perfil (capçalera, destacats, graella i visor)
├── styles.css
├── app.js              obre el post, navega amb ← → i tanca amb Esc
├── data.js             copy de les 21 publicacions (generat)
└── assets\posts\       els 21 PNG
```

Per regenerar-la després de canviar creativitats o copy:

```
python tools\build_site.py
```

Per veure-la en local, obre `site\index.html` al navegador o aixeca un servidor:

```
python -m http.server 8000 --directory site
```

### Desplegar a Render

El repositori inclou `render.yaml`, així que Render crea el servei sol:

1. Puja aquesta carpeta a un repositori de GitHub o GitLab.
2. A Render: **New → Blueprint** i connecta el repositori.
3. Render llegeix `render.yaml` i publica `site\` com a lloc estàtic.

Alternativa manual (sense blueprint): **New → Static Site**, *Build Command*
buit i *Publish Directory* = `site`.

> El repositori pesa força per les fotos d'origen (`PDVIG\` ≈ 62 MB i
> `fotos-outside\` ≈ 28 MB). Si no les necessites al control de versions, afegeix-les
> al `.gitignore`: el SVG de les peces 07 i 08 ja porta les imatges incrustades.
