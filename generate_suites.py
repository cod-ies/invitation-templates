"""Original stationery suites. Craft follows cards sold above €100 / $100. Not copies."""
from pathlib import Path

ROOT = Path("/Users/tariqsaeed/Downloads/invitation-templates")

FAMILIES = [
    ("band", "Bauchbinde", "Ein Band aus Folie hält die Karte, dann gibt es nach."),
    ("vellum", "Pergament", "Ein Pergamentblatt hebt sich vom Brief."),
    ("gate", "Torfalz", "Zwei Klappen öffnen sich am Falz."),
    ("ribbon", "Seidenband", "Das Band löst sich vom Kreuz."),
    ("deckle", "Bütten", "Die Büttenkarte dreht sich aus der Prägung."),
    ("roma", "Brief", "Der gefaltete Brief öffnet seine Klappe."),
    ("laser", "Laserschnitt", "Das geschnittene Fenster gibt den Blick frei."),
    ("pocket", "Tasche", "Die Karte gleitet aus der Tasche."),
    ("blind", "Blindprägung", "Die stille Prägung weicht dem Text."),
    ("gilt", "Farbschnitt", "Die Karte dreht sich aus der goldenen Kante."),
]
TONES = ["olive", "champagne", "velvet", "copper", "newport", "blush", "peach", "forest", "ink"]
FONTS = {
    "olive": "Cormorant+Garamond:ital,wght@0,500;0,600;1,500",
    "peach": "Cormorant+Garamond:ital,wght@0,500;0,600;1,500",
    "champagne": "Cinzel:wght@500;600",
    "velvet": "Italiana",
    "copper": "Bodoni+Moda:ital,opsz,wght@0,6..96,500;1,6..96,500",
    "ink": "Bodoni+Moda:ital,opsz,wght@0,6..96,500;1,6..96,500",
    "newport": "Libre+Baskerville:ital,wght@0,400;1,400",
    "blush": "Fraunces:ital,opsz,wght@0,9..144,500;1,9..144,500",
    "forest": "Newsreader:ital,opsz,wght@0,6..72,500;1,6..72,500",
}
FIRST = ["Ada","Anselm","Bea","Benno","Cara","Caspar","Dora","Emil","Enna","Finn","Greta","Hugo","Ida","Jona","Kira","Levin","Mara","Nils","Oda","Piet","Rosa","Sven","Thea","Urs","Vera","Wanja","Ylva","Arno","Bente","Clio","Dalia","Erik","Felia","Gero","Hanna","Ivo","Jette","Kian","Lotta","Mats","Nele","Ole","Pia","Quirin","Rune","Siri","Tilde","Uwe","Vita","Wolf"]
SECOND = ["Adler","Berg","Claus","Dahl","Ebn","Falk","Graf","Holm","Irmer","Jost","Kern","Lind","Mohr","Nord","Orth","Pauli","Quart","Reis","Sander","Thal","Ulrich","Voss","Wahl","York","Zahn","Amsel","Bode","Cremer","Dorn","Ehlers","Faber","Grote","Hesse","Imhof","Jahn","Kruse","Lenz","Maier","Neumann","Oster","Preuss","Rabe","Sommer","Tiede","Unger","Vogel","Weber","Xavier","Yildiz","Zorn"]
# 50 x 50 is plenty; pair by index with a stride so names do not repeat a couple
PLACES = [
    ("Im Gutshaus", "Samstag, 15. Mai 2027", "16:00 Uhr"),
    ("An der Alster", "Samstag, 5. Juni 2027", "17:00 Uhr"),
    ("Im Palmenhaus", "Sonntag, 20. Juni 2027", "15:00 Uhr"),
    ("Auf dem Weingut", "Samstag, 11. Juli 2027", "16:30 Uhr"),
    ("Im Stadthaus", "Samstag, 8. August 2027", "17:00 Uhr"),
    ("Am See", "Samstag, 29. August 2027", "18:00 Uhr"),
    ("In der Orangerie", "Samstag, 12. September 2027", "16:00 Uhr"),
    ("Im Atelier", "Sonntag, 3. Oktober 2027", "15:00 Uhr"),
    ("Auf dem Hof", "Samstag, 24. Oktober 2027", "16:00 Uhr"),
    ("Im Wintergarten", "Samstag, 14. November 2027", "17:00 Uhr"),
]
PHOTOS = [
    "01-sonnengold/couple.jpg",
    "02-elfenbein/couple.jpg",
    "03-pfingstrose/couple.jpg",
    "04-perle/couple.jpg",
    "05-seeufer/couple.jpg",
    "06-steintreppe/couple.jpg",
    "07-laterne/couple.jpg",
    "08-glashaus/couple.jpg",
    "09-hortensien/couple.jpg",
    "10-weisser-bogen/couple.jpg",
]
PHOTO_FAMILIES = {"laser", "pocket", "gilt", "roma", "ribbon"}

