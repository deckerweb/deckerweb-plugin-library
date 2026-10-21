# Online catalog and independent updates

[Deutsch](CATALOG-de.md)

The catalog contains 27 approved public plugin releases. Each entry pins repository identity, plugin main file, version, original ZIP URL, SHA 256 and platform requirements. Updates are explicitly reviewed; no automatic enrollment. Online retrieval is optional and initially off, cached for 24 hours; installed-plugin update checks use an independent 12 hour cache. Package actions require fresh approval. Existing Library 0.6.0,0.7.0 and 0.8.1 readers accept the additive catalog fields, show supported series and retain conservative dependency checks. New local icons use versioned filenames where older bundled assets would otherwise be stale; older hosts use initials when the file is absent. No remote icons or executable code are loaded.

Cards with no available local image use initials on a subtle background. An explicit catalog `icon_background` takes precedence over the stable built-in pastel palette. Original icons are bundled locally; no remote image requests occur. A removed old image path falls back to initials until compatible local artwork is available. Cards subtly highlight on hover and keyboard focus without moving.

