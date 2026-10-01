# 📋 Portanova Privatschule – Projekt-Log

> Letzte Aktualisierung: 01.10.2026
> Diese Datei dokumentiert alles, was bisher an der Website gemacht wurde, damit du es jederzeit wiederfindest.
> (Ergänzt das technische `CHANGELOG.md` um einen leicht verständlichen Gesamtüberblick.)

---

## 🌐 Das Projekt auf einen Blick

| Was | Wert |
|-----|------|
| **Projekt** | Website der Portanova Privatschule, Feldmeilen ZH (am Zürichsee) |
| **Hauptdatei** | `index.html` (~97 KB, 1'411 Zeilen – HTML, CSS & JavaScript alles inline) |
| **Galerie-Seite** | `galerie.html` (~519 KB, 1'498 Zeilen) |
| **Ordnergröße gesamt** | ca. 276 MB (v. a. Bilder & Video) |
| **Externe Abhängigkeiten** | Google Fonts, `gallery-data.js` |
| **Vorlage/Original** | Inhalte originalgetreu von privatschule.ch übernommen, lokal gehostet |

---

## 🧩 Aufbau der Startseite (`index.html`)

Die Seite ist eine moderne Single-Page mit folgenden Sektionen (Reihenfolge = Navigation):

| # | Sektion | Inhalt |
|---|---------|--------|
| 1 | **Hero** (`#top`) | Video-Hintergrund `Schulhaus.MOV`, Vignette, Play/Pause, Stat-Count-up („8" & „25") |
| 2 | **Aktuelles / News** (`#news`) | Neuigkeiten-Block |
| 3 | **Agenda** (`#agenda`) | Termine, Ferien & Events aus dem ICS-Kalender (32 Termine), „Nächster Termin"-Highlight |
| 4 | **Stimmen** (`#stimmen`) | Zitate / Testimonials |
| 5 | **Angebot** (`#angebot`) | 6 Angebote mit klickbaren Detail-Modals |
| 6 | **Team** (`#team`) | 3D-Flip-Karten: Foto ↔ KI-Bild |
| 7 | **Gebäude** (`#gebaeude`) | Schulhaus-Bild mit Reveal-Animation |
| 8 | **Galerie** (`#galerie`) | Vorschau der Fotoalben → verlinkt auf `galerie.html` |
| 9 | **Weiteres** (`#weiteres`) | Broschüre, Kostenübersicht, Aufnahmeprüfung, Ferienplan |
| 10 | **FAQ** (`#faq`) | Barrierefreies Akkordeon (`<details>`) |
| 11 | **Kontakt** (`#kontakt`) | Kontaktformular (⚠️ sendet noch nicht – siehe To-do) |

**Header:** Escola-Login oben rechts (→ portal-1.escola.ch), „Kontakt aufnehmen"-Button (auch im mobilen Burger-Menü).

---

## 📸 Fotogalerie

| Was | Wert |
|-----|------|
| **Alben** | **31** Fotoalben (z. B. Burgund 25/26, Sportlager Tenero, München-Reise, Wales, Berlin …) |
| **Fotos gesamt** | **688** Bilder in `images/galleries/` |
| **Aufbau-Skripte** | `fetch_albums.py` (lädt Alben von privatschule.ch herunter) · `gen_data.py` (erzeugt die Album-Daten) |
| **Datendateien** | `gallery_manifest.json` (751 Zeilen, Bildliste pro Album) · `gallery-data.js` |
| **Test-/Experimentdateien** | `album_test.html`, `_shot2.html`, `lb_test.png` |

> Die Galerie wurde automatisiert von privatschule.ch gespiegelt: `fetch_albums.py` lädt alle Album-Fotos herunter, `gen_data.py` baut daraus die Datenstruktur für die Anzeige.

---

## 🗂️ Wichtige Dateien & Ordner

```
Portanova Site/
├─ index.html                 ← Hauptseite
├─ galerie.html               ← Galerie-Seite
├─ gallery-data.js            ← Galerie-Daten (von index/galerie genutzt)
├─ gallery_manifest.json      ← Bildliste pro Album
├─ fetch_albums.py            ← Skript: Alben von privatschule.ch laden
├─ gen_data.py                ← Skript: Album-Daten erzeugen
├─ Schulhaus.MOV             ← Hero-Video (29 MB)
├─ CHANGELOG.md               ← technisches Änderungsprotokoll
├─ LOG.md                     ← diese Datei
├─ dokumente/
│   └─ Kostenuebersicht-SJ26-27.pdf
└─ images/                    ← 833 Dateien gesamt
    ├─ angebote/              ← 6 Grafiken der Angebot-Detailseiten
    ├─ broschuere/            ← Schulbroschüre, 24 Seiten (seite-01…24.jpg)
    ├─ galleries/             ← 31 Alben, 688 Fotos
    └─ (Team-Portraits, KI-Bilder, Icons …)
```

---

## ✨ Was bisher gebaut/optimiert wurde (Stand 27.06.2026)

### Hero
- Video `Schulhaus.MOV` als Hintergrund (Autoplay, stumm, Loop, `playsinline`), Poster `images/school-image.jpeg`.
- Filmische Vignette, Play/Pause unten rechts, respektiert `prefers-reduced-motion`.
- Stat-Count-up: „8" und „25" zählen beim Sichtbarwerden hoch.

### Agenda (neu)
- Sektion „Termine, Ferien & Events" aus dem ICS-Kalender von privatschule.ch (32 Termine).
- Zeigt clientseitig nur kommende Termine, kategorisiert (Event / Ferien / Schulfrei), „Nächster Termin"-Highlight.
- „Gesamte Agenda ansehen" klappt alle Termine auf. Live-Sync-Versuch mit Fallback auf statische Daten (CORS).

### Team
- 3D-Flip-Karten: Vorderseite = professionelles Foto, Rückseite = KI-Bild (mit „KI"-Tag). Umdrehen per Klick / Enter / Leertaste.

### Angebot
- Detail-Modals für alle 6 Angebote (Sekundarschule, 6. Klasse, 10. Schuljahr, Gymivorbereitung, Wahlfächer, Kulturschiene) – kompletter Wortlaut + Grafiken.
- Kacheln klickbar, Scale-in-Animation, Escape/Backdrop zum Schliessen.
- Neuer Leitsatz-/„Drama"-Abschnitt in Navy.

### Weiteres (Links & Dokumente)
- **Schulbroschüre:** integrierter Viewer, 24 Seiten lokal (`images/broschuere/`), blättern per Pfeil/Tastatur.
- **Kostenübersicht:** PDF lokal (`dokumente/Kostenuebersicht-SJ26-27.pdf`).
- **Aufnahmeprüfung:** Link zur Kantonsseite (zh.ch). **Ferienplan:** Link zu privatschule.ch.
- **Instagram & Facebook:** offizielle Portanova-Accounts (auch Footer-Icons).

### Header
- Escola-Login (Icon + „Login") → `https://portal-1.escola.ch/escola/login/99`.
- „Kontakt aufnehmen" auch im mobilen Burger-Menü.

### Design / Politur
- Gemeinsame Easing-Variablen, gestaffelte Reveal-Animationen, Button-Press-Feedback, globale Fokus-Ringe.
- Bild-Fade-in beim Lazy-Loading, `prefers-reduced-motion` durchgängig.
- Emojis → einheitliche SVG-Icons. Gold als wiederkehrender Akzent.
- FAQ-Akkordeon, Sticky Mobile-Kontaktleiste („Anrufen" / „Anfrage").
- Wärmeres Off-White (`#fcfcfa`), mehrschichtige Schatten, feine Grain-Textur, Button-Glanz, Scroll-Fortschrittsbalken, vereinheitlichte Radius-Skala.

---

## ✅ Offene Punkte / To-do

- [ ] **Kontaktformular versendet noch nicht** (Demo) – Anbindung an FormSubmit/Formspree/Netlify offen.
      *(Tipp: Beim KI-Camp-Projekt wurde genau das schon mit FormSubmit gelöst – lässt sich hier wiederverwenden.)*
- [ ] **Impressum & Datenschutz** (Footer-Links) noch nicht hinterlegt.
- [ ] **`Schulhaus.MOV` (29 MB) → `.mp4`/H.264** konvertieren für schnelleres Laden.
- [ ] Detailtexte/Grafiken der Angebote werden **manuell** gepflegt (Stand der privatschule.ch-Seiten).
- [ ] Hosting/Live-URL noch nicht festgelegt (Projekt liegt aktuell lokal).

---

## 🗓️ Verlauf

- **24.06.2026** – Hero-Video `Schulhaus.MOV` zum Projekt hinzugefügt.
- **27.06.2026** – Grosser Ausbau (siehe oben): Hero-Video, Agenda-Sektion, Team-Flip-Karten,
  Angebot-Modals, Broschüren-Viewer, Escola-Login, umfangreiche Design-Politur.
- **27.06.2026** – Fotogalerie automatisiert von privatschule.ch gespiegelt (31 Alben, 688 Fotos)
  via `fetch_albums.py` + `gen_data.py`.
- **27.06.2026** – `CHANGELOG.md` (technisches Protokoll) erstellt.
- **01.07.2026** – Dieses Gesamt-Log (`LOG.md`) erstellt.
- **01.10.2026** – **CMS eingebaut** (Decap CMS unter `/admin`): alle Inhalte nach `content/*.json` ausgelagert,
  `index.html` rendert daraus. Start lokal via `start-cms.command`. Anleitung: `CMS-ANLEITUNG.md`.
- **01.10.2026** – **Inhalte mit privatschule.ch abgeglichen** (Stand 01.10.2026):
  News-Text Schulplätze, Spotify-Link auf Folge 1 · Agenda komplett aus Live-Kalender (43 Termine) ·
  Team: Nadine Caplunik, Larissa Spälti, Lovis Friess entfernt; Manuela Otter & Marc Kämpfen neu
  (Marc: noch Platzhalter «Bild folgt», wie live); Daiana «Frei (ehem. Gandossi)»; Rollen Hajo/Carlos/Eva ergänzt ·
  Galerie: 5 neue Alben (93 Fotos → 36 Alben / 781 Fotos) · 3 neue Elternstimmen ·
  Neues Angebot «Gestalterischer Vorkurs» · neue Kostenübersicht SJ 26/27 (Version 23.09.2026, alte in `_backup/`) ·
  Weiteres: Jahrbuch, Texte 6. Klässler:innen, Artikel Treffpunkt (PDFs in `dokumente/`), Tipp 10.
