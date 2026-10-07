# Release-Prüfung · 0.7.0

[English](VALIDATION-0.7.0.md)

7. Oktober 2026. Inline-Installation und Aktivierung wurden auf WordPress 6.7 Multisite und WordPress 7.1.2 als Einzelwebsite mit PHP 8.4.5 geprüft: echte Paketinstallation/Aktivierung, Erhalt von Katalogfiltern und URL, Inline-Fehler mit Wiederholung, Abweisung ungültiger Nonces/Aktionen, mobile Ansicht sowie Abbrechen/Escape im nativen Dateisystemdialog. Original-Release-ZIPs wurden über einen kontrollierten lokalen Testtransport bereitgestellt; Hash-, Identitäts- und Archivprüfung blieben aktiv. Auch die Formularinstallation ohne JavaScript wurde getestet.

Mindestversionen der Komponente bleiben WordPress 6.4/PHP 8.0. PHP8.0-Ausführung, lizenzierte Builder, echte FTP-/SSH-Verbindungen und Parallelität mehrerer PHP-Worker sind nicht erneut bestätigt. Vollständige Parameter-/Rückgabeverträge und finale Archivmanifeste sind geprüft. Die optionale Updater-Brücke bleibt separat; keine kanonische Host- oder Updaterquelle überschrieben.
