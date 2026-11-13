# Branding — thinkoutside.es

Documentación de la identidad de marca del sitio web **thinkoutside.es**, recopilada a partir del HTML y CSS público del sitio. Fecha de captura: 22‑09‑2026.

---

## 1. Información de la empresa

| Campo | Valor |
|---|---|
| Marca comercial | **Think Outside** |
| Razón social | Outside Instalaciones y Técnicos S.L. |
| Sitio web principal | thinkoutside.es |
| Dominio alternativo (Aviso Legal) | outsideinstalaciones.com |
| Sector | Carpintería de madera — instalaciones, reparación y mantenimiento |
| Mercados | Residencial, hoteles, edificios corporativos, hospitales, retail, industrial |
| Sede | Carrer Apol·lo 10 — 08228 Terrassa, Barcelona (España) |
| Teléfono | 630 377 574 (+34 630 377 574) |
| Email | comercial@oitinstalaciones.com |
| Email — selección / CV | unete@thinkoutside.es (ES) · uneixte@thinkoutside.es (CA) — canal principal de captación: formulario web `https://forms.gle/KPky7uANSZC52mFUA` |
| Año fundación (footer) | 2025 |
| Idiomas publicados | es, ca, en, ar (RTL) |

> El footer indica "© Copyright 2025". El aviso legal menciona CIF B12345678 (placeholder). El contenido se posiciona como una empresa con experiencia dilatada en el sector.

---

## 2. Voz y mensajes clave

### Tagline principal (header)
> **Think Outside** — Expertos en Instalaciones y Mantenimiento de Carpintería de Madera

### Eslogan hero (H2)
> **Pasión por un trabajo bien hecho**

### Subtítulo sobre nosotros
> Somos una empresa con amplia experiencia en el campo de instalaciones y mantenimiento de carpintería de madera, tanto residencial como industrial. Nuestra principal motivación es la satisfacción de nuestros clientes, por lo que trabajamos cuidando al máximo los detalles y la calidad, adaptándonos a sus necesidades.

### Tono de comunicación
- Profesional pero cercano.
- Artesanal y de oficio, sin ser rústico.
- Confianza y trayectoria (palabras recurrentes: *experiencia*, *detalles*, *calidad*, *satisfacción*).
- Tratamiento de **usted** ligero (uso de "le informamos" en el legal).
- Español peninsular.

### Pilares de marca
1. **Experiencia** — varios años en el sector.
2. **Detalle y calidad** — "cuidando al máximo los detalles".
3. **Adaptabilidad** — residencial + industrial.
4. **Servicio integral** — instalación + reparación + mantenimiento.

---

## 3. Sistema de color

Definido como tokens HSL dentro del `:root` de Tailwind v3.4.17, consumidos vía `hsl(var(--token))`. A continuación se ofrece también la conversión HEX equivalente para uso directo en diseño.

| Token CSS | HSL | HEX | Uso |
|---|---|---|---|
| `--background` | 36 33% 97% | **#FAF8F3** | Fondo general (crema cálido) |
| `--foreground` | 20 10% 20% | **#36332F** | Texto principal (marrón muy oscuro) |
| `--primary` | 25 30% 28% | **#54453A** | Brand principal — footer, headings, hero overlay |
| `--primary-foreground` | 36 33% 97% | #FAF8F3 | Texto sobre primary |
| `--secondary` | 33 43% 90% | **#EFE6DA** | Fondo de secciones, tarjetas suaves (beige cálido) |
| `--secondary-foreground` | 25 30% 28% | #54453A | Texto sobre secondary |
| `--accent` | 35 50% 64% | **#D4A373** | CTAs, hover, focus ring, iconos (tan / dorado suave) |
| `--accent-foreground` | 20 10% 20% | #36332F | Texto sobre accent |
| `--muted` | 33 43% 90% | #EFE6DA | — |
| `--border` | 33 43% 85% | **#DED3C4** | Bordes finos |
| `--card` | 0 0% 100% | **#FFFFFF** | Tarjetas blancas |
| `--destructive` | 0 65% 52% | #D94646 | Errores |
| `--ring` | 35 50% 64% | #D4A373 | Foco accesible |

