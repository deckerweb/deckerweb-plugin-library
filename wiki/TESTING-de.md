# Tests

[English](TESTING.md)

Isolierte Staging-Installationen verwenden, keine Produktion. WordPress-6.4-Basis und aktuellen stabilen Zielstand mit unterstütztem PHP prüfen; native Dateisystem-Installation und repräsentative FTP-/SSH-Hosts. Tatsächliches finales Laufzeit-ZIP im ausgewählten Host testen.

1. Einzelhost und alte/neue Hosts in beiden Reihenfolgen aktivieren: eine kompatible Laufzeit, ein Tab. Inkompatible höhere Versionen und unvollständige Kopien ohne Fatal Error überspringen.
2. Englisch, de_DE und de_DE_formal einschließlich Locale-Wechsel, Hinweis, Einstellungen, Katalog-/Paketfehler und neutraler Beschreibungen prüfen. Host-Domain und Textextraktion kontrollieren.
3. Ohne optionale Online-Abfrage keine entfernten Aufrufe beim Rendern. Quellen, leeren Katalog, Ablehnung, Cache/Backoff und fehlgeschlagene frische Freigabe testen. Ausblenden erhält Schutz und Updates.
4. Originalarchive installieren, separat aktivieren, vorhandene Plugin-Verzeichnisse erhalten. Fehlende/inaktive Abhängigkeiten, Netzwerkkontext und eigener Updater. Nativen Updateweg von älterer Version testen.
5. Übergroße komprimierte Hauptdateien, Gesamtgröße, unsichere Pfade, Symlinks, Duplikate, Identität und Hash prüfen; Fehler ohne Speichererschöpfung. Temporäre Bereinigung bei Erfolg/Fehler kontrollieren.
6. Deaktivierung ohne Datenverlust. Deinstallation mit anderem installierten inaktiven Host, dann letztem Host mit Löschoption aus/an. Fremde Optionen, Plugins und Inhalte erhalten. Netzwerkeinstellungen, alle Netzwerke und neue Websites testen.
7. Tastatur-/Screenreaderprüfung für Labels/Fokus, Dialog öffnen/schließen/Escape/Fokusrückgabe, schmale Ansicht und Kontrast. Browser-/PHP-Logs prüfen.

Builder-Fixtures belegen keine Kompatibilität mit Lizenzinstallationen. Echte Builder und Host-Funktionen vor Host-Veröffentlichung in deren Projekten prüfen. Screenshots blockieren keinen Release.
