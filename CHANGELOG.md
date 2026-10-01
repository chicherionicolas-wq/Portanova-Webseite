# Änderungsprotokoll – Portanova Privatschule Website

Alle Änderungen betreffen `index.html` (CSS, HTML und JavaScript sind dort inline integriert),
sofern nicht anders angegeben. Externe Abhängigkeiten: Google Fonts und `gallery-data.js` (bestanden bereits).

---

## 2026-06-27

### Hero
- Video `Schulhaus.MOV` als Hintergrund eingebaut (Autoplay, stumm, Loop, `playsinline`),
  mit `images/school-image.jpeg` als Poster/Fallback.
- Filmische Vignette für Tiefe und Lesbarkeit.
- Play/Pause-Steuerung unten rechts; respektiert `prefers-reduced-motion` (Video pausiert).
- Stat-Count-up: „8" und „25" zählen beim Sichtbarwerden hoch.

### Agenda (neu)
- Neue Sektion „Termine, Ferien & Events", Inhalte aus dem ICS-Kalender von privatschule.ch
  (`calendar.ics`, 32 Termine) ausgelesen.
- Zeigt clientseitig nur kommende Termine, kategorisiert (Event / Ferien / Schulfrei).
- „Nächster Termin"-Highlight oben.
- Button „Gesamte Agenda ansehen" klappt alle kommenden Termine auf (statt externem Link).
- Versucht Live-Sync über relativen ICS-Pfad; Fallback auf statische Daten (CORS).
- Nav-Eintrag „Agenda" in Haupt- und Footer-Navigation.

### Team
- Karten als 3D-Flip-Karten (wie privatschule.ch): Vorderseite = professionelles Foto,
  Rückseite = lustiges KI-Bild (mit „KI"-Tag). Umdrehen per Klick / Enter / Leertaste.
- Hinweis-Chip „Karte anklicken/antippen für ein KI-Bild".

### Angebot
- Detail-Modals für alle 6 Angebote (Sekundarschule, 6. Klasse, 10. Schuljahr,
  Gymivorbereitung, Wahlfächer, Kulturschiene) – kompletter Wortlaut + Grafiken,
  originalgetreu von privatschule.ch übernommen und lokal gehostet.
- Kacheln klickbar mit „Mehr erfahren"-Hinweis (Klick / Tastatur), Modal mit
  Scale-in-Animation, Escape/Backdrop zum Schliessen.
- Neuer Leitsatz-/„Drama"-Abschnitt in Navy zwischen Angebot und Team.

### Weiteres-Links korrekt verknüpft
- Schulbroschüre: integrierter Viewer (24 Seiten lokal in `images/broschuere/`),
  blättern per Pfeil/Tastatur, Seitenzähler, Vorab-Laden der Nachbarseiten.
- Kostenübersicht: PDF lokal gehostet (`dokumente/Kostenuebersicht-SJ26-27.pdf`).
- Aufnahmeprüfung: Link zur offiziellen Kantonsseite (zh.ch).
- Ferienplan: Link zu privatschule.ch/ferienplan.
- Instagram & Facebook: auf die offiziellen Portanova-Accounts umgestellt
  (auch Footer-Icons).

### Header
- Escola-Login oben rechts: Icon (`images/escola-icon.png`) + „Login",
  verlinkt direkt zu `https://portal-1.escola.ch/escola/login/99`.
- „Kontakt aufnehmen"-Button zusätzlich im mobilen Burger-Menü.

### Design / Politur
- Gemeinsame Easing-Variablen (`--ease-out`, `--ease-in-out`).
- Gestaffelte Reveal-Animationen (Stagger pro Container).
- Button-Press-Feedback (`scale(.97)`) und globale Fokus-Ringe (Tastatur).
- Bild-Fade-in beim Lazy-Loading.
- `prefers-reduced-motion` durchgängig respektiert.
- Emojis durch einheitliche SVG-Icons ersetzt (Weiteres, Kontakt, Footer-Social).
- Gold als wiederkehrender Akzent (Anführungszeichen, dunkle Panels).
- FAQ-Akkordeon (barrierefreies `<details>`).
- Sticky Mobile-Kontaktleiste („Anrufen" / „Anfrage").
- Wärmeres Off-White (`#fcfcfa`), mehrschichtige Schatten, feine Grain-Textur.
- Button-Verlauf mit innerem Glanz.
- Scroll-Fortschrittsbalken.
- Radius-Skala vereinheitlicht (`--r-sm` / `--r` / `--r-lg`).

### Korrekturen
- Gebäude-Bild: vom Clip-Path-Reveal auf das zuverlässige Standard-`reveal`
  zurückgestellt (Bild wurde sonst nicht angezeigt).

---

## Neue Dateien / Assets
- `images/broschuere/seite-01.jpg` … `seite-24.jpg` – Schulbroschüre (24 Seiten)
- `images/angebote/` – Grafiken der Angebot-Detailseiten (6 Bilder, ~800 KB)
- `images/escola-icon.png` – Escola-Login-Icon
- `dokumente/Kostenuebersicht-SJ26-27.pdf` – Kostenübersicht (lokal)

## Offen / To-do
- Kontaktformular versendet noch nicht (Demo) – Anbindung an FormSubmit/Formspree/Netlify offen.
- Impressum & Datenschutz (Footer-Links) noch nicht hinterlegt.
- Empfehlung: `Schulhaus.MOV` (29 MB) nach `.mp4` konvertieren für schnelleres Laden.
- Detailtexte/Grafiken der Angebote sind manuell gepflegt (Stand der privatschule.ch-Seiten).
