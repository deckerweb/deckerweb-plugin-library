# Fragen nach Themen

[English](FAQ)

## Einstieg

### Wo ist der Katalog?

Plugins → Plugin hinzufügen → deckerweb öffnen. WordPress.org bleibt die Standardansicht.

### Werden externe Dienste kontaktiert?

Der optionale Katalogabruf lädt den eigenen JSON-Katalog und sendet weder Website-URL noch Pluginliste oder Nutzungsdaten. GitHub erhält Paketabrufe bei der Erstinstallation. Installierte Plugins verwenden die bestehenden normalen Updater-Verbindungen, unabhängig von der Katalogeinstellung. Lokale Icons und Filter lösen keine zusätzlichen Releaseabfragen aus.

## Voraussetzungen und Installation

### Warum ist eine Installation nicht verfügbar?

Die Karte nennt WordPress-/PHP-Anforderungen und den angebotenen Release. Fehlende Mutter-Plugins oder Themes sind bei Katalogversionen mit geprüfter Pausenregel ein Hinweis: Installation und Aktivierung bleiben möglich, während abhängige Funktionen pausieren. Ältere installierte Versionen können noch Pflichtabhängigkeiten haben. Native WordPress-Sperren und Plattformanforderungen gelten weiterhin. Voraussetzungen werden nicht automatisch installiert; Aktivierung ist ein eigener Schritt.

### Kann der Katalog ausgeblendet werden?

Unter Einstellungen → deckerweb Library (bei Multisite in den Netzwerkeinstellungen). Ausblenden erhält Abhängigkeitsprüfungen und normale Pluginupdates. Der Onlineabruf ist eine getrennte Einstellung für Katalogmetadaten und Erstinstallationen.

## Katalog und Updateprüfungen

### Benötigt jeder Plugin-Release eine neue Library?

Nein. Eine freigegebene Online-Katalogrevision kann eine neuere Plugin-Version unabhängig von der eingebetteten Komponente enthalten.

### Warum können Katalog und Updater unterschiedlich aktuell sein?

Der Katalog ist ein geprüfter Stand zum Entdecken und Erstinstallieren mit 24-Stunden-Cache. Updates installierter Plugins folgen dem getrennten normalen WordPress-Updater und dessen bestehenden Prüfungen. Installierte oder regulär angebotene Versionen können deshalb neuer als die Katalogversion sein. Der ältere Katalog stuft sie weder zurück noch blockiert er sie. Beim Stöbern wird kein zusätzlicher Releaseabruf ausgelöst.

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

Plugin-Status → Update verfügbar auswählen. Der Filter verwendet vorhandene WordPress-Updateangebote für installierte Plugins und keinen Vergleich mit Katalogversionen. Suche, Serie und Kompatibilität können kombiniert werden. Ohne vorhandenes Angebot meldet die Karte Kein Update gemeldet; das ist keine Behauptung einer frischen GitHub-Prüfung.

### Was bleibt beim Zurücksetzen der Filter erhalten?

Filter zurücksetzen leert Suche, Serie und Installationskompatibilität und wählt alle Status. Persönliche Sortierung und bestehende Zufallsreihenfolge bleiben erhalten. Neu mischen ändert die Zufallsfolge bewusst. Die Auswahl wird pro WordPress-Benutzer gespeichert.

### Was bedeutet ein Fehler bei der Prüfung?

Library 1.2.0 unterscheidet Katalogprüfung, Paketdownload, Prüfsumme und Archivprüfung. Bereinigte Verbindungs-/TLS-/DNS-/Timeout- oder HTTP-Angaben enthalten keine fremden Antworttexte oder Zugangsdaten. Nach vorübergehenden Serverproblemen Katalog aktualisieren oder erneut versuchen. Eine verweigerte Freigabe wird nicht umgangen. Der separate Host-Updater kann weiterhin eine allgemeinere Meldung zeigen. Siehe [Updater](UPDATER-de) und [Tests](TESTING-de).

## Pluginupdates und Katalogfreigabe

### Begrenzt der Onlinekatalog Pluginupdates?

Nein. Mit Library 1.3.0 und Updater 2.4.0 verwenden installierte Plugins ihren normalen WordPress-Updater, unabhängig von Katalogeinstellung und Katalogversion. Die Library zeigt die tatsächlich installierte Version und vorhandene WordPress-Updateangebote. Eine Katalogversion bestimmt nur das geprüfte Paket für die Erstinstallation. Beim Stöbern gibt es keine zusätzlichen GitHub-Releaseabfragen. Normale Prüfintervalle, Caches und technische Anforderungen gelten weiterhin. Automatische Installation wird dadurch nicht aktiviert. Ältere Komponentenkombinationen können bis zum Update ihr bisheriges Verhalten behalten. Siehe die [Updateanleitung](CATALOG-de#pluginupdates-und-der-onlinekatalog).


