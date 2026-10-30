# Optional public updater bridge

[Deutsch](UPDATER-de)

## Catalog actions and host updater

Library 1.2.0 installs, activates and explicitly updates selected catalog plugins inline. Native `Plugin_Upgrader` processing preserves activation scope and plugin data. Existing plugins without an updater can be updated after exact plugin/repository identity checks; this is not automatic ownership of every installed plugin. Different versions, foreign repositories or unrecognized package sources are rejected.

A matching GitHub source-archive offer may be accepted only when repository, plugin, version and tag match exactly. The installed package is still the approved catalog release asset, with SHA256, identity and archive verification. Other update offers and third-party hooks remain intact. Git Updater interoperability includes the native updates nonce while retaining the Library’s own action nonce and capability checks. The local conflict notice recommends temporary deactivation when needed; nothing is deactivated automatically.

## Optional provider contract

An explicitly configured public host updater can call `updater_release(repository, file, fresh)`: an array supplies approved metadata, `false` permits its existing direct-updater mode when Library online retrieval is off, and `null` refuses approval. Refused approval must not silently fall back to an unapproved package. Display cache is 24 hours; independent update metadata cache is 12 hours. Fresh package approval still requires a successful source check.

`updater_package(repository, file, package)` returns a verified temporary package path or `WP_Error`. The caller removes successful temporary archives after use. Repository URL, plugin basename and package URL must identify the same approved target. Preserve private authentication and other updater behavior; this bridge is for explicitly opted-in public hosts.

Library 1.2.0 also offers `updater_diagnostic(repository, file)` for an available safe failure from the same request and target. It performs no HTTP request. It may return `null`; it does not cover every possible error. Existing Updater 2.2.1 does not automatically display these extra diagnostics and can still show a general verification message. Do not change the array/null/false provider contract to pass error objects as release metadata.

Filesystem credentials stay in WordPress’s native dialog. Without JavaScript, actions remain in administration; updates needing credentials use the native Plugins screen. Online catalog failure never disables checksum/identity checks. The old `integration/updater-v2.1-dev.3-catalog-provider.patch` is a historical example for that exact development version, not a patch to apply to current updaters.

