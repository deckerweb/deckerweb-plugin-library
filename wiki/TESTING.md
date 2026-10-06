# Testing

[Deutsch](TESTING-de)

Use disposable staging installations, never production. Test WordPress 6.4 baseline and the current stable target with supported PHP; native filesystem installation and representative FTP/SSH hosts. Test the actual final runtime ZIP embedded in the selected host.

1. Activate a single host, then old/new hosts in both orders; one elected compatible runtime and one tab. Skip incompatible higher versions and incomplete copies without a fatal error.
2. Test English, de_DE and de_DE_formal, including locale switches, notice, settings, validation/package failures and neutral catalog descriptions. Inspect the host domain and translation extraction.
3. Without optional online retrieval, rendering must make no remote requests. Test trusted sources, valid empty catalogs, rejection, cache/backoff and fresh approval failure. Hiding preserves protection and updates.
4. Install approved original archives, activate separately, retain existing plugin directories. Exercise missing/inactive dependencies, network scopes and own updater precedence. Test native update from an older installed version.
5. Test oversized compressed main files, total expansion limits, invalid paths, symlinks, duplicates, identity and hashes; failures should not exhaust memory. Check normal and failed temporary cleanup.
6. Deactivate without data loss. Uninstall with another installed inactive host, then the final host with deletion off/on. Preserve foreign options, plugins and content. Test network settings, all-network cleanup and new sites.
7. Use keyboard and screenreader checks for labels/focus, open/close/Escape/focus return in changelog, narrow layouts and adequate contrast. Check browser/PHP logs.

Commercial builder fixtures do not establish licensed builder compatibility. Complete real builder and host feature tests in their own staging projects before host publication. Screenshots do not block release.
