"""
build_site.py — Genera la web estàtica que simula el feed d'Instagram.

Fa tres coses:
  1. copia les 21 creativitats catalanes (creatives/ca-installadors/png) a
     site/assets/posts/
  2. escriu site/data.js amb el copy de cada publicació
  3. comprova que hi siguin totes

Uso (des de l'arrel del projecte):

    python tools\\build_site.py
"""

import json
import pathlib
import re
import shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "creatives" / "ca-installadors" / "png"
SITE = ROOT / "site"
DST = SITE / "assets" / "posts"

# ---------------------------------------------------------------------------
# Copy de cada publicació (català). Ordre = ordre del feed.
# ---------------------------------------------------------------------------
POSTS = [
    {
        "fitxer": "01-bienvenida.png",
        "titol": "Benvinguda",
        "alt": "Portada de benvinguda de Think Outside amb el titular «Hola, Instagram» i el text «Som Think Outside».",
        "magrada": 384,
        "comentaris": 21,
        "caption": """Per fi també som aquí.

Som Think Outside, una empresa de fusteria amb
9 anys d'experiència. Fem instal·lacions,
reparacions i manteniment, i treballem amb
instal·ladors i muntadors propis.

En aquest perfil compartirem projectes, abans i després,
consells pràctics i moments del dia a dia de les obres
perquè la fusta duri més.

Comencem!""",
        "hashtags": "#ThinkOutside #Fusteria #Terrassa #Instaladors #NouPerfil",
    },
    {
        "fitxer": "02-trayectoria.png",
        "titol": "Trajectòria",
        "alt": "Peça de trajectòria de Think Outside: +9 anys donant forma a la fusta, amb una línia del temps del 2017 al 2026.",
        "magrada": 512,
        "comentaris": 34,
        "caption": """Vam començar el 2017 amb una taula de taller
i moltes ganes. Nou anys després, encara creiem
el mateix: cada tall compta.

Al llarg d'aquests anys hem treballat en habitatges,
hotels, hospitals, botigues i naus industrials.
La nostra manera de treballar no ha canviat:
ofici, atenció al detall i compromís.

Gràcies a totes les persones que ens heu confiat
els vostres projectes.""",
        "hashtags": "#9Anys #Trajectòria #ThinkOutside #Fusteria #Professionalitat",
    },
    {
        "fitxer": "03-servicio-instalaciones.png",
        "titol": "Servei: instal·lacions",
        "alt": "Peça del servei d'instal·lacions de Think Outside amb la llista de treballs que fan.",
        "magrada": 297,
        "comentaris": 12,
        "caption": """Comencem per un dels serveis que més ens demanen:

INSTAL·LACIONS.
Instal·lem parquet i portes, col·loquem armaris
encastats, revestim parets i muntem mobles de cuina.
Prenem mides, fabriquem si cal i fem la instal·lació
amb cura i dins del termini acordat.

Tens una reforma entre mans? Escriu-nos:
visitarem l'espai i t'assessorarem sense compromís.

→ Enllaç a la bio · missatge directe
comercial@oitinstalaciones.com""",
        "hashtags": "#Instalacions #Parquet #ArmarisEncastats #FusteriaAMida #Reformes",
    },
    {
        "fitxer": "04-servicio-reparacion.png",
        "titol": "Servei: reparació",
        "alt": "Peça del servei de reparació de Think Outside amb cinc avaries habituals de fusteria.",
        "magrada": 341,
        "comentaris": 27,
        "caption": """Allò que es trenca també es pot reparar — i, de vegades,
queda millor que abans.

REPARACIÓ.
Reparem elements de fusta: portes que freguen,
frontisses fluixes o trencades, calaixos desquadrats,
parquet malmès per l'aigua i marcs desencaixats.

Valorem l'avaria, preparem un pressupost tancat
i acordem una data d'intervenció.

Escriu-nos per missatge directe o truca al 630 377 574.""",
        "hashtags": "#ReparacióDeFusta #Restauració #Fusteria #Reparacions #ThinkOutside",
    },
    {
        "fitxer": "05-servicio-mantenimiento.png",
        "titol": "Servei: manteniment",
        "alt": "Peça del servei de manteniment de Think Outside amb els tipus de client a qui donen servei.",
        "magrada": 268,
        "comentaris": 9,
        "caption": """La fusta pot durar dècades si se'n té cura.
Aquí és on et podem ajudar.

MANTENIMENT.
Treballem amb comunitats de propietaris, hotels,
oficines, hospitals, comerços i naus industrials.
Oferim plans periòdics i intervencions puntuals,
amb un informe de cada actuació.

Gestiones un hotel, una oficina o un edifici
amb molts elements de fusta? Parlem-ne.""",
        "hashtags": "#Manteniment #GestióDInstalacions #Hotels #Comerç #Indústria #ThinkOutside",
    },
    {
        "fitxer": "06-manifiesto.png",
        "titol": "Manifest",
        "alt": "Manifest de Think Outside sobre fons marró: «Passió per una feina ben feta».",
        "magrada": 623,
        "comentaris": 41,
        "caption": """No és només una frase de la nostra web.

És la norma no escrita del taller:
mesurar dues vegades i tallar-ne una.
polir fins i tot allò que no es veu.
deixar l'obra més neta del que l'hem trobada.
tornar l'endemà si alguna cosa no acaba d'encaixar.

És el que oferim i el que fem des de fa 9 anys.""",
        "hashtags": "#PassióPelOfici #FetAMà #AtencióAlDetall #ThinkOutside #Marca",
    },
    {
        "fitxer": "07-proyecto-residencial.png",
        "titol": "Projecte: cuina",
        "alt": "Cuina reformada per Think Outside a Terrassa, amb mobles a mida i fronts lacats en blanc mat.",
        "magrada": 887,
        "comentaris": 56,
        "caption": """Una de les últimes cuines que hem acabat.

Mobles a mida amb fronts lacats en blanc mat,
encimera i frontal de pedra clara, i una
prestatgeria que aprofita el racó al costat de
la finestra. Placa i aigüera integrades.

Una cuina pensada per al dia a dia: neta,
lluminosa i fàcil de mantenir.

Parlem del teu projecte? Enllaç a la bio.""",
        "hashtags": "#ProjecteReal #CuinaAMida #ReformaIntegral #Terrassa #CuinaBlanca #MoblesAMida",
    },
    {
        "fitxer": "08-proyecto-corporativo.png",
        "titol": "Projecte: vinoteca",
        "alt": "Vinoteques a mida en un restaurant: dos armaris expositius amb portes de vidre i llum LED, abans i després del muntatge.",
        "magrada": 742,
        "comentaris": 48,
        "caption": """Vinoteques a mida per a un restaurant.

Dos armaris expositius amb portes de vidre,
prestatges de cristall i llum LED integrada.
Marcs de fusta a joc amb la resta de la sala.

La primera foto és durant el muntatge; la segona,
el resultat amb les ampolles ja col·locades.

Tens un local o una oficina que necessita
fusteria a mida? Enllaç a la bio.""",
        "hashtags": "#ProjecteReal #Hostaleria #Vinoteca #FusteriaAMida #Restaurants #Terrassa #ThinkOutside",
    },
    {
        "fitxer": "09-antes-despues.png",
        "titol": "El procés: de la caixa a l'obra",
        "alt": "Armari encastat en una habitació i cuina a mida en ple muntatge: dues estances sense acabats, amb els mobles ja col·locats.",
        "magrada": 431,
        "comentaris": 33,
        "caption": """De la caixa a l'obra.

Un armari encastat i una cuina a mida, tots dos
encara en muntatge. Així es veu la feina abans
dels acabats.

Armaris de terra a sostre amb portes llises i
tiradors de barra. Cuina amb fronts lacats en
blanc mat, a l'espera d'encimera, placa i
aigüera.

Tens un projecte? Enllaç a la bio.""",
        "hashtags": "#ProjecteReal #ArmarisEncastats #CuinaAMida #ReformaIntegral #Terrassa #ThinkOutside",
    },
    {
        "fitxer": "10-unete-equipo.png",
        "titol": "Busquem instal·ladors i muntadors",
        "alt": "Anunci de feina de Think Outside: busquem instal·ladors i muntadors amb ofici.",
        "magrada": 356,
        "comentaris": 29,
        "caption": """Estem creixent i busquem instal·ladors i muntadors
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

Si ho prefereixes, escriu-nos a uneixte@thinkoutside.es.""",
        "hashtags": "#Instaladors #Muntadors #OfertaDeFeina #TreballaAmbNosaltres #ThinkOutside",
    },
    {
        "fitxer": "11-cta-presupuesto.png",
        "titol": "Demana pressupost",
        "alt": "Peça de crida a l'acció de Think Outside per demanar pressupost sense compromís.",
        "magrada": 214,
        "comentaris": 11,
        "caption": """ Demana pressupost sense compromís.

Explica'ns què necessites — una instal·lació,
una reparació o un servei de manteniment — i et
respondrem en menys de 24 hores amb una primera
valoració.

Com ens pots contactar:
· Missatge directe
· comercial@oitinstalaciones.com
· +34 630 377 574
· Enllaç a la bio""",
        "hashtags": "#PressupostSenseCompromís #DemanaPressupost #Reformes #Fusteria #ThinkOutside",
    },
    {
        "fitxer": "12-tarjeta-contacto.png",
        "titol": "Targeta de contacte",
        "alt": "Targeta de contacte de Think Outside amb telèfon, correu, web i adreça a Terrassa.",
        "magrada": 189,
        "comentaris": 7,
        "caption": """Guarda aquesta targeta als teus destacats.

Think Outside · Fusteria
Terrassa · Barcelona
+34 630 377 574
comercial@oitinstalaciones.com
thinkoutside.es""",
        "hashtags": "#Contacte #ThinkOutside #FusteriaTerrassa",
    },
    {
        "fitxer": "B1-cuidados-invierno.png",
        "titol": "Consells d'hivern",
        "alt": "Quatre consells per cuidar el parquet a l'hivern.",
        "magrada": 508,
        "comentaris": 24,
        "caption": """Quatre consells per cuidar el parquet a l'hivern
(i evitar que es faci malbé).

La calefacció resseca la fusta i pot fer que
s'encongeixi. Si s'obren juntes entre les peces,
la humitat de l'habitatge també hi pot influir.

Evita mullar massa el parquet. Fes servir un drap
humit i ben escorregut. L'aigua entollada pot fer
que la fusta s'infli i deixar taques al vernís.

Cada 3–5 anys, renova el vernís si cal:
un bon manteniment allarga la vida del paviment.

Quin altre consell hi afegiries? Explica'ns-ho
als comentaris.""",
        "hashtags": "#ThinkOutside #Parquet #CuraDeLaFusta #ConsellsDeFusteria #Hivern #Fusta",
    },
    {
        "fitxer": "B2-mitos-vs-realidad.png",
        "titol": "Mites i realitat",
        "alt": "Tres mites sobre la fusta desmuntats amb tres parelles de mite i realitat.",
        "magrada": 674,
        "comentaris": 62,
        "caption": """Tres mites sobre la fusta que no són certs.

«La fusta i l'aigua no són compatibles.»
Amb el tractament adequat i un bon manteniment,
la fusta pot durar dècades.

«El parquet és per a cases antigues.»
És un paviment actual, tant en obra nova
com en reformes.

«Com més vernís, millor.»
L'excés de vernís pot fer que l'acabat
s'esquerdi. Més no sempre vol dir millor.

Quin d'aquests mites t'havien explicat?
Si t'ha semblat útil, desa la publicació.""",
        "hashtags": "#ThinkOutside #MitesSobreLaFusta #Fusteria #Curiositats #Fusta #Parquet",
    },
    {
        "fitxer": "B3-cinco-senales-puerta.png",
        "titol": "Cinc senyals",
        "alt": "Llista de comprovació amb cinc senyals que indiquen que cal revisar una porta.",
        "magrada": 442,
        "comentaris": 19,
        "caption": """Cinc senyals que indiquen que cal revisar la porta.

Si n'hi reconeixes una, probablement té solució.
Si en detectes dues o més, contacta amb nosaltres
abans que el problema vagi a més.

· La porta frega amb el marc
· Les frontisses estan fluixes o grinyolen
· La fusta s'ha inflat per la humitat
· El vernís està esquerdat o aixecat
· El pany falla o es mou

Escriu-nos o truca al 630 377 574.
T'assessorarem sense compromís.""",
        "hashtags": "#ThinkOutside #ReparacióDeFusta #PortesDeFusta #Reparacions #Fusteria #Restauració",
    },
    {
        "fitxer": "B4-tipos-de-madera.png",
        "titol": "Les nostres fustes",
        "alt": "Fitxes amb sis tipus de fusta: roure, noguera, castanyer, cirerer, faig i pi.",
        "magrada": 731,
        "comentaris": 38,
        "caption": """Les sis fustes que més treballem al taller.

Roure — dur i resistent; un clàssic per al parquet.
Noguera — fosca, de veta marcada i tacte noble.
Castanyer — resistent a la humitat, ideal per a exteriors.
Cirerer — càlid, de veta fina; envelleix amb caràcter.
Faig — clar, dur i fàcil de treballar.
Pi — econòmic i versàtil, amb nusos característics.

Tens un projecte al cap? Digues-nos quina fusta
t'agrada i t'assessorarem.""",
        "hashtags": "#ThinkOutside #TipusDeFusta #FustesNobles #Roure #Noguera #Cirerer #Fusteria",
    },
    {
        "fitxer": "B5-glosario.png",
        "titol": "Glossari del taller",
        "alt": "Glossari amb sis termes de fusteria: esquadria, encadellat, vernís, oli d'acabat, veta i tapajunts.",
        "magrada": 596,
        "comentaris": 31,
        "caption": """Sis termes que sentiràs en un taller de fusteria.

Esquadria → mides de la secció d'una peça
(gruix × amplada).

Encadellat → unió de peces amb una ranura
i una llengüeta que encaixen.

Vernís → capa protectora amb acabat mat,
setinat o brillant.

Oli d'acabat → nodreix la fusta sense segellar-la;
permet reparar-ne zones concretes.

Veta → dibuix natural de les fibres de la fusta.
Cada peça és única.

Tapajunts → motllura que cobreix la junta
entre el terra i la paret o entre taulers.

Desa-ho per a la pròxima reforma. """,
        "hashtags": "#ThinkOutside #GlossariDeFusteria #Fusta #Ofici #Fusteria #AprenemAlTaller",
    },
    {
        "fitxer": "B6-sabias-que.png",
        "titol": "Sabies que…",
        "alt": "Dada curiosa: una porta de fusta massissa aïlla cinc vegades més que una de buida.",
        "magrada": 389,
        "comentaris": 22,
        "caption": """Sabies que...?

Una porta de fusta massissa aïlla cinc vegades més
tèrmicament i acústicament que una porta buida
del mateix gruix.

Ho veiem sovint en hotels i oficines: substituir
portes buides per portes massisses pot millorar
l'aïllament acústic i reduir la pèrdua de calor.

Quin altre tema sobre la fusta t'agradaria que
expliquéssim? Escriu-nos i en parlarem.""",
        "hashtags": "#ThinkOutside #SabiesQue #CuriositatsDeFusta #PortesDeFusta #AïllamentAcústic",
    },
    {
        "fitxer": "C1-calidad.png",
        "titol": "Captació: qualitat",
        "alt": "Anunci de feina de Think Outside amb tres targetes: eficiència, talent i qualitat.",
        "magrada": 402,
        "comentaris": 26,
        "caption": """Busquem persones que facin bé la seva feina
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

O escriu-nos a uneixte@thinkoutside.es · 630 377 574""",
        "hashtags": "#Instaladors #Muntadors #OfertaDeFeina #TreballaAmbNosaltres #ThinkOutside",
    },
    {
        "fitxer": "C2-oficio.png",
        "titol": "Captació: ofici",
        "alt": "Anunci de feina de Think Outside: «No busquem només mans. Busquem ofici.»",
        "magrada": 468,
        "comentaris": 35,
        "caption": """No busquem només mans. Busquem ofici.

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

uneixte@thinkoutside.es · 630 377 574""",
        "hashtags": "#Instaladors #Muntadors #Ofici #OfertaDeFeina #ThinkOutside",
    },
    {
        "fitxer": "C3-perfil.png",
        "titol": "Captació: perfil",
        "alt": "Anunci de feina de Think Outside amb quatre requisits: ofici, eficiència, criteri i ganes de créixer.",
        "magrada": 377,
        "comentaris": 24,
        "caption": """Què busquem en tu?

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

uneixte@thinkoutside.es · 630 377 574""",
        "hashtags": "#Instaladors #Muntadors #OfertaDeFeina #TreballaAmbNosaltres #ThinkOutside",
    },
]


