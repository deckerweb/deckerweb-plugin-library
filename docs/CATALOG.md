# Online catalog and independent updates

[Deutsch](CATALOG-de.md)

Current Library: **1.3.0** · catalog revision **2026-11-10.1**.

The catalog contains 32 approved public plugin releases in 8 series. Each entry pins repository identity, main file, first-installation version, original ZIP URL, SHA256 and requirements. Catalog retrieval is optional, off by default and cached for 24 hours. New plugins and catalog changes require explicit review. Older readers retain their historical conservative behavior.

Original icons are bundled locally. Initials use a subtle background when no matching local icon exists; an explicit `icon_background` takes precedence over the stable pastel palette. Cards retain subtle hover/keyboard focus. No remote icons, scripts or executable catalog code are loaded. WPCodeBox QuickNav uses its local original icon in this Library version.

Current [catalog release/package sources](CATALOG-SOURCES-2026-11-10.1.json). Catalog versions choose first-installation packages; they do not cap installed-plugin updates.

## Plugin updates and the online catalog

**Online catalog and installed-plugin updates are independent with Library 1.3.0 and Updater 2.4.0.** Enable the catalog when you want fresh discovery metadata. There is no need to disable it to receive newer plugin releases.

Example: the catalog lists 1.3.0, your site has 1.3.1, and the normal updater offers 1.4.0. The Library shows Installed: 1.3.1 and Update available: 1.4.0. Its update button uses the normal WordPress update. An older, unavailable or disabled catalog does not block it. If you manually install 1.4.0, the installed version updates accordingly and no downgrade is offered.

For a plugin not installed yet, Install now uses the verified catalog package. Later updates come from its normal updater. This requires a working updater; the Library does not add one to arbitrary old plugins. Online catalog settings do not enable automatic installation or change private-repository credentials.

“No update reported” means the existing WordPress update state contains no newer offer. It does not claim a fresh GitHub check or that your installed version is the latest. Browsing, sorting and filters start no additional release checks. Use Dashboard → Updates for the normal WordPress checking workflow; caches and technical requirements still apply.

Settings → deckerweb Library (Network Admin → Settings on Multisite) controls optional online metadata. Hiding the catalog changes visibility only. Both settings leave installed-plugin updates independent. Previous versions may still use their older catalog-approval behavior; update both components for the complete current behavior.


Revision 2026-11-09.1 updates 28 reviewed plugin releases from the component-maintenance matrix. The catalog retains 32 plugins and eight series. Daily Scripture, Brand Admin Schemes, Site Essentials and TabulaMea are unchanged. Library 1.3.0 and its embedded fallback catalog are unchanged.

Revision 2026-11-10.1 updates TabulaMea to 1.0.0 and Site Essentials, Brand Admin Schemes and Daily Scripture to 1.2.0. The other 28 entries, eight series and local icons are unchanged. Library remains 1.3.0; its embedded fallback catalog and release packages are unchanged.
