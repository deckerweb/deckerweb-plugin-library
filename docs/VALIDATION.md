# Validation · 1.3.0

[Deutsch](VALIDATION-de.md)

The component is tested together with Updater 2.4.0 in isolated WordPress installations. Coverage includes catalog retrieval on/off, stale/future/unavailable catalogs, manual newer installations, ordinary update offers, native individual/bulk/automatic upgrades, actual AJAX nonces/capabilities, submitted-version recovery and verified first installation. Tests use controlled transport responses and SQLite fixtures on WordPress 6.7/7.1.2, PHP 8.1/8.2/8.4 and Multisite. Full Plugin Check 2.2.0 includes static and runtime checks with individual contextual assessment; it is not a zero-findings assertion. Native v4 cleanup and old/new component load order are checked. Neutral EN/DE component renders cover 32 local icons, mobile width and keyboard update submission.

Limits: PHP 8.0, WordPress 6.4, live MySQL concurrency and real SSH2 filesystem transport were not executed. Earlier FTPS confirmation belongs to 1.2.0. Prepared CI is not evidence of a GitHub run. No customer installation is a test environment. The host integration still needs its own final-package check.


