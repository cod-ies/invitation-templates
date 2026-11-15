#!/usr/bin/env python3
"""Add the evening folio to every invitation. Safe to run again."""

from html import escape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent

MEET = [
    "haben sich an einem Bahnsteig die Zeitung geteilt",
    "kennen sich aus einer Küche, in der der Herd zu klein war",
    "sind sich im Regen unter einem einzigen Schirm begegnet",
    "haben sich in der Schlange vor dem Bäcker die Zeit vertrieben",
    "kennen sich von einer Hochzeit, auf der sie beide nicht tanzen wollten",
    "sind im Museum vor demselben Bild stehen geblieben",
    "sind sich auf einer Fähre über den Weg gelaufen",
    "kennen sich aus einem Chor, der immer einen Ton zu tief lag",
    "haben sich beim Umzug die Kisten verwechselt",
    "sind in einer Buchhandlung zwischen zwei Regalen stehen geblieben",
    "kennen sich von einem Sonntag, der nur ein Kaffee werden sollte",
    "haben sich auf dem Markt den letzten Strauß geteilt",
    "sind sich im Treppenhaus begegnet und dann nicht weitergegangen",
    "kennen sich aus einem Kurs, den beide nach der dritten Stunde geliebt haben",
    "haben sich an einem See die Schuhe ausgezogen und sind geblieben",
    "saßen sich im Zug gegenüber und haben das Ziel verpasst",
    "kennen sich von einem Brief, der an die falsche Tür ging",
    "haben sich auf einem Dach die Stadt gezeigt",
    "haben sich bei der Arbeit über denselben Fehler gebeugt",
    "kennen sich aus einem Winter, in dem die Heizung ausfiel",
    "haben sich auf einer Brücke die Richtung erklärt",
    "sind sich im Theater in der Pause nicht mehr losgeworden",
    "kennen sich von einem Hund, der beiden nachlief",
    "haben sich an einem Tisch mit zu wenigen Stühlen kennengelernt",
    "sind sich im Garten der Nachbarn begegnet und geblieben",
    "kennen sich aus einer Nacht, in der der letzte Bus schon weg war",
    "haben sich beim Kochen die Pfanne geteilt und dann den Abend",
    "haben sich auf einer glatten Treppe an der Hand gehalten",
    "kennen sich von einem Lied, das in zwei Wohnungen gleichzeitig lief",
    "haben sich am Hafen eine Orange geteilt und die Zeit dazu",
]

TURN = [
    "Seitdem gibt es ein Wir, und ihr seid der Kreis darum.",
    "Aus dem Zufall wurde ein Tisch, und an dem Tisch ist für euch immer Raum.",
    "Was damals klein anfing, hat jetzt ein Datum.",
    "Sie haben nicht lange überlegt. Sie haben euch dazugenommen.",
    "Der Rest ist dieser Abend, den ihr mit ihnen offen haltet.",
    "Deshalb stehen hier Namen und kein leeres Plus-eins.",
    "Heute geht die Tür auf, und ihr sollt hindurch.",
    "Der Abend gehört den beiden. Ihr gehört dazu.",
    "Aus zwei Wegen wurde einer, und der führt hierher.",
    "Sie feiern, weil ihr kommt.",
    "Was sie euch geben, ist ein langer Abend und ein ehrliches Glas.",
    "Der Satz, der alles geändert hat, war kurz. Der Abend darf länger sein.",
    "Sie haben das Datum gewählt, weil es sich nach euch anfühlt.",
    "Ohne euch wäre es nur eine Unterschrift. Mit euch wird es ein Fest.",
    "Der Ort ist schön. Schön wird er erst, wenn ihr da seid.",
    "Ihr kennt sie einzeln. Heute seht ihr sie als Paar.",
    "Der Abend hat keinen Plan, der lauter ist als ihr.",
    "Was bleibt, ist nicht die Rede. Es ist, dass ihr da wart.",
    "Sie öffnen das Haus. Bringt Zeit mit, nichts sonst.",
    "Zwei Namen auf der Karte, und eure sollen dazukommen.",
]

