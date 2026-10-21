# Prüfstand 1.1.0

[English](VALIDATION-1.1.0)

Prüfstand zur freigegebenen Version 1.1.0. WordPress 7.1.2 / PHP 8.4.5 mit isolierten SQLite-Einzel- und Netzwerkinstallationen.

Am tatsächlich eingebetteten Referenz-ZIP geprüft: 27 freigegebene Originalpakete und lokale Icons, strenge Katalogprüfung einschließlich Leser 0.6.0–1.0.0, Eingabebereinigung und kontextgerechte Ausgabeabsicherung, Ablehnung ungültiger Nonces und unzureichender Rechte, wiederholte persönliche Sortierung, lokale Diagnose, Deutsch/Du und Deutsch/Sie, Kartenhervorhebung mit Maus und Tastatur, reduzierte Bewegung, mobile Ansicht und Schließen des Verlaufsdialogs. Mischbetrieb älterer/neuer Komponenten sowie Netzwerkeinstellungen und Übernahme auf neuen Websites bestanden.

Offizielles Plugin Check 2.1.0 im Host-Kontext ausgeführt. Statische Library-Befunde gegenüber 1.0.0 von 106 auf 34 verringert; die verbleibenden Meldungen benötigen Kontextbewertung und bedeuten keine 34 bestätigten Sicherheitslücken. Explizite Laufzeitprüfungen zum Geltungsbereich geladener Assets endeten ohne Befund; der vollständige verfügbare statische/Laufzeit-Prüfsatz wurde ebenfalls ausgeführt. Keine Regeln global abgeschaltet. Host und Updater haben getrennte Befunde außerhalb dieser Komponentenprüfung.

Zusätzlich geprüft: zwei aufeinanderfolgende native Updates mit aktivem Git Updater 14.4.2 und vollständigen Browser-Anfragen. Der eigene aktionsgebundene Nonce bleibt verpflichtend; zusätzlich wird der WordPress-Updates-Nonce übermittelt. Gleichwertige GitHub-Quellarchivangebote werden ausschließlich bei identischer Repository-, Plugin-, Versions- und Tagidentität akzeptiert. Installiert wird weiterhin nur das freigegebene, hashgeprüfte Katalogpaket. Abweichende Angebote werden abgelehnt; der temporäre Angebotsfilter wird nach der Aktion entfernt.

Der anschließende Praxistest auf einer Local-Installation mit WordPress 7.1.3 und aktivem Git Updater wurde vom Tester bestätigt: zunächst Quick Edit Featured Image und Post Author Taxonomy, anschließend Portfolio Content und Purify WPCode Lite erfolgreich aktualisiert. Dieser gemeldete Praxistest ergänzt die isolierten Prüfungen; er ersetzt keinen vollständigen Test aller Hosting-Konfigurationen.

Zwei warme lokale Kataloglesevorgänge verursachten in der gemessenen Testumgebung keine SQL-Abfrage und keinen HTTP-Aufruf. Dies ist eine gezielte Messung, kein allgemeiner Hosting-Benchmark. Keine externen Icon-Abfragen.

Nicht neu nachgewiesen: Ausführung unter PHP 8.0, frischer WordPress-6.4-Lauf, echte FTP-/SSH-Zugangsdaten und Übertragungen, historische GitHub-Updater-Varianten oder vollständige Funktionen lizenzpflichtiger Builder. Bisherige Komponentenuntergrenzen WordPress 6.4 / PHP 8.0 bleiben erhalten; Host-/Updateranforderungen können höher liegen. Integration auf einer Testinstallation mit Sicherung prüfen.
