# 🛠️ Inhalte pflegen – Portanova CMS

Alle Inhalte der Startseite liegen in `content/*.json` und werden im CMS (Decap CMS) bearbeitet.
Die Website liest diese Dateien beim Laden – HTML muss nicht mehr angefasst werden.

## Lokal bearbeiten (jetzt)
1. Im Finder **`start-cms.command`** doppelklicken (beim ersten Mal: Rechtsklick → Öffnen).
2. Der Browser öffnet **http://localhost:8080/admin/** → auf **Login** klicken (lokal ohne Passwort).
3. Inhalte ändern → **Veröffentlichen**. Die Änderung steht sofort in `content/…json`.
4. Website ansehen: **http://localhost:8080/**
5. Beenden: Terminal-Fenster schliessen.

> Die Seite muss über `http://localhost:8080` geöffnet werden – ein Doppelklick auf `index.html` lädt die Inhalte nicht.

## Was wo gepflegt wird
| CMS-Bereich | Datei | Inhalt |
|---|---|---|
| Startseite → News | `content/news.json` | News-Karten (eine hervorheben = gross in Navy) |
| Startseite → Elternstimmen | `content/stimmen.json` | Zitate |
| Startseite → FAQ | `content/faq.json` | Fragen & Antworten |
| Startseite → Weiteres | `content/links.json` | Links & PDFs (Upload nach `dokumente/`) |
| Startseite → Allgemein | `content/allgemein.json` | Hero-Text, Kennzahlen, Leitsatz, Kontaktdaten |
| Agenda | `content/agenda.json` | Termine – vergangene werden automatisch ausgeblendet |
| Angebote | `content/angebote.json` | Kacheln + Detailtext im «Mehr erfahren»-Fenster |
| Team | `content/team.json` | Portrait + KI-Bild (Rückseite) |
| Galerie | `content/galerie.json` | Alben mit Titelbild und Fotos |

Hochgeladene Bilder landen in `images/uploads/`.

## Online gehen (später)
1. Projekt in ein GitHub-Repository hochladen.
2. In `admin/config.yml` unter `backend: repo:` das Repository eintragen.
3. Bei Netlify oder Cloudflare Pages hosten und GitHub-Login für das CMS einrichten
   (z. B. Netlify OAuth oder DecapBridge). Danach können Lehrpersonen unter `deine-domain.ch/admin` einloggen –
   jede Änderung wird als Version gespeichert und die Seite automatisch neu veröffentlicht.

## Hinweise
- `gallery-data.js`, `gen_data.py` und `fetch_albums.py` werden von der Seite nicht mehr verwendet (Galerie läuft über `content/galerie.json`).
- Sicherung vor dem Umbau: `_backup/index.before-cms.html`.
