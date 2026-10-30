# Einbindung

[English](INTEGRATION.md)

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

Das Library-Kit ist nicht separat installierbar. `deckerweb-plugin-library-runtime-1.2.0.zip` enthält nur Laufzeitdateien. Das vollständige Kit enthält zusätzlich Werkzeuge und Dokumentation, die nicht in produktive Plugin-ZIPs gehören. Externen Installer und deckerweb Updater nicht auf WordPress.org ausliefern.

Siehe [Sicherheit](../SECURITY-de.md), [Daten](DATA-de.md), [Tests](TESTING-de.md) und [Release-Konventionen](CONVENTIONS-de.md).

## Gemischte Versionen und Bereinigung

Pro Anfrage wird die höchste kompatible vollständige Kopie gewählt. Registrierung bleibt `register_v2`; das Kompatibilitätsmanifest verwendet Protokoll 2. Der Bereinigungseinstieg heißt `uninstall_v3`—dieser Suffix ändert das Manifestprotokoll nicht. Manifest und alle aufgeführten Hashes müssen vollständig bleiben. Installierte inaktive Hosts und ihre Einbindungspfade erhalten.

Der aktuelle Bootstrap kann bei nativer Aktivierung an eine neuere gültige Kopie übergeben. Ein alter Offlinekatalog kann eine gesperrte Karte vor Aktivierung dieser Kopie nicht neu darstellen; für einen solchen Erstwechsel die native Pluginverwaltung verwenden. Ältere Hosts behalten ihre eigenen Deinstallationsroutinen und müssen separat geprüft werden. Keine fremde Hostdatei wird umgeschrieben. Historisch unterschiedliche Kopien derselben Version vollständig ersetzen, statt auf die Auswahl nach Hostnamen zu vertrauen.

Library 1.2.0 benötigt WordPress 6.4 und PHP 8.0. Ein Host mit Updater 2.2.1 benötigt mindestens PHP 8.1; höhere Hostanforderungen bleiben maßgeblich. Aktuelle stabile kompatible Komponenten verwenden und das tatsächlich integrierte Host-ZIP prüfen. Siehe [Updater](UPDATER-de.md), [Grafiken](ASSETS-de.md) und [Prüfstand 1.2.0](VALIDATION-1.2.0-de.md).
