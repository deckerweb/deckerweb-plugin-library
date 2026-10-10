# Optional public updater bridge

[Deutsch](UPDATER-de.md)

Install, activate and explicitly update plugins within the catalog card. Updates use native Plugin_Upgrader bulk processing for one selected plugin, preserving activation scope. Pre-existing plugins without an updater can be adopted after exact name and repository-header checks. Foreign Update URI or differing existing update offers are refused; no competing updater takeover. Approved package hashes and identity are checked before replacement. Settings/content are not uninstalled. Shared preferences save inline; catalog refresh retains the current admin URL. Interrupted actions reconcile physical status without repeating successful writes. Native filesystem credentials remain in WordPress’s modal. Without JavaScript, actions stay within administration; updates requiring filesystem credentials use the native Plugins screen. External product/documentation/support links are voluntary and open separately.
