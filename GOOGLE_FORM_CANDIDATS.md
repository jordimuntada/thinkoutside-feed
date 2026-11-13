# Formulari de candidats — Think Outside

Formulari de captació per a **fusters, instal·ladors i muntadors**.
Duration objectiu: **menys de 2 minuts**.

**Lliga viva:** `https://forms.gle/KPky7uANSZC52mFUA`

> El formulari viu a **Google Forms**, no a Typeform. El CV **no** s'adjunta al
> formulari: s'envia per correu a `uneixte@thinkoutside.es` (CA) o
> `unete@thinkoutside.es` (ES).

---

## Fitxers

| Fitxer | contingut |
|---|---|
| `GOOGLE_FORM_CANDIDATOS.md` | Especificació del formulari en **català** (canònic) |
| `GOOGLE_FORM_CANDIDATOS_ES.md` | Especificació del formulari en **castellà** |

---

## Regles de la casa

- **No es pregunta edat ni data de naixement**: no és necessari per al lloc i
  obre la porta a discriminació per edat. Si cal saber que la persona és
  major d'edat, pregunta-ho dins del consentiment, no com a dada personal.
- **No s'adjunta cap fitxer al formulari**: el CV va per correu.
- **Sí hi ha una dada de contacte clau**: correu electrònic i telèfon, tots dos
  obligatoris. Són el canal de retorno.
- **Salt de línia de ~30–40 caràcters** en descripcions i textos d'ajuda.
- **Una pregunta per apartat**, amb l'etiqueta de secció `SECCIÓ` quan en cal una.

---

## Els 12 apartats (català)

| # | Pregunta | Tipus de camp | Obligatòria |
|---|---|---|---|
| 1 | Nom i cognoms | Text curt | Sí |
| 2 | Correu electrònic de contacte | Text curt (validació correu) | Sí |
| 3 | Telèfon | Text curt | Sí |
| 4 | Per quin perfil et vols inscriure? | Caselles (selecció única) | Sí |
| 5 | Quines feines concretes has fet? | Caselles (selecció múltiple) | Sí |
| 6 | Tens experiència prèvia en fusteria? | Opció | Sí |
| 7 | Tens carnet de conduir? | Opció | Sí |
| 8 | En quina zona pots treballar? | Caselles (selecció única) | Sí |
| 9 | Explica'ns breument per què t'interessa treballar amb nosaltres (2-3 frases) | Paràgraf | No |
| 10 | Adjuntar el CV: NO es pot fer des d'aquest formulari | Text fix + casella de confirmació | Sí (la casella) |
| 11 | Com ens has conegut? | Opció | No |
| 12 | Política de privacitat | Casella d'acceptació | Sí |

### L'apartat 10 — el CV

Google Forms **no permet** pujar fitxers de manera fiable en tots els comptes i,
a més, Google no els adjunta al correu de resposta. Per això el CV **no** s'adjunta:

```
Envia'ns el teu CV per correu a uneixte@thinkoutside.es amb el teu nom i cognoms
a l'assumpte (per exemple: «CV — Maria Garcia López»). Formats acceptats: PDF o
DOCX, màx. 5 MB. Sense el CV la candidatura no es pot gestionar.

Un cop hagis enviat el CV, torna a aquest formulari i marca la casella següent
per confirmar-nos que ja l'has enviat.
```

Amb la casella marcada, el correu de resposta arriba a `uneixte@thinkoutside.es`
i l'equip pot fer l'emparellament **formulari ↔ CV** pel nom.

### L'apartat 4 — perfils

Els perfils cobreixen els dos grups de l'empresa:

- **Instal·lador/a** — muntatge de parquet, portes, armaris, mobles de cuina a obra
- **Muntador/a** — muntatge de mobles i elements de fusta en taller i a client
- **Oficial de manteniment** — reparacions i manteniments en edificis, hotels, retail
- **Fuster/a de taller** — fabricació a mida, retalls, preparació de peces
- **Ajudant de taller / obra** — suport al equip, aprenentatge
- **Altres perfils** — comercial, administració, oficina tècnica

### L'apartat 5 — tasques

Caselles per marcar totes les que apliquin: parquet, portes i armaris, cuines,
mobles a client, reparacions, manteniment en edificis i fabricació a taller.

---

## Destinatari de les respostes

**`uneixte@thinkoutside.es`** (formulari en català) · **`unete@thinkoutside.es`**
(formulari en castellà).

Aquest correu rep la notificació de cada resposta amb el cos del missatge
preparat (vegeu la secció final de `GOOGLE_FORM_CANDIDATOS.md`).

### Filtres de correu

| Regla | Condició | Etiqueta / acció |
|---|---|---|
| 1 | Assumpte `Nova candidatura` + resposta 4 conté «Instal·lador/a» | `Perfil-Instal·lador` |
| 2 | resposta 4 conté «Muntador/a» | `Perfil-Muntador` |
| 3 | resposta 4 conté «Oficial de manteniment» | `Perfil-Manteniment` |
| 4 | resposta 4 conté «Fuster/a de taller» o «Ajudant» | `Perfil-Taller` |
| 5 | resta | `Perfil-Altres` |
| 6 | Assumpte `CV — <Nom i Cognoms>` | reenviar a `comercial@oitinstalaciones.com` + etiqueta `CV-Candidatura-<NomApellido>` |

Totes les respostes es reenvien a `comercial@oitinstalaciones.com` perquè el
personal de RRHH les centralitzi.

### Emparellament formulari ↔ CV

Es crea una carpeta compartida `RRHH/Candidatures/<any>-<mes>/<NomApellido>/` i
s'hi mouen tots els correus d'aquesta persona per ordre cronològic.

Sense CV al correu, la candidatura queda marcada com a `incompleta` i no es
gestiona fins que arriba.

---

## Què **no** posar-hi

- **Edat o data de naixement** → innecessari i arriscat legalment.
- **Foto** → no aporta res per valorar l'ofici i alenteix el procés.
- **Camp d'adjuntar fitxer al formulari** → el CV va per correu.
- **Dades d'estat civil, salut o situació familiar** → no són necessàries.
- **Noms de clients o obres concretes** → no cal que el candidat exposi el
  client. Demana experiència, no clients.

---

## Checklist abans de publicar

- [ ] Formulari en castellà creat a partir del de català (`GOOGLE_FORM_CANDIDATOS_ES.md`)
- [ ] Destinatari de respostes = `uneixte@thinkoutside.es` / `unete@thinkoutside.es`
- [ ] Casella de confirmació del CV marcada com a obligatòria
- [ ] Casella de política de privacitat marcada com a obligatòria
- [ ] Enllaç del botó als SVG: `creatives/es/`, `creatives/ca/` i `creatives/ca-installadors/`
      (peces `10-unete-equipo`, `C1-calidad`, `C2-oficio`, `C3-perfil`)
- [ ] `python tools\check_layout.py creatives\es` → 0 avisos
- [ ] `python tools\check_layout.py creatives\ca` → 0 avisos
- [ ] `python tools\check_layout.py creatives\ca-installadors` → 0 avisos
- [ ] `python tools\make_ca.py` executat després de tocar l'ES
- [ ] `python tools\svg2png.py creatives\es creatives\es\png` i idem CA i CA-installadors
- [ ] `python tools\export_ai.py creatives\es` i idem CA
- [ ] `python tools\build_site.py` (web de mostra)