CRAFTS = {
    "01-sonnengold": "Folienprägung · Briefumschlag",
    "02-elfenbein": "Wachssiegel · Blüten",
    "03-pfingstrose": "Torfalz",
    "04-perle": "Blindprägung · Iris",
    "05-seeufer": "Farbschnitt · Horizont",
    "06-steintreppe": "Wappen · Siegel",
    "07-laterne": "Seidenband · Laterne",
    "08-glashaus": "Laserschnitt",
    "09-hortensien": "Bogen · Siegel",
    "10-weisser-bogen": "Pergament · Ring",
}

PAGE = """<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family={font}&family=Outfit:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../invite.css?v=5">
  <link rel="stylesheet" href="../luxury.css?v=6">
  <script>if (matchMedia("(prefers-reduced-motion: reduce)").matches) document.documentElement.classList.add("reduce");</script>
  <noscript><style>.card{{opacity:1;pointer-events:auto;transform:translate(-50%,-50%)}}.opener{{display:none}}</style></noscript>
</head>
<body>
  <main class="stage" data-invite="{family}" data-tone="{tone}" style="--portrait:url('{photo}')">
    <div class="opener">
      {mech}
    </div>
    <article class="card">
      <p class="eyebrow">Vorlage · {label}</p>
      {medallion}
      <p class="invite-line">ihr seid eingeladen</p>
      <h1>{a}<i>&amp;</i>{b}</h1>
      <div class="rule"></div>
      <p class="when">{day}<br>{time}</p>
      <p class="where">{place}</p>
      <p class="craft">{craft}</p>
      <p class="note">Namen, Tag und Ort sind Beispiele. Das Handwerk ist eigenes, nach Suiten über 100 Euro.</p>
    </article>
  </main>
  <script src="../invite.js"></script>
</body>
</html>
"""

def seal(initial):
    return f"""<div class="seal-wrap"><button class="seal" type="button" aria-expanded="false" aria-label="Öffnet das Siegel"><span class="wax"><b>{initial}</b></span><span class="hint">Öffnet das Siegel</span></button></div>"""

def mechanism(family, a, b, photo):
    mark = f"{a[0]}<span>{b[0]}</span>"
    s = seal(a[0])
    if family == "band":
        return f'<div class="sheet"><p class="pressed">{mark}</p><div class="band">{s}</div></div>'
    if family == "vellum":
        return f'<div class="sheet"><p class="pressed">{mark}</p></div><div class="vellum"><p>ihr seid eingeladen</p>{s}</div>'
    if family == "gate":
        return f'<div class="gatebox"><div class="panel left">{a[0]}</div><div class="panel right">{b[0]}</div>{s}</div>'
    if family == "ribbon":
        return f'<div class="sheet"><p class="pressed">{mark}</p></div><i class="ribbon h"></i><i class="ribbon v"></i>{s}'
    if family == "deckle":
        return f'<div class="sheet"><p class="pressed">{mark}</p>{s}</div>'
    if family == "roma":
        return f'<div class="sheet">{seal and ""}<div class="roma-flap"></div>{s}</div>'
    if family == "laser":
        return f'<div class="sheet"><div class="window"></div>{s}</div>'
    if family == "pocket":
        return f'<div class="pocket"><img class="peek" src="../{photo}" alt=""><div class="pocket-face"></div>{s}</div>'
    if family == "blind":
        return f'<div class="sheet"><p class="pressed">{mark}</p>{s}</div>'
    if family == "gilt":
        return f'<div class="slab">{s}</div>'
    raise ValueError(family)

