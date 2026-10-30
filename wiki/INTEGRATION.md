# Integration

[Deutsch](INTEGRATION-de)

Only direct-distribution hosts are supported. Copy `lib/` to `includes/deckerweb-plugin-library/` in the explicitly selected current host source. Preserve the host's updater and current development work.

Before `plugins_loaded`:

```php
require_once __DIR__ . '/includes/deckerweb-plugin-library/bootstrap.php';
deckerweb_library_register_v2( __FILE__, [], __DIR__ . '/includes/deckerweb-plugin-library' );
```

In the host's existing `uninstall.php`, after its direct-access guard, add a bounded cleanup block (do not replace its own cleanup):

```php
require_once __DIR__ . '/includes/deckerweb-plugin-library/lifecycle.php';
deckerweb_library_uninstall_v3( __DIR__ . '/YOUR-HOST-SLUG.php' );
```

The exact host basename must match `WP_UNINSTALL_PLUGIN`. This contract is required for final-host cleanup. Inactive installed hosts are detected from their physical embedded bootstrap files; no active-only registration list is trusted. Keep the conventional library directory for discovery, including future copies. Hosts in custom locations require an explicitly reviewed detection contract.

Translations use the elected host's header Text Domain (its slug if missing), never an extra component domain. Component MO files are merged into that existing domain; host messages retain precedence. The bundle includes EN POT and informal/formal German PO/MO resources. `lib/messages.json` is the maintained dictionary. Run `tools/build-languages.py` after changes and merge the POT entries into host translation workflows. Locale changes reload the elected host-domain component resource.

`prepare-plugin.py` only accepts BAS and Daily Scripture source ZIPs with known version markers and compatible minimum headers. It preserves code after the exact legacy integration block, adds bounded replacement markers and refuses ambiguous custom integrations or conditional uninstall code. It creates a new destination, never overwrites the supplied source and never raises minimums. Other hosts need reviewed manual integration. Review host translations, security policy and its actual final ZIP before release.

The Library kit itself is not installable. `deckerweb-plugin-library-runtime-1.2.0.zip` contains runtime files only; the full kit additionally contains authoring tools and documentation, which must not enter production plugin ZIPs. Do not ship this external installer or the deckerweb Updater on WordPress.org.

Read [security](SECURITY), [data](DATA), [tests](TESTING) and [release conventions](CONVENTIONS).

## Mixed versions and cleanup

The highest compatible complete copy is elected for a request. Registration remains `register_v2`; the compatibility manifest uses protocol 2. The cleanup entry is `uninstall_v3`—its suffix does not change the manifest protocol. Keep the manifest and every listed hash intact. Preserve installed inactive hosts and their integration paths.

The current bootstrap can hand off to a newer valid copy during native activation. An old offline catalog cannot redraw its disabled card before that copy is active; use the native Plugins screen for such a first transition. Older hosts retain their own uninstall routines and must be reviewed separately. No other host file is rewritten. For historically different copies with the same version, replace all affected copies rather than relying on the host-name tie-breaker.

Library 1.2.0 requires WordPress 6.4 and PHP 8.0. A host embedding Updater 2.2.1 requires at least PHP 8.1; higher host requirements remain authoritative. Use the latest stable compatible components and test the actual integrated host ZIP. See [Updater](UPDATER), [Assets](ASSETS) and [Validation 1.2.0](VALIDATION-1.2.0).
