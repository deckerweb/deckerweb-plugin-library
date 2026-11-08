# Daten und Lebenszyklus

[English](DATA)

Gemeinsame Einstellungen liegen in `deckerweb_library_settings_v1`, bei Multisite je Netzwerk, auf Einzelwebsites als normale Optionen. Der Onlineabruf steuert ausschließlich Entdeckung und geprüfte Erstinstallationen. Persönliche Ansichten bleiben in `deckerweb_library_view_v1`; Filter zurücksetzen erhält Sortierung und Zufallsfolge. Einführungs- und Konflikthinweis-Metadaten bleiben unverändert. Diagnosekopien enthalten keine Zugangsdaten oder Website-Inhalte.

Der Anzeigecache heißt `dwl_catalog_<URL-md5>_061` (24 Stunden), ergänzt durch `_last` (48 Stunden) und `_retry` (15 Minuten). Die alte `_updates`-Familie liefert keine Bestandsupdates mehr; der Lebenszyklus erkennt sie weiterhin zur Bereinigung. `deckerweb_library_cache_keys_v2` erfasst die Schlüssel. Erstinstallationen verlangen unabhängig vom Anzeigecache eine frische Freigabe. Kein Library-Cron, dauerhafter Zugangsschlüssel oder zusätzlicher GitHub-Releasepoll wird eingeführt.

Die Installationshistorie nutzt unabhängige `deckerweb_library_managed_v2_<SHA256 Hauptdatei>`-Einträge mit lesendem Rückgriff auf `deckerweb_library_installed_v1`. Diese Einträge autorisieren keine Updateangebote oder Downloads mehr. Vor expliziten Bestandsaktionen wird die aktuelle Identität geprüft. Native Updateangebote gehören WordPress/Updater; die Library entfernt nur ihre überholten `dwl_managed`-Angebote.

Eigene Erstinstallations-Temporärdateien und Arbeitsverzeichnisse verwenden einzelne `deckerweb_library_temp_v3_<SHA256 Pfad>`-Einträge; altes temp_v2 bleibt zur Bereinigung lesbar. Regulärer Abschluss und Ausnahmebereinigung entfernen nur eigene Pfade. Uninstall v4 bereinigt registrierte Absturzreste im temporären Verzeichnis. Inlineaktionen behalten `dwl_inline_lock_<slug>` auf der Hauptwebsite mit tokengebundener Freigabe und 15-Minuten-Wiederherstellung. Dateisystemzugangsdaten werden nicht gespeichert.

Deaktivierung erhält Daten. Ein weiterer physisch installierter, auch inaktiver Host verhindert die Letzt-Host-Bereinigung. Beim letzten Host werden Library-Caches, Locks und eigene Temporärdateien über Netzwerkkontexte bereinigt. Einstellungen/Historie bleiben ohne ausdrückliche Löschwahl erhalten; globale persönliche Ansichten werden nur bei Freigabe aller relevanten Netzwerke entfernt. Installierte Plugins, Inhalte, Hosteinstellungen und Fremddaten bleiben erhalten. Hosts müssen `deckerweb_library_uninstall_v4` aufrufen; alte Hosts werden nicht umgeschrieben.

