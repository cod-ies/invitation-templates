from pathlib import Path

ROOT = Path("/Users/tariqsaeed/Downloads/invitation-templates")

SUN = """<svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="8" fill="none" stroke="currentColor" stroke-width="2.4"/><g stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M32 10v8M32 46v8M10 32h8M46 32h8M16 16l6 6M42 42l6 6M48 16l-6 6M22 42l-6 6"/></g></svg>"""
ROSE = """<svg viewBox="0 0 64 64" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2.2" d="M32 46c0-8 6-12 6-18a6 6 0 0 0-12 0c0 6 6 10 6 18z"/><circle cx="32" cy="26" r="3" fill="currentColor"/></svg>"""
CLASP = """<svg viewBox="0 0 64 64" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2.4" d="M18 32h28M32 18v28"/><circle cx="32" cy="32" r="14" fill="none" stroke="currentColor" stroke-width="2.2"/></svg>"""
PEARL = """<svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="10" fill="currentColor" opacity=".9"/><circle cx="32" cy="32" r="18" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>"""
HORIZON = """<svg viewBox="0 0 64 64" aria-hidden="true"><path fill="currentColor" d="M12 38h40v3H12z"/><path fill="currentColor" d="M32 14a12 12 0 0 0 0 24 14 14 0 0 1 0-24z"/></svg>"""
CREST = """<svg viewBox="0 0 64 64" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2.2" d="M32 10 50 18v16c0 12-8 18-18 22C22 52 14 46 14 34V18z"/><path stroke="currentColor" stroke-width="2" d="M32 24v16M26 32h12"/></svg>"""
LANTERN = """<svg viewBox="0 0 64 64" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2.2" d="M26 14h12M32 14v6M22 22h20v22H22zM26 44l-2 8h16l-2-8"/></svg>"""
LEAF = """<svg viewBox="0 0 64 64" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2.2" d="M18 46c12-2 28-16 28-30-14 0-28 16-28 30z"/><path stroke="currentColor" stroke-width="2" d="M22 42c8-8 14-14 20-18"/></svg>"""
ARCH = """<svg viewBox="0 0 64 64" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2.2" d="M16 50V30a16 16 0 0 1 32 0v20"/></svg>"""
RING = """<svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="12" fill="none" stroke="currentColor" stroke-width="2.4"/><circle cx="32" cy="32" r="4" fill="currentColor"/></svg>"""

