# Release validation · 0.4.0

[Deutsch](VALIDATION-0.4.0-de.md)

Checked on 5 October 2026 against disposable WordPress installations. Library requirements remain WordPress 6.4 and PHP 8.0; no host minimum was raised.

- 70 integration assertions: capabilities, nonces, sources, approval, caches, dependencies and host updater preservation.
- 54 catalog/package assertions: all 14 approved release archives and twelve current local original icons; two generated fallbacks.
- 11 network assertions, 34 final-host lifecycle assertions across single-site and multisite, six additional multiple-network assertions and an actual newly created site.
- 13 localization, lifecycle setting, history and bounded-memory assertions, including oversized compressed main files under a 64 MiB PHP memory limit.
- Six mixed-version election scenarios, including legacy registration first and incompatible, incomplete or corrupted higher copies.
- 11 end-to-end assertions around a real WordPress Plugin_Upgrader installation/update and separate activation in disposable fixtures.
- 12 integration-tool assertions for preservation, idempotence, archive purity and conflicting host minima.
- Actual WordPress 6.4, 6.7 and current stable 7.1.2 run on PHP 8.4.5. The current-version database was upgraded normally. Informal/formal German and locale switching work on both endpoint versions.
- Browser review on WordPress 7.1.2: fourteen cards, twelve local icons, GitHub stars, keyboard dialog, focus containment/return, Escape, narrow layout and no JavaScript errors.

The final archives are checked for integrity, public naming and development/private files; the runtime archive is extracted into a disposable host and loaded on WordPress 6.4 and 7.1.2. Frontend requests keep the runtime unloaded.

Limits: PHP 8.0 was not available for an execution test. WordPress 6.4 emits an existing core deprecation on PHP 8.4. Commercial builder fixtures do not prove actual licensed-builder compatibility. FTP/SSH transports, full host features, assistive-technology review and private GitHub reporting configuration remain host publication checks. A Library build does not change repository settings or publish host releases. See [Testing](TESTING.md) and [Security](../SECURITY.md).