def main():
    for folder, craft in CRAFTS.items():
        path = ROOT / folder / "index.html"
        text = path.read_text(encoding="utf-8")
        text = text.replace("../invite.css?v=4", "../invite.css?v=5")
        needle = "</p>\n      <p class=\"invite-line\">"
        insert = f"</p>\n      <p class=\"craft\">{craft}</p>\n      <p class=\"invite-line\">"
        if "class=\"craft\"" not in text:
            text = text.replace(needle, insert, 1)
        path.write_text(text, encoding="utf-8")

    cards = []
    n = 11
    pair = 0
    for family, label, _ in FAMILIES:
        for tone in TONES:
            a = FIRST[pair % len(FIRST)]
            b = SECOND[(pair * 7) % len(SECOND)]
            pair += 1
            place, day, time = PLACES[pair % len(PLACES)]
            photo = PHOTOS[pair % len(PHOTOS)]
            slug = f"{n:03d}-{family}-{tone}"
            title = f"{a} & {b} — {label}"
            medallion = f'<img class="medallion" src="../{photo}" alt="">' if family in PHOTO_FAMILIES else ""
            html = PAGE.format(
                title=title, font=FONTS[tone], family=family, tone=tone, photo=photo,
                mech=mechanism(family, a, b, photo), label=label, medallion=medallion,
                a=a, b=b, day=day, time=time, place=place, craft=label,
            )
            folder = ROOT / slug
            folder.mkdir(parents=True, exist_ok=True)
            (folder / "index.html").write_text(html, encoding="utf-8")
            swatch = tone
            cards.append((slug, a, b, label, swatch, family))
            n += 1

    originals = [
        ("01-sonnengold/", "Mira", "Elias", "Sonnengold", "01-sonnengold/couple.jpg", "center 28%", "foto"),
        ("02-elfenbein/", "Clara", "Henrik", "Elfenbein", "02-elfenbein/couple.jpg", "center 20%", "foto"),
        ("03-pfingstrose/", "Lina", "Matteo", "Pfingstrose", "03-pfingstrose/couple.jpg", "center 30%", "foto"),
        ("04-perle/", "Amelie", "Adrian", "Perle", "04-perle/couple.jpg", "center 24%", "foto"),
        ("05-seeufer/", "Nora", "Julian", "Seeufer", "05-seeufer/couple.jpg", "center 34%", "foto"),
        ("06-steintreppe/", "Sophie", "Leon", "Steintreppe", "06-steintreppe/couple.jpg", "center 40%", "foto"),
        ("07-laterne/", "Emma", "Paul", "Laterne", "07-laterne/couple.jpg", "center 22%", "foto"),
        ("08-glashaus/", "Freya", "Nico", "Glashaus", "08-glashaus/couple.jpg", "center 26%", "foto"),
        ("09-hortensien/", "Ida", "Felix", "Hortensien", "09-hortensien/couple.jpg", "center 36%", "foto"),
        ("10-weisser-bogen/", "Marie", "Anton", "Weißer Bogen", "10-weisser-bogen/couple.jpg", "center 30%", "foto"),
    ]
    bits = []
    for href, a, b, label, img, pos, kind in originals:
        bits.append(f"""<a class="project" href="{href}" data-kind="{kind}"><div class="frame"><img src="{img}" alt="" style="object-position:{pos}"><span class="tag">{label}</span></div><div class="body"><h2>{a} &amp; {b}</h2><p class="open">Siegel öffnen</p></div></a>""")
    tone_color = {
        "olive": "#6e7640", "champagne": "#c6a15a", "velvet": "#1e4d34", "copper": "#b87333",
        "newport": "#3d6f86", "blush": "#e0b0b8", "peach": "#e0b090", "forest": "#2c4a38", "ink": "#161616",
    }
    for slug, a, b, label, tone, family in cards:
        bits.append(
            f"""<a class="project" href="{slug}/" data-kind="{family}"><div class="frame paper" style="--swatch:{tone_color[tone]}"><b>{a[0]}&amp;{b[0]}</b><span class="tag">{label}</span></div><div class="body"><h2>{a} &amp; {b}</h2><p class="open">Siegel öffnen</p></div></a>"""
        )

    gallery = f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>FeierLink · 100 Vorlagen</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Outfit:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {{ --ink:#2c261f; --muted:#6f655c; --line:#e4d9cc; --paper:#f7f1ea; --card:#fffdfb; }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; min-height:100vh; background:radial-gradient(900px 420px at 10% -10%, #fff 0%, transparent 60%), var(--paper); color:var(--ink); font-family:Outfit,sans-serif; }}
    a {{ color:inherit; }}
    .wrap {{ max-width:1180px; margin:0 auto; padding:36px 22px 80px; }}
    .brand {{ font-family:"Cormorant Garamond",Georgia,serif; font-size:34px; font-weight:600; letter-spacing:-0.03em; }}
    .brand span {{ display:block; margin-top:4px; font-family:Outfit,sans-serif; font-size:13px; font-weight:500; letter-spacing:0.16em; text-transform:uppercase; color:var(--muted); }}
    .lede {{ max-width:40em; margin:28px 0 0; font-size:18px; line-height:1.5; color:var(--muted); }}
    .filters {{ display:flex; flex-wrap:wrap; gap:8px; margin-top:22px; }}
    .filters button {{ border:1px solid var(--line); background:#fff; border-radius:999px; padding:8px 12px; cursor:pointer; }}
    .filters button[aria-pressed="true"] {{ background:var(--ink); color:#fff; }}
    .projects {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(200px,1fr)); gap:16px; margin-top:22px; }}
    .project {{ display:flex; flex-direction:column; background:var(--card); border:1px solid var(--line); border-radius:18px; overflow:hidden; text-decoration:none; }}
    .project[hidden] {{ display:none; }}
    .frame {{ position:relative; aspect-ratio:3/4; overflow:hidden; background:#efe8dc; }}
    .frame img {{ width:100%; height:100%; object-fit:cover; display:block; }}
    .paper {{ display:grid; place-items:center; background:radial-gradient(circle at 30% 20%, #fff, transparent 45%), var(--swatch); color:#fff; font-family:"Cormorant Garamond",Georgia,serif; font-size:42px; }}
    .tag {{ position:absolute; left:10px; bottom:10px; padding:5px 8px; border-radius:999px; font-size:10px; letter-spacing:.14em; text-transform:uppercase; background:rgba(255,253,251,.92); color:var(--ink); font-family:Outfit,sans-serif; }}
    .body {{ padding:14px 14px 16px; }}
    h2 {{ margin:0; font-family:"Cormorant Garamond",Georgia,serif; font-weight:500; font-size:28px; letter-spacing:-0.03em; }}
    .open {{ margin:6px 0 0; font-weight:600; font-size:14px; }}
  </style>
</head>
<body>
  <main class="wrap">
    <div class="brand">FeierLink<span>100 Vorlagen</span></div>
    <p class="lede">Eigene Karten nach dem Handwerk von Suiten, die über 100 Euro oder Dollar liegen: Letterpress, Bütten, Folie, Pergament, Band, Farbschnitt und Siegel. Keine Kopie einer Druckerei. Namen sind Beispiele.</p>
    <div class="filters" role="toolbar" aria-label="Filter">
      <button type="button" aria-pressed="true" data-filter="all">Alle 100</button>
      <button type="button" data-filter="foto">Foto</button>
      <button type="button" data-filter="band">Bauchbinde</button>
      <button type="button" data-filter="vellum">Pergament</button>
      <button type="button" data-filter="deckle">Bütten</button>
      <button type="button" data-filter="gilt">Farbschnitt</button>
      <button type="button" data-filter="laser">Laserschnitt</button>
      <button type="button" data-filter="pocket">Tasche</button>
    </div>
    <section class="projects" aria-label="Vorlagen">
      {''.join(bits)}
    </section>
  </main>
  <script>
    document.querySelector(".filters").addEventListener("click", function (event) {{
      var button = event.target.closest("button");
      if (!button) return;
      var kind = button.getAttribute("data-filter");
      document.querySelectorAll(".filters button").forEach(function (item) {{
        item.setAttribute("aria-pressed", item === button ? "true" : "false");
      }});
      document.querySelectorAll(".project").forEach(function (card) {{
        card.hidden = kind !== "all" && card.getAttribute("data-kind") !== kind;
      }});
    }});
  </script>
</body>
</html>
"""
    (ROOT / "index.html").write_text(gallery, encoding="utf-8")
    print("suites", len(cards), "total", 10 + len(cards))

if __name__ == "__main__":
    main()
