# Online catalog and independent updates

[Deutsch](CATALOG-de.md)

Enable the optional online catalog in Settings → deckerweb Library (network settings in Multisite). The public catalog is available at `https://raw.githubusercontent.com/deckerweb/deckerweb-plugin-library/main/catalog/catalog.json`. This address is prefilled; online retrieval remains optional and off by default. Only HTTPS JSON sources under raw.githubusercontent.com/deckerweb are accepted.

The display cache lasts 24 hours, shared by all embedded hosts in the current site/network. A request after expiry refreshes it; low-traffic sites have no guaranteed refresh time. Refresh catalog performs a manual check. Installed-plugin update checks use an independent 12-hour cache; native manual force checks bypass it. Neither interval overrides WordPress scheduling. Cached valid metadata remains available for up to 48 hours on failure, with a 15-minute retry delay. Installation/update approval always requires a successful fresh read. A valid empty catalog withdraws all offers; an invalid catalog cannot approve a package.

The public document keeps schema_version: 1 and plugins, adding catalog_revision, generated_at and requires_library. Revision tracks approved metadata independently of Library code. Runtime checks reject an unsupported Library minimum. Existing entry fields, approvals, repository/ZIP identity, platform and dependency metadata, series and checksums remain mandatory. No remote executable code or icons are loaded; artwork stays local to the embedded component.

Prepare a candidate on the operator machine with tools/refresh-catalog.py --output NEW_DIRECTORY --revision REVISION. It reads only repositories already approved in the bundled catalog, checks stable release ZIP identity and hashes, and writes review.json. A server-only DECKERWEB_CATALOG_GITHUB_TOKEN is optional; never distribute it. Review localized text, dependency/network requirements and icon changes. Export the exact reviewed candidate with tools/approve-catalog.py CANDIDATE DESTINATION --sha256 REVIEWED_HASH. Both tools stop before publication. Publish the approved JSON separately to the chosen endpoint; retain older revisions for rollback. A plugin release alone never grants approval.

Read the source record and [Updater integration](UPDATER.md). Existing installed hosts retain their own Update URI and authentication behavior.

Keep the schema-1 endpoint compatible for existing hosts. Do not increase requires_library merely because a newer host includes a newer component. If a future metadata format requires incompatible values, provide a compatible older feed until those hosts can migrate; this prevents the catalog from blocking its own host update.

Series metadata is additive: series retains a legacy primary membership (quicknav, builder or purify), while series_memberships lists all explicit memberships, including manage-content. Older readers can keep using the primary field. A plugin appears once in the catalog and in every matching series filter.

Daily Scripture uses network_activation=false as the protective legacy policy and network_activation_min_version=1.0.0 as the versioned approval understood by Library 0.6.1. The minimum policy takes precedence in capable readers and checks the installed version; older readers retain their block. Daily 1.0.1 carries the new runtime needed for cold activation beside old copies.


## Catalog revision 2026-10-07.4

20 approved plugins. Redirect Draft Content 0.9.0 joins Manage Content (RDC). Tools for FluentCart 0.9.0 is temporarily unassigned (TFC); Tools and Shop will follow in a later component update. Both entries are accepted by Library 0.6.0 and 0.7.0 and require WordPress 7.1.2/PHP 8.2 as published. Older hosts use RDC/TFC text fallbacks until their local icons are updated. All catalog labels are present and unique. Component release ZIPs remain unchanged.