def neteja_etiquetes(txt):
    """Els hashtags no poden contenir el punt volat (·)."""
    out = []
    for paraula in txt.split():
        if paraula.startswith("#") and "·" in paraula:
            paraula = paraula.replace("·", "")
        out.append(paraula)
    return " ".join(out)


def main():
    if not SRC.exists():
        raise SystemExit(f"No existeix la carpeta d'origen: {SRC}")

    DST.mkdir(parents=True, exist_ok=True)
    for vell in DST.glob("*.png"):
        vell.unlink()

    faltes = []
    for post in POSTS:
        origen = SRC / post["fitxer"]
        if not origen.exists():
            faltes.append(post["fitxer"])
            continue
        shutil.copy2(origen, DST / post["fitxer"])
        post["hashtags"] = neteja_etiquetes(post["hashtags"])

    if faltes:
        raise SystemExit("Falten imatges: " + ", ".join(faltes))

    for post in POSTS:
        post.setdefault("pendent", False)
        post["caption"] = post["caption"].strip()
        post["hashtags"] = re.sub(r"\s+", " ", post["hashtags"]).strip()

    dades = json.dumps(POSTS, ensure_ascii=False, indent=2)
    (SITE / "data.js").write_text("window.POSTS = " + dades + ";\n", encoding="utf-8")

    print(f"OK {len(POSTS)} publicacions")
    print(f"OK imatges a {DST.relative_to(ROOT)}")
    print(f"OK {SITE.joinpath('data.js').relative_to(ROOT)}")


if __name__ == "__main__":
    main()
