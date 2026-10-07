# Einbindung

[English](INTEGRATION)

Nur Direktvertriebs-Hosts werden unterstützt. `lib/` in `includes/deckerweb-plugin-library/` des ausdrücklich ausgewählten aktuellen Host-Quellstands kopieren. Eigenen Updater und aktuelle Entwicklungsarbeit erhalten.

Vor `plugins_loaded`:

```php
require_once __DIR__ . '/includes/deckerweb-plugin-library/bootstrap.php';
deckerweb_library_register_v2( __FILE__, [], __DIR__ . '/includes/deckerweb-plugin-library' );
```

In der vorhandenen Host-Datei `uninstall.php` nach dem Schutz gegen direkten Aufruf einen begrenzten Cleanup-Block ergänzen; eigene Bereinigung nicht ersetzen:

```php
require_once __DIR__ . '/includes/deckerweb-plugin-library/lifecycle.php';
deckerweb_library_uninstall_v3( __DIR__ . '/DEIN-HOST-SLUG.php' );
```

Der genaue Host-Basename muss `WP_UNINSTALL_PLUGIN` entsprechen. Dieser Vertrag ist für die Bereinigung beim letzten Host erforderlich. Auch deaktivierte installierte Hosts werden über ihre physische Bootstrap-Datei erkannt; ein Register ausschließlich aktiver Hosts reicht nicht. Den üblichen Library-Pfad auch bei künftigen Kopien erhalten. Eigene Pfade benötigen einen ausdrücklich geprüften Erkennungsvertrag.

Übersetzungen verwenden die Textdomain des gewählten Hosts aus dessen Header (ersatzweise seinen Slug), keine eigene Komponentendomain. Library-MO-Dateien werden in diese Domain eingebunden; vorhandene Host-Texte haben Vorrang. EN-POT und deutsche PO/MO-Dateien für Du und Sie liegen bei. `lib/messages.json` ist die gepflegte Wörterbuchquelle. Nach Änderungen `tools/build-languages.py` ausführen und die POT-Einträge in den Host-Übersetzungsprozess übernehmen. Bei Locale-Wechsel wird die passende Host-Domain-Ressource neu geladen.

`prepare-plugin.py` akzeptiert nur BAS und Daily Scripture mit bekannten Versionsmarkern und kompatiblen Mindestversions-Headern. Es erhält Code hinter dem genauen alten Einbindungsblock, nutzt begrenzte Ersetzungsmarker und lehnt unklare individuelle Einbindungen bzw. bedingten Uninstall-Code ab. Neue Zieldatei, keine Überschreibung der Quelle und keine Erhöhung von Mindestversionen. Andere Hosts benötigen geprüfte manuelle Integration. Vor Release Host-Übersetzungen, Sicherheitsrichtlinie und tatsächliches finales ZIP prüfen.

Das Library-Kit ist nicht separat installierbar. `deckerweb-plugin-library-runtime-0.6.1.zip` enthält nur Laufzeitdateien. Das vollständige Kit enthält zusätzlich Werkzeuge und Dokumentation, die nicht in produktive Plugin-ZIPs gehören. Externen Installer und deckerweb Updater nicht auf WordPress.org ausliefern.

Siehe [Sicherheit](SECURITY-de), [Daten](DATA-de), [Tests](TESTING-de) und [Release-Konventionen](https://github.com/deckerweb/deckerweb-plugin-library/blob/main/docs/CONVENTIONS-de.md).

Alte Hosts mit 0.1–0.3 können parallel bestehen; deren alter Uninstall-Code erfüllt diesen neuen Vertrag jedoch noch nicht. Alle Host-Einbindungen aktualisieren, bevor nach Entfernen des letzten 0.4-Hosts eine abschließende Bereinigung durch einen alten Host erwartet wird. Alte Host-Dateien werden nicht automatisch verändert.

Für zentralen Feed und optionale Brücke zum bestehenden Updater [Katalog](CATALOG-de) und [Updater](UPDATER-de) lesen. Aktuelle Host-Entwicklungsquelle erhalten und Nachrichten über deren Textdomain übersetzen.

Beim Ersetzen eines früheren 0.6.0-Builds sämtliche installierten 0.6.0-Kopien gemeinsam austauschen. Gleiche Versionen verwenden den Host-Basename als eindeutige Auswahlregel; sonst kann eine ältere Kopie derselben Version gewinnen. Frühere Pakete archivieren und nach Austausch die Hashes in compatibility.json prüfen.

Der 0.6.1-Bootstrap registriert eine Übergabe vor Aktivierung. Bei erstmaliger Aktivierung prüft er das Manifest des gerade eingebundenen Zielhosts und ersetzt eine ältere gewählte Library vor deren Aktivierungsprüfung. Nur Callbacks der bisherigen Library-Instanz werden entfernt; Host-/Updater-Hooks bleiben erhalten. Das Protokoll-2-Manifest muss vollständig sein. Daily-Scripture-Netzwerkfreigabe gilt ab installierter Version 1.0.0. Den aktualisierten Online-Katalog vor Auslieferung des Host-Updates veröffentlichen.

Ein alter Offline-Library-Katalog kann seine gesperrte Aktivierungskarte vor dem Komponentenwechsel nicht neu darstellen. Für den Erstwechsel Netzwerkverwaltung → Plugins → Daily Scripture → Netzwerkweit aktivieren verwenden (oder einen bereits aktiven Host aktualisieren). Der neue Zielhost-Bootstrap übernimmt diese native Aktivierung; danach stellt die neue Library die Katalogaktionen bereit.

Protokoll3 verhindert, dass eine zuvor geladene v2-Kopie den Deinstallationseinstieg des neuen Hosts übernimmt. Ältere Hosts, die weiterhin v2 aufrufen, müssen separat geprüft werden; die Komponente schreibt deren Uninstall-Code nicht um.

Neue 0.8.0-Hosts rufen uninstall_v3 auf. Die Bereinigung prüft am Request-Ende nach einer nativen Sammeldeinstallation nochmals, ob Hosts installiert bleiben. Ein physisch installierter inaktiver Host schützt gemeinsame Daten weiterhin. Ein allein deinstallierter alter Host verwendet seine alte Routine; neuer Code ändert dessen Datei nicht rückwirkend. Lokale unveröffentlichte 0.7.1-Testkopien vor dem abschließenden gemischten Rollout ersetzen.