PAGES = [
    dict(slug="01-sonnengold", invite="sun", font="Cormorant+Garamond:ital,wght@0,500;0,600;1,500", title="Mira & Elias — Sonnengold", names=("Mira", "Elias"), when="Samstag, 20. Juni 2027<br>17:00 Uhr", where="Rosengarten am Abend", label="Sonnengold", icon=SUN, focus="center 28%",
         mech="""<div class="mech env"><div class="env-body"></div><div class="env-flap"></div></div>"""),
    dict(slug="02-elfenbein", invite="ivory", font="Fraunces:ital,opsz,wght@0,9..144,500;1,9..144,500", title="Clara & Henrik — Elfenbein", names=("Clara", "Henrik"), when="Sonntag, 4. Juli 2027<br>15:00 Uhr", where="Weißer Garten", label="Elfenbein", icon=ROSE, focus="center 20%",
         mech="""<div class="mech petals" aria-hidden="true"><i style="--i:0"></i><i style="--i:1"></i><i style="--i:2"></i><i style="--i:3"></i><i style="--i:4"></i><i style="--i:5"></i><i style="--i:6"></i><i style="--i:7"></i><i style="--i:8"></i><i style="--i:9"></i></div>"""),
    dict(slug="03-pfingstrose", invite="doors", font="Instrument+Serif:ital@0;1", title="Lina & Matteo — Pfingstrose", names=("Lina", "Matteo"), when="Samstag, 15. August 2027<br>16:00 Uhr", where="Laube der Pfingstrosen", label="Pfingstrose", icon=CLASP, focus="center 30%",
         mech="""<div class="mech"><div class="door left"></div><div class="door right"></div></div>"""),
    dict(slug="04-perle", invite="pearl", font="Libre+Baskerville:ital,wght@0,400;1,400", title="Amelie & Adrian — Perle", names=("Amelie", "Adrian"), when="Sonntag, 6. September 2027<br>15:30 Uhr", where="An der Blütenwand", label="Perle", icon=PEARL, focus="center 24%",
         mech="""<div class="mech iris"></div>"""),
    dict(slug="05-seeufer", invite="lake", font="Playfair+Display:ital,wght@0,500;1,500", title="Nora & Julian — Seeufer", names=("Nora", "Julian"), when="Samstag, 12. September 2027<br>18:00 Uhr", where="Am Seeufer", label="Seeufer", icon=HORIZON, focus="center 34%",
         mech="""<div class="mech"><div class="half top"></div><div class="half bottom"></div></div>"""),
    dict(slug="06-steintreppe", invite="stairs", font="Cinzel:wght@500;600", title="Sophie & Leon — Steintreppe", names=("Sophie", "Leon"), when="Samstag, 3. Oktober 2027<br>16:00 Uhr", where="Auf der Steintreppe", label="Steintreppe", icon=CREST, focus="center 40%",
         mech="""<div class="mech strips"><div class="strip"></div><div class="strip"></div><div class="strip"></div><div class="strip"></div></div>"""),
    dict(slug="07-laterne", invite="city", font="Bodoni+Moda:ital,opsz,wght@0,6..96,500;1,6..96,500", title="Emma & Paul — Laterne", names=("Emma", "Paul"), when="Samstag, 18. Oktober 2027<br>17:30 Uhr", where="Im Laternenhof", label="Laterne", icon=LANTERN, focus="center 22%",
         mech="""<div class="mech"><div class="col left"></div><div class="col right"></div></div>"""),
    dict(slug="08-glashaus", invite="glass", font="Newsreader:ital,opsz,wght@0,6..72,500;1,6..72,500", title="Freya & Nico — Glashaus", names=("Freya", "Nico"), when="Samstag, 2. Mai 2027<br>15:00 Uhr", where="Im Glashaus", label="Glashaus", icon=LEAF, focus="center 26%",
         mech="""<div class="mech panes"><div class="pane"></div><div class="pane"></div><div class="pane"></div><div class="pane"></div></div>"""),
    dict(slug="09-hortensien", invite="arch", font="Italiana", title="Ida & Felix — Hortensien", names=("Ida", "Felix"), when="Samstag, 22. Mai 2027<br>16:00 Uhr", where="Auf dem Hortensienweg", label="Hortensien", icon=ARCH, focus="center 36%",
         mech="""<div class="mech arch"><div class="door left"></div><div class="door right"></div></div>"""),
    dict(slug="10-weisser-bogen", invite="ring", font="Cormorant+Garamond:ital,wght@0,500;0,600;1,500", title="Marie & Anton — Weißer Bogen", names=("Marie", "Anton"), when="Samstag, 8. Juni 2027<br>15:00 Uhr", where="Unter dem weißen Bogen", label="Weißer Bogen", icon=RING, focus="center 30%",
         mech="""<div class="mech"><div class="burst"></div><div class="burst late"></div></div>"""),
]

TEMPLATE = """<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family={font}&family=Outfit:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../invite.css?v=4">
  <style>
    .env-flap, .door, .iris, .half, .strip, .col, .pane {{ background-image: url("couple.jpg"); }}
  </style>
  <script>if (matchMedia("(prefers-reduced-motion: reduce)").matches) document.documentElement.classList.add("reduce");</script>
  <noscript><style>.card{{opacity:1;pointer-events:auto;transform:translate(-50%,-50%)}}.opener{{display:none}}</style></noscript>
</head>
<body>
  <main class="stage" data-invite="{invite}" style="--photo:url('couple.jpg');--focus:{focus}">
    <img class="photo-bg" src="couple.jpg" alt="">
    <div class="opener">
      {mech}
      <div class="seal-wrap">
        <button class="seal" type="button" aria-expanded="false" aria-label="Öffnet das Siegel">
          <span class="wax">{icon}</span>
          <span class="hint">Öffnet das Siegel</span>
        </button>
      </div>
    </div>
    <article class="card">
      <p class="eyebrow">Vorlage · {label}</p>
      <p class="invite-line">ihr seid eingeladen</p>
      <h1>{a}<i>&amp;</i>{b}</h1>
      <div class="rule"></div>
      <p class="when">{when}</p>
      <p class="where">{where}</p>
      <p class="note">Namen, Tag und Ort sind Beispiele für diese Vorlage.</p>
    </article>
  </main>
  <script src="../invite.js"></script>
</body>
</html>
"""

