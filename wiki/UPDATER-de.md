# Optionale Anbindung öffentlicher Updater

[English](UPDATER)

## Zwei getrennte Aufgaben

Library 1.3.0 verwendet den geprüften Katalog zum Entdecken und zur Erstinstallation eines verifizierten Pakets. Updater 2.4.0 versorgt installierte Plugins im normalen WordPress-Updateprozess. Onlinekatalog-Einstellung, Katalogversion, zurückgezogene Katalogeinträge oder Abruffehler bestimmen nicht die dort angebotene Updateversion.

Die Library liest die tatsächlich installierten Header und vorhandene WordPress-Angebote aus `update_plugins`. Statusfilter und Updatebuttons verwenden dieses vorhandene Angebot. Beim Rendern der Karten wird weder `wp_update_plugins()` noch ein GitHub-Releaseabruf oder eine Hintergrundprüfung gestartet. Bis ein gerade veröffentlichtes Release erscheint, kann weiterhin eine normale WordPress-Prüfung nötig sein.

Der Updatebutton ruft nativ `Plugin_Upgrader::bulk_upgrade()` für die genaue installierte Hauptdatei auf. Wie beim Core-AJAX-Updater verarbeitet die Bulk-Methode das einzelne ausgewählte Plugin unter Erhalt des Aktivierungsumfangs. Er erfindet kein Angebot, ersetzt das normale Paket nicht durch ein Katalogpaket und überträgt keine Katalog-Mindestversionen oder Abhängigkeitsregeln auf das Update. Paketidentität, angebotene Version, Berechtigungen und tatsächliche Archiv-Mindestanforderungen bleiben durch WordPress/Updater geprüft. Ein inzwischen geändertes angezeigtes Angebot wird bis zum Neuladen abgewiesen. Fremde Updateanbieter und ihre Angebote bleiben erhalten.

## Einbindung und ältere Kopien

Beide eingebetteten Komponenten aktualisieren und die beim Include der Updater-Runtime zurückgegebene Klasse verwenden. Vorhandene Hostaufrufe von `deckerweb_library_updater_options_v1()` können bleiben: Updater 2.4.0 ignoriert die überholten Katalog-Release-/Paketcallbacks. Library 1.3.0 liefert in ihrem alten `updater_release()` ausdrücklich `false`, damit ältere Updater ihren bekannten Direktweg verwenden. Sie liefert dafür keine Katalog-Updatepakete oder Cleanup-Leases mehr. Dieser bewusst geänderte Zuständigkeitsvertrag gilt für die neue Runtime und ist keine allgemeine Aufforderung, frühere Provider-Ablehnungen zu umgehen.

Alte `dwl_managed`-Angebote des bisherigen Katalog-Updaters werden entfernt, normale Angebote bleiben erhalten. Die Library richtet keinen neuen Updater für Altplugins ohne eigenen Updater ein. Solche Plugins benötigen eine getrennte Aktualisierung ihrer normalen Updater-Einbindung; die Plugins-Seite bleibt der Verwaltungseinstieg. Unveränderte alte Kopien behalten ihr historisches Verhalten, bis eine passende neue Runtime gewählt wird. Update URI, Authentifizierung und native Einstellungen für automatische Updates bleiben erhalten.

## Erstinstallation und Bereinigung

Die Erstinstallation verlangt weiterhin eine frische Katalogfreigabe, die Katalog-SHA256 und begrenzte Archiv-/Identitätsprüfung. Die Library verwaltet und entfernt ihre Installations-Temporärdateien auch bei Ausnahmen und erhält fremde/ersetzte Pfade. Updater 2.4.0 verwaltet normale Bestandsupdates ohne Library-Paketlease. Hosts übernehmen `deckerweb_library_uninstall_v4` und erhalten ihre eigene Bereinigung.

Dateisystemzugangsdaten bleiben im nativen WordPress-Dialog und werden nicht von der Library gespeichert. Die native Updates-Nonce für Drittanbieterkompatibilität wird zusätzlich zur unabhängig geprüften Library-Aktionsnonce gesendet. Ohne JavaScript läuft dasselbe normale Update über einen autorisierten Admin-POST; nötige Dateisystemzugangsdaten werden dann über die native Plugins-Seite eingegeben. Git-Updater-Konflikthinweise bleiben Empfehlungen; nichts wird automatisch deaktiviert.