PLACE = {
    "Rosengarten am Abend": "Der Rosengarten hält das letzte Licht fest, lange nachdem die Stadt schon dunkel ist.",
    "Weißer Garten": "Im weißen Garten ist alles leise, bis jemand lacht.",
    "Laube der Pfingstrosen": "Unter den Pfingstrosen riecht es schwer und süß, und niemand hat es eilig.",
    "An der Blütenwand": "Die Blütenwand ist nur der Hintergrund. Ihr seid der Grund.",
    "Am Seeufer": "Am See kühlt der Abend schnell ab. Drinnen wird es warm.",
    "Auf der Steintreppe": "Die Treppe ist alt, die Schuhe sind neu, beides darf sein.",
    "Im Laternenhof": "Im Hof gehen die Laternen an, eine nach der anderen.",
    "Im Glashaus": "Im Glashaus bleibt der Tag länger, als er draußen ist.",
    "Auf dem Hortensienweg": "Der Weg ist schmal. Geht nebeneinander, nicht hintereinander.",
    "Unter dem weißen Bogen": "Der Bogen rahmt nur den Anfang. Danach ist der ganze Garten offen.",
    "Im Gutshaus": "Das Gutshaus kennt große Tische und lange Abende.",
    "An der Alster": "An der Alster spiegelt sich das Licht, auch wenn der Himmel grau bleibt.",
    "Im Palmenhaus": "Im Palmenhaus ist es warm, auch wenn draußen der Wind geht.",
    "Auf dem Weingut": "Auf dem Weingut zählt der Abend mehr als die Uhr.",
    "Im Stadthaus": "Das Stadthaus hat hohe Fenster und einen stillen Flur.",
    "Am See": "Am See legt sich der Tag aufs Wasser, bevor er verschwindet.",
    "In der Orangerie": "In der Orangerie duftet es nach Blättern und nach warmem Stein.",
    "Im Atelier": "Im Atelier ist Raum für Farbe, auch an der Kleidung.",
    "Auf dem Hof": "Auf dem Hof trägt der Wind die Musik weiter als die Stimmen.",
    "Im Wintergarten": "Im Wintergarten bleibt das Licht, wenn draußen schon die Lampen an sind.",
}

PRACTICAL = {
    "Rosengarten am Abend": "Flache Schuhe. Der Kies ist ehrlich.",
    "Weißer Garten": "Hell muss nicht weiß sein. Ein Tuch für den Abend reicht.",
    "Laube der Pfingstrosen": "Weiche Farben, nichts, was an den Blüten zerrt.",
    "An der Blütenwand": "Kommt so, dass man euch vor den Blüten noch sieht.",
    "Am Seeufer": "Ein Schal für den Wind, sobald die Sonne weg ist.",
    "Auf der Steintreppe": "Schuhe, denen eine Treppe nichts ausmacht.",
    "Im Laternenhof": "Etwas, das im Lampenlicht warm bleibt.",
    "Im Glashaus": "Leichtes, das auch im Warmen noch gut sitzt.",
    "Auf dem Hortensienweg": "Der Weg ist uneben. Lasst die dünnen Absätze zu Hause.",
    "Unter dem weißen Bogen": "Weiß ist der Bogen. Ihr dürft Farbe tragen.",
    "Im Gutshaus": "Etwas Festliches, in dem man noch sitzen und lachen kann.",
    "An der Alster": "Ein Mantel für den Weg am Wasser. Drinnen wird es warm.",
    "Im Palmenhaus": "Luftig. Drinnen ist es wärmer als draußen.",
    "Auf dem Weingut": "Schuhe, die den Boden und den Abend können.",
    "Im Stadthaus": "Stadthell, nicht steif. Eine Jacke für den Flur.",
    "Am See": "Ein Tuch für die Schultern, wenn der See die Wärme nimmt.",
    "In der Orangerie": "Helle Stoffe, nichts, was am Stein schleift.",
    "Im Atelier": "Farbe ist willkommen. Neu muss nichts sein.",
    "Auf dem Hof": "Der Hof ist aus Stein und Gras. Schuhe für beides.",
    "Im Wintergarten": "Drinnen leicht, für den Weg ein Mantel.",
}

