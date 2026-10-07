# Inline-Installation

[English](INLINE.md)

Library 0.7.0 installiert und aktiviert Katalogplugins direkt in ihrer Karte, ohne die Seite zu verlassen. Suche, Serienfilter und Scrollposition bleiben erhalten. Installation und Aktivierung sind getrennte Aktionen. Fehler erscheinen als Klartext neben der Aktion; ein erneuter Versuch ist möglich. Benötigte Dateisystem-Zugangsdaten werden im nativen WordPress-Dialog angefragt. Sie bleiben im Seitenspeicher von WordPress, ohne zusätzliche Library-Speicherung. Ohne JavaScript wird der vorhandene geprüfte Formular-Installer verwendet.

Jede Aktion prüft Berechtigungen, Nonce, Netzwerkbereich, frische Freigabe und Abhängigkeiten. Installation prüft weiterhin Original-ZIP-Hash, Archiv und Identität. Eine installationsweite Aktionssperre verhindert gleichzeitige Änderungen am selben Katalogplugin. Bei unerwarteter Aktivierungsausgabe oder Verbindungsabbruch muss vor einem erneuten Versuch der installierte Plugin-Status geprüft werden.
