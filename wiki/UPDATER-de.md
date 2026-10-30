# Optionale Anbindung öffentlicher Updater

[English](UPDATER)

## Katalogaktionen und Host-Updater

Library 1.2.0 installiert, aktiviert und aktualisiert ausdrücklich gewählte Katalogplugins inline. Die native `Plugin_Upgrader`-Verarbeitung erhält Aktivierungsbereich und Plugindaten. Bereits vorhandene Plugins ohne Updater können nach genauer Plugin-/Repositoryprüfung aktualisiert werden; das ist keine automatische Übernahme aller installierten Plugins. Andere Versionen, fremde Repositories oder unbekannte Paketquellen werden abgewiesen.

Ein passendes GitHub-Quellarchivangebot kann nur akzeptiert werden, wenn Repository, Plugin, Version und Tag exakt übereinstimmen. Installiert wird weiterhin das freigegebene Katalog-Release-Asset mit SHA256-, Identitäts- und Archivprüfung. Fremde Updateangebote und Hooks bleiben erhalten. Das Zusammenspiel mit Git Updater berücksichtigt die native Update-Nonce bei weiterhin eigener Aktions-Nonce und Rechteprüfung. Der lokale Konflikthinweis empfiehlt bei Bedarf vorübergehendes Deaktivieren; automatisch wird nichts deaktiviert.

## Optionaler Providervertrag

Ein ausdrücklich angebundener öffentlicher Host-Updater kann `updater_release(repository, file, fresh)` aufrufen: Ein Array liefert freigegebene Metadaten, `false` erlaubt den bisherigen direkten Updatermodus bei ausgeschalteter Library-Onlineabfrage, und `null` verweigert die Freigabe. Verweigerte Freigabe darf nicht still auf ein ungeprüftes Paket zurückfallen. Anzeigecache: 24 Stunden; unabhängiger Updatemetadatencache: zwölf Stunden. Frische Paketfreigabe benötigt weiterhin eine erfolgreiche Quellenprüfung.

`updater_package(repository, file, package)` liefert einen geprüften temporären Paketpfad oder `WP_Error`. Erfolgreiche temporäre Archive entfernt der Aufrufer nach Gebrauch. Repository-URL, Plugin-Basename und Paket-URL müssen dasselbe freigegebene Ziel bezeichnen. Private Authentifizierung und sonstiges Updaterverhalten erhalten; diese Brücke gilt für ausdrücklich angebundene öffentliche Hosts.

Library 1.2.0 bietet außerdem `updater_diagnostic(repository, file)` für einen verfügbaren bereinigten Fehler derselben Anfrage und desselben Ziels. Es entsteht keine HTTP-Abfrage. Die Methode kann `null` zurückgeben und deckt nicht jeden möglichen Fehler ab. Der vorhandene Updater 2.2.1 zeigt diese Zusatzdiagnosen nicht automatisch und kann weiterhin eine allgemeine Prüfungsmeldung ausgeben. Den Array/null/false-Providervertrag nicht durch Fehlerobjekte als Release-Metadaten verändern.

Dateisystem-Zugangsdaten bleiben im nativen WordPress-Dialog. Ohne JavaScript bleiben Aktionen im Admin; Updates mit Zugangsdaten nutzen die native Pluginverwaltung. Ein Katalogausfall schaltet Prüfsummen-/Identitätsschutz niemals aus. Der alte Patch `integration/updater-v2.1-dev.3-catalog-provider.patch` ist ein historisches Beispiel für genau diesen Entwicklungsstand, kein Patch für aktuelle Updater.

