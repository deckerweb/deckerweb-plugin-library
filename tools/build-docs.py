#!/usr/bin/env python3
"""Generate synchronized readmes, topic FAQ, history and local Wiki sources."""
from pathlib import Path
import json,shutil,re
kit=Path(__file__).resolve().parents[1];docs=kit/'docs';content=json.loads((docs/'content.json').read_text());history=json.loads((kit/'lib/history.json').read_text());labels={'New':'Neu','Improved':'Verbessert','Fixed':'Behoben','Misc':'Sonstiges'};wiki=kit/'wiki';wiki.mkdir(exist_ok=True)
for lang in ['en','de']:
 suffix=''if lang=='en'else'-de';other='[Deutsch](README-de.md)'if lang=='en'else'[English](README.md)';faqs='\n\n'.join('### '+q['question'][lang]+'\n\n'+q['answer'][lang]for q in content['faq']);changes=''
 for r in history:
  changes+='### '+r['version']+(' · '+r['date']if r['date']else'')+'\n\n'
  for cat in ['New','Improved','Fixed','Misc']:
   for entry in r['changes'].get(cat,[]):changes+='- **'+(cat if lang=='en'else labels[cat])+':** '+entry[lang]+'\n'
  changes+='\n'
 heading=lambda en,de:en if lang=='en'else de
 readme='# deckerweb Plugin Library\n\n'+other+'\n\n![deckerweb Library](assets-github/banner-'+lang+'.png)\n\n## About\n\n'+content['intro'][lang]+'\n\n**'+heading('Version','Version')+':** '+content['version']+' · WordPress ≥ 6.4 · PHP ≥ 8.0\n\n'+heading('[Documentation](docs/INTEGRATION.md) · [FAQ by topic](docs/FAQ.md) · [Security](SECURITY.md)','[Dokumentation](docs/INTEGRATION-de.md) · [Fragen nach Themen](docs/FAQ-de.md) · [Sicherheit](SECURITY-de.md)')+'\n\n## '+heading('Contents','Inhalt')+'\n\n- [At a Glance](#at-a-glance)\n- ['+heading('Installation','Einbindung')+'](#installation)\n- ['+heading('Features','Funktionen')+'](#features)\n- [FAQ](#faq)\n- [Changelog](#changelog)\n- ['+heading('Author and scope','Autor und Umfang')+'](#author)\n- ['+heading('Support','Unterstützung')+'](#support)\n\n<a id="at-a-glance"></a>\n## At a Glance\n\n'+heading('- Selected public GitHub releases with local icons and clear requirements.\n- Search, product-family filters and installation compatibility.\n- Optional daily online catalog; independent installed-plugin update checks.','- Ausgewählte öffentliche GitHub-Releases mit lokalen Icons und klaren Voraussetzungen.\n- Suche, Serienfilter und passende Voraussetzungen.\n- Optionaler täglicher Online-Katalog; unabhängige Updateprüfungen installierter Plugins.')+'\n\n<a id="installation"></a>\n## '+heading('Installation and first steps','Einbindung und erste Schritte')+'\n\n'+content['integration'][lang]+'\n\n<a id="features"></a>\n## '+heading('Main features','Hauptfunktionen')+'\n\n### '+heading('Discover suitable plugins','Passende Plugins finden')+'\n\n'+heading('Use the deckerweb tab under Plugins → Add New. Combine search, QuickNav/Builder/Purify/Manage Content/Connect and Fits my installation. Each card explains missing requirements; installation and activation remain separate.','Den deckerweb-Tab unter Plugins → Installieren öffnen. Suche, QuickNav/Builder/Purify/Manage Content/Connect und „Passt zu meiner Installation“ kombinieren. Jede Karte erklärt fehlende Voraussetzungen; Installation und Aktivierung bleiben getrennt.')+'\n\n### '+heading('Approved catalog updates','Freigegebene Katalogupdates')+'\n\n'+heading('The public GitHub catalog address is prefilled. Enable online retrieval in Library settings. Discovery is cached for 24 hours. Approved plugin releases can change without replacing Library code. [Catalog guide](docs/CATALOG.md).','Die öffentliche GitHub-Katalogadresse ist vorausgefüllt. Online-Abfragen in den Library-Einstellungen aktivieren. Die Anzeige wird 24 Stunden gespeichert. Freigegebene Plugin-Releases können sich ohne Austausch des Library-Codes ändern. [Kataloganleitung](docs/CATALOG-de.md).')+'\n\n### '+heading('Shared preferences and safe packages','Gemeinsame Einstellungen und sichere Pakete')+'\n\n'+heading('Installed hosts share settings; deactivation preserves data. Fresh release approval, checksums and archive checks guard package actions. [Data](docs/DATA.md) · [Updater integration](docs/UPDATER.md).','Installierte Hosts teilen Einstellungen; Deaktivieren erhält Daten. Frische Freigabe, Prüfsummen und Archivprüfung schützen Paketaktionen. [Daten](docs/DATA-de.md) · [Updater-Einbindung](docs/UPDATER-de.md).')+'\n\n## FAQ\n\n'+faqs+'\n\n'+heading('[Complete FAQ by topic](docs/FAQ.md).','[Vollständige Fragen nach Themen](docs/FAQ-de.md).')+'\n\n<a id="changelog"></a>\n## '+heading('Changelog','Änderungsverlauf')+'\n\n'+changes+'<a id="author"></a>\n## '+heading('Author and scope','Autor und Umfang')+'\n\n'+heading('Developed and published by David Decker — DECKERWEB. A shared embedded component for direct-distribution plugins, not a standalone WordPress.org plugin.','Entwickelt und herausgegeben von David Decker — DECKERWEB. Gemeinsame eingebettete Komponente für direkt vertriebene Plugins, kein eigenständiges WordPress.org-Plugin.')+'\n\n<a id="support"></a>\n## '+heading('Issues, security and support','Fragen, Sicherheit und Unterstützung')+'\n\n'+heading('Use the embedding host repository for ordinary issues and questions, and its private reporting channel for security details.','Normale Fehler und Fragen im Repository des einbettenden Hosts melden; Sicherheitsdetails über dessen privaten Meldeweg.')+' '+heading('[Security policy](SECURITY.md).','[Sicherheitsrichtlinie](SECURITY-de.md).')+'\n\n[Ko-fi](https://ko-fi.com/deckerweb) · [Buy Me a Coffee](https://buymeacoffee.com/daveshine) · [PayPal](https://paypal.me/deckerweb)\n\n## Copyright & License\n\nCopyright © 2026 David Decker — DECKERWEB. GPL-2.0-or-later. '+heading('[License](LICENSE) · [Artwork and provenance](docs/ASSETS.md).','[Lizenz](LICENSE) · [Grafiken und Herkunft](docs/ASSETS-de.md).')+'\n'
 if lang=='de':readme=readme.replace('## About\n','## Über die Library\n').replace('## At a Glance\n','## Auf einen Blick\n').replace('[At a Glance]','[Auf einen Blick]').replace('## Copyright & License\n','## Copyright und Lizenzen\n')
 (kit/('README'+suffix+'.md')).write_text(readme)
 full=''
 for topic in content['full_faq']:
  full+='## '+topic[lang]+'\n\n'+'\n\n'.join('### '+q['question'][lang]+'\n\n'+q['answer'][lang]for q in topic['items'])+'\n\n'
 for name,title,body in [('FAQ',heading('FAQ by topic','Fragen nach Themen'),full),('CHANGELOG',heading('Changelog','Änderungsverlauf'),changes)]:
  link=f'[Deutsch]({name}-de.md)'if lang=='en'else f'[English]({name}.md)';(docs/(name+suffix+'.md')).write_text('# '+title+'\n\n'+link+'\n\n'+body+'\n')
 for name,pages in content['pages'].items():
  page=pages[lang];link=f'[Deutsch]({name}-de.md)'if lang=='en'else f'[English]({name}.md)';(docs/(name+suffix+'.md')).write_text('# '+page['title']+'\n\n'+link+'\n\n'+page['body']+'\n')
 for name in ['FAQ','CHANGELOG','INTEGRATION','DATA','CATALOG','UPDATER','SERIES','TESTING']:
  text=(docs/(name+suffix+'.md')).read_text().replace('../SECURITY','SECURITY');(wiki/(name+suffix+'.md')).write_text(text)
 shutil.copyfile(kit/('SECURITY'+suffix+'.md'),wiki/('SECURITY'+suffix+'.md'))
 (wiki/'assets').mkdir(exist_ok=True);shutil.copyfile(kit/'assets-github'/('banner-'+lang+'.png'),wiki/'assets'/('banner-'+lang+'.png'))
 (wiki/('Home'+suffix+'.md')).write_text('# deckerweb Plugin Library\n\n'+('[Deutsch](Home-de)'if lang=='en'else'[English](Home)')+'\n\n![Library](assets/banner-'+lang+'.png)\n\n'+content['intro'][lang]+'\n\n'+heading('Small plugins. Practical improvements.','Kleine Plugins. Konkrete Verbesserungen.')+'\n\n'+ '\n'.join('- ['+name+']('+name+suffix+')'for name in ['INTEGRATION','SERIES','CATALOG','FAQ','DATA','UPDATER','CHANGELOG','TESTING','SECURITY'])+'\n')