### Paleta HEX resumida (la que se debe usar en piezas)

```
primary          #54453A   (marrón oscuro de marca)
accent           #D4A373   (tan / dorado suave)
background       #FAF8F3   (crema cálido)
foreground       #36332F   (texto principal)
secondary        #EFE6DA   (beige cálido)
border           #DED3C4   (línea fina)
card / white     #FFFFFF
```

### Colores sueltos detectados en el CSS
- `#E9EDC9` verde oliva claro
- `#FAEDCD` crema
- `#FEFAE0` crema muy pálido
- `#CCD5AE` verde salvia
- `#C39B6A` / `#B38E60` tonos tan más profundos (hover / active)
- `#5C4033` marrón oscuro (texto auxiliar)

> Recomendación: en nuevas piezas usar **solo** la paleta token principal (primary / accent / background / secondary / foreground). Los colores sueltos son estados internos y no deben aparecer en creatividades públicas.

---

## 4. Tipografía

| Elemento | Familia | Pesos cargados |
|---|---|---|
| Latín / Español (body) | **Raleway** (Google Fonts) | 300, 400, 500, 600, 700 |
| Árabe / RTL | **Tajawal** (Google Fonts) | 400, 500, 700 |
| Monoespaciado | `ui-monospace, SFMono-Regular, Menlo, …` | — |
| Sans genérico | `ui-sans-serif, system-ui, sans-serif, …` | — |

Uso observado:
- **H1 / H2 hero**: weight 700 (bold), uppercase en H1 ("EXPERTOS EN INSTALACIONES Y MANTENIMIENTO DE CARPINTERÍA DE MADERA").
- **H2 secciones**: weight 500 (medium), tamaño 30px (text-3xl).
- **H3 / títulos tarjeta**: weight 500 (medium).
- **Body**: weight 400, 18px (text-lg) en el about, 16px en general.
- **Botones**: weight 500, 16px (text-base).
- **Logo wordmark**: weight 700 (font-bold), tamaño 20px en header.

Letter‑spacing y tracking no están personalizados — se usa el default de Raleway.

---

## 5. Logotipo

- **Tipo:** wordmark textual. No se detecta ningún `<img>` de logo: la marca se representa con el texto "Think Outside".
- **Implementación en HTML:**
  ```html
  <a href="/">
    <span class="text-xl font-bold text-primary">Think Outside</span>
  </a>
  ```
