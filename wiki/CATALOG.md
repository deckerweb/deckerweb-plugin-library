# Online catalog and independent updates

[Deutsch](CATALOG-de)

Enable the optional online catalog in Settings → deckerweb Library (network settings in Multisite). The public catalog is available at `https://raw.githubusercontent.com/deckerweb/deckerweb-plugin-library/main/catalog/catalog.json`. This address is prefilled; online retrieval remains optional and off by default. Only HTTPS JSON sources under raw.githubusercontent.com/deckerweb are accepted.

The display cache lasts 24 hours, shared by all embedded hosts in the current site/network. A request after expiry refreshes it; low-traffic sites have no guaranteed refresh time. Refresh catalog performs a manual check. Installed-plugin update checks use an independent 12-hour cache; native manual force checks bypass it. Neither interval overrides WordPress scheduling. Cached valid metadata remains available for up to 48 hours on failure, with a 15-minute retry delay. Installation/update approval always requires a successful fresh read. A valid empty catalog withdraws all offers; an invalid catalog cannot approve a package.

The public document keeps schema_version: 1 and plugins, adding catalog_revision, generated_at and requires_library. Revision tracks approved metadata independently of Library code. Runtime checks reject an unsupported Library minimum. Existing entry fields, approvals, repository/ZIP identity, platform and dependency metadata, series and checksums remain mandatory. No remote executable code or icons are loaded; artwork stays local to the embedded component.

Prepare a candidate on the operator machine with tools/refresh-catalog.py --output NEW_DIRECTORY --revision REVISION. It reads only repositories already approved in the bundled catalog, checks stable release ZIP identity and hashes, and writes review.json. A server-only DECKERWEB_CATALOG_GITHUB_TOKEN is optional; never distribute it. Review localized text, dependency/network requirements and icon changes. Export the exact reviewed candidate with tools/approve-catalog.py CANDIDATE DESTINATION --sha256 REVIEWED_HASH. Both tools stop before publication. Publish the approved JSON separately to the chosen endpoint; retain older revisions for rollback. A plugin release alone never grants approval.

Read the source record and [Updater integration](UPDATER). Existing installed hosts retain their own Update URI and authentication behavior.

Keep the schema-1 endpoint compatible for existing hosts. Do not increase requires_library merely because a newer host includes a newer component. If a future metadata format requires incompatible values, provide a compatible older feed until those hosts can migrate; this prevents the catalog from blocking its own host update.

Series metadata is additive: series retains a legacy primary membership (quicknav, builder or purify), while series_memberships lists all explicit memberships, including manage-content. Older readers can keep using the primary field. A plugin appears once in the catalog and in every matching series filter.

Connect for Shopware starts the Connect series as an explicitly approved preview of planned version 1.0.0. Until its stable release ZIP is published and verified, its card is visible with a preparation notice and cannot install, activate or offer an update. There are 18 visible entries and 17 verified package offers. The original icon is bundled locally. Preliminary requirements come from the pinned public development header, not an unverified stable release.

After publication, use tools/refresh-catalog.py --include-preparing --output NEW_DIRECTORY --revision REVISION to review exactly the authorized first stable release 1.0.0. Verify ZIP identity, checksum, final platform requirements and localized text, then publish the approved JSON. No new Library build is needed. The Connect entry uses series_memberships without a legacy series field so older readers do not reject an unknown primary series.
