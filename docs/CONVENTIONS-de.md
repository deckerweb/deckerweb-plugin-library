# Release-Konventionen

[English](CONVENTIONS.md)

Die Komponente verwendet dreiteilige Versionen: neue Funktionen erhöhen Minor, kompatible Fixes Patch. Inkompatible Bootstrap-/Daten-/API-Änderungen benötigen einen dokumentierten Kompatibilitätsplan und eine Major-Entscheidung. Vor 1.0 dürfen Minor-Versionen das Einbindungsverhalten nur mit klaren Migrationshinweisen ändern. Höhere Mindestversionen brauchen eine ausdrückliche Entscheidung; sie sind kein automatischer Integrationsschritt.

Vor Host-Releases aktuelle Library-/Updater-/Footer-Stände, Datenzuordnung, Sprachen und Plattformen abgleichen; aktuellen Host-Code und eigenen Updater erhalten. Nur freigegebenen Katalog und Quellenstände aktualisieren. Abhängigkeiten und installierte Versionen, dann Hashes, Originalpaket-Identität, aktuelle Icons und datierte Sterne prüfen. Installation überschreibt keine vorhandenen Verzeichnisse; Aktivierung bleibt separat. Code fremder Abhängigkeiten wird niemals übernommen.

Gemeinsame öffentliche Inhalte in `docs/content.json`, Laufzeitverlauf in `lib/history.json` pflegen; entsprechende FAQ/Readmes/Changelogs generieren. EN-Kategorien New, Improved, Fixed, Misc; DE Neu, Verbessert, Behoben, Sonstiges. Alle vier vorhandenen Versionen stehen im Verlauf; unbekannte frühere Release-Daten werden nicht erfunden. Vor Veröffentlichung aktuelle GitHub-Regeln und privaten Meldeweg je Host prüfen und das tatsächliche Auslieferungs-ZIP durch die Testliste führen. Die Werkzeuge veröffentlichen nichts.

Dokumentation EN/DE synchron halten. Öffentliche Prozessbezüge bei Bedarf als Plugin-Konventionen, einheitlicher Standard oder gemeinsame Grundlage formulieren. Interne Arbeitsunterlagen nicht öffentlich exportieren.

Der aktuelle Banner leitet sich aus dem bereits freigegebenen Kataloglayout und Original-Produkt-Icons ab, ohne neues Logo. Screenshots bleiben eine Ergänzung niedriger Priorität.
