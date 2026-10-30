# Oxygen-QuickNav-Kompatibilität

[English](OXYGEN.md)

Aktuell freigegebene Releases stehen mit ihren Versionen im [Katalog](SERIES-de.md). Die folgenden Versionsgrenzen beschreiben Kompatibilitätsregeln, nicht den neuesten Plugin-Release.

Oxygen QuickNav 2.0.0 unterstützt modernes Oxygen und Classic; Einstellungen bleiben ohne Builder erreichbar. dependency_rules sind begrenzte Daten je Abhängigkeit: since_version, optional eine ausschließliche Obergrenze until_version sowie required oder pause. Aktivierung prüft die installierte, Paketprüfung die angebotene Version. Ältere installierte QuickNav-Versionen behalten Pflichtabhängigkeiten. Pausenregeln gelten nur für geprüfte Hosts: Oxygen 2.0.0-rc.1+, Breakdance 2.0.0+, Advanced Scripts QuickNav 1.2.1+, Purify WPCode Lite/Elementor/WPForms Lite 1.1.0+, Bricks QuickNav 2.0.0+, GP Project Export Name 2.0.0+ und GlotFrame 1.0.0+. Fehlende Voraussetzungen werden angezeigt; betroffene Hostfunktionen pausieren. Native Requires-Plugins-Header und Plattformgrenzen bleiben maßgeblich. Keine Ausdrücke und kein nachgeladener Code.
