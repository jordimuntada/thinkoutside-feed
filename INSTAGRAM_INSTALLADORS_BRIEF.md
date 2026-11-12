# Variant CA — Captació: instal·ladors i muntadors

Còpia del **set català complet** (`creatives\ca\`) on el rol que es busca ja no és
«fusters», sinó **instal·ladors i muntadors**.

> **Ubicació:** `creatives\ca-installadors\` — 21 peces, `png\` i `ai\{svg,outlined,pdf}\`.
> És un duplicat del set català: la maquetació i els colors són idèntics, només
> canvien les paraules que designaven el rol.

---

## 1. Què canvia (5 de les 21 peces)

| Peça | Abans | Ara |
|---|---|---|
| `01-bienvenida` | «Som Think Outside — **fusters** de Terrassa, Barcelona.» | «Som Think Outside — **instal·ladors i muntadors** de Terrassa, Barcelona.» |
| `10-unete-equipo` | «BUSQUEM **FUSTERS**» · «Cerquem **fusters** amb ofici.» | «BUSQUEM **INSTAL·LADORS I MUNTADORS**» · «Cerquem **instal·ladors i muntadors**.» |
| `C1-calidad` | «BUSQUEM **FUSTERS**» | «BUSQUEM **INSTAL·LADORS I MUNTADORS**» |
| `C2-oficio` | «BUSQUEM **FUSTERS**» | «BUSQUEM **INSTAL·LADORS I MUNTADORS**» |
| `C3-perfil` | «BUSQUEM **FUSTERS**» · «Saps treballar la fusta i entens com s'instal·la.» | «BUSQUEM **INSTAL·LADORS I MUNTADORS**» · «Saps **instal·lar i muntar** elements de fusteria.» |

Les altres **16 peces són idèntiques** al set original: no parlaven de fusters
(bienvenida a banda), sinó de serveis, projectes, consells i marca.

> **No s'ha tocat «FUSTERIA»** al peu de pàgina ni a les etiquetes de servei: és
> el nom del gremi i de l'empresa, no el lloc de treball.

---

## 2. Captions de les peces que canvien

### 01 · Bienvenida

```
Per fi també som aquí.

Som Think Outside, una empresa de fusteria amb
9 anys d'experiència. Fem instal·lacions,
reparacions i manteniment, i treballem amb
instal·ladors i muntadors propis.

En aquest perfil compartirem projectes, abans i després,
consells pràctics i moments del dia a dia de les obres
perquè la fusta duri més.

Comencem!

#ThinkOutside #Fusteria #Terrassa #Instal·ladors #NouPerfil
```

### 10 · Únete al equipo

```
Estem creixent i busquem instal·ladors i muntadors
amb ofici i actitud professional.

 Què demanem:
· Experiència en instal·lació i muntatge de fusteria
· Ganes de fer bé la feina
· Carnet de conduir (no és imprescindible, però es valora)

 Què oferim:
· Estabilitat i un projecte a llarg termini
· Bon ambient d'equip

 Inscriu-t'hi en 2 minuts, sense adjuntar cap PDF:
https://typeform.com/to/thinkoutside-unete

Si ho prefereixes, escriu-nos a uneixte@thinkoutside.es.

#Instaladors #Muntadors #OfertaDeFeina
#TreballaAmbNosaltres #ThinkOutside
```

### C1 · Calidad

```
Busquem persones que facin bé la seva feina
i que treballin amb criteri.

A Think Outside valorem tres coses:
· Eficiència — fer la feina bé, sense repeticions
· Talent — saber trobar solucions
· Qualitat — tenir cura dels detalls

Som una empresa de fusteria fundada el 2017.
Fem instal·lacions, reparacions i manteniment
a Terrassa i rodalia.

 Inscriu-t'hi en 2 minuts, sense adjuntar cap PDF:
https://typeform.com/to/thinkoutside-unete

O escriu-nos a uneixte@thinkoutside.es · 630 377 574

#Instaladors #Muntadors #OfertaDeFeina
#TreballaAmbNosaltres #ThinkOutside
```

### C2 · Oficio

```
No busquem només mans. Busquem ofici.

Persones que entenen la feina i l'acaben bé.
Que deixen l'obra millor de com l'han trobada.

 Eficiència — Treballen amb ordre i saben què
cal fer, quan i com.

 Talent — Aporten criteri quan les coses
no van com haurien d'anar.

 Qualitat — L'acabat no es negocia.

T'hi reconeixes? Omplir el formulari et portarà
dos minuts:
https://typeform.com/to/thinkoutside-unete

uneixte@thinkoutside.es · 630 377 574

#Instaladors #Muntadors #Ofici
#OfertaDeFeina #ThinkOutside
```

### C3 · Perfil

```
Què busquem en tu?

1. Ofici — Saps instal·lar i muntar elements
de fusteria.

2. Eficiència — Treballes amb eficàcia i vas
més enllà de la teva tasca.

3. Criteri — Quan alguna cosa no quadra,
ho dius i saps com millorar-la.

4. Ganes de créixer — T'impliques en les tasques
del taller i de les obres.

T'hi reconeixes? Inscriu-t'hi:
https://typeform.com/to/thinkoutside-unete

uneixte@thinkoutside.es · 630 377 574

#Instaladors #Muntadors #OfertaDeFeina
#TreballaAmbNosaltres #ThinkOutside
```

La resta de peces (02–09, 11, 12, B1–B6) fan servir **els captions del pla
general** (`POSTS_CONTENT_PLAN.md`), sense canvis.

---

## 3. Si necessites la versió en castellà

Aquest duplicat és **només en català**, com el set del qual surt. Si vols la
bessona en castellà («instaladores y montadores»), es pot generar igual sobre
`creatives\es\`; digues-ho i la faig.

---

## 4. Checklist abans de publicar

- [ ] Substituir `https://typeform.com/to/thinkoutside-unete` pel formulari real
- [ ] Que el formulari pregunti per **instal·lació i muntatge**, no només taller
- [ ] `python tools\check_layout.py creatives\ca-installadors` → 0 avisos
- [ ] PNG a 1080 × 1350 oberts i revisats
- [ ] `ai\` reexportat si es toca algun SVG
- [ ] Hashtags **sense** punt volat: `#Instaladors`, mai `#Instal·ladors`

---

## 5. Plantillas sin texto

Dentro de `creatives\ca-installadors\sense-text\` hay las **mismas 21 piezas sin
ningún texto**: se han eliminado los 307 elementos `<text>` (titulares, eyebrows,
listas, pies, wordmark y también los glifos usados como icono).

| Carpeta | Contenido |
|---|---|
| `sense-text/svg/` | SVG limpio: solo fondos, tarjetas, formas, líneas y botones |
| `sense-text/png/` | PNG 1080 × 1350 |
| `sense-text/ai/` | `svg/` · `outlined/` · `pdf/` para Illustrator |

Sirven de **plantilla base**: se abre la pieza y se añade el texto propio encima
(en Illustrator, Figma o Inkscape), sin heredar la maquetación anterior.

> Ojo: al eliminar todos los `<text>` también desaparecen los iconos que eran
> caracteres tipográficos: `☎ @ W P` de la pieza 12, `⏱` y `📍` de la 09, y los
> números dentro de círculos de la B3 y la C3. Si los quieres conservar, se puede
> generar una variante que mantenga esos elementos.
