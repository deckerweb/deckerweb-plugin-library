# Fragen nach Themen

[English](FAQ.md)

## Einstieg

### Wo ist der Katalog?

Plugins → Plugin hinzufügen → deckerweb öffnen. WordPress.org bleibt die Standardansicht.

### Werden externe Dienste kontaktiert?

Die lokale Ansicht nicht. Installation lädt das ausgewählte GitHub-Release. Optionale Online-Freigaben kontaktieren die konfigurierte eigene HTTPS-Quelle; deren Server sieht die anfragende IP-Adresse. Website-URL, Nutzer-ID, Plugin-Inventar und Telemetrie werden nicht übertragen.

## Voraussetzungen und Installation

### Warum ist eine Installation nicht verfügbar?

Die Karte zeigt fehlende oder inaktive Abhängigkeiten sowie WordPress-/PHP-Anforderungen. Voraussetzungen werden nicht automatisch installiert; Aktivierung ist ein eigener Schritt.

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

Library-Einstellungen gelten je Netzwerk, der Einführungshinweis je Nutzer. Netzwerkaktionen erfordern passende Berechtigungen und Abhängigkeiten. Bricks QuickNav behält bis zur separaten Host-Anpassung seine Website-Beschränkung; Daily folgt den veröffentlichten Release-Regeln.

### Wie wird eine Sicherheitslücke gemeldet?

Im Host-Plugin-Repository Security → Advisories → Report a vulnerability verwenden. Host- und Library-Version nennen; Sicherheitsdetails nicht in öffentlichen Issues posten. Hosts müssen den privaten Meldeweg vor Veröffentlichung aktivieren.


