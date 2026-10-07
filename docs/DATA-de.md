# Daten und Lebenszyklus

[English](DATA.md)

Einstellungen und Installationszuordnung liegen in den Site Options `deckerweb_library_settings_v1` und `deckerweb_library_installed_v1` (bei Multisite je Netzwerk, sonst normale Optionen). Die Löschoption ist standardmäßig aus. Der Einführungshinweis verwendet den globalen User-Meta-Schlüssel `deckerweb_library_intro_seen_v1`. Einstellungen, Zuordnung und Hinweisstatus bleiben standardmäßig erhalten.

Katalog-Caches verwenden `_site_transient_dwl_catalog_<URL-md5>` mit `_last` und `_retry`: 24 Stunden, 48 Stunden, 15 Minuten. `deckerweb_library_cache_keys_v2` hält Schlüssel zur Bereinigung in Datenbank und persistentem Cache fest. Download und Aufbereitung verwenden Library-markierte temporäre Dateien und in `deckerweb_library_temp_v2` erfasste Arbeitsverzeichnisse. Normaler Abschluss bereinigt sie sofort; der letzte Host entfernt erfasste Absturzreste im aktuellen temporären Verzeichnis. Die Library plant keine Hintergrundaufgaben.

Deaktivierung verändert diese Daten nicht. Beim Entfernen eines Hosts bleiben gemeinsame Daten erhalten, solange ein weiterer Host installiert ist, auch deaktiviert. Der letzte Host bereinigt Caches, Schlüsselregister und erfasste temporäre Dateien. Die optionale Löschung entfernt zusätzlich Library-Einstellungen, Installationszuordnung und Hinweisstatus. Der Hinweisstatus gilt global: bei mehreren Netzwerken erst entfernen, wenn deren Library-Einstellungen sämtlich gelöscht sind. Installierte Plugins und Inhalte bleiben immer erhalten; fremde Tabellen, Optionen und Host-Einstellungen werden nicht angefasst.

Die Bereinigung umfasst beim Entfernen des letzten physischen Hosts alle Netzwerke, niemals nur wegen einer Website-Deaktivierung. Neue Websites nutzen automatisch die Netzwerkeinstellungen und benötigen keine Initialisierung. Vorhandene v1-Daten bleiben unverändert; v2-Verwaltungsdaten entstehen bei Bedarf. Alte Datenbank-Caches werden über ihren dokumentierten Namespace bereinigt. Nicht erfasste Schlüssel externer Objekt-Caches laufen mit ihrer TTL aus.

Kein zusätzlicher Export/Import für die wenigen Einstellungen: Sichtbarkeit, optionale Katalog-URL/Online-Modus und Löschoption.

Anzeigecache: dwl_catalog_<URL-Hash>, 24 Stunden. Updatecache: dwl_catalog_<URL-Hash>_updates, zwölf Stunden, unabhängig bei WordPress-Updateprüfungen gelesen. Beide haben _last (48 Stunden) und _retry (15 Minuten); die bestehende gemeinsame Schlüsselregistrierung deckt beide ab. Frische Paketfreigabe umgeht diese Caches. Kein neuer Cronjob und kein dauerhaft gespeicherter Updater-Schlüssel. Letzt-Host-Bereinigung entfernt beide Cachefamilien.

Library 0.6.1 ergänzt registrierte Katalogcache-Basisschlüssel um _061, damit frühere Netzwerkfreigaben nicht aus alten Caches übernommen werden. Bestehende Letzt-Host-Bereinigung entfernt registrierte Schlüssel und Cachefamilien.

Inline-Aktionen verwenden eine temporäre, nicht automatisch geladene Sperroption dwl_inline_lock_<slug> auf der Hauptwebsite des Hauptnetzwerks beziehungsweise der Einzelwebsite. Eine Anfrage gibt ihren eigenen Token bei Abschluss oder beim Herunterfahren frei; verwaiste Sperren können nach 15 Minuten aufgehoben werden. Die Deinstallation des letzten Hosts entfernt verbliebene Library-Sperroptionen. Die Library speichert keine Dateisystem-Zugangsdaten.
