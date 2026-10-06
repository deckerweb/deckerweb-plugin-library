# Release-Prüfung · 0.4.0

[English](VALIDATION-0.4.0.md)

Am 5. Oktober 2026 in isolierten WordPress-Installationen geprüft. Mindestanforderungen bleiben WordPress 6.4 und PHP 8.0; keine Host-Mindestanforderung wurde erhöht.

- 70 Integrationsprüfungen: Rechte, Nonces, Quellen, Freigabe, Caches, Voraussetzungen und Erhalt eigener Host-Updater.
- 54 Katalog-/Paketprüfungen: alle 14 freigegebenen Release-Archive und zwölf aktuelle lokale Originalicons; zwei generierte Ersatzicons.
- Elf Netzwerkprüfungen, 34 Letzt-Host-Lebenszyklusprüfungen auf Einzelwebsite und Multisite, sechs zusätzliche Mehrnetzwerkprüfungen sowie eine tatsächlich neu angelegte Website.
- 13 Prüfungen zu Übersetzungen, Löschoption, Verlauf und begrenztem Speicherbedarf, darunter übergroße komprimierte Hauptdateien bei 64 MiB PHP-Speicherlimit.
- Sechs Szenarien zur gemeinsamen Versionswahl, einschließlich zuerst geladener alter Registrierung und inkompatibler, unvollständiger oder beschädigter höherer Kopien.
- Elf Ablaufprüfungen rund um echte Installation/Update mit dem WordPress Plugin_Upgrader und separate Aktivierung in isolierten Testplugins.
- Zwölf Werkzeugprüfungen zu Codeerhalt, wiederholter Integration, Paketinhalt und widersprüchlichen Host-Mindestanforderungen.
- Tatsächliche WordPress-Versionen 6.4, 6.7 und die aktuelle stabile 7.1.2 auf PHP 8.4.5. Die Datenbank der aktuellen Version wurde regulär aktualisiert. Du/Sie und Sprachwechsel funktionieren auf beiden Eckversionen.
- Browserprüfung auf WordPress 7.1.2: 14 Karten, zwölf lokale Icons, GitHub-Sterne, Tastaturdialog, Fokusbegrenzung und -rückgabe, Escape, schmale Darstellung und keine JavaScript-Fehler.

Die fertigen Archive werden auf Integrität, öffentliche Benennung und Entwicklungs-/interne Dateien geprüft; das Laufzeitarchiv wird in einen isolierten Host entpackt und auf WordPress 6.4 und 7.1.2 geladen. Im Frontend bleibt die Laufzeit ungeladen.

Grenzen: PHP 8.0 stand für einen Ausführungstest nicht zur Verfügung. WordPress 6.4 meldet unter PHP 8.4 eine bestehende Core-Deprecation. Builder-Testplugins ersetzen keinen Test mit tatsächlichen lizenzierten Buildern. FTP/SSH, vollständige Host-Funktionen, Prüfung mit assistiven Technologien und die private GitHub-Meldekonfiguration bleiben Prüfungen vor der jeweiligen Host-Veröffentlichung. Ein Library-Build ändert keine Repository-Einstellungen und veröffentlicht keine Host-Releases. Siehe [Tests](TESTING-de.md) und [Sicherheit](../SECURITY-de.md).
