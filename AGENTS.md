# AGENTS.md — thinkoutside.es · Instagram

Instrucciones para agentes de código que trabajen en este repositorio.

## Contexto rápido

Repositorio de **material de producción para Instagram** de **Think Outside**
(Outside Instalaciones y Técnicos S.L.), carpintería de madera en Terrassa,
Barcelona. No es una aplicación: no hay build, ni servidor, ni tests. El
"output" es arte final (SVG → PNG / PDF) y copy.

**Contacto de la empresa: 630 377 574** (`+34 630 377 574`).
Comercial: `comercial@oitinstalaciones.com` · Selección/CV: `unete@thinkoutside.es` (ES) / `uneixte@thinkoutside.es` (CA)
(captació via formulari) · Web: `thinkoutside.es` · 9 años de experiencia
(fundada en 2017).

## Workflow obligatorio

1. Edita **siempre el SVG maestro** en `creatives\es\` (español) o
   `creatives\ca\` (catalán). Nunca edites el PNG ni los ficheros de `ai\` —
   son derivados.
2. Si editas el español, regenera el catalán:
   ```
   python tools\make_ca.py
   ```
3. Reexporta:
   ```
   python tools\svg2png.py creatives\es creatives\es\png
   python tools\svg2png.py creatives\ca creatives\ca\png
   python tools\export_ai.py creatives\es
   python tools\export_ai.py creatives\ca
   ```
4. **Abre el PNG y míralo.** No hay test suite: la revisión visual es la única
   validación real. Comprueba que el PNG mide 1080 × 1350 exactos.
5. Pasa el corrector de maquetación; debe dar **0 avisos**:
   ```
   python tools\check_layout.py creatives\es
   python tools\check_layout.py creatives\ca
   ```
6. Si tocaste un SVG, actualiza también el brief correspondiente (el copy de la
   pieza y su caption viven en los `.md`, no en el SVG) y `POSTS_CONTENT_PLAN.md`.

## Dónde vive cada cosa

| Contenido | Ubicación |
|---|---|
| SVG maestros (ES) | `creatives\es\*.svg` |
| SVG maestros (CA) | `creatives\ca\*.svg` |
| PNG publicable | `creatives\<es\|ca>\png\*.png` |
| Entregables Illustrator | `creatives\<es\|ca>\ai\{svg,outlined,pdf}\` |
| Copy + captions | `INSTAGRAM_LAUNCH_BRIEF.md`, `INSTAGRAM_BATCH_EDU_BRIEF.md`, `INSTAGRAM_CONTRATACION_BRIEF.md` |
| Qué publicar y cuándo | `POSTS_CONTENT_PLAN.md` / `.txt` |
| Identidad de marca | `BRANDING.md` |
| Datos de la empresa | `BRANDING.md` (tabla de información) |
| Diccionario es→ca | `tools\make_ca.py` (regla `T`) |

## Formatos de entrega

| Carpeta | Qué es | Fuente que necesita |
|---|---|---|
| `ai/svg/` | SVG limpio, texto vivo, `font-family="Raleway"` | Raleway instalada |
| `ai/outlined/` | SVG con el texto convertido en trazados | ninguna |
| `ai/pdf/` | PDF vectorial, texto real con fuente incrustada | ninguna |

Si el destinatario no tiene Raleway instalada, entrega `ai/outlined/` o
`ai/pdf/`. Son idénticos visualmente al PNG.

## Los dos idiomas

- **Español** (`creatives/es/`) es el feed principal.
- **Catalán** (`creatives/ca/`) son las mismas 21 piezas traducidas. El
  catálogo es el mismo nombre de fichero en los dos idiomas.
- El catalán **se genera**, no se edita a mano: edita el español y ejecuta
  `python tools\make_ca.py`. Si necesitas cambiar una palabra en catalán,
  cambia el valor en el diccionario `T` de `tools\make_ca.py`.
- Anything que escribas en un idioma (captions, briefs) debe existir también
  en el otro.

## Al editar contenido, recuerda

- **Español peninsular** en todo el copy.
- **9 años** de experiencia, no 5, no 10, no "más de 5". La línea de tiempo de
  la pieza 02 va de **2017 a 2026**.
- La captación de candidatos va por **formulario web**; el email es solo el
  fallback (`unete@thinkoutside.es` en ES, `uneixte@thinkoutside.es` en CA).
- El email comercial (`comercial@oitinstalaciones.com`) es para clientes
  (presupuestos, proyectos), **no** para candidatos.
- Mantén el salto de línea de las captions a ~30–40 caracteres.
- Las piezas `07`, `08` y `09` llevan ya su foto real incrustada en el SVG.

## Reglas de la casa

Ver `RULES.md` — es la lista corta de cosas que no se tocan. Léelo antes de
modificar cualquier pieza.

## Checks antes de dar algo por terminado

- [ ] PNG a 1080 × 1350 y abierto para revisión visual
- [ ] Ningún texto fuera del lienzo ni solapado
- [ ] Solo colores de la paleta token
- [ ] `ai/` reexportado si el SVG cambió
- [ ] Copy del brief sincronizado con el SVG
- [ ] Teléfono `630 377 574` correcto si se tocó un dato de contacto
- [ ] `check_layout.py` da 0 avisos en `es` y en `ca`
