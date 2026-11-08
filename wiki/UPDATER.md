# Optional public updater bridge

[Deutsch](UPDATER-de)

## Two separate tasks

Library 1.3.0 uses the reviewed catalog to discover plugins and install a verified package for the first time. Updater 2.4.0 handles installed-plugin releases through the normal WordPress update process. Online catalog preference, catalog version, withdrawal or catalog retrieval failure do not determine the version offered by that updater.

The Library reads the actual installed headers and existing WordPress `update_plugins` offers. Status filters and update buttons use that existing offer. No `wp_update_plugins()` call, GitHub release request or background check is started by rendering Library cards. A normal WordPress check may still be needed before a newly published release appears.

The update button invokes native `Plugin_Upgrader::bulk_upgrade()` for the exact installed basename. As in the Core AJAX updater, the bulk method processes the single selected plugin while preserving activation scope. It does not synthesize an offer, replace the normal package with a catalog asset or impose catalog platform/dependency rules on the new package. Native/updater package identity, offered-version, permissions and actual archive platform checks remain effective. A changed displayed offer is refused until the page is reloaded. Other update providers and their offers remain untouched.

## Integration and older copies

Update both embedded components and retain the pinned class returned by the Updater runtime include. Existing `deckerweb_library_updater_options_v1()` host calls can remain: new Updater 2.4.0 ignores the obsolete catalog release/package callbacks. Library 1.3.0 returns `false` from its legacy `updater_release()` to select the known direct path for older updaters; it no longer supplies catalog update packages or cleanup leases for that path. This deliberate ownership change is specific to the new runtime, not a general instruction to bypass old provider refusals.

The Library removes old `dwl_managed` offers from its retired catalog updater while preserving ordinary offers. It does not create a new updater for old plugins without one. Such plugins need their normal updater integration updated separately; the Plugins screen remains the management entry point. Unchanged old copies retain their historical behavior until an appropriate new runtime is elected. Update URI, authentication and native automatic-update preferences are preserved.

## First installation and cleanup

First installation still requires fresh catalog approval, the catalog SHA256 and bounded archive/identity verification. The Library owns and removes its installation temporary files, including exception paths, and preserves foreign/replaced paths. Updater 2.4.0 owns ordinary installed updates and does not request a Library package lease. Hosts adopt `deckerweb_library_uninstall_v4` while retaining their own cleanup.

Filesystem credentials remain in WordPress’s native dialog; the Library does not store them. The native updates nonce for third-party compatibility is sent alongside the independently verified Library action nonce. Without JavaScript the same normal update runs through an authorized administration POST; when filesystem credentials are needed, use the native Plugins screen. Git Updater conflict notices remain advisory; nothing is deactivated automatically.

