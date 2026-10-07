# Series and catalog filters

[Deutsch](SERIES-de)

Explicit product families use the optional series_memberships list: quicknav, builder, purify, manage-content and connect. The legacy series field remains a primary membership for older hosts; new readers accept scalar-only metadata too. Unknown, duplicate or inconsistent memberships are rejected atomically. Names do not determine membership. The catalog contains 17 verified plugins plus the Connect preview below: QuickNav 5, Builder 7, Purify 3, Manage Content 4. The four content plugins belong to both Builder and Manage Content; Plugin Submenu Mover belongs to Builder. Brand Admin Schemes and Daily Scripture remain independent. Each card appears once and carries all relevant badges.

Filters remain combinable with search and Fits my installation. All clears only the series; Reset filters clears every filter. Controls work without JavaScript, use GET and support keyboard/network contexts. Categories and original icons remain unchanged; no persistent selection or additional sorting.

Connect for Shopware starts the Connect series as an explicitly approved preview of planned version 1.0.0. Until its stable release ZIP is published and verified, its card is visible with a preparation notice and cannot install, activate or offer an update. There are 18 visible entries and 17 verified package offers. The original icon is bundled locally. Preliminary requirements come from the pinned public development header, not an unverified stable release.

After publication, use tools/refresh-catalog.py --include-preparing --output NEW_DIRECTORY --revision REVISION to review exactly the authorized first stable release 1.0.0. Verify ZIP identity, checksum, final platform requirements and localized text, then publish the approved JSON. No new Library build is needed. The Connect entry uses series_memberships without a legacy series field so older readers do not reject an unknown primary series.

Tools and Shop are available from Library 0.8.0. Tools for FluentCart belongs to both. The additive series_memberships_v2 field carries these memberships; older readers ignore it and still offer the card without a series. The legacy fields contain only older supported series.
