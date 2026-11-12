"""
make_ca.py — Genera la version catalana de cada pieza a partir de la espanola.

Aplica un diccionario de traduccion sobre el contenido de texto de los SVG
(es -> ca). Los cambios de posicion (por texto mas largo/corto) se ajustan
despues con el corrector de maquetacion (tools/check_layout.py).

Uso:  python tools\\make_ca.py
"""

import pathlib
import re
import sys

# En Windows la consola usa cp1252 y revienta con los emojis del informe.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = pathlib.Path(__file__).resolve().parent.parent
ES = ROOT / "creatives" / "es"
CA = ROOT / "creatives" / "ca"

# --------------------------------------------------------------------------
# Diccionario es -> ca. Se aplica de mas largo a mas corto para que las
# frases largas se traduzcan antes que sus fragmentos.
# --------------------------------------------------------------------------
T = {
    # --- pie de pagina (comun) ---
    "EXPERTOS EN INSTALACIONES Y MANTENIMIENTO DE CARPINTERÍA DE MADERA":
        "ESPECIALISTES EN INSTAL·LACIONS I MANTENIMENT DE FUSTERIA",
    "EXPERTOS EN INSTALACIONES Y MANTENIMIENTO":
        "ESPECIALISTES EN INSTAL·LACIONS I MANTENIMENT",
    "DE CARPINTERÍA DE MADERA": "DE FUSTERIA",

    # --- correu de selecció (ES / CA) ---
    "unete@thinkoutside.es": "uneixte@thinkoutside.es",

    # --- 01 bienvenida ---
    "NUEVO EN INSTAGRAM": "NOU A INSTAGRAM",
    "Somos <tspan font-weight=\"700\">Think Outside</tspan> —":
        "Som <tspan font-weight=\"700\">Think Outside</tspan> —",
    "carpinteros de madera en Terrassa,": "fusters de Terrassa,",
    "Síguenos →": "Segueix-nos →",

    # --- 02 trayectoria ---
    "NUESTRA HISTORIA": "NOSTRA HISTÒRIA",
    "años dando forma": "anys donant forma",
    "a la madera": "a la fusta",
    "RESIDENCIAL  ·  HOTELES  ·  RETAIL  ·  INDUSTRIA":
        "RESIDENCIAL  ·  HOTELS  ·  COMERÇ  ·  INDÚSTRIA",

    # --- 03/04/05 servicios ---
    "SERVICIO 01 / 03": "SERVEI 01 / 03",
    "SERVICIO 02 / 03": "SERVEI 02 / 03",
    "SERVICIO 03 / 03": "SERVEI 03 / 03",
    "Instalaciones": "Instal·lacions",
    "Reparación": "Reparació",
    "Mantenimiento": "Manteniment",
    "Puertas de interior y exterior": "Portes d'interior i exterior",
    "Armarios empotrados a medida": "Armaris encastats a mida",
    "Forrado de paredes": "Revestiment de parets",
    "Muebles de cocina": "Mobles de cuina",
    "Puertas que no cierran bien": "Portes que no tanquen bé",
    "Bisagras sueltas o rotas": "Frontisses fluixes o trencades",
    "Cajones descuadrados": "Calaixos desquadrats",
    "Suelos dañados por humedad": "Sòls danyats per la humitat",
    "Marcos desencajados": "Marcs desencaixats",
    "Edificios residenciales": "Edificis residencials",
    "Hoteles y restauración": "Hotels i restauració",
    "Oficinas y corporativos": "Oficines i corporatius",
    "Hospitales y sanitarios": "Hospitals i sanitaris",
    "Cadenas de retail y naves industriales": "Cadenes de comerç i naus industrials",
    "Pide presupuesto →": "Demana pressupost →",

    # --- 06 manifiesto ---
    "Pasión por": "Passió per",
    "un trabajo": "una feina",
    "bien hecho.": "ben feta.",
    "En cada corte. En cada instalación.": "A cada tall. A cada instal·lació.",
    "En cada detalle.": "A cada detall.",

    # --- 07 proyecto residencial ---
    "PROYECTO · COCINA": "PROJECTE · CUINA",
    "[ FOTO DE PROYECTO ]": "[ FOTO DEL PROJECTE ]",
    "REEMPLAZAR POR FOTO REAL · 960 × 540": "CANVIA-HO PER UNA FOTO REAL · 960 × 540",
    "Cocina en Terrassa": "Cuina a Terrassa",
    "Muebles de cocina a medida y": "Mobles de cuina a mida i",
    "frentes lacados en blanco mate": "fronts lacats en blanc mat",
    "Cocina a medida": "Cuina a mida",
    "Frentes lacados": "Fronts lacats",
    "12 días": "12 dies",
    "Acabado mate": "Acabat mat",

    # --- 08 proyecto corporativo ---
    "PROYECTO · HOSTELERÍA": "PROJECTE · HOSTALERIA",
    "Vinotecas a medida": "Vinoteques a mida",
    "para un restaurante.": "per a un restaurant.",
    "Armarios expositores de madera con puertas": "Armaris expositius de fusta amb portes",
    "de vidrio, luz LED integrada y marcos a juego.": "de vidre, llum LED integrada i marcs a joc.",
    "Madera maciza": "Fusta massissa",
    "Luz LED integrada": "Llum LED integrada",

    # --- 09 antes/despues ---
    "EL PROCESO": "EL PROCÉS",
    "Reforma de puerta": "Reforma de porta",
    "De la caja": "De la caixa",
    "a la cocina.": "a la cuina.",
    "Montaje de una cocina a medida, paso a paso.": "Muntatge d'una cuina a mida, pas a pas.",
    "ESTRUCTURA": "ESTRUCTURA",
    "INTERIOR": "INTERIOR",
    "¿Tienes un proyecto? Escríbenos →": "Tens un projecte? Escriu-nos →",
    "[ FOTO ANTES ]": "[ FOTO D'ABANS ]",
    "[ FOTO DESPUÉS ]": "[ FOTO DE DESPRÉS ]",
    "DESPUÉS": "DESPRÉS",
    "ANTES": "ABANS",
    "⏱ 1 día de trabajo": "⏱ 1 dia de feina",
    "¿Algo parecido? Escríbenos →": "Alguna cosa semblant? Escriu-nos →",

    # --- 10 unete equipo ---
    "WE'RE HIRING": "BUSQUEM FUSTERS",
    "Buscamos": "Cerquem",
    "carpinteros": "fusters",
    "con oficio.": "amb ofici.",
    "Cuéntanos qué sabes hacer. En 2 minutos.": "Explica'ns què saps fer. En 2 minuts.",
    "Aplica al puesto →": "Inscriu-t'hi →",
    "¿PREFIERES EMAIL?": "PREFEREIXES EL CORREU?",

    # --- 11 CTA presupuesto ---
    "¿Tienes un": "Tens un",
    "en mente?": "en ment?",
    "proyecto": "projecte",
    "Te enviamos un presupuesto": "T'enviem un pressupost",
    "sin compromiso.": "sense compromís.",
    "Pide presupuesto": "Demana pressupost",
    "↳ RESPONDEMOS EN MENOS DE 24 H": "↳ RESPONEM EN MENYS DE 24 H",

    # --- 12 tarjeta de contacto ---
    "CONTACTO": "CONTACTE",
    "Hablemos.": "Parlem.",

    # --- B1 cuidados invierno ---
    "TIP DE TALLER · INVIERNO": "CONSELL DE TALLER · HIVERN",
    "Cuida tu parquet": "Cuida el parquet",
    "este invierno.": "aquest hivern.",
    "Humedad estable": "Humitat estable",
    "Mantén la humedad relativa de la casa entre el": "Mantén la humitat relativa de casa entre el",
    "40% y el 60%. La calefacción reseca mucho.": "40% i el 60%. La calefacció resseca molt.",
    "Cuidado con la calefacción": "Compte amb la calefacció",
    "No pongas alfombras justo encima de los": "No posis catifes just a sobre dels",
    "radiadores. La madera se deforma con el calor.": "radiadors. La fusta es deforma amb la calor.",
    "Limpieza casi seca": "Neteja gairebé seca",
    "Paño húmedo, bien escurrido. Nada de charcos": "Drap humit i ben escorregut. Evita els bassals",
    "ni productos abrasivos.": "i els productes abrasius.",
    "Repaso de barniz": "Manteniment del vernís",
    "Cada 3–5 años, una mano de mantenimiento": "Cada 3–5 anys, un repàs de manteniment",
    "alarga décadas la vida del suelo.": "allarga dècades la vida del terra.",
    "GUÁRDALO PARA EL FRÍO · PIENSA EN MADERA": "DESA-HO PER A L'HIVERN · PENSA EN LA FUSTA",

    # --- B2 mitos vs realidad ---
    "DESMONTANDO MITOS": "DESMUNTEM ELS MITES",
    "Madera: mito": "Fusta: mite",
    "vs. realidad.": "o realitat?",
    "REALIDAD": "REALITAT",
    "MITO": "MITE",
    "«La madera y el": "«La fusta i l'aigua",
    "agua no se llevan.»": "no són compatibles.»",
    "Con tratamiento hidrófugo": "Amb tractament hidròfug",
    "y mantenimiento, aguanta": "i un bon manteniment, la fusta",
    "décadas.": "pot durar dècades.",
    "«El parquet es cosa": "«El parquet és cosa",
    "de casas antiguas.»": "de cases antigues.»",
    "Es uno de los suelos más": "És un dels paviments més",
    "actuales en obra nueva": "actuals en obra nova",
    "y rehabilitación.": "i rehabilitació.",
    "«Cuanta más capa": "«Com més capa",
    "de barniz, mejor.»": "de vernís, millor.»",
    "Demasiado barniz ahoga": "L'excés de vernís ofega",
    "la madera y la acaba": "la fusta i pot fer que",
    "cuarteando.": "s'esquerdi.",
    "¿CUÁL DE ESTOS MITOS TE HAN CONTADO? ↓": "QUIN D'AQUESTS MITES T'HAN EXPLICAT? ↓",

    # --- B3 cinco senales ---
    "CHECKLIST DE TALLER": "LLISTA DE COMPROVACIÓ",
    "5 señales de que": "5 senyals que indiquen",
    "tu puerta pide revisión.": "que cal revisar la porta.",
    "Roza con el marco o no encaja bien": "Frega amb el marc o no encaixa bé",
    "Bisagras sueltas o chirridos al abrir": "Frontisses fluixes o que grinyolen",
    "Madera hinchada por humedad": "Fusta inflada per la humitat",
    "Barniz cuarteado o levantado": "Vernís esquerdat o aixecat",
    "Cerradura que falla o se mueve": "El pany falla o es mou",
    "¿Te suena alguna? Escríbenos →": "Et sona alguna? Escriu-nos →",

    # --- B4 tipos de madera ---
    "NUESTRAS MADERAS": "LES NOSTRES FUSTES",
    "Las maderas que": "Les fustes que",
    "más trabajamos.": "més treballem.",
    "Roble": "Roure",
    "Duro, estable. El clásico": "Dur i resistent. Clàssic",
    "para parquet y mueble.": "per a parquet i moble.",
    "PARQUET · MUEBLE": "PARQUET · MOBLE",
    "Nogal": "Noguera",
    "Tono oscuro, veta marcada,": "De to fosc i veta marcada,",
    "muy noble al tacto.": "amb un tacte molt noble.",
    "MUEBLE · CARPINTERÍA": "MOBLES · FUSTERIA",
    "Castaño": "Castanyer",
    "Resistente a la humedad.": "Resistent a la humitat.",
    "Ideal para exterior.": "Ideal per a exteriors.",
    "EXTERIOR · VALLAS": "EXTERIOR · TANQUES",
    "Cerezo": "Cirerer",
    "Cálido, veta fina.": "Càlid, veta fina.",
    "Envejece con carácter.": "Envelleix amb caràcter.",
    "MUEBLE · DECORACIÓN": "MOBLE · DECORACIÓ",
    "Haya": "Faig",
    "Tono claro y duro.": "To clar i dur.",
    "Se trabaja muy limpia.": "Fàcil de treballar.",
    "MUEBLE · ESCALERAS": "MOBLE · ESCALES",
    "Pino": "Pi",
    "Económico y versátil.": "Econòmic i versàtil.",
    "Sus nudos tienen personalidad.": "Els seus nusos tenen personalitat.",
    "REVESTIMIENTO · OBRA": "REVESTIMENTS · OBRA",

    # --- B5 glosario ---
    "GLOSARIO DEL TALLER": "GLOSSARI DEL TALLER",
    "6 palabras que": "6 paraules que",
    "usamos a diario.": "fem servir cada dia.",
    "Escuadría": "Esquadria",
    "Las dimensiones exactas (grosor × anchura)": "Les dimensions exactes (gruix × amplada)",
    "de un tablón o listón.": "d'un tauló o llistó.",
    "Machihembrado": "Encadellat",
    "Unión de tablas con ranura y lengüeta.": "Unió de taules amb ranura i llengüeta.",
    "Encajan sin clavos ni tornillos.": "Encaixen sense claus ni cargols.",
    "Barniz": "Vernís",
    "Capa protectora que sella la madera.": "Capa protectora que segella la fusta.",
    "Brillo mate, satinado o brillo.": "Acabat mat, setinat o brillant.",
    "Acedur / Aceite": "Oli d'acabat",
    "Acabado que nutre la madera sin sellarla.": "Acabat que nodreix la fusta sense segellar-la.",
    "Tacto natural, se repara por zonas.": "Té un tacte natural i es pot reparar per zones.",
    "Veta": "Veta",
    "Dibujo natural de la fibra de la madera.": "Dibuix natural de les fibres de la fusta.",
    "Cada pieza es única.": "Cada peça és única.",
    "Junquillo": "Tapajunts",
    "Listón fino que remata la unión entre suelo": "Motllura estreta que cobreix la junta entre el terra",
    "y pared, o entre tableros.": "i la paret o entre taulers.",

    # --- B6 sabias que ---
    "SABÍAS QUE...": "SABIES QUE...",
    "Una puerta de madera maciza": "Una porta de fusta massissa",
    "aísla 5 veces más que una hueca.": "aïlla cinc vegades més que una de buida.",
    "También aísla mejor del ruido y aguanta": "També aïlla millor del soroll i resisteix",
    "décadas sin deformarse.": "el pas de les dècades sense deformar-se.",
    "¿OTRA CURIOSIDAD? → DM": "UNA ALTRA CURIOSITAT? → DM",

    # --- C1 calidad (contratación) ---
    "ESTAMOS CONTRATANDO": "BUSQUEM FUSTERS",
    "Gente que sabe": "Gent que sap",
    "hacer las cosas bien": "fer les coses bé",
    "Eficientes, con oficio y sin excusas.": "Persones eficients, amb ofici i sense excuses.",
    "EFICIENCIA": "EFICIÈNCIA",
    "TALENTO": "TALENT",
    "CALIDAD": "QUALITAT",
    "Rinden desde el primer": "Rendeixen des del primer",
    "día, sin repetir tareas": "dia, sense repetir tasques",
    "ni perder el tiempo.": "ni perdre el temps.",
    "Manos de oficio y": "Mans d'ofici i",
    "cabeza de profesional.": "criteri professional.",
    "Resuelven, no estorban.": "Resolen problemes.",
    "El detalle se nota en": "El detall es nota en",
    "cada corte y cada": "cada tall i cada",
    "instalación. Siempre.": "instal·lació. Sempre.",

    # --- C2 oficio (contratación) ---
    "No buscamos": "No busquem",
    "manos vacías.": "només mans.",
    "Buscamos oficio.": "Busquem ofici.",
    "Gente que llega, entiende y termina.": "Persones que entenen la feina i l'acaben bé.",
    "Dejan la obra como la encontraron, pero mejor.":
        "Deixen l'obra millor de com l'han trobada.",
    "Eficiencia real": "Eficiència real",
    "Trabaja con orden: sabe qué toca, cuándo y cómo.":
        "Treballa amb ordre: sap què toca, quan i com.",
    "Talento aplicado": "Talent aplicat",
    "Aporta criterio cuando la obra no sale derecha.":
        "Aporta criteri quan les coses no van com haurien d'anar.",
    "Calidad sin bajarse": "Qualitat innegociable",
    "El acabado es la parte que no se negocia.": "L'acabat no es negocia.",

    # --- C3 perfil (contratación) ---
    "Qué buscamos": "Què busquem",
    "en ti": "en tu",
    "Personas que rinden, que saben y que cuidan el detalle.":
        "Persones eficients i amb ofici, que tenen cura dels detalls.",
    "Oficio real": "Ofici real",
    "Sabes trabajar la madera y entiendes cómo se monta.":
        "Saps treballar la fusta i entens com s'instal·la.",
    "Eficiencia": "Eficiència",
    "Rindes, no ocupas: haces tu parte y algo más.":
        "Treballes amb eficàcia i vas més enllà de la teva tasca.",
    "Criterio": "Criteri",
    "Cuando algo no cuadra, lo dices y sabes cómo mejorarlo.":
        "Quan alguna cosa no quadra, ho dius i saps com millorar-la.",
    "Ganas de crecer": "Ganes de créixer",
    "Te apuntas a lo que toque, dentro y fuera del taller.":
        "T'apuntes al que toca, dins i fora del taller.",
}