for page in PAGES:
    a, b = page["names"]
    html = TEMPLATE.format(a=a, b=b, **page)
    path = ROOT / page["slug"] / "index.html"
    path.write_text(html, encoding="utf-8")
    print(path)

# gallery
cards = []
for page in PAGES:
    a, b = page["names"]
    cards.append(f"""
      <a class="project" href="{page['slug']}/">
        <div class="frame"><img src="{page['slug']}/couple.jpg" alt="" style="object-position:{page['focus']}"><span class="tag">{page['label']}</span></div>
        <div class="body"><h2>{a} &amp; {b}</h2><p class="open">Siegel öffnen</p></div>
      </a>""")

gallery = f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>FeierLink · Vorlagen</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Outfit:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {{ --ink:#2c261f; --muted:#6f655c; --line:#e4d9cc; --paper:#f7f1ea; --card:#fffdfb; }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; min-height:100vh; background:radial-gradient(900px 420px at 10% -10%, #fff 0%, transparent 60%), var(--paper); color:var(--ink); font-family:Outfit,sans-serif; }}
    a {{ color:inherit; }}
    .wrap {{ max-width:1080px; margin:0 auto; padding:36px 22px 80px; }}
    .brand {{ font-family:"Cormorant Garamond",Georgia,serif; font-size:34px; font-weight:600; letter-spacing:-0.03em; }}
    .brand span {{ display:block; margin-top:4px; font-family:Outfit,sans-serif; font-size:13px; font-weight:500; letter-spacing:0.16em; text-transform:uppercase; color:var(--muted); }}
    .lede {{ max-width:36em; margin:28px 0 0; font-size:18px; line-height:1.5; color:var(--muted); }}
    .projects {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:18px; margin-top:32px; }}
    .project {{ display:flex; flex-direction:column; background:var(--card); border:1px solid var(--line); border-radius:22px; overflow:hidden; text-decoration:none; box-shadow:0 18px 50px rgba(61,44,28,.06); }}
    .project:focus-visible {{ outline:2px solid var(--ink); outline-offset:4px; }}
    .frame {{ position:relative; aspect-ratio:3/4; overflow:hidden; }}
    .frame img {{ width:100%; height:100%; object-fit:cover; display:block; }}
    .tag {{ position:absolute; left:12px; bottom:12px; padding:6px 10px; border-radius:999px; font-size:11px; letter-spacing:.14em; text-transform:uppercase; background:rgba(255,253,251,.92); }}
    .body {{ padding:16px 16px 18px; }}
    h2 {{ margin:0; font-family:"Cormorant Garamond",Georgia,serif; font-weight:500; font-size:32px; letter-spacing:-0.03em; }}
    .open {{ margin:8px 0 0; font-weight:600; }}
  </style>
</head>
<body>
  <main class="wrap">
    <div class="brand">FeierLink<span>Vorlagen</span></div>
    <p class="lede">Zehn Einladungen. Jedes Siegel öffnet anders. Namen und Orte sind Beispiele.</p>
    <section class="projects" aria-label="Vorlagen">
      {''.join(cards)}
    </section>
  </main>
</body>
</html>
"""
(ROOT / "index.html").write_text(gallery, encoding="utf-8")
(ROOT / ".nojekyll").write_text("", encoding="utf-8")
print("gallery")
