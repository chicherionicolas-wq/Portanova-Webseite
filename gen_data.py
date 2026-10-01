import json
m=json.load(open("gallery_manifest.json"))
# album order: title, cover (existing homepage cover), slug
albums=[
 ["Burgund 25/26","crop_700x500_0x13_resize_700x525_Burgund-31.jpg","burgund-25-26"],
 ["Fotobox März 2026","crop_700x500_25x0_resize_750x500_IMG_0014_20260320_120555.jpg","fotobox-maerz-2026"],
 ["Portanova Reunion","crop_700x500_25x0_resize_750x500_IMG_0034_20260321_1429481.jpg","portanova-reunion"],
 ["Klassenfotos Schuljahr 25/26","crop_700x500_0x217_resize_700x933_olive1.jpg","klassenfotos-schuljahr-25-26"],
 ["Samichlaus Besuch","crop_700x500_0x217_resize_700x933_IMG_7723.jpg","samichlaus-besuch"],
 ["Sportlager Tenero 2025","crop_700x500_0x13_resize_700x525_PHOTO-2025-08-31-12-17-24.jpg","sportlager-tenero-2025"],
 ["München Kultur- und Sprachreise 2025","crop_700x500_25x0_resize_750x500_DSC07911.jpg","muenchen-kultur-und-sprachreise-2025"],
 ["Schlittschuhlaufen KEK 2024","crop_700x500_0x13_resize_700x525_IMG_8357.jpg","schlittschuhlaufen-kek-2024"],
 ["Klassenfotos Schuljahr 24/25","crop_700x500_94x0_resize_889x500_IMG_7258.jpg","klassenfotos-schuljahr-24-25"],
 ["Sportlager Tenero 24","crop_700x500_0x13_resize_700x525_PHOTO-2024-08-27-13-32-26-41.jpg","sportlager-tenero-24"],
 ["Portanova Schnee- u. Eistage 24","crop_700x500_0x13_resize_700x525_9f4a145f-4fc5-4922-ad9b-62a6bb7a15f4.jpg","portanova-schnee-u-eistage-24"],
 ["Wales 2. Sek Juni 24","crop_700x500_0x13_resize_700x525_Bild-20240616-130716-e69910131.jpg","wales-2-sek-juni-24"],
 ["Weihnachtliches 23","crop_700x500_94x0_resize_889x500_IMG_5052.jpg","weihnachtliches-23"],
 ["Bouldern 6. Klasse Dez 23","crop_700x500_0x13_resize_700x525_D73CDE93-F1B3-4169-AF7A-4E2CD31CEC4D.jpg","bouldern-6-klasse-dez-23"],
 ["Musical «Mamma Mia»","crop_700x500_0x13_resize_700x525_dfe24982-5b4b-456a-ba52-d4e2fc239f07.jpg","musical-mama-mia-projektarbeit-einer-schuelerin"],
 ["Sommerfest 2023","crop_700x500_0x13_resize_700x525_Titel-Sommer.jpg","sommerfest-2023"],
 ["Events Kulturschiene","crop_700x500_0x13_resize_700x525_IMG_0505.jpg","events-kulturschiene"],
 ["Surselva 6. Klasse 22/23","crop_700x500_0x13_resize_700x525_IMG_2946.jpg","surselva-6-klasse-22_23"],
 ["Berlin 1. Sek 22/23","crop_700x500_0x13_resize_700x525_PHOTO-2023-06-16-04-45-47-2.jpg","berlin-1-sek-22_23"],
 ["Atelier 22/23","crop_700x500_0x13_resize_700x525_E4CB47F3-BCE0-42F0-A8FD-350755C4DCD4_1_105_c.jpg","atelier-22_23"],
 ["Bounce Lab 6. Klasse April 23","crop_700x500_0x217_resize_700x933_IMG_1853.jpg","bounce-lab-6-klasse-april-23"],
 ["Opernhaus Workshop Nov 22","crop_700x500_0x13_resize_700x525_UNADJUSTEDNONRAW_thumb_26701.jpg","opernhaus-workshop-u-besuch-6-klasse-nov-22"],
 ["Winterball Dez 22","crop_700x500_94x0_resize_889x500_20220622_130820.jpg","winterball-dez-22"],
 ["Kulturtage","crop_700x500_0x13_resize_700x525_IMG_1106.jpg","kulturtage"],
 ["Iglu Übernachtung & Skitag Davos","crop_700x500_25x0_resize_750x500_Dolder-Kopie.jpg","iglu-uebernachtung-u-skitag-davos-kloster"],
 ["Ballett «On the move» Opernhaus","crop_700x500_0x13_resize_700x525_IMG_1349.jpg","ballett-workshop-und-besuch-on-the-move-opernhaus-zuerich"],
 ["Sprachausflug Neuchâtel","crop_700x500_0x13_resize_700x525_d7b62e10-da3d-4708-a29e-051674c03710.jpg","sprachausflug-neuchatel"],
 ["Sportlager Tenero Sep 22","crop_700x500_25x0_resize_750x500_DSC05258.jpg","sportlager-tenero-sep-22"],
 ["FIFA Museum Zürich","crop_700x500_0x13_resize_700x525_3_Sek-Abend.jpg","fifa-museum-zuerich"],
 ["Süsswasser-Aquarium Aquatis","crop_700x500_94x0_resize_889x500_PHOTO-2024-02-08-12-17-50-2.jpg","suesswasser-aquarium-aquatis"],
 ["Vergangene Schuljahre","crop_700x500_94x0_resize_889x500_PHOTO-2024-02-07-07-25-04-3.jpg","vergangene-schuljahre"],
]
# verify all slugs exist in manifest
miss=[a[2] for a in albums if a[2] not in m]
print("missing slugs:", miss)
with open("gallery-data.js","w",encoding="utf-8") as f:
    f.write("// Auto-generiert: Galerie-Daten (Alben + Fotos)\n")
    f.write("const GALLERY_ALBUMS = "+json.dumps(albums, ensure_ascii=False)+";\n")
    f.write("const GALLERY_PHOTOS = "+json.dumps(m, ensure_ascii=False)+";\n")
print("albums:",len(albums),"| total photos:",sum(len(m[a[2]]) for a in albums))