DATA_URI = re.compile(r'href="data:[^"]*"')

def translate(svg_text):
    """Substitució en una sola passada: els resultats no es tornen a
    processar, de manera que una traducció no pot activar una altra regla.

    Els data URI (imatges en base64) es deixen de banda: el seu contingut
    podria coincidir per atzar amb una clau del diccionari."""
    stash = []

    def keep(m):
        stash.append(m.group(0))
        return f"@@IMG{len(stash)-1}@@"

    safe = DATA_URI.sub(keep, svg_text)
    pattern = re.compile("|".join(re.escape(k) for k in sorted(T, key=len, reverse=True)))
    out = pattern.sub(lambda m: T[m.group(0)], safe)
    for i, blob in enumerate(stash):
        out = out.replace(f"@@IMG{i}@@", blob)
    return out


def main():
    CA.mkdir(parents=True, exist_ok=True)
    for es_file in sorted(ES.glob("*.svg")):
        txt = es_file.read_text(encoding="utf-8")
        ca = translate(txt)
        (CA / es_file.name).write_text(ca, encoding="utf-8")
        # informe rapido de textos que siguen en espanol (sin traducir)
        missing = []
        for line in txt.splitlines():
            for m in re.finditer(r">([^<>]{3,})</text>", line):
                s = m.group(1).strip()
                if not s or s == "5×":
                    continue
                if f">{s}</text>" in ca:
                    missing.append(s)
        flag = "  <-- SIN TRADUCIR: " + ", ".join(missing) if missing else ""
        print(f"OK  {es_file.name}{flag}")


if __name__ == "__main__":
    main()
