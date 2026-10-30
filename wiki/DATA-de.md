# Daten und Lebenszyklus

[English](DATA)

Einstellungen und Installationszuordnung verwenden `deckerweb_library_settings_v1` und `deckerweb_library_installed_v1`: Netzwerkoptionen bei Multisite, normale Optionen auf Einzelwebsites. Die optionale Einstellungslöschung ist standardmäßig aus. Der Einführungshinweis verwendet das globale Benutzermetafeld `deckerweb_library_intro_seen_v1`.

Persönliche Ansichten liegen in `deckerweb_library_view_v1`: Suche, Serie, Kompatibilität, Status, Sortierung und Zufallsstartwert. Filter zurücksetzen leert die Filter, nicht die gewählte Sortierung oder Zufallsfolge. Das Ausblenden des Konflikthinweises speichert einen lokalen Fingerabdruck in `deckerweb_git_updater_notice_v1`. Diagnosekopien enthalten keine persönlichen Suchwerte, Zugangsdaten oder Website-Inhalte.

Katalogcache-Schlüssel heißen `dwl_catalog_<URL-md5>_061` für die Anzeige (24 Stunden) und derselbe Basisschlüssel mit `_updates` für Host-Updatemetadaten (zwölf Stunden). Beide haben `_last` (48 Stunden) und `_retry` (15 Minuten). Es sind Site Transients, bei Multisite je Netzwerk. `deckerweb_library_cache_keys_v2` erfasst Schlüssel zur Bereinigung. Frische Paketfreigabe umgeht Anzeige-/Updatecaches; eine fehlgeschlagene frische Prüfung erlaubt kein Paket. Kein Library-Cronjob und keine dauerhaft gespeicherten Updater-Zugangsdaten kommen hinzu.

Download und Aufbereitung verwenden Library-markierte temporäre Dateien und in `deckerweb_library_temp_v2` erfasste Arbeitsverzeichnisse. Normaler Abschluss entfernt sie. Der letzte Host bereinigt erfasste Absturzreste innerhalb des aktuellen temporären Verzeichnisses. Inlineaktionen verwenden eine nicht automatisch geladene Option `dwl_inline_lock_<slug>` auf der Hauptwebsite des Hauptnetzwerks beziehungsweise der Einzelwebsite. Anfragen geben ihre eigenen Token bei Abschluss/Herunterfahren frei; verwaiste Sperren können nach 15 Minuten aufgehoben werden. Die Library speichert keine Dateisystem-Zugangsdaten.

Deaktivierung erhält Daten. Bei Deinstallation bleiben gemeinsam benötigte Daten erhalten, solange ein weiterer physischer Host installiert ist, auch deaktiviert. Der letzte Host bereinigt Library-Caches, Schlüsselregister, Sperren und erfasste temporäre Dateien über die Netzwerkbereiche. Einstellungen und Zuordnungen bleiben ohne aktivierte Löschoption erhalten. Globale Benutzerpräferenzen, Hinweis- und Einführungsstatus werden nur entfernt, wenn alle betreffenden Netzwerkbereiche die Einstellungslöschung erlauben. Installierte Plugins, deren Inhalte, Host-Einstellungen und fremde Daten werden niemals durch die Library-Bereinigung entfernt.

Hosts müssen den aktuellen Vertrag `deckerweb_library_uninstall_v3` aufrufen. Alte Hosts verwenden weiterhin ihren eigenen Bereinigungscode; die Library schreibt ihn nicht um. Neue Websites übernehmen Netzwerkeinstellungen ohne Initialisierung je Website. Altdaten bleiben erhalten; Verwaltungsdaten entstehen bei Bedarf. Ein gesonderter umfassender Einstellungsexport/-import besteht nicht.

