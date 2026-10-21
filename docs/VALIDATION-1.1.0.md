# Validation 1.1.0

[Deutsch](VALIDATION-1.1.0-de.md)

Validation record for approved version 1.1.0. WordPress 7.1.2 / PHP 8.4.5 with disposable SQLite single-site and network fixtures.

Checked the actual embedded reference ZIP: 27 approved original packages and local icons, strict catalog validation including readers 0.6.0–1.0.0, input normalization and contextual output protection, nonce/capability refusals, repeated personal sorting, local diagnostics, informal/formal German, card hover and keyboard focus, reduced motion, mobile layout and changelog closure. Mixed older/new component election and network settings/new-site inheritance passed.

Official Plugin Check 2.1.0 was run in the host context. Static Library findings decreased from 106 to 34 compared with 1.0.0; these remaining findings require contextual review and do not represent 34 confirmed vulnerabilities. Explicit runtime asset-scope checks completed without findings; the complete eligible static/runtime check set was also run. No rules were globally disabled. The host and its updater have separate findings and are outside this component review.

Additional checks covered two consecutive native updates with Git Updater 14.4.2 active and complete browser requests. The action-bound Library nonce remains mandatory; the WordPress updates nonce is also sent. Equivalent GitHub source-archive offers are accepted only for an identical repository, plugin, version and tag. Installation still uses only the approved, hash-verified catalog package. Conflicting offers are rejected and the temporary offer filter is removed after the action.

The tester subsequently confirmed successful updates on a Local installation running WordPress 7.1.3 with Git Updater active: Quick Edit Featured Image and Post Author Taxonomy, followed by Portfolio Content and Purify WPCode Lite. This reported practical test supplements the isolated checks; it does not replace coverage of every hosting configuration.

Two warm local catalog reads made zero SQL queries and zero HTTP requests in the measured fixture. This is a scoped measurement, not a general hosting benchmark. No remote icon requests occur.

Not newly demonstrated: PHP 8.0 execution, a fresh WordPress 6.4 run, real FTP/SSH credentials/transport, historical GitHub Updater variants, or complete licensed-builder functionality. Existing WordPress 6.4 / PHP 8.0 component minimums remain unchanged; host/updater requirements can be higher. Use staging and backups for integration testing.
