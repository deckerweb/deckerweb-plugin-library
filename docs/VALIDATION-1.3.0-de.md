# Prüfstand 1.3.0

[English](VALIDATION-1.3.0.md)

Die Komponente wird gemeinsam mit Updater 2.4.0 in isolierten WordPress-Installationen geprüft. Abgedeckt sind Onlineabruf an/aus, veraltete/zukünftige/nicht erreichbare Kataloge, manuell neuere Installationen, normale Updateangebote, native Einzel-/Sammel-/automatische Updates, echte AJAX-Nonces/Berechtigungen, Statuswiederherstellung mit abgesendeter Zielversion und geprüfte Erstinstallation. Kontrollierte Transportantworten und SQLite-Testumgebungen unter WordPress 6.7/7.1.2, PHP 8.1/8.2/8.4 und Multisite. Der vollständige Plugin Check 2.2.0 umfasst statische und Laufzeitprüfungen mit individueller Kontextbewertung; damit wird keine leere Befundliste behauptet. Nativer v4-Uninstall und alte/neue Komponenten-Ladereihenfolgen werden geprüft. Neutrale EN/DE-Komponentenansichten decken 32 lokale Icons, Mobilbreite und Tastatur-Updates ab.

Grenzen: PHP 8.0, WordPress 6.4, echte MySQL-Parallelität und echter SSH2-Dateisystemtransport wurden nicht ausgeführt. Die frühere FTPS-Bestätigung gehört zu 1.2.0. Vorbereitete CI belegt keinen GitHub-Lauf. Keine Kundenseite dient als Testumgebung. Die Host-Einbindung benötigt weiterhin ihre eigene finale Paketprüfung.

