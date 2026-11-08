# Data and lifecycle

[Deutsch](DATA-de)

Shared preferences use `deckerweb_library_settings_v1`, per network on Multisite and regular options on single sites. Online retrieval controls discovery and verified first installations only. Personal view metadata remains `deckerweb_library_view_v1`; Reset filters preserves sort order and random seed. Introduction and conflict-dismissal metadata remain unchanged. Diagnostic copies contain no credentials or site content.

The display cache is `dwl_catalog_<URL-md5>_061` (24 hours), with `_last` (48 hours) and `_retry` (15 minutes). The old `_updates` family is not used to supply installed updates; lifecycle cleanup still recognizes it. `deckerweb_library_cache_keys_v2` inventories cleanup keys. First installation requires fresh approval independent of display cache. No Library cron, persistent credential or additional GitHub release poll is introduced.

Installation history uses independent `deckerweb_library_managed_v2_<SHA256 basename>` records with a read-only legacy `deckerweb_library_installed_v1` fallback. These records no longer authorize update offers or downloads. Current identity is checked before explicit installed actions. Native update offers belong to the normal WordPress/updater state; the Library only prunes its obsolete `dwl_managed` offers.

Own first-installation temporary files and staging directories use independent `deckerweb_library_temp_v3_<SHA256 path>` records, with legacy temp_v2 retained for cleanup. Normal and exception completion remove only owned paths. Uninstall v4 cleans tracked crash leftovers inside the temporary directory. Inline actions retain main-site `dwl_inline_lock_<slug>` locks with token-bound release and 15-minute stale recovery. Filesystem credentials are never stored.

Deactivation preserves data. Another physical installed host, including an inactive one, prevents last-host cleanup. Final-host uninstall clears Library caches, locks and owned temporary artifacts across network scopes. Settings/history remain unless deletion was explicitly enabled; global personal preferences are removed only when all relevant network scopes permit it. Installed plugins, contents, host settings and foreign data are preserved. Hosts must call `deckerweb_library_uninstall_v4`; the Library does not rewrite old hosts.

