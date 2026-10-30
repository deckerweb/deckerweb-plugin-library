# Data and lifecycle

[Deutsch](DATA-de)

Settings and managed-install records use `deckerweb_library_settings_v1` and `deckerweb_library_installed_v1`: network options on Multisite, regular options on a single site. The optional settings-deletion switch defaults off. Introduction state uses global user meta `deckerweb_library_intro_seen_v1`.

Personal preferences use `deckerweb_library_view_v1`: search, series, compatibility, status, sort order and random seed. Reset filters clears the filters, not the chosen sort or random sequence. Conflict-notice dismissal stores a local fingerprint in `deckerweb_git_updater_notice_v1`. Diagnostic copies exclude personal searches, credentials and site content.

Catalog cache keys are `dwl_catalog_<URL-md5>_061` for display (24 hours) and the same base plus `_updates` for host update metadata (12 hours). Both have `_last` (48 hours) and `_retry` (15 minutes) companions. These are site transients; on Multisite they are network-scoped. `deckerweb_library_cache_keys_v2` tracks keys for cleanup. Fresh package approval bypasses display/update caches; failed fresh approval does not authorize a package. No Library cron event or persistent updater credential is added.

Downloads and normalization use Library-prefixed temporary files and tracked staging directories in `deckerweb_library_temp_v2`. Normal completion removes them. Final-host uninstall removes tracked crash leftovers within the current temporary directory. Inline actions use a non-autoloaded `dwl_inline_lock_<slug>` option on the main site of the main network, or the single site. Requests release their own tokens on completion/shutdown; abandoned locks can recover after 15 minutes. The Library does not save filesystem credentials.

Deactivation preserves data. Uninstall preserves shared data while any other physical host remains installed, including inactive hosts. Final-host uninstall cleans component caches, key registry, locks and tracked temporary artifacts across network scopes. Settings and install records remain unless optional deletion is enabled. Global user preferences, introduction and notice state are removed only when all relevant network scopes permit settings deletion. Installed plugins, their content, host settings and other plugins’ data are never removed by Library cleanup.

Hosts must call the current `deckerweb_library_uninstall_v3` contract. Old hosts continue to use their own cleanup code; the Library does not rewrite them. New sites inherit network settings without per-site initialization. Legacy data is retained; bookkeeping is created as needed. There is no separate bulk settings export/import.

