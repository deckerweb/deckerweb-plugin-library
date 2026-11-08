# FAQ by topic

[Deutsch](FAQ-de.md)

## Getting started

### Where is the catalog?

Open Plugins → Add New → deckerweb. WordPress.org remains the default view.

### Does it contact external services?

Optional catalog retrieval requests the first-party JSON feed and sends no site URL, plugin inventory or usage data. GitHub receives release downloads for first installation. Installed updates use the existing normal updater connections, independently of the Library catalog preference. Local icons and filtering make no extra release requests.

## Requirements and installation

### Why is an installation unavailable?

Check the card for WordPress/PHP requirements and the selected release. Missing mother plugins or themes are advisory for catalog versions with a verified safe-pause rule: installation and activation remain available while dependent features pause. Older installed versions may still have required dependencies. Native WordPress restrictions and platform requirements remain effective. Prerequisites are not installed automatically; activation is separate.

### Can I hide it?

Use Settings → deckerweb Library (Network Settings on Multisite). Hiding the catalog preserves dependency checks and ordinary plugin updates. Online retrieval is a separate preference for catalog metadata and first installations.

## Catalog and update checks

### Does each plugin release require a new Library?

No. An approved online catalog revision can carry a newer plugin version independently of the embedded component.

### Why can the catalog and updater show different freshness?

The catalog is a reviewed snapshot for discovery and first installation, cached for 24 hours. Installed updates follow the separate normal WordPress updater and its existing checks. A newer installed or normally offered version can therefore exceed the catalog version. It is not downgraded or blocked by the older catalog. No extra release request occurs while browsing.

### Do users need a GitHub token?

Public catalog and release downloads do not require user tokens. Optional operator credentials remain outside distributed files.

## Shared settings and data

### What happens when I remove a host?

Another installed host, even inactive, preserves shared data. The final host removes temporary Library data and caches. Settings remain unless optional deletion was enabled. Installed plugins and their content remain. Hosts must call the supplied uninstall contract.

### Does it support Multisite?

Library settings apply per network; catalog preferences are personal. Plugin actions respect site/network permissions and each catalog entry. Multisite Toolbar Additions supports single sites and Multisite. Daily Scripture permits network activation from version 1.0.0. The current Bricks QuickNav catalog version has no blanket per-site activation block; its theme-dependent features still depend on each site’s active theme. See the validation guide for the actual tested scope.

### How do I report a vulnerability?

Use Security → Advisories → Report a vulnerability in the host plugin repository. Include host and Library versions; do not post security details in public issues. Hosts must enable private reporting before publication.

## Personal filters and troubleshooting

### How do I find plugins with updates?

Choose Plugin status → Update available. The filter uses existing WordPress update offers for installed plugins, not a comparison with catalog versions. Combine it with search, series and compatibility. If no offer exists yet, the card says No update reported; this does not claim a fresh GitHub check.

### What does Reset filters keep?

Reset filters clears search, series and installation compatibility and selects All statuses. It keeps the personal sort order and existing random order. Shuffle again deliberately changes the random sequence. Preferences are saved per WordPress user.

### What does a verification error mean?

Library 1.2.0 distinguishes catalog verification, package download, checksum and archive stages. It uses safe connection/TLS/DNS/timeout or HTTP descriptions without exposing remote response bodies or credentials. Refresh the catalog or retry after a temporary server problem. A refused approval is never bypassed. The host’s separate updater can still display a more general message. See [Updater](UPDATER.md) and [Testing](TESTING.md).

## Plugin updates and catalog approval

### Does the online catalog limit plugin updates?

No. With Library 1.3.0 and Updater 2.4.0, installed plugins use their normal WordPress update provider regardless of catalog settings or catalog version. The Library shows the actual installed version and existing WordPress update offers. A catalog version only selects the verified package for first installation. No additional GitHub release checks are made when browsing. Normal update intervals, caches and technical requirements still apply. This does not enable automatic installation. Older component combinations may retain their previous behavior until updated. See the [update guide](CATALOG.md#plugin-updates-and-the-online-catalog).