SECRET = [
    "Um Mitternacht gibt es warme Brezeln, nicht noch eine Torte.",
    "Der erste Tanz ist langsam, und wer will, tanzt von der ersten Minute mit.",
    "Der Trinkspruch hat drei Sätze. Danach seid ihr dran, wenn ihr wollt.",
    "Nach dem Essen geht die Tür noch einmal in den Garten auf.",
    "Die Musik fängt leise an und wird später unelegant. Das ist Absicht.",
    "Zum Nachtisch gibt es etwas Warmes aus der Kindheit der beiden.",
    "Ein Lied gehört euch allen. Ihr erkennt es, wenn es anfängt.",
    "Zwischen den Gängen wird es eine Minute still. Sie hält nicht lange.",
    "Wer friert, bekommt eine Decke, ohne fragen zu müssen.",
    "Das letzte Glas ist klein und süß.",
    "Aus der Küche kommt noch etwas, das auf keiner Karte steht.",
    "Irgendwann werden die Schuhe egal. Das ist der richtige Moment.",
    "Ein Freund spielt ein Stück, das die beiden seit Jahren summen.",
    "Wenn die Lichterketten angehen, bleibt noch.",
    "Zum Abschied liegt etwas in der Hand, das nach dem Tag duftet.",
    "Die Rede ist kurz. Das Versprechen davor war es auch.",
    "Wer den Weg nicht kennt, folgt den Lichtern.",
    "Es gibt einen Tanz, den niemand übt. Er wird trotzdem gut.",
    "Das Essen kommt in Schüsseln. Langt zu.",
    "Wenn es dunkel ist, gibt es Sterne oder Laternen. Beides reicht.",
    "Die Bar schließt nicht. Sie wird nur leiser.",
    "Es gibt einen Moment barfuß. Ihr entscheidet, ob ihr mitmacht.",
    "Der Kuchen hat eine Schicht, die niemand erwartet.",
    "Zum Auftakt spielt nur ein Klavier, ohne Worte.",
    "Die beiden verschwinden für zehn Minuten. Sie kommen wieder.",
    "Auf jedem Glas liegt ein Zettel mit einem Wort, mehr nicht.",
    "Der Garten wird später zur Tanzfläche. Die Beete bleiben tabu.",
    "Wer keinen Wein will, bekommt heißen Apfelsaft. Der ist kein Trostpreis.",
    "Wenn es regnet, zieht der Abend unter das Dach, nicht auseinander.",
    "Die erste Stunde gehört den Gesprächen.",
    "Ein altes Lied der Eltern kommt, aber nur wenn sie es wollen.",
    "Zum Schluss steht ihr draußen, auch wenn es windet.",
    "Es gibt eine kleine Bühne und keinen Zwang, sie zu betreten.",
    "Der Nachtisch wird geteilt. Löffel sind genug da.",
    "Eine Lampe geht erst an, wenn ihr da seid.",
    "Es gibt zweite Portionen, ohne dass jemand winken muss.",
    "Zwischen zwei Liedern fällt ein Satz, den nur die beiden kennen.",
    "Der Weg zurück ist beleuchtet.",
    "Wenn der Abend kippt, kippt er ins Lachen, nicht in die Eile.",
    "Das letzte Stück Musik ist das erste, das sie zusammen gehört haben.",
]

MONTHS = {
    "januar": 1, "februar": 2, "märz": 3, "marz": 3, "april": 4, "mai": 5,
    "juni": 6, "juli": 7, "august": 8, "september": 9, "oktober": 10,
    "november": 11, "dezember": 12,
}

NOSCRIPT_OLD = (
    "<noscript><style>.card{opacity:1;pointer-events:auto;transform:translate(-50%,-50%)}"
    ".opener{display:none}</style></noscript>"
)
NOSCRIPT_NEW = (
    "<noscript><style>.card{opacity:1;pointer-events:auto;position:relative;left:auto;top:auto;"
    "transform:none;margin:6vh auto 0}.opener{display:none}.folio{display:block}"
    ".panel{opacity:1;transform:none}.scratch canvas{display:none}</style></noscript>"
)


def text_of(html, cls):
    match = re.search(rf'class="{cls}"[^>]*>(.*?)</p>', html, re.S)
    if not match:
        raise SystemExit(f"missing .{cls}")
    raw = re.sub(r"<br\s*/?>", " ", match.group(1))
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", raw)).strip()


def names_of(html):
    match = re.search(r"<h1>(.*?)</h1>", html, re.S)
    parts = re.split(r"<i>.*?</i>", match.group(1))
    clean = [re.sub(r"<[^>]+>", "", part).strip() for part in parts]
    return clean[0], clean[1]


def when_stamp(when):
    match = re.search(r"(\d{1,2})\.\s+(\w+)\s+(\d{4})", when)
    clock = re.search(r"(\d{1,2}):(\d{2})", when)
    month = MONTHS[match.group(2).lower()]
    hour = int(clock.group(1)) if clock else 17
    minute = int(clock.group(2)) if clock else 0
    return f"{int(match.group(3)):04d}-{month:02d}-{int(match.group(1)):02d}T{hour:02d}:{minute:02d}"


