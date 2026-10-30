# Inline-Installation

[English](INLINE)

Library 1.2.0 installiert, aktiviert und aktualisiert Katalogplugins in ihren Karten. Installation und Aktivierung bleiben getrennt. Persönliche Filter und Sortierung bleiben verfügbar; erfolgreiche Aktionen erneuern Kartenstatus und Trefferzahl. Eine Karte kann nach der Aktion verschwinden, wenn sie nicht mehr zum gewählten Status passt. Tastaturfokus wechselt bei Bedarf auf ein geeignetes verbleibendes Bedienelement oder die Trefferzahl.

Jede Aktion prüft Rechte, Aktions-Nonce, Netzwerkbereich, zutreffende Voraussetzungen und Releasefreigabe. Downloads behalten Original-SHA256-, Archiv- und Identitätsprüfung. Eine temporäre installationsweite Sperre verhindert parallele Änderungen am selben Plugin. Nach unterbrochenen Anfragen prüft die Statuswiederherstellung das tatsächliche Ergebnis, ohne erfolgreiche Schreibvorgänge automatisch zu wiederholen. Fehlgeschlagene oder unbestätigte Aktionen erscheinen nicht als Erfolg.

Benötigte Dateisystem-Zugangsdaten fragt WordPress im nativen Dialog ab; die Library speichert sie nicht zusätzlich. FTPS wurde mit 1.2.0 erfolgreich durch einen Nutzer getestet; SSH bleibt ungetestet. Ohne JavaScript bleiben native Formularwege im Admin; Updates mit Zugangsdaten können die Pluginverwaltung nutzen. Siehe [Tests](TESTING-de) und [Prüfstand](VALIDATION-1.2.0-de).

Fehler nennen verfügbare bereinigte Katalog-/Download-/Prüfursachen. Ein Fremd-Updater kann eigene Meldungen anzeigen. Veraltete Angebote vor erneutem Versuch aktualisieren; verweigerte Freigaben oder Prüfsummenfehler nicht umgehen.

