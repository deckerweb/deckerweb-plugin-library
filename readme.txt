=== deckerweb Plugin Library ===
Requires at least: 6.4
Requires PHP: 8.0
Stable tag: 0.7.0
License: GPLv2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html

== Description ==
The deckerweb Plugin Library adds a selected catalog of deckerweb plugins to WordPress. It comes bundled with certain plugins and gives you another way to discover and install useful additions under **Plugins → Add New → deckerweb**. The usual WordPress.org catalog remains the default.

If you found an `includes/deckerweb-plugin-library/` folder inside a plugin, this is the shared component behind that catalog. The plugin author included it deliberately; you do not need to install or configure a separate Library plugin.

This repository contains the reusable PHP component, catalog, integration examples and documentation. It is also open for developers who want to read the code, reuse it under its license or build their own approach.

Installation and activation happen directly in the selected card. Status and errors appear there; search, series filters and scroll position remain. Filesystem credentials use the native WordPress dialog. Without JavaScript, the checked form workflow remains available.

Embedded component for direct distribution only; not a standalone WordPress.org submission.

== Installation ==
See README.md and docs/INTEGRATION.md.

== Frequently Asked Questions ==
= Where is the catalog? =
Open Plugins → Add New → deckerweb. WordPress.org remains the default view.

= Does it contact external services? =
Local browsing does not. Installation downloads the selected GitHub release. Optional online approval updates contact the configured first-party HTTPS endpoint; its server sees the requesting IP. No site URL, user ID, inventory or telemetry is sent.

= Why is an installation unavailable? =
Check the card for missing or inactive dependencies and WordPress/PHP requirements. Prerequisites are not installed automatically; activation is separate.

= Can I hide it? =
Use Settings → deckerweb Library (Network Settings on Multisite). Hiding discovery preserves dependency checks and existing managed updates. Disable online catalog retrieval separately to stop its requests.

= What happens when I remove a host? =
Another installed host, even inactive, preserves shared data. The final host removes temporary Library data and caches. Settings remain unless optional deletion was enabled. Installed plugins and their content remain. Hosts must call the supplied uninstall contract.

= Does it support Multisite? =
Library settings are shared per network. Daily Scripture 1.0.0 and newer support network activation; earlier installed versions must be updated first. Bricks QuickNav retains its per-site restriction. Permissions and dependency checks still apply.

= How do I report a vulnerability? =
Use Security → Advisories → Report a vulnerability in the host plugin repository. Include host and Library versions; do not post security details in public issues. Hosts must enable private reporting before publication.

== Changelog ==
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


