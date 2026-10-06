=== deckerweb Plugin Library ===
Requires at least: 6.4
Requires PHP: 8.0
Stable tag: 0.6.0
License: GPLv2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html

== Description ==
A small embedded catalog for directly distributed WordPress plugins. Only explicitly approved GitHub releases appear under Plugins → Add New → deckerweb. This is an embedding kit, not a standalone installable plugin.

Requirements: WordPress 6.4+, PHP 8.0+, ZipArchive for installation. GPL-2.0-or-later. Only direct-distribution builds; exclude Library and deckerweb Updater entirely from WordPress.org builds.

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
Library settings are shared per network and the introduction is per user. Network actions require appropriate capabilities and dependencies. Bricks QuickNav retains its per-site restriction pending separate host work; Daily follows its published release policy.

= How do I report a vulnerability? =
Use Security → Advisories → Report a vulnerability in the host plugin repository. Include host and Library versions; do not post security details in public issues. Hosts must enable private reporting before publication.

== Changelog ==
### 0.6.0 · 2026-10-06

- **Neu:** Freigegebene Plugin-Releases können im Online-Katalog erscheinen, ohne die eingebettete Library auszutauschen.
- **Neu:** Purify WPCode Lite und Purify WPForms Lite im Katalog entdecken.
- **Neu:** Plugins können mehreren Serien angehören, darunter Inhalte verwalten.
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


