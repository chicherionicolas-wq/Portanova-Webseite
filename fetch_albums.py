import urllib.request, re, os, json, ssl
ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
BASE="https://www.privatschule.ch"
slugs="""atelier-22_23 ballett-workshop-und-besuch-on-the-move-opernhaus-zuerich berlin-1-sek-22_23 bouldern-6-klasse-dez-23 bounce-lab-6-klasse-april-23 burgund-25-26 events-kulturschiene fifa-museum-zuerich fotobox-maerz-2026 iglu-uebernachtung-u-skitag-davos-kloster klassenfotos-schuljahr-24-25 klassenfotos-schuljahr-25-26 kulturtage muenchen-kultur-und-sprachreise-2025 musical-mama-mia-projektarbeit-einer-schuelerin opernhaus-workshop-u-besuch-6-klasse-nov-22 portanova-reunion portanova-schnee-u-eistage-24 samichlaus-besuch schlittschuhlaufen-kek-2024 sommerfest-2023 sportlager-tenero-2025 sportlager-tenero-24 sportlager-tenero-sep-22 sprachausflug-neuchatel suesswasser-aquarium-aquatis surselva-6-klasse-22_23 vergangene-schuljahre wales-2-sek-juni-24 weihnachtliches-23 winterball-dez-22""".split()

def get(url):
    req=urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
    return urllib.request.urlopen(req, context=ctx, timeout=30)

os.makedirs("images/galleries", exist_ok=True)
manifest={}
for slug in slugs:
    try:
        html=get(f"{BASE}/galerie/galeriedetail/{slug}").read().decode('utf-8','ignore')
    except Exception as e:
        print("PAGE FAIL", slug, e); continue
    # bases from resize thumbnails (these are exactly the album photos)
    bases=re.findall(r'/temp/resize_\d+x\d+_([^"\']+?\.(?:jpg|jpeg|png))', html, re.I)
    seen=set(); ordered=[]
    for b in bases:
        if b not in seen: seen.add(b); ordered.append(b)
    outdir=f"images/galleries/{slug}"; os.makedirs(outdir, exist_ok=True)
    saved=[]
    for b in ordered:
        dest=os.path.join(outdir,b)
        if os.path.exists(dest) and os.path.getsize(dest)>1000:
            saved.append(b); continue
        ok=False
        for url in (f"{BASE}/resources/{b}", f"{BASE}/temp/resize_320x569_{b}", f"{BASE}/temp/resize_320x240_{b}", f"{BASE}/temp/resize_320x180_{b}"):
            try:
                data=get(url).read()
                if len(data)>1000:
                    open(dest,'wb').write(data); saved.append(b); ok=True; break
            except Exception: pass
        if not ok: print("  imgfail", slug, b)
    manifest[slug]=saved
    print(f"{slug}: {len(saved)} photos")

json.dump(manifest, open("gallery_manifest.json","w"), ensure_ascii=False, indent=1)
total=sum(len(v) for v in manifest.values())
print(f"\nTOTAL PHOTOS: {total} across {len(manifest)} albums")
