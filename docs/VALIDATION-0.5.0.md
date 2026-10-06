# Release validation · 0.5.0

[Deutsch](VALIDATION-0.5.0-de.md)

5 October 2026. This feature update adds series metadata and filtering and the approved Purify Elementor entry; Library minimum versions and lifecycle rules remain unchanged.

33 focused assertions pass on each of WordPress 6.4 and 7.1.2 site installations and 32 on a WordPress 6.7 network installation (98 in total). They cover eight badges, explicit family membership, independent plugins, legacy metadata, malformed series rejection, empty/unknown filters, search and compatibility combinations, reset, network requirements and EN/de_DE/de_DE_formal controls. Browser checks cover actual form submission, Enter preserving the chosen family, All preserving search, resets, empty states, mobile layout and the five-version accessible history. Both JavaScript-enabled and disabled modes are checked.

Final kit/runtime archives are integrity-checked and the runtime archive is loaded on WordPress 6.4 and 7.1.2. The previous security, lifecycle and package baseline remains documented in [0.4.0 validation](VALIDATION-0.4.0.md). Execution uses PHP 8.4.5; PHP 8.0, licensed builders, FTP/SSH and repository private-reporting settings remain host publication checks. No host development source was overwritten and no repository was published.

Final 0.5.0 catalog correction: fifteen entries, five QuickNav, two Builder, one Purify and seven unassigned. Purify Elementor 1.0.1 original ZIP digest matches GitHub; package identity, local icon and missing/inactive/active Elementor guards checked. Earlier 0.5.0 packages are archived separately. Final catalog filters are rechecked on both endpoint cores and multisite.
