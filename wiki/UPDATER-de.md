# Optionale Anbindung öffentlicher Updater

[English](UPDATER)

Der installierte Host bleibt für seinen Updater verantwortlich. Die Library ersetzt dessen Update-URI-Handler nie stillschweigend. Öffentliche Katalog-Callbacks sind optional; private Repositories behalten ihren Auth-Provider und gehören nicht in diesen öffentlichen Feed.

Das Kit enthält integration/updater-v2.1-dev.3-catalog-provider.patch, basierend auf der separat gepflegten Engine V2.1-dev.3. Auf genau diesen Quellstand in einer geprüften Integration anwenden; dies ist ein Integrationspatch, kein neuer kanonischer Updater-Release. Er ergänzt SUPPORTS_CATALOG_PROVIDER und optionale Konstruktoroptionen release_provider/package_provider. Beide Callbacks werden zusammen benötigt und im privaten Modus abgelehnt. Ohne diese Optionen bleiben öffentliches/privates Verhalten, lokale Grafiken, Detaildialoge und Quellauswahl erhalten.

Nach Laden des Library-Bootstraps und des Host-Updaters die Konfiguration mit defined(Updater::class . '::SUPPORTS_CATALOG_PROVIDER') absichern. Bei öffentlichen Hosts deckerweb_library_updater_options_v1(HOST_HAUPTDATEI, EXAKTE_REPOSITORY_URL) in bestehende Updateroptionen übernehmen; Host-Übersetzer und Grafiken erhalten. Die verzögert ausgeführten Callbacks funktionieren schon vor der Library-Wahl. Die Brücke registriert keine Updater-Hooks; der Host registriert weiterhin genau einen eigenen Updater.

Release-Callback: (Repository-URL, Plugin-Basename, fresh-Boolean) liefert false für den bisherigen direkten GitHub-Modus bei deaktiviertem Online-Katalog beziehungsweise fehlender geeigneter Laufzeit, null zur Ablehnung nicht freigegebener/ungeprüfter Releases oder validierte Release-Daten. Im aktiven Online-Modus führt eine Ablehnung nie zum GitHub-Fallback. Normale Abrufe verwenden den unabhängigen Updatecache. Paket-Callback: (Repository-URL, Plugin-Basename, angebotene Paket-URL) liefert ein begrenztes hashgeprüftes temporäres Archiv oder WP_Error nach frischer Freigabe und Abhängigkeitsprüfung. Bereits behandelte Downloads bleiben erhalten; andere Hosts/Plugins werden nicht abgefangen.

Der Patch ändert keine bestehenden Hosts, privaten Zugangsdaten, Repositories oder ausgelieferten Updater-Artefakte. Gegen den aktuellen Updater-Projektstand integrieren und Mischkopien sowie native Einzel-/Bulk-Updates vor einem Host-Release prüfen. Nicht blind auf andere Updater-Versionen anwenden.

Integration/updater-catalog-translations.json in die Host-Übersetzerressourcen übernehmen; die Komponente liefert diese Nachrichten ebenfalls im Host-Domain-Paket. Konfigurationsfehler im privaten Modus richten sich an Entwickler. Exakter geprüfter Basis-Hash und Patch-Übergabe werden separat zur Betreiberprüfung festgehalten.
