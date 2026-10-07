# Oxygen-QuickNav-Kompatibilität

[English](OXYGEN.md)

Der Katalog bietet den geprüften Release Oxygen QuickNav 2.0.0 an. Installierte 1.0.0-Kopien behalten ihre Anforderung an modernes Oxygen. Ein installiertes Oxygen QuickNav ab 2.0.0-rc.1 folgt seinem ausdrücklichen Host-Vertrag: Aktivierung auf Website oder Netzwerk ist auch ohne Builder möglich; Einstellungen bleiben erreichbar, die Navigation pausiert. Diese Regel für die installierte Version ändert die Anforderungen des angebotenen 1.0.0-Pakets nicht. Ein neuer öffentlicher QuickNav-Release wird erst nach Prüfung seines tatsächlichen ZIPs und seiner Release-Metadaten aufgenommen.

Modernes Oxygen wird anhand von Oxygen-Modus, Laufzeitversion, Builder-Funktion und tatsächlicher aktiver Hauptdatei erkannt; die Funktion muss aus derselben Installation stammen. Breakdance verwendet seinen eigenen Modus. Advanced Scripts wird der Installation seiner geladenen Funktion zugeordnet. Ein nur auf einer Website aktives Plugin belegt keine netzwerkweite Aktivierung. Anzeigenamen allein beweisen keine Aktivierung.

Nach verlorener Inline-Antwort prüft die Library den Plugin-Status, ohne Installation oder Aktivierung zu wiederholen. Bei noch laufender oder unbekannter Aktion erscheint Status prüfen; erst ein bestätigt nicht installiertes Plugin erlaubt einen erneuten Installationsversuch. Die reine Statusabfrage prüft Nonce, Berechtigungen und frische Freigabe, bevor sie eine Aktivierung anbietet. Kein zusätzlicher dauerhafter Inventarcache; WordPress speichert Plugin-Header bereits zwischen.

Die bisherigen Abhängigkeitsfelder bleiben als Schutzwert für ältere Leser erhalten. Library0.8.0 ermittelt die tatsächlichen Voraussetzungen je Zielversion und zeigt das angebotene2.0.0-Paket ohne Builderpflicht. Ältere Libraries können bis zum Update vorsorglich modernes Oxygen verlangen.