def folio_for(n, a, b, where, when, dress):
    history = (
        f"{a} und {b} {MEET[(n * 3) % len(MEET)]}. "
        f"{PLACE[where]} {TURN[n % len(TURN)]}"
    )
    secret = f"{a} und {b}: {SECRET[n % len(SECRET)]}"
    practical = PRACTICAL[where]
    stamp = when_stamp(when)
    return f"""
    <div class="folio" data-when="{stamp}">
      <section class="panel hero in" aria-label="Bis zum Abend">
        <p class="kicker">Bis zum Abend</p>
        <p class="count">
          <span data-unit="days"><b>0</b><small>Tage</small></span>
          <span data-unit="hours"><b>0</b><small>Stunden</small></span>
          <span data-unit="minutes"><b>0</b><small>Minuten</small></span>
        </p>
        <p class="gesture">Nach oben wischen <i></i></p>
      </section>
      <section class="panel history">
        <p class="kicker">Geschichte</p>
        <h2>Wie es anfing</h2>
        <p class="story">{escape(history)}</p>
      </section>
      <section class="panel dresscode">
        <p class="kicker">Kleider</p>
        <h2>Was ihr tragt</h2>
        <p class="dress-line">{escape(dress)}</p>
        <p class="practical">{escape(practical)}</p>
        <p class="wear">Ihr müsst nichts Neues kaufen. Kommt so, dass ihr bis zum letzten Lied bleibt.</p>
      </section>
      <section class="panel surprise">
        <p class="kicker">Überraschung</p>
        <h2>Unter dem Gold</h2>
        <p class="lead">Eine Geste mit dem Finger. Das Gold gibt den Satz frei.</p>
        <div class="scratch">
          <p class="secret">{escape(secret)}</p>
          <canvas aria-hidden="true"></canvas>
        </div>
        <button class="reveal-secret" type="button">Lieber aufdecken</button>
      </section>
      <section class="panel rsvp">
        <p class="kicker">Antwort</p>
        <h2>Kommt ihr?</h2>
        <div class="choices">
          <button type="button" data-answer="yes">Wir kommen</button>
          <button type="button" data-answer="no">Wir können nicht</button>
        </div>
        <div class="party" hidden>
          <p class="ask">Wie viele Personen kommen? Jede mit Namen.</p>
          <div class="stepper">
            <button type="button" data-step="-1" aria-label="Eine Person weniger">−</button>
            <b data-amount>1</b>
            <button type="button" data-step="1" aria-label="Eine Person mehr">+</button>
          </div>
          <div class="names"></div>
        </div>
        <p class="tally" aria-live="polite"><b data-live-count>—</b><span data-live-label>Noch keine Antwort</span></p>
        <p class="hint">Nur auf diesem Gerät gespeichert. Keine E-Mail.</p>
      </section>
      <footer class="panel foot">
        <p class="kicker">Dieser Abend</p>
        <p class="where-line">{escape(where)}</p>
        <p class="until" data-until>Noch ein paar Tage.</p>
        <p class="coming">Noch keine Antwort auf diesem Gerät.</p>
        <p class="note">Namen, Tag und Ort sind Beispiele.</p>
      </footer>
      <p class="nudge">Nach oben wischen <i></i></p>
    </div>
"""


def main():
    pages = sorted(ROOT.glob("*/index.html"))
    histories = []
    for path in pages:
        n = int(path.parent.name.split("-", 1)[0])
        html = path.read_text()
        html = html.replace("invite.css?v=8", "invite.css?v=9")
        html = html.replace("luxury.css?v=8", "luxury.css?v=9")
        html = html.replace('src="../invite.js"', 'src="../invite.js?v=9"')
        if NOSCRIPT_OLD in html:
            html = html.replace(NOSCRIPT_OLD, NOSCRIPT_NEW)
        if 'class="folio"' not in html:
            a, b = names_of(html)
            where = text_of(html, "where")
            when = text_of(html, "when")
            dress = text_of(html, "detail dress")
            if where not in PLACE or where not in PRACTICAL:
                raise SystemExit(f"unknown place {where} in {path}")
            block = folio_for(n, a, b, where, when, dress)
            html = html.replace("</article>", "</article>" + block, 1)
            histories.append(block)
        path.write_text(html)
    print(f"pages {len(pages)} stories {len(histories)} unique {len(set(histories))}")


if __name__ == "__main__":
    main()