(wiki/'_Sidebar.md').write_text('## deckerweb Plugin Library\n\n[English](Home) · [Deutsch](Home-de)\n\n'+ '\n'.join('- ['+name+' EN]('+name+') · [DE]('+name+'-de)'for name in ['INTEGRATION','SERIES','CATALOG','FAQ','DATA','UPDATER','CHANGELOG','TESTING','SECURITY'])+'\n')
# An authoring reference only: external installer components remain excluded from WordPress.org.
(kit/'readme.txt').write_text('=== deckerweb Plugin Library ===\nRequires at least: 6.4\nRequires PHP: 8.0\nStable tag: '+content['version']+'\nLicense: GPLv2 or later\nLicense URI: https://www.gnu.org/licenses/gpl-2.0.html\n\n== Description ==\n'+content['intro']['en']+'\n\nEmbedded component for direct distribution only; not a standalone WordPress.org submission.\n\n== Installation ==\nSee README.md and docs/INTEGRATION.md.\n\n== Frequently Asked Questions ==\n'+ '\n\n'.join('= '+q['question']['en']+' =\n'+q['answer']['en']for q in content['faq'])+'\n\n== Changelog ==\n'+changes+'\n')

# Wiki routes omit Markdown suffixes; repository-only files keep explicit links.
repository = 'https://github.com/deckerweb/deckerweb-plugin-library/blob/main/'
for page in wiki.glob('*.md'):
 text = page.read_text()
 def wiki_link(match):
  label, target = match.groups()
  if target.startswith(('https://', '#')):
   return match[0]
  if target.startswith('assets/'):
   target = 'https://raw.githubusercontent.com/wiki/deckerweb/deckerweb-plugin-library/' + target
  elif target.endswith('.md'):
   name = Path(target).name[:-3]
   target = name if (wiki / (name + '.md')).exists() else repository + ('docs/' if not target.startswith('../') else '') + Path(target).name
  return '[' + label + '](' + target + ')'
 text = re.sub(r'\[([^\]]*)\]\(([^)]+)\)', wiki_link, text)
 page.write_text(text)
