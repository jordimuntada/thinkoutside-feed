# RULES.md — thinkoutside.es · Instagram

Lista corta de lo que **no se toca**. Si algo aquí contradice una petición,
pregunta antes de aplicar el cambio.

## 1. Datos de la empresa (no se inventan)

| Campo | Valor correcto |
|---|---|
| **Teléfono** | **630 377 574** · internacional `+34 630 377 574` |
| Email comercial (clientes) | comercial@oitinstalaciones.com |
| Email selección / CV | unete@thinkoutside.es (ES) · uneixte@thinkoutside.es (CA) |
| Web | thinkoutside.es |
| Dirección | Carrer Apol·lo 10 · 08228 Terrassa, Barcelona |
| Razón social | Outside Instalaciones y Técnicos S.L. |
| Experiencia | **9 años** (desde 2017) |

- El teléfono de la empresa es **630 377 574**. El antiguo `+34 93 012 95 73`
  está obsoleto: no debe aparecer en ninguna pieza ni documento.
- `comercial@oitinstalaciones.com` es **solo para clientes** (presupuestos,
  proyectos). **Nunca** para candidatos.
- `unete@thinkoutside.es` (castellano) y `uneixte@thinkoutside.es` (catalán) son
  **solo para selección/CV**, y siempre como
  *fallback* detrás del Typeform.
- La captación de candidatos se hace por **Typeform**. El email es el plan B.
- Si un dato cambia, se actualiza en **los tres sitios**: `BRANDING.md` +
  briefs, el SVG de la pieza, y estos ficheros de reglas.

## 2. Identidad visual

- **Formato:** 1080 × 1350 px (feed 4:5), sRGB. **Nunca** otras proporciones.
- **Safe area:** 60 px de margen en cada borde. Nada de texto ni logo en el filo.
- **Tipografía:** solo Raleway (300/400/500/600/700). Tajawal únicamente si
  alguna pieza se traducen al árabe.
- **Paleta:** exclusivamente estos tokens —
  `#54453A` `#D4A373` `#FAF8F3` `#EFE6DA` `#36332F` `#DED3C4` `#FFFFFF`.
  - Los verdes `#E9EDC9` `#FAEDCD` `#FEFAE0` `#CCD5AE` son **estados internos
    de la web**, nunca en creatividades públicas.
  - `#D4A373` (accent) no se usa como texto sobre `#54453A`: ahí va `#FAF8F3`
    o `#EFE6DA`.
- **Wordmark:** "THINK OUTSIDE" en Raleway Bold. Sobre fondo claro, `#54453A`.
  Sobre fondo oscuro, `#FAF8F3`. Siempre la misma proporción.
- **Radios:** 8 px (cards), 6 px (botones), 22–32 px (píldoras). No mezclar
  radios dentro de una misma pieza.
- **Iconos:** estilo Lucide, línea fina, heredando `currentColor`.
- **Fotografía (cuando la haya):** taller, madera, manos, herramientas. Nunca
  imágenes genéricas de "decoración del hogar".
- **Footer obligatorio** en cada pieza: "EXPERTOS EN INSTALACIONES Y
  MANTENIMIENTO DE CARPINTERÍA DE MADERA".

## 3. Reglas de contenido

- **Español peninsular.** Sin "usted" formal forzado, sin anglicismos innecesarios.
- **9 años**, no 5 ni 10. La línea de tiempo de la pieza 02 va de 2017 a 2026.
- Nada de cifras de experiencia inventadas, ni de servicios que no se ofrecen.
- Los claims deben ser verificables: si la pieza dice "respuesta en menos de
  24 h", es porque es verdad.
- No hay logos de terceros, ni marcas ajenas, ni stock visible con marca de agua.
- Sin emojis en las **piezas gráficas**. En las **captions** sí se permiten
  (el set del brief ya está definido).
- No publicar piezas con placeholders `[ FOTO ... ]` sin sustituir.

## 4. Reglas de workflow

- Los **SVG maestros** (`creatives\es\` y `creatives\ca\`) son la única fuente
  de verdad. `png/` y `ai/` son derivados: se regeneran, no se editan.
- El **catalán se genera**: se edita el español y se ejecuta
  `python tools\make_ca.py`. Editar a mano un SVG de `creatives\ca\` se
  perderá en la siguiente regeneración.
- Tras tocar un SVG: reexportar PNG **y** `ai/`, y pasar `check_layout.py`
  (0 avisos en los dos idiomas).
- Si cambias el copy de una pieza, sincroniza el `.md` del brief correspondiente
  y `POSTS_CONTENT_PLAN.md` / `.txt`. El copy vive en el `.md`, no en el SVG.
  Los textos nuevos en español necesitan su entrada en el diccionario `T` de
  `tools\make_ca.py` antes de regenerar el catalán.
- No renumerar ficheros (`01-`, `B1-`, `C1-`, …): los briefs y el plan los referencian.
- No publiques la pieza `09` sin sustituir el placeholder `[ FOTO ... ]`.
  Las `07` y `08` ya tienen foto real incrustada.
- No borres `tools\_fonts\` ni `fonts\` — son las fuentes embebidas que
  garantizan que el PNG y el PDF se vean igual en cualquier máquina.

## 5. Reglas de los entregables

- `ai/svg/` → texto vivo. Necesita Raleway instalada en el equipo del
  destinatario. Si no la tiene, avisar y entregar `ai/outlined/`.
- `ai/outlined/` → texto convertido en trazados. Sin dependencias. Es la entrega
  "a prueba de todo".
- `ai/pdf/` → PDF vectorial, texto real, fuente incrustada.
- Todos a 1080 × 1350 px de caja.
- Verificar el resultado abriéndolo (o renderizándolo) antes de entregarlo.
