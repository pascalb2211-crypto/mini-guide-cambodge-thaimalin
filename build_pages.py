# -*- coding: utf-8 -*-
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
TOTAL_PAGES = 24

TITLES = {
    1: "Couverture",
    2: "Bienvenue au Cambodge",
    3: "Carte du Cambodge",
    4: "Visa et formalites",
    5: "Comment aller au Cambodge",
    6: "Depuis La Reunion",
    7: "Se deplacer au Cambodge",
    8: "Phnom Penh",
    9: "Siem Reap et les temples d'Angkor",
    10: "Sihanoukville et les iles du sud",
    11: "Kep et Kampot",
    12: "Battambang",
    13: "Kampong Thom",
    14: "Ratanakiri et Mondulkiri",
    15: "Koh Ker et Preah Vihear",
    16: "Gastronomie et culture",
    17: "Informations pratiques",
    18: "Itineraires conseilles",
    19: "Bien-etre et experiences insolites",
    20: "Hebergements au Cambodge",
    21: "Internet et eSIM",
    22: "Que mettre dans son sac",
    23: "Kit de survie en khmer",
    24: "Merci et a tres bientot",
}

TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tha&#xEF; Malin &#x2014; Mini-guide Cambodge &#x2014; Page {num}</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background: #0f1115;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    padding: 24px 0;
    font-family: 'Segoe UI', Arial, sans-serif;
  }}
  .page {{
    position: relative;
    width: 100%;
    max-width: 680px;
    aspect-ratio: 1024 / 1536;
    margin: 0 auto;
  }}
  .page img {{
    width: 100%;
    height: 100%;
    display: block;
    object-fit: cover;
    border-radius: 6px;
  }}
  .hotspot {{
    position: absolute;
    text-decoration: none;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    letter-spacing: 0.5px;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
    cursor: pointer;
  }}
  .hotspot:active {{ transform: scale(0.97); }}

  .btn-prev {{
    border-radius: 50px;
    font-size: clamp(13px, 2.1vw, 16px);
    background: rgba(255,255,255,0.12);
    color: #fff;
    border: 1px solid rgba(255,255,255,0.5);
    backdrop-filter: blur(2px);
  }}
  .btn-prev:hover {{ background: rgba(255,255,255,0.22); }}

  .btn-next, .btn-restart {{
    border-radius: 50px;
    font-size: clamp(13px, 2.1vw, 16px);
    background: linear-gradient(135deg, #d35400, #f0955a);
    color: #fff;
    box-shadow: 0 6px 18px rgba(211, 84, 0, 0.45);
  }}
  .btn-next:hover, .btn-restart:hover {{ box-shadow: 0 8px 22px rgba(211, 84, 0, 0.6); }}

  /* Barre de navigation sous l'image (hors illustration, jamais de superposition) */
  .navbar{{display:flex;gap:12px;width:100%;max-width:680px;margin:14px auto 0;padding:0 14px;}}
  .navbar .hotspot{{position:static;width:auto;height:48px;flex:1;}}
  .navbar .btn-prev{{flex:0 0 auto;min-width:140px;}}

  /* Encart infos pratiques complementaires */
  .infobar{{width:100%;max-width:680px;margin:14px auto 0;padding:0 14px;}}
  .infocard{{background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.12);border-radius:12px;padding:14px 16px;color:#fff;}}
  .infocard .infotitle{{font-size:0.8rem;color:#f0955a;text-transform:uppercase;letter-spacing:0.5px;font-weight:700;margin-bottom:8px;}}
  .infocard ul{{list-style:none;padding:0;margin:0;}}
  .infocard li{{font-size:0.85rem;color:#dcd6d0;margin-bottom:6px;padding-left:18px;position:relative;}}
  .infocard li::before{{content:"\\2713";position:absolute;left:0;color:#f0955a;font-weight:700;}}

  /* Encart meteo en temps reel */
  .weatherbar{{display:flex;gap:12px;width:100%;max-width:680px;margin:14px auto 0;padding:0 14px;}}
  .weathercard{{flex:1;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.12);border-radius:12px;padding:12px 14px;color:#fff;text-align:center;}}
  .weathercard .city{{font-size:0.78rem;color:#c9c9c9;text-transform:uppercase;letter-spacing:0.5px;margin-bottom:4px;}}
  .weathercard .temp{{font-size:1.5rem;font-weight:800;color:#f0955a;}}
  .weathercard .desc{{font-size:0.78rem;color:#dcd6d0;margin-top:2px;}}

  /* Liens affilies supplementaires */
  .affiliatebar{{width:100%;max-width:680px;margin:14px auto 0;padding:0 14px;display:flex;flex-direction:column;gap:10px;}}
  .affiliate-extra{{display:block;text-align:center;padding:13px;border-radius:50px;background:linear-gradient(135deg,#d35400,#f0955a);color:#fff;font-weight:700;font-size:0.92rem;text-decoration:none;box-shadow:0 6px 18px rgba(211,84,0,0.45);}}
  .affiliate-extra:hover{{box-shadow:0 8px 22px rgba(211,84,0,0.6);}}

  .btn-affiliate{{background:rgba(255,255,255,0);}}

  /* Convertisseur de devises en temps reel */
  .currencybar{{display:flex;gap:12px;width:100%;max-width:680px;margin:14px auto 0;padding:0 14px;}}
  .currencycard{{flex:1;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.12);border-radius:12px;padding:12px 14px;color:#fff;text-align:center;}}
  .currencycard .pair{{font-size:0.78rem;color:#c9c9c9;text-transform:uppercase;letter-spacing:0.5px;margin-bottom:4px;}}
  .currencycard .rate{{font-size:1.25rem;font-weight:800;color:#f0955a;}}
  .currencybar-note{{width:100%;max-width:680px;margin:6px auto 0;padding:0 14px;color:#8a8a8a;font-size:0.72rem;text-align:center;}}
</style>
<!-- PWA Mini-guide -->
<link rel="manifest" href="manifest.json">
<meta name="theme-color" content="#0f1115">
<link rel="icon" type="image/png" sizes="32x32" href="icons/favicon-32.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Mini-guide Cambodge">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
</head>
<body>

<div class="page">
  <img src="images/page{num}.webp" alt="Mini-guide Tha&#xEF; Malin Cambodge - {title}">
{page_extra}</div>
<div class="navbar">
{nav}
</div>
{extra}
<script src="gate.js"></script>
<script src="pwa.js" data-name="Mini-guide Cambodge" data-slug="cambodge"{banner}></script>
</body>
</html>
"""

EXTRA_BLOCKS = {
    2: """<div class="weatherbar" id="weatherBar">
  <div class="weathercard" id="wCardPhnomPenh">
    <div class="city">Phnom Penh</div>
    <div class="temp">&#x2014;</div>
    <div class="desc">Chargement&#x2026;</div>
  </div>
  <div class="weathercard" id="wCardSiemReap">
    <div class="city">Siem Reap</div>
    <div class="temp">&#x2014;</div>
    <div class="desc">Chargement&#x2026;</div>
  </div>
</div>
<script>
(function () {
  var CITIES = [
    { id: 'wCardPhnomPenh', lat: 11.5564, lon: 104.9282 },
    { id: 'wCardSiemReap', lat: 13.3671, lon: 103.8448 }
  ];

  function weatherLabel(code) {
    if (code === 0) return 'Ciel d\\u00e9gag\\u00e9';
    if (code === 1 || code === 2) return 'Partiellement nuageux';
    if (code === 3) return 'Nuageux';
    if (code === 45 || code === 48) return 'Brumeux';
    if (code >= 51 && code <= 57) return 'Bruine';
    if (code >= 61 && code <= 67) return 'Pluie';
    if (code >= 80 && code <= 82) return 'Averses';
    if (code >= 95) return 'Orage';
    return 'Variable';
  }

  CITIES.forEach(function (c) {
    var url = 'https://api.open-meteo.com/v1/forecast?latitude=' + c.lat + '&longitude=' + c.lon + '&current_weather=true';
    fetch(url)
      .then(function (r) { return r.json(); })
      .then(function (data) {
        var card = document.getElementById(c.id);
        if (!card || !data.current_weather) return;
        var temp = Math.round(data.current_weather.temperature);
        var label = weatherLabel(data.current_weather.weathercode);
        card.querySelector('.temp').textContent = temp + '\\u00b0C';
        card.querySelector('.desc').textContent = label;
      })
      .catch(function () {
        var card = document.getElementById(c.id);
        if (card) card.querySelector('.desc').textContent = 'Indisponible';
      });
  });
})();
</script>
""",
    20: """<div class="affiliatebar">
  <a href="https://www.agoda.com/partners/partnersearch.aspx?pcs=1&cid=1972177" target="_blank" rel="noopener" class="affiliate-extra">&#x1F3E8; Trouver un h&#xE9;bergement sur Agoda</a>
  <a href="https://www.trip.com/?Allianceid=9852508&SID=327644129&trip_sub3=D19106369" target="_blank" rel="noopener" class="affiliate-extra">&#x2708;&#xFE0F; Comparer vols et s&#xE9;jours sur Trip.com</a>
  <a href="https://gyg.me/qSQwVEug" target="_blank" rel="noopener" class="affiliate-extra">&#x1F3DE;&#xFE0F; R&#xE9;server une excursion sur GetYourGuide</a>
</div>
""",
    17: """<div class="currencybar" id="currencyBar">
  <div class="currencycard" id="cCardUsd">
    <div class="pair">1 USD =</div>
    <div class="rate">&#x2014;</div>
  </div>
  <div class="currencycard" id="cCardEur">
    <div class="pair">1 EUR =</div>
    <div class="rate">&#x2014;</div>
  </div>
</div>
<div class="currencybar-note">Taux en temps r&#xE9;el (Riel cambodgien, KHR)</div>
<script>
(function () {
  fetch('https://api.exchangerate-api.com/v4/latest/USD')
    .then(function (r) { return r.json(); })
    .then(function (data) {
      if (!data || !data.rates) return;
      var khrPerUsd = data.rates.KHR;
      var eurPerUsd = data.rates.EUR;
      if (khrPerUsd) {
        var usdCard = document.getElementById('cCardUsd');
        if (usdCard) usdCard.querySelector('.rate').textContent = Math.round(khrPerUsd).toLocaleString('fr-FR') + ' KHR';
      }
      if (khrPerUsd && eurPerUsd) {
        var khrPerEur = khrPerUsd / eurPerUsd;
        var eurCard = document.getElementById('cCardEur');
        if (eurCard) eurCard.querySelector('.rate').textContent = Math.round(khrPerEur).toLocaleString('fr-FR') + ' KHR';
      }
    })
    .catch(function () {
      var bar = document.getElementById('currencyBar');
      if (bar) bar.querySelectorAll('.rate').forEach(function (el) { el.textContent = 'Indisponible'; });
    });
})();
</script>
""",
    12: """<div class="infobar">
  <div class="infocard">
    <div class="infotitle">Infos pratiques Battambang</div>
    <ul>
      <li>Duree recommandee : 2 a 3 jours</li>
      <li>Budget : 15 a 30 USD par jour selon l'hebergement</li>
      <li>Bonus : la ferme de crocodiles, une visite originale en famille</li>
    </ul>
  </div>
</div>
""",
}

def nav_html(n):
    parts = []
    if n > 1:
        parts.append('  <a href="page{0}.html" class="hotspot btn-prev">&#x2190; Pr&#xE9;c&#xE9;dent</a>'.format(n - 1))
    if n < TOTAL_PAGES:
        parts.append('  <a href="page{0}.html" class="hotspot btn-next">Suivant &#x2192;</a>'.format(n + 1))
    else:
        parts.append('  <a href="page1.html" class="hotspot btn-restart">Revenir au d&#xE9;but</a>')
    return "\n".join(parts)

PAGE_EXTRA = {
    1: """  <!-- cover-zones -->
  <a href="page9.html" class="hotspot btn-cover" style="left:2.44%;top:71.94%;width:23.44%;height:18.88%;" aria-label="Temples majestueux"></a>
  <a href="page10.html" class="hotspot btn-cover" style="left:26.86%;top:71.94%;width:22.75%;height:18.88%;" aria-label="Plages paradisiaques"></a>
  <a href="page23.html" class="hotspot btn-cover" style="left:50.49%;top:71.94%;width:23.05%;height:18.88%;" aria-label="Rencontres authentiques"></a>
  <a href="page16.html" class="hotspot btn-cover" style="left:74.41%;top:71.94%;width:23.24%;height:18.88%;" aria-label="Culture fascinante"></a>
  <!-- /cover-zones -->
""",
    21: """  <a href="https://airalo.pxf.io/PzWeQQ" target="_blank" rel="noopener" class="hotspot btn-affiliate" style="left:2%;top:55.5%;width:46%;height:3.4%;"></a>
  <a href="https://holafly.sjv.io/OYdRjN" target="_blank" rel="noopener" class="hotspot btn-affiliate" style="left:52%;top:55.5%;width:46%;height:3.4%;"></a>
""",
    24: """  <a href="https://pascalb2211-crypto.github.io/thai-malin-mini-guide-anime/" target="_blank" rel="noopener" class="hotspot btn-affiliate" style="left:2.3%;top:28%;width:22.9%;height:27.7%;"></a>
  <a href="https://pascalb2211-crypto.github.io/thai-malin-mini-guide-vietnam/" target="_blank" rel="noopener" class="hotspot btn-affiliate" style="left:26.3%;top:28%;width:22.9%;height:27.7%;"></a>
  <a href="https://pascalb2211-crypto.github.io/thai-malin-mini-guide-laos/" target="_blank" rel="noopener" class="hotspot btn-affiliate" style="left:50.2%;top:28%;width:22.9%;height:27.7%;"></a>
  <a href="https://www.facebook.com/share/1aPCoUNWbm/?mibextid=wwXIfr" target="_blank" rel="noopener" class="hotspot btn-affiliate" style="left:13.8%;top:62%;width:11.4%;height:7%;"></a>
""",
}

def build(n):
    title = TITLES.get(n, "Page {0}".format(n))
    extra = EXTRA_BLOCKS.get(n, "")
    page_extra = PAGE_EXTRA.get(n, "")
    html = TEMPLATE.format(num=n, title=title, nav=nav_html(n), extra=extra, page_extra=page_extra, banner=(' data-banner="1"' if n == 1 else ''))
    path = os.path.join(OUT_DIR, "page{0}.html".format(n))
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path

if __name__ == "__main__":
    import sys
    nums = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else list(range(1, TOTAL_PAGES + 1))
    for n in nums:
        p = build(n)
        print("built", p)
