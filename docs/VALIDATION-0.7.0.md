# Release validation · 0.7.0

[Deutsch](VALIDATION-0.7.0-de.md)

7 October 2026. Inline installation and activation were tested on WordPress 6.7 Multisite and WordPress 7.1.2 single sites with PHP 8.4.5. Tests cover real package installation and activation, retained catalog filters and URL, inline errors and retry, rejected invalid nonces/operations, mobile layout and the native filesystem dialog’s Cancel/Escape controls. Original release ZIPs were supplied by a controlled local transport fixture; checksum, identity and archive validation stayed active. The form-based no-JavaScript installation was also tested.

The release retains WordPress 6.4/PHP 8.0 component minimums. PHP 8.0 execution, licensed builders, live FTP/SSH connections and multiple-worker concurrency are not newly verified. Complete parameter/return contracts and final archive manifests are checked. The optional updater bridge remains separate; no updater or canonical host source is overwritten.
