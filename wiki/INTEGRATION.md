# Integration

[Deutsch](INTEGRATION-de.md)

Only direct-distribution hosts are supported. Copy `lib/` to `includes/deckerweb-plugin-library/` in the explicitly selected current host source. Preserve the host's updater and current development work.

Before `plugins_loaded`:

```php
require_once __DIR__ . '/includes/deckerweb-plugin-library/bootstrap.php';
deckerweb_library_register_v2( __FILE__, [], __DIR__ . '/includes/deckerweb-plugin-library' );
```

In the host's existing `uninstall.php`, after its direct-access guard, add a bounded cleanup block (do not replace its own cleanup):

```php
require_once __DIR__ . '/includes/deckerweb-plugin-library/lifecycle.php';
deckerweb_library_uninstall_v2( __DIR__ . '/YOUR-HOST-SLUG.php' );
```

The exact host basename must match `WP_UNINSTALL_PLUGIN`. This contract is required for final-host cleanup. Inactive installed hosts are detected from their physical embedded bootstrap files; no active-only registration list is trusted. Keep the conventional library directory for discovery, including future copies. Hosts in custom locations require an explicitly reviewed detection contract.

Translations use the elected host's header Text Domain (its slug if missing), never an extra component domain. Component MO files are merged into that existing domain; host messages retain precedence. The bundle includes EN POT and informal/formal German PO/MO resources. `lib/messages.json` is the maintained dictionary. Run `tools/build-languages.py` after changes and merge the POT entries into host translation workflows. Locale changes reload the elected host-domain component resource.

`prepare-plugin.py` only accepts BAS and Daily Scripture source ZIPs with known version markers and compatible minimum headers. It preserves code after the exact legacy integration block, adds bounded replacement markers and refuses ambiguous custom integrations or conditional uninstall code. It creates a new destination, never overwrites the supplied source and never raises minimums. Other hosts need reviewed manual integration. Review host translations, security policy and its actual final ZIP before release.

The Library kit itself is not installable. `deckerweb-plugin-library-runtime-0.6.0.zip` contains runtime files only; the full kit additionally contains authoring tools and documentation, which must not enter production plugin ZIPs. Do not ship this external installer or the deckerweb Updater on WordPress.org.

Read [security](SECURITY.md), [data](DATA.md), [tests](TESTING.md) and [release conventions](CONVENTIONS.md).

Legacy 0.1–0.3 hosts can coexist, but their old uninstall code does not implement this new contract. Upgrade every host integration before relying on final-host cleanup after the last 0.4 host has been removed. No legacy host files are modified automatically.

For the central feed and optional existing updater bridge, read [Catalog](CATALOG.md) and [Updater](UPDATER.md). Always keep the current host development source and translate component messages through its domain.

When replacing an earlier 0.6.0 build, replace every installed 0.6.0 copy together. Equal versions use the host basename as a deterministic election tie-breaker; an older same-version copy can otherwise win. Archive earlier packages and verify compatibility.json hashes after replacement.
