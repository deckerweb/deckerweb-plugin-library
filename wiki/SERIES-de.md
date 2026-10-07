# Serien und Katalogfilter

[English](SERIES)

Produktfamilien werden ausdrücklich über die optionale Liste series_memberships zugeordnet: quicknav, builder, purify, manage-content und connect. Das ältere Feld series bleibt als Hauptzuordnung für ältere Hosts erhalten; neue Leser akzeptieren auch Metadaten mit alleiniger Einzelzuordnung. Unbekannte, doppelte oder widersprüchliche Zuordnungen werden vollständig abgelehnt. Namen bestimmen die Zugehörigkeit nicht. Der Katalog enthält 17 geprüfte Plugins und die unten beschriebene Connect-Vorschau: QuickNav 5, Builder 7, Purify 3, Inhalte verwalten 4. Die vier Inhaltsplugins gehören zu Builder und Inhalte verwalten; Plugin Submenu Mover zu Builder. Brand Admin Schemes und Daily Scripture bleiben eigenständig. Jede Karte erscheint einmal und zeigt alle passenden Badges.

Serienfilter bleiben mit Suche und „Passt zu meiner Installation“ kombinierbar. „Alle“ hebt nur die Serie auf; „Filter zurücksetzen“ löscht sämtliche Filter. GET-Bedienelemente funktionieren ohne JavaScript, per Tastatur und im Netzwerk-Kontext. Kategorien und Originalicons bleiben erhalten; keine dauerhaft gespeicherte Auswahl und keine zusätzliche Sortierung.

Connect for Shopware startet die Connect-Serie als ausdrücklich freigegebene Vorschau der geplanten Version 1.0.0. Bis das stabile Release-ZIP veröffentlicht und geprüft ist, zeigt die Karte einen Vorbereitungshinweis und bietet keine Installation, Aktivierung oder Updates an. Es gibt 18 sichtbare Einträge und 17 geprüfte Paketangebote. Das Originalicon wird lokal mitgeliefert. Vorläufige Voraussetzungen stammen aus dem gepinnten öffentlichen Entwicklungsheader, nicht aus einem ungeprüften stabilen Release.

Nach Veröffentlichung mit tools/refresh-catalog.py --include-preparing --output NEUER_ORDNER --revision REVISION exakt den freigegebenen ersten stabilen Release 1.0.0 prüfen. ZIP-Identität, Prüfsumme, endgültige Mindeststände und übersetzte Texte kontrollieren, danach das freigegebene JSON veröffentlichen. Kein weiterer Library-Build nötig. Der Connect-Eintrag verwendet series_memberships ohne altes series-Feld, damit ältere Leser keine unbekannte Hauptserie ablehnen.

Werkzeuge und Shop sind ab Library 0.8.0 verfügbar. Tools for FluentCart gehört zu beiden. Das zusätzliche Feld series_memberships_v2 enthält diese Zuordnungen; ältere Leser ignorieren es und bieten die Karte weiterhin ohne Serie an. Die bisherigen Felder enthalten nur ältere unterstützte Serien.
