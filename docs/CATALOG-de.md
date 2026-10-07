# Online-Katalog und unabhängige Updates

[English](CATALOG.md)

Den optionalen Online-Katalog unter Einstellungen → deckerweb Library aktivieren (in Multisite Netzwerkeinstellungen). Der öffentliche Katalog liegt unter `https://raw.githubusercontent.com/deckerweb/deckerweb-plugin-library/main/catalog/catalog.json`. Diese Adresse ist vorausgefüllt; Online-Abfragen bleiben optional und standardmäßig ausgeschaltet. Erlaubt sind ausschließlich HTTPS-JSON-Quellen unter raw.githubusercontent.com/deckerweb.

Der Anzeigecache gilt 24 Stunden, gemeinsam für alle eingebundenen Hosts auf der Website beziehungsweise im Netzwerk. Eine Anfrage nach Ablauf aktualisiert ihn; wenig besuchte Websites haben keinen garantierten Zeitpunkt. „Katalog aktualisieren“ prüft manuell. Updateprüfungen installierter Plugins nutzen einen unabhängigen Zwölf-Stunden-Cache; native manuelle Zwangsprüfungen umgehen ihn. Beide Intervalle ersetzen keine WordPress-Zeitplanung. Bei Ausfall bleiben gültige Metadaten bis zu 48 Stunden verfügbar, mit 15 Minuten Wiederholungsabstand. Installation/Update erfordern immer einen erfolgreichen frischen Freigabeabruf. Ein gültiger leerer Katalog zieht alle Angebote zurück; ein ungültiger Katalog kann kein Paket freigeben.

Das öffentliche Dokument behält schema_version: 1 und plugins; catalog_revision, generated_at und requires_library ergänzen es. Die Revision kennzeichnet freigegebene Metadaten unabhängig vom Library-Code. Nicht unterstützte Library-Mindeststände werden abgelehnt. Eintragsfelder, Freigaben, Repository-/ZIP-Identität, Plattform- und Abhängigkeitsdaten, Serien und Prüfsummen bleiben verbindlich. Kein entfernter ausführbarer Code und keine entfernten Icons; Grafiken bleiben lokal in der Komponente.

Einen Kandidaten auf dem Betreiberrechner mit tools/refresh-catalog.py --output NEUER_ORDNER --revision REVISION vorbereiten. Das Werkzeug liest nur im mitgelieferten Katalog freigegebene Repositories, prüft stabile Release-ZIPs und Hashes und schreibt review.json. Optionaler Schlüssel DECKERWEB_CATALOG_GITHUB_TOKEN bleibt ausschließlich auf dem Betreiberrechner/Server; niemals ausliefern. Übersetzte Texte, Abhängigkeiten, Netzwerkanforderungen und Iconänderungen prüfen. Den exakt geprüften Kandidaten mit tools/approve-catalog.py KANDIDAT ZIEL --sha256 GEPRUEFTER_HASH exportieren. Beide Werkzeuge stoppen vor Veröffentlichung. Freigegebenes JSON separat am ausgewählten Endpunkt veröffentlichen; ältere Revisionen zum Zurücksetzen erhalten. Ein Plugin-Release allein erteilt keine Freigabe.

Quellennachweis und [Updater-Einbindung](UPDATER-de.md) lesen. Installierte Hosts behalten eigene Update URI und Authentifizierung.

Den Schema-1-Endpunkt für bestehende Hosts kompatibel halten. requires_library nicht allein erhöhen, weil ein neuerer Host eine neuere Komponente enthält. Wenn künftige Metadaten inkompatible Werte benötigen, bis zur Host-Migration einen kompatiblen älteren Feed bereitstellen; der Katalog darf sein eigenes Host-Update nicht blockieren.

Serienmetadaten werden ergänzend geführt: series erhält eine ältere Hauptzuordnung (quicknav, builder oder purify), series_memberships enthält alle ausdrücklichen Mitgliedschaften einschließlich manage-content. Ältere Leser können weiter das Hauptfeld verwenden. Ein Plugin erscheint einmal im Katalog und unter jedem passenden Serienfilter.

Daily Scripture verwendet network_activation=false als vorsichtige Altleser-Regel und network_activation_min_version=1.0.0 als versionierte Freigabe für Library 0.6.1. Diese hat in geeigneten Lesern Vorrang und prüft die installierte Version; ältere Leser behalten ihre Sperre. Daily 1.0.1 bringt die neue Laufzeit für erstmalige Aktivierung neben älteren Kopien mit.
