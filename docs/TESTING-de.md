# Tests

[English](TESTING.md)

Dies ist eine Prüfliste, keine Liste bereits bestandener Tests. Tatsächliche Ergebnisse stehen im verlinkten Prüfstand.

Isolierte Staging-Installationen verwenden, keine Produktion. WordPress-6.4-Basis und aktuellen stabilen Zielstand mit unterstütztem PHP prüfen; native Dateisystem-Installation und repräsentative FTP-/SSH-Hosts. Tatsächliches finales Laufzeit-ZIP im ausgewählten Host testen.

1. Einzelhost und alte/neue Hosts in beiden Reihenfolgen aktivieren: eine kompatible Laufzeit, ein Tab. Inkompatible höhere Versionen und unvollständige Kopien ohne Fatal Error überspringen.
2. Englisch, de_DE und de_DE_formal einschließlich Locale-Wechsel, Hinweis, Einstellungen, Katalog-/Paketfehler und neutraler Beschreibungen prüfen. Host-Domain und Textextraktion kontrollieren.
3. Ohne optionale Online-Abfrage keine entfernten Aufrufe beim Rendern. Quellen, leeren Katalog, Ablehnung, Cache/Backoff und fehlgeschlagene frische Freigabe testen. Ausblenden erhält Schutz und Updates.
4. Originalarchive installieren, separat aktivieren, vorhandene Plugin-Verzeichnisse erhalten. Fehlende/inaktive Abhängigkeiten, Netzwerkkontext und eigener Updater. Nativen Updateweg von älterer Version testen.
5. Übergroße komprimierte Hauptdateien, Gesamtgröße, unsichere Pfade, Symlinks, Duplikate, Identität und Hash prüfen; Fehler ohne Speichererschöpfung. Temporäre Bereinigung bei Erfolg/Fehler kontrollieren.
6. Deaktivierung ohne Datenverlust. Deinstallation mit anderem installierten inaktiven Host, dann letztem Host mit Löschoption aus/an. Fremde Optionen, Plugins und Inhalte erhalten. Netzwerkeinstellungen, alle Netzwerke und neue Websites testen.
7. Tastatur-/Screenreaderprüfung für Labels/Fokus, Dialog öffnen/schließen/Escape/Fokusrückgabe, schmale Ansicht und Kontrast. Browser-/PHP-Logs prüfen.

Builder-Fixtures belegen keine Kompatibilität mit Lizenzinstallationen. Echte Builder und Host-Funktionen vor Host-Veröffentlichung in deren Projekten prüfen. Screenshots blockieren keinen Release.

[Tatsächlicher Prüfstand für 1.2.0](VALIDATION-1.2.0-de.md).

Sechs Statusmodi, Benutzerspeicherung, kombinierte Filter, Trefferzahl, Zurücksetzen mit erhaltener Sortierung/Zufallsfolge, Statusaktualisierung/Fokus nach Aktionen und mobile kompakte Bedienung einschließen. Fehlerstufen ohne Ausgabe von URLs, Pfaden oder Zugangsdaten prüfen. FTPS ist für 1.2.0 benutzerbestätigt; SSH und PHP-8.0-Ausführung bleiben ungetestet. Dokumentationsbilder ausschließlich in neutralen Testinstallationen aufnehmen.


## Ausführbare Regressionstests

Im Kit-Stamm `php tests/security-regressions.php`, `php tests/cleanup-regressions.php`, `php tests/cleanup-regressions.php --older-alias` und `php tests/parallel-regressions.php` ausführen. Die Tests führen die Komponentenmethoden mit ausdrücklich ersetzten WordPress-APIs aus. Sie prüfen Identitätswechsel, veraltete Downloads, installierte gegenüber angebotenen Plattformanforderungen, versionierte Abhängigkeits-/Netzwerkregeln, einzelne Registereinträge und die Letzt-Host-Bereinigung. Der Paralleltest verwendet zwölf CLI-Prozesse und isolierte dateibasierte Speicherung; keine echte WordPress-Datenbank. Produktive Websites, echte HTTP-Anfragen und Zugangsdaten werden nicht verwendet.

`python3 tests/manifest.py` prüft die Laufzeithashes. Der nur lesende CI-Workflow prüft PHP-Syntax und diese Tests für PHP 8.0–8.4 sowie JavaScript-Syntax. Die vorhandene Konfiguration belegt keine bereits erfolgten entfernten Läufe oder Tests sämtlicher PHP-Versionen. Die Suite ersetzt keine tatsächlichen WordPress-Aktivierungen/-Updates, persistenten Object-Cache-, MySQL-Parallelitäts-, Plugin-Check- oder FTP-/SSH-Integrationstests. Test-/Werkzeugverzeichnisse gehören nicht in Host-Laufzeitpakete.




Veraltete, zukünftige, ungültige und fehlende Kataloge bei Onlineabruf an/aus, manuell neuere Installationen, fehlende normale Angebote und alte zuerst geladene Helper prüfen. Erstinstallationsfreigabe und Prüfsummen bleiben wirksam; Bestandsupdates verwenden normale Angebote. Statuswiederherstellung muss mit der abgesendeten normalen Zielversion statt der Katalogversion vergleichen. Native Einzel-, Sammel- und automatische Updates prüfen; geänderte Angebote, Archividentität/-version/-plattformfehler und unberechtigte Anfragen müssen die Installation erhalten.
