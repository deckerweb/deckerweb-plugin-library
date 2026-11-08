# Testing

[Deutsch](TESTING-de)

This is a test checklist, not a list of completed tests. See the linked validation record for actual results.

Use disposable staging installations, never production. Test WordPress 6.4 baseline and the current stable target with supported PHP; native filesystem installation and representative FTP/SSH hosts. Test the actual final runtime ZIP embedded in the selected host.

1. Activate a single host, then old/new hosts in both orders; one elected compatible runtime and one tab. Skip incompatible higher versions and incomplete copies without a fatal error.
2. Test English, de_DE and de_DE_formal, including locale switches, notice, settings, validation/package failures and neutral catalog descriptions. Inspect the host domain and translation extraction.
3. Without optional online retrieval, rendering must make no remote requests. Test trusted sources, valid empty catalogs, rejection, cache/backoff and fresh approval failure. Hiding preserves protection and updates.
4. Install approved original archives, activate separately, retain existing plugin directories. Exercise missing/inactive dependencies, network scopes and own updater precedence. Test native update from an older installed version.
5. Test oversized compressed main files, total expansion limits, invalid paths, symlinks, duplicates, identity and hashes; failures should not exhaust memory. Check normal and failed temporary cleanup.
6. Deactivate without data loss. Uninstall with another installed inactive host, then the final host with deletion off/on. Preserve foreign options, plugins and content. Test network settings, all-network cleanup and new sites.
7. Use keyboard and screenreader checks for labels/focus, open/close/Escape/focus return in changelog, narrow layouts and adequate contrast. Check browser/PHP logs.

Commercial builder fixtures do not establish licensed builder compatibility. Complete real builder and host feature tests in their own staging projects before host publication. Screenshots do not block release.

[Current validation](VALIDATION-1.3.0) · [Historical 1.2.0 validation](VALIDATION-1.2.0).

Include six status modes, per-user persistence, combined filters, result counts, Reset filters retaining sort/random order, successful action recovery and focus, and mobile compact controls. Check error stages without leaking URLs, paths or credentials. FTPS is user-confirmed for 1.2.0; SSH and PHP 8.0 execution remain untested. Take documentation screenshots only in neutral test installations.


## Executable regression checks

Run `php tests/security-regressions.php`, `php tests/cleanup-regressions.php`, `php tests/cleanup-regressions.php --older-alias` and `php tests/parallel-regressions.php` from the kit root. These tests execute the component methods using explicit WordPress API doubles. They cover retired managed offers, independent native offers, installed versus offered platform requirements, versioned dependency/network rules, independent register entries and final-host cleanup. The parallel test uses twelve CLI processes with isolated file-backed storage, not a live WordPress database. No production site, real HTTP request or credential is used.

`python3 tests/manifest.py` checks runtime hashes. The read-only CI workflow runs PHP syntax and these checks on PHP 8.0–8.4, plus JavaScript syntax. Its presence is not evidence that the remote workflow or each PHP version has run. The suite does not replace actual WordPress activation/update, persistent object-cache, MySQL concurrency, Plugin Check, or FTP/SSH integration testing. Keep test/tool directories outside host runtime packages.




Include stale/future/invalid/missing catalogs with retrieval on/off, manually installed newer versions, missing ordinary offers and legacy helper load order. First-install approval and checksums must remain effective while installed updates use ordinary offers. Update recovery must compare the submitted normal target version, never the catalog version. Validate native individual, bulk and automatic upgrades; changed offers, archive identity/version/platform failures and unauthorized requests must preserve the installation.
