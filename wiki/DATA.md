# Data and lifecycle

[Deutsch](DATA-de)

Settings and managed-install records use `deckerweb_library_settings_v1` and `deckerweb_library_installed_v1` site options (per network on Multisite, regular options on single sites). The settings deletion switch defaults off. Introduction state is the global user-meta key `deckerweb_library_intro_seen_v1`. Settings, records and introduction status are retained by default.

Catalog caches use `_site_transient_dwl_catalog_<URL-md5>` with `_last` and `_retry` companions: 24 hours, 48 hours, 15 minutes. `deckerweb_library_cache_keys_v2` records keys for cleanup of persistent caches and database storage. Package downloads/normalization use Library-prefixed temp files and tracked staging directories in `deckerweb_library_temp_v2`. Normal completion cleans them immediately; final-host uninstall cleans tracked crash leftovers in the current temporary directory. The Library schedules no background tasks.

Deactivation changes none of these data. Removing one host preserves shared data while any other host is installed, even inactive. Final-host uninstall cleans caches/key registry and tracked temporary artifacts. Optional deletion also removes Library settings, install records and introduction status. User introduction status is global: on multiple networks it is only removed when every network's Library settings have been removed. No installed plugin or content is deleted. No host settings or foreign tables/options are touched.

Cleanup covers all networks on final physical host removal and never follows a per-site deactivation. Newly created sites use the network settings automatically; no per-site initialization is required. Existing v1 data are preserved in place; v2 bookkeeping is added lazily. Legacy cache keys stored in the database are cleaned by their exact documented namespace; keys not recorded in an external object cache expire with their TTL.

No large settings export/import is added: the component has only visibility, optional catalog URL/online mode and the deletion switch.

Display cache: dwl_catalog_<URL hash>, 24 hours. Update cache: dwl_catalog_<URL hash>_updates, 12 hours, independently read by WordPress update checks. Both have _last (48 hours) and _retry (15 minutes) companions; the existing shared cache-key registry covers both. Fresh package approval bypasses their caches. No new cron event or permanently stored updater credential is added. Final-host cleanup removes both cache families.
