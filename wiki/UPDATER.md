# Optional public updater bridge

[Deutsch](UPDATER-de.md)

The installed host remains the owner of its updater. The Library never silently replaces its Update URI handler. Public catalog callbacks are optional; private repositories keep their authentication provider and are not part of this public feed.

The authoring kit includes integration/updater-v2.1-dev.3-catalog-provider.patch, based on the separately maintained V2.1-dev.3 engine. Apply it to that exact source in a reviewed integration; it is an integration patch, not a newly released canonical updater. It adds SUPPORTS_CATALOG_PROVIDER and optional release_provider/package_provider constructor options. Both callbacks are required together and rejected in private mode. Existing public/private behavior, local artwork, detail dialogs and source selection are retained when the options are absent.

After requiring the Library bootstrap and the host updater, guard configuration with defined(Updater::class . '::SUPPORTS_CATALOG_PROVIDER'). For public hosts merge deckerweb_library_updater_options_v1(HOST_MAIN_FILE, EXACT_REPOSITORY_URL) into existing updater options without replacing the host translator or artwork. The lazy callbacks work even before Library election. No updater hooks are registered by the bridge; the host still registers its own updater once.

Release callback: (repository URL, plugin basename, fresh boolean) returns false to retain direct GitHub mode while the online catalog is disabled or a capable runtime is unavailable, null to refuse an unapproved/unverified release, or validated release data. Refusal never falls back to GitHub while online catalog mode is active. The normal provider uses the separate update cache. Package callback: (repository URL, plugin basename, offered package URL) returns a bounded, hash-verified temporary archive or WP_Error after fresh approval and dependency checks. An earlier handled download is preserved, and another host/plugin is never intercepted.

The patch does not change any existing host, private credential, repository or released updater artifact. Integrate against the current updater project source and test mixed copies and native single/bulk updates before a host release. Do not apply it blindly to another updater version.

Merge integration/updater-catalog-translations.json into the host translator resources; the component also ships these source messages in its host-domain bundle. Private-mode configuration errors remain developer-facing. The exact tested base source hash and patch handoff are recorded separately for operator review.
