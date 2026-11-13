# Online-Katalog und unabhängige Updates

[English](CATALOG)

Aktuelle Library: **1.3.0** · Katalogrevision **2026-11-13.1**.

Der Katalog enthält 33 freigegebene öffentliche Plugin-Releases in 8 Serien. Jeder Eintrag legt Repository, Hauptdatei, Erstinstallationsversion, Original-ZIP, SHA256 und Voraussetzungen fest. Der Katalogabruf ist optional, standardmäßig aus und wird 24 Stunden gespeichert. Neue Plugins und Katalogänderungen werden ausdrücklich geprüft. Ältere Leser behalten ihr historisches konservatives Verhalten.

Originalicons werden lokal mitgeliefert. Ohne passendes lokales Icon erscheint ein Kürzel auf dezentem Hintergrund; ein explizites `icon_background` hat Vorrang vor der stabilen Pastellpalette. Dezente Hover-/Tastaturfokusdarstellung bleibt erhalten. Keine externen Icons, Skripte oder ausführbaren Kataloginhalte. WPCodeBox QuickNav verwendet in dieser Library sein lokales Originalicon.

Aktuelle [Katalog-Release-/Paketquellen](https://github.com/deckerweb/deckerweb-plugin-library/blob/main/docs/CATALOG-SOURCES-2026-11-13.1.json). Katalogversionen bestimmen Pakete für Erstinstallationen, begrenzen aber keine Bestandsupdates.

## Pluginupdates und der Onlinekatalog

**Onlinekatalog und Bestandsupdates sind mit Library 1.3.0 und Updater 2.4.0 unabhängig.** Der Onlinekatalog kann für aktuelle Entdeckungsmetadaten eingeschaltet werden. Für neuere Plugin-Releases muss er nicht ausgeschaltet werden.

Beispiel: Der Katalog nennt 1.3.0, installiert ist 1.3.1 und der normale Updater bietet 1.4.0. Die Library zeigt Installiert: 1.3.1 und Update verfügbar: 1.4.0. Ihr Updatebutton verwendet das normale WordPress-Update. Ein älterer, nicht erreichbarer oder abgeschalteter Katalog blockiert es nicht. Wird 1.4.0 manuell installiert, erscheint diese installierte Version und es wird kein Downgrade angeboten.

Bei noch nicht installierten Plugins verwendet Jetzt installieren das geprüfte Katalogpaket. Danach kommen Updates vom normalen Plugin-Updater. Ein funktionierender Updater bleibt Voraussetzung; die Library rüstet beliebige Altplugins nicht damit nach. Die Katalogeinstellung aktiviert keine automatische Installation und verändert keine Zugangsdaten privater Repositories.

Kein Update gemeldet bedeutet: Im vorhandenen WordPress-Updatestand liegt kein neueres Angebot. Das behauptet weder eine frische GitHub-Prüfung noch, dass die Installation den neuesten Stand hat. Stöbern, Sortieren und Filter starten keine zusätzlichen Releaseabfragen. Die normale Prüfung ist unter Dashboard → Aktualisierungen erreichbar; Caches und technische Anforderungen gelten weiterhin.

Einstellungen → deckerweb Library (bei Multisite Netzwerkverwaltung → Einstellungen) steuert den optionalen Onlineabruf. Ausblenden ändert nur die Sichtbarkeit. Beide Einstellungen lassen Bestandsupdates unabhängig. Frühere Komponenten können noch ihr älteres Freigabeverhalten besitzen; beide Komponenten für das vollständige aktuelle Verhalten aktualisieren.


Revision 2026-11-09.1 aktualisiert 28 geprüfte Plugin-Releases aus der Komponentenpflegematrix. Der Katalog behält 32 Plugins und acht Serien. Daily Scripture, Brand Admin Schemes, Site Essentials und TabulaMea bleiben unverändert. Library 1.3.0 und ihr eingebauter Rückfallkatalog bleiben unverändert.

Revision 2026-11-10.1 aktualisiert TabulaMea auf 1.0.0 sowie Site Essentials, Brand Admin Schemes und Daily Scripture auf 1.2.0. Die übrigen 28 Einträge, acht Serien und lokalen Icons bleiben unverändert. Library bleibt bei 1.3.0; eingebauter Rückfallkatalog und Release-Pakete bleiben unverändert.

Revision 2026-11-13.1 ergänzt Tools for WooCommerce 1.0.0 in der Serie Shop. Library 1.3.0 zeigt auf der Karte das Kürzel TWC.
