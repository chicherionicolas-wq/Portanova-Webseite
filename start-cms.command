#!/bin/bash
# Portanova CMS lokal starten: Doppelklick im Finder.
# Website: http://localhost:8080/   ·   CMS: http://localhost:8080/admin/
cd "$(dirname "$0")"
echo "▶ Starte Portanova-CMS … (Fenster offen lassen, zum Beenden ctrl+C drücken)"
npx --yes decap-server &
CMS_PID=$!
python3 -m http.server 8080 &
WEB_PID=$!
trap 'kill $CMS_PID $WEB_PID 2>/dev/null; exit' INT TERM EXIT
sleep 3
open "http://localhost:8080/admin/"
wait
