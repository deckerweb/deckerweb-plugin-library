# Fragen nach Themen

[English](FAQ.md)

## Einstieg

### Wo ist der Katalog?

Plugins → Plugin hinzufügen → deckerweb öffnen. WordPress.org bleibt die Standardansicht.

### Werden externe Dienste kontaktiert?

Die lokale Ansicht nicht. Installation lädt den ausgewählten freigegebenen GitHub-Release. Optionale Online-Abfragen kontaktieren den konfigurierten vertrauenswürdigen öffentlichen GitHub-Katalog; der Server sieht die anfragende IP-Adresse. Die Library überträgt keine Website-URL, Nutzer-ID oder Pluginliste und enthält keine Telemetrie. Der separate Host-Updater kann eigene dokumentierte Anfragen stellen.

## Voraussetzungen und Installation

### Warum ist eine Installation nicht verfügbar?

Die Karte nennt WordPress-/PHP-Anforderungen und den angebotenen Release. Fehlende Mutter-Plugins oder Themes sind bei Katalogversionen mit geprüfter Pausenregel ein Hinweis: Installation und Aktivierung bleiben möglich, während abhängige Funktionen pausieren. Ältere installierte Versionen können noch Pflichtabhängigkeiten haben. Native WordPress-Sperren und Plattformanforderungen gelten weiterhin. Voraussetzungen werden nicht automatisch installiert; Aktivierung ist ein eigener Schritt.

### Kann der Katalog ausgeblendet werden?

Unter Einstellungen → deckerweb Library (bei Multisite in den Netzwerkeinstellungen). Ausblenden erhält Abhängigkeitsprüfungen und bereits eingerichtete Updates. Online-Abrufe separat abschalten.

## Katalog und Updateprüfungen

### Benötigt jeder Plugin-Release eine neue Library?

Nein. Eine freigegebene Online-Katalogrevision kann eine neuere Plugin-Version unabhängig von der eingebetteten Komponente enthalten.

### Warum können Katalog und Updater unterschiedlich aktuell sein?

Die Kataloganzeige wird 24 Stunden gespeichert; installierte Plugins nutzen einen unabhängigen Cache im WordPress-Zyklus. Paketaktionen prüfen die Freigabe frisch.

### Benötigen Nutzer einen GitHub-Token?

Öffentlicher Katalog und Release-Downloads benötigen keine Nutzer-Tokens. Optionale Betreiberzugangsdaten bleiben außerhalb ausgelieferter Dateien.

## Gemeinsame Einstellungen und Daten

### Was passiert beim Entfernen eines Hosts?

Ein weiterer installierter Host erhält gemeinsam genutzte Daten, auch deaktiviert. Der letzte Host bereinigt temporäre Library-Daten und Caches. Einstellungen bleiben ohne ausdrücklich aktivierte Löschoption erhalten. Installierte Plugins und Inhalte bleiben bestehen. Hosts müssen den mitgelieferten Uninstall-Vertrag aufrufen.

### Wird Multisite unterstützt?

Library-Einstellungen gelten je Netzwerk; Katalogansichten sind persönlich. Pluginaktionen berücksichtigen Website-/Netzwerkrechte und den jeweiligen Katalogeintrag. Multisite Toolbar Additions unterstützt Einzelwebsites und Multisite. Daily Scripture erlaubt Netzwerkaktivierung ab Version 1.0.0. Die aktuelle Bricks-QuickNav-Katalogversion hat keine pauschale Sperre auf Website-Aktivierung; themeabhängige Funktionen richten sich weiterhin nach dem aktiven Theme der jeweiligen Website. Der Prüfstand nennt den tatsächlich getesteten Umfang.

### Wie wird eine Sicherheitslücke gemeldet?

Im Host-Plugin-Repository Security → Advisories → Report a vulnerability verwenden. Host- und Library-Version nennen; Sicherheitsdetails nicht in öffentlichen Issues posten. Hosts müssen den privaten Meldeweg vor Veröffentlichung aktivieren.

## Persönliche Filter und Fehlerbehebung

### Wie finde ich Plugins mit verfügbaren Updates?

Plugin-Status → Update verfügbar wählen. Der Filter vergleicht bekannte stabile installierte Versionen mit der freigegebenen Katalogversion. Suche, Serie und Kompatibilitätsfilter gelten zusätzlich; die Trefferzahl berücksichtigt deren Kombination. Es entsteht keine zusätzliche GitHub-Abfrage; fremde WordPress.org-Updates gehören nicht zu diesem Filter.

### Was bleibt beim Zurücksetzen der Filter erhalten?

Filter zurücksetzen leert Suche, Serie und Installationskompatibilität und wählt alle Status. Persönliche Sortierung und bestehende Zufallsreihenfolge bleiben erhalten. Neu mischen ändert die Zufallsfolge bewusst. Die Auswahl wird pro WordPress-Benutzer gespeichert.

### Was bedeutet ein Fehler bei der Prüfung?

Library 1.2.0 unterscheidet Katalogprüfung, Paketdownload, Prüfsumme und Archivprüfung. Bereinigte Verbindungs-/TLS-/DNS-/Timeout- oder HTTP-Angaben enthalten keine fremden Antworttexte oder Zugangsdaten. Nach vorübergehenden Serverproblemen Katalog aktualisieren oder erneut versuchen. Eine verweigerte Freigabe wird nicht umgangen. Der separate Host-Updater kann weiterhin eine allgemeinere Meldung zeigen. Siehe [Updater](UPDATER-de.md) und [Tests](TESTING-de.md).


