=== deckerweb Plugin Library ===
Requires at least: 6.4
Requires PHP: 8.0
Stable tag: 1.3.0
License: GPLv2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html

== Description ==
The deckerweb Plugin Library adds a selected catalog of deckerweb plugins to WordPress. It comes bundled with certain plugins and gives you another way to discover and install useful additions under **Plugins → Add New → deckerweb**. The usual WordPress.org catalog remains the default.

If you found an `includes/deckerweb-plugin-library/` folder inside a plugin, this is the shared component behind that catalog. The plugin author included it deliberately; you do not need to install or configure a separate Library plugin.

This repository contains the reusable PHP component, catalog, integration examples and documentation. It is also open for developers who want to read the code, reuse it under its license or build their own approach.

Installation and activation happen directly in the selected card. Status and errors appear there; search, series filters and scroll position remain. Filesystem credentials use the native WordPress dialog. Without JavaScript, the checked form workflow remains available.

Component: **Library 1.3.0**. See the [website](https://deckerwebplugins.com/en/library/), [catalog](docs/CATALOG.md) and [validation](docs/VALIDATION-1.3.0.md).

Current online catalog: **2026-11-08.1 · 32 plugins · eight series**. Library component: **1.3.0**. Catalog discovery and first installation are separate from ordinary installed-plugin updates.

Embedded component for direct distribution only; not a standalone WordPress.org submission.

== Installation ==
See README.md and docs/INTEGRATION.md.

== Frequently Asked Questions ==
= Where is the catalog? =
Open Plugins → Add New → deckerweb. WordPress.org remains the default view.

= Does the online catalog limit plugin updates? =
No. With Library 1.3.0 and Updater 2.4.0, installed plugins use their normal WordPress update provider regardless of catalog settings or catalog version. The Library shows the actual installed version and existing WordPress update offers. A catalog version only selects the verified package for first installation. No additional GitHub release checks are made when browsing. Normal update intervals, caches and technical requirements still apply. This does not enable automatic installation. Older component combinations may retain their previous behavior until updated. See the [update guide](docs/CATALOG.md#plugin-updates-and-the-online-catalog).

= Why is an installation unavailable? =
Check the card for WordPress/PHP requirements and the selected release. Missing mother plugins or themes are advisory for catalog versions with a verified safe-pause rule: installation and activation remain available while dependent features pause. Older installed versions may still have required dependencies. Native WordPress restrictions and platform requirements remain effective. Prerequisites are not installed automatically; activation is separate.

= Can I hide it? =
Use Settings → deckerweb Library (Network Settings on Multisite). Hiding the catalog preserves dependency checks and ordinary plugin updates. Online retrieval is a separate preference for catalog metadata and first installations.

= What happens when I remove a host? =
Another installed host, even inactive, preserves shared data. The final host removes temporary Library data and caches. Settings remain unless optional deletion was enabled. Installed plugins and their content remain. Hosts must call the supplied uninstall contract.

= Does it support Multisite? =
Library settings apply per network; catalog preferences are personal. Plugin actions respect site/network permissions and each catalog entry. Multisite Toolbar Additions supports single sites and Multisite. Daily Scripture permits network activation from version 1.0.0. The current Bricks QuickNav catalog version has no blanket per-site activation block; its theme-dependent features still depend on each site’s active theme. See the validation guide for the actual tested scope.

= How do I report a vulnerability? =
Use Security → Advisories → Report a vulnerability in the host plugin repository. Include host and Library versions; do not post security details in public issues. Hosts must enable private reporting before publication.

== Changelog ==
### 1.3.0 · 2026-11-08

- **Neu:** Bestandsupdates sind unabhängig von Onlinekatalog-Einstellung und Katalogversionen.
- **Verbessert:** Karten zeigen tatsächlich installierte Versionen und normale WordPress-Updateangebote, auch neuere Releases als im Katalog.
- **Verbessert:** Freigegebenen eingebauten Katalog und lokale Originalicons aktualisiert.
- **Behoben:** Veraltete katalogverwaltete Updateangebote entfernen und installierte Identität vor expliziten Updates prüfen.
- **Behoben:** Bei der Aktivierung eines vorhandenen Plugins die Voraussetzungen seiner installierten Version prüfen.
- **Behoben:** Parallele Installations- und Temporärdateieinträge unabhängig speichern und eigene Erstinstallationsdateien nach Fehlern zuverlässig bereinigen.
- **Sonstiges:** Altplugins ohne normalen Updateanbieter benötigen einmalig ein manuelles ZIP-Update; die Library liefert keine katalogverwalteten Ersatz-Updateangebote mehr.

### 1.2.0 · 2026-10-30

- **Neu:** Plugins nach Installation, Aktivierung und verfügbaren Katalogupdates filtern, mit passender Trefferzahl.
- **Verbessert:** Plugin-Status und Treffer werden nach erfolgreichen Katalogaktionen aktualisiert. Filter zurücksetzen erhält die persönliche Sortierung.
- **Verbessert:** Aktualisierter eingebauter Katalog und lokale Originalicons.
- **Verbessert:** Katalog- und Downloadfehler nennen die betroffene Fehlerstufe sowie eine bereinigte Verbindungs-, HTTP-, Prüfsummen- oder Archivursache.
- **Verbessert:** Kompaktere Katalogfilter erhalten vertraute WordPress-Bedienelemente und Tastaturfokus.
- **Behoben:** Katalogaktionen bleiben auch nach Filter- oder Sortierwechseln inline.

### 1.1.0 · 2026-10-21

- **Verbessert:** Aktualisierter freigegebener Katalog und lokale Originalicons mit weniger Bild-Doppeldateien. Kürzel erhalten dezente Hintergrundfarben; Karten reagieren auf Maus und Tastaturfokus.
- **Behoben:** Strengere Bereinigung von Admin-Eingaben und kontextgerechte Absicherung der Katalogausgabe.
- **Behoben:** Inline-Updates berücksichtigen die Nonce-Prüfung von Git Updater, ohne die Library-Autorisierung abzuschwächen; fehlgeschlagene Aktionen bleiben als Fehler erkennbar.
- **Behoben:** Gezielte Katalogupdates erkennen passende GitHub-Quellarchivangebote und installieren weiterhin ausschließlich das freigegebene Release-ZIP mit geprüfter Prüfsumme.

### 1.0.0 · 2026-10-15

- **Neu:** Persönliche Katalogsortierung, stabile Zufallsansicht und kopierbare technische Informationen in den Library-Einstellungen.
- **Verbessert:** Gespeicherte Filter, klarer Katalogstatus und Plugin-Aktivierungszustand, aktualisierte freigegebene Releases und lokale Originalicons.
- **Behoben:** Inline-Installationen übergeben die native Pluginidentität für die Zusammenarbeit mit Git Updater. Verlaufsdialoge behalten native Schließ- und Dokumentationslink-Fallbacks.

### 0.9.0 · 2026-10-10

- **Neu:** Geprüfte installierte Katalogplugins direkt in ihren Karten aktualisieren, einschließlich älterer Releases ohne Updater.
- **Neu:** Katalogdefinierte Serien, übersetzte Kategorien, Reihenfolge und versionsabhängige Regeln für sichere Funktionspausen.
- **Verbessert:** Aktuelle freigegebene Katalogpakete und lokale Originalicons, einschließlich Builder Content Guide und Admin-Serie.
- **Verbessert:** Gemeinsame Einstellungen direkt speichern und Library-Aktionen innerhalb der WordPress-Verwaltung halten.
- **Behoben:** Frühe Ausfallmeldungen verwenden Host-Sprachressourcen; die Aktivierungsübergabe ist direkt an der Funktion dokumentiert.

### 0.8.1 · 2026-10-08

- **Neu:** Katalogserien Werkzeuge und Shop mit rückwärtskompatiblen Metadaten.
- **Verbessert:** Der mitgelieferte Katalog enthält alle 20 freigegebenen Plugins und ihre aktuellen lokalen Icons.
- **Verbessert:** Nach unterbrochenen Inline-Aktionen den Plugin-Status prüfen, ohne eine erfolgreiche Aktion zu wiederholen.
- **Verbessert:** Builder-Laufzeitmarker der aktiven Installation zuordnen und den versionsabhängigen Aktivierungsvertrag von Oxygen QuickNav 2.0 berücksichtigen.
- **Verbessert:** Pakete, Voraussetzungen und Originalicons von Oxygen QuickNav2.0.0 und Quick Edit Featured Image1.4.0 aktualisiert.
- **Behoben:** Beim Entfernen des letzten Hosts werden aktuelle Katalog- und Update-Caches ebenso wie ältere Caches bereinigt.
- **Behoben:** Der aktuelle Deinstallationseinstieg bleibt wirksam, wenn zuvor eine ältere Cleanup-Kopie geladen wurde.

### 0.7.0 · 2026-10-07

- **Verbessert:** Katalogplugins direkt in ihrer Karte installieren und aktivieren, mit Status und Fehlern an Ort und Stelle.
- **Verbessert:** Die freigegebenen dreistelligen Fallback-Kürzel verwenden, wenn kein Originalicon verfügbar ist.

### 0.6.1 · 2026-10-07

- **Verbessert:** Freigegebene Plugin-Releases und originale Katalogicons aktualisiert.
- **Verbessert:** Der Einstellungs-Footer zeigt das lokale SVG-Icon, den Namen und die Version der Library.
- **Behoben:** Daily Scripture ab 1.0.0 kann auch neben einer älteren eingebetteten Library netzwerkweit aktiviert werden.
- **Behoben:** Einzelne gefilterte Treffer behalten auf breiten Ansichten die normale Kartenbreite.
- **Behoben:** Multisite Toolbar Additions wird auch für einzelne Websites und Website-Aktivierung angeboten.

### 0.6.0 · 2026-10-06

- **Neu:** Freigegebene Plugin-Releases können im Online-Katalog erscheinen, ohne die eingebettete Library auszutauschen.
- **Neu:** Purify WPCode Lite und Purify WPForms Lite im Katalog entdecken.
- **Neu:** Plugins können mehreren Serien angehören, darunter Inhalte verwalten.
- **Neu:** Die Connect-Serie und das kommende Connect for Shopware 1.0.0 mit klarem Vorbereitungshinweis entdecken.
- **Verbessert:** Der Katalog wird nach 24 Stunden aktualisiert; Updateprüfungen installierter Plugins nutzen einen unabhängigen Cache.
- **Verbessert:** Die optionale Anbindung des Host-Updaters erhält aktuelle Paketfreigaben und Prüfsummenprüfungen.
- **Verbessert:** Die öffentliche GitHub-Katalogadresse ist in den Library-Einstellungen vorausgefüllt.
- **Behoben:** Katalog- und Paketabfragen verwenden eine Clientkennung ohne Website-URL.
- **Behoben:** Plugins mit eigenem Updater bleiben bei nicht erreichbarem Katalog unabhängig.
- **Behoben:** Online-Katalogquellen sind auf den GitHub-Raw-Dateihost von deckerweb beschränkt.

### 0.5.0 · 2026-10-05

- **Neu:** Ausdrückliche Serienzuordnung für QuickNav, Builder und Purify, dezente Karten-Badges und Serienfilter. Leere Serien bleiben verborgen.
- **Neu:** Purify Elementor ergänzt den freigegebenen Katalog und die Purify-Serie; Multisite Toolbar Additions gehört zu QuickNav.
- **Verbessert:** Serien und Suche mit „Passt zu meiner Installation“ kombinieren; Filter ohne Einstellungsänderung zurücksetzen.

### 0.4.0 · 2026-10-05

- **Neu:** Übersetzungen über die Host-Textdomain auf Englisch, Deutsch (Du) und Deutsch (Sie).
- **Neu:** Gemeinsame Bereinigung beim letzten Host mit optionaler Einstellungslöschung und lokalem zugänglichem Änderungsverlauf.
- **Verbessert:** Kompatible Laufzeitwahl mit alten und neuen Hosts; aktuelle freigegebene Katalogquellen und lokale Icons.
- **Behoben:** Übergroße Archivinhalte vor dem Lesen ablehnen und Dateien über begrenzte Streams aufbereiten.
- **Behoben:** Host-Code bei Integration erhalten und Plattformkonflikte ohne Erhöhung der Mindestversionen melden.
- **Sonstiges:** Zweisprachige Dokumentation, private Sicherheitsmeldungen über Host-Repositories und dokumentierte Datenzuordnung.

### 0.3.0 · 2026-10-01

- **Neu:** Vierzehn freigegebene Plugins, zwölf lokale Original-Icons und datierte GitHub-Sterne.
- **Verbessert:** Explizite Multisite-Anforderungen und aktualisierte Release-Quellen.

### 0.2.0

- **Neu:** Zusätzliche Katalogeinträge, lokale Produkt-Icons und GitHub-Sterne als Zahlenstand.

### 0.1.0

- **Neu:** Eingebetteter kuratierter Katalog, geprüfte Installation, separate Aktivierung und optionale Online-Freigaben.