- En el footer se repite como heading H3 con `text-secondary` (#EFE6DA).
- **Color del wordmark:** `--primary` (#54453A) sobre fondos claros, `--secondary` (#EFE6DA) sobre fondos primary.
- **Tagline que acompaña al logo** en footer: "EXPERTOS EN INSTALACIONES Y MANTENIMIENTO DE CARPINTERÍA DE MADERA".

> Nota: al ser solo texto, cualquier reproducción del logotipo debe usar **Raleway Bold**, kerning normal, en color `--primary` o blanco/cream sobre fondos oscuros.

---

## 6. Iconografía y elementos gráficos

- Set de iconos: **Lucide** (`lucide-react`) — outline, stroke 2.
- Iconos utilizados en el sitio: `menu`, `chevron-down`, `users`, `mail`, `arrow-right`, `phone`, `map-pin`.
- Estilo: línea fina, mismo `currentColor` que el texto adyacente.
- En el footer, los iconos de contacto van en color `--accent`.

---

## 7. Geometría / radios / sombras

- **Border radius base:** `--radius: 0.5rem` (8px)
  - `rounded-sm` → 4px
  - `rounded-md` → 6px (botones, inputs, cards de servicio)
  - `rounded-lg` → 8px (cards generales)
  - `rounded-xl` → 12px (disponible, poco usado)
  - `rounded-full` → 9999px (iconos, badges circulares)
- **Sombras** (Tailwind por defecto):
  - `shadow-sm` — header sticky
  - `shadow-md` — cards de servicio, formulario
  - `shadow-lg` / `hover:shadow-xl` — botones primarios
- **Contenedor:** `max-w` ≈ 1200px (`container mx-auto px-4`).
- **Grid de servicios:** 3 columnas en desktop (`md:grid-cols-3 gap-8`).
- **Espaciado vertical de secciones:** `py-20` (80px) o `py-24` (96px en hero final).

---

## 8. Animaciones

- `animate-fade-in-up` — opacity 0→1 + translateY 20px→0, basada en `@keyframes fadeInUp`.
- `animate-bounce` — chevron del hero (1s infinite).
- `animate-pulse` — disponible, no usado en landing.
- Duración por defecto: 1000ms con `transition-opacity` y `transition-colors duration-300`.

---

## 9. Fotografía / estilo visual

- **Fuente:** Pexels (stock libre de uso comercial). URLs visibles:
  - Hero: `pexels-photo-3637837.jpeg` (carpintero / reparación)
  - Sobre nosotros: `pexels-photo-1094767.jpeg` (carpintero trabajando)
  - Servicio Instalaciones: `pexels-photo-6474475.jpeg`
  - Servicio Reparación: `pexels-photo-3637837.jpeg`
  - Servicio Mantenimiento: `pexels-photo-4491881.jpeg`
  - Cierre CTA: `pexels-photo-6758773.jpeg`
- **Paleta fotográfica dominante:** maderas cálidas (roble, nogal), herramientas, ambiente de taller, manos del carpintero en primer plano.
- **Tratamiento:** overlay oscuro `bg-primary/40` sobre la imagen del hero, `bg-primary/70` en el CTA final.
- **Estilo de imagen:** real, sin filtros pesados, iluminación natural o de taller. Evitar imágenes genéricas de "hogar"/"decoración" — el foco debe ser **oficio + madera**.

---

## 10. Componentes UI clave

| Componente | Estilo |
|---|---|
| Header | `bg-white shadow-sm sticky top-0 z-50`, altura 80px |
| Botón primario | `bg-accent text-white rounded-md shadow-lg hover:shadow-xl` |
| Botón secundario | `bg-white text-primary rounded-md shadow-lg hover:shadow-xl` |
| Botón outline | borde 2px blanco, transparente |
| Input | `border border-gray-300 rounded-md focus:ring-2 focus:ring-primary/50` |
| Tarjeta de servicio | `bg-white rounded-md shadow-md hover:shadow-lg`, imagen 256px con hover scale 1.05 |
| Footer | `bg-primary text-primary-foreground` con borde superior `border-primary-foreground/20` |
| Badge circular | `bg-accent/10 rounded-full` para iconos |

---

## 11. SEO / metadata

- `<title>`: "Think Outside - Expertos en Carpintería de Madera"
- `<meta description>`: "Expertos en instalaciones y mantenimiento de carpintería de madera. Servicios de instalación, reparación y mantenimiento para proyectos residenciales e industriales."
- `hreflang`: es, ca, en, ar.
- Tracking: Google Analytics `G-NCY985VYZP` + script de `cdn.softgen.ai`.

---

## 12. Reglas de uso de marca (resumen ejecutivo)

1. **Nunca** usar `--accent` (#D4A373) como texto principal sobre fondo `--primary` — usar `--primary-foreground` (#FAF8F3) o `--secondary` (#EFE6DA).
2. **Wordmark:** Raleway Bold, color `--primary` sobre fondos claros, `--secondary` sobre fondos `--primary`.
3. **Tagline oficial** siempre en mayúsculas cuando acompaña al logotipo en formato brand block.
4. **Iconos:** estilo Lucide (línea fina), heredar `currentColor`. En CTAs y listas de contacto pueden ir en `--accent`.
5. **Fotografía:** priorizar madera, taller, manos, herramientas. Evitar imágenes abstractas o de stock genérico de "interior design".
6. **Tipografía:** Raleway en cualquier comunicación. Tajawal solo en árabe.
7. **Bordes / radios:** esquinas suaves (4–8px). Solo `rounded-full` para iconos o badges.
8. **Sombras:** progresión coherente (`shadow-sm` → `md` → `lg`).
