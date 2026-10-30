# FAQ by topic

[Deutsch](FAQ-de)

## Getting started

### Where is the catalog?

Open Plugins → Add New → deckerweb. WordPress.org remains the default view.

### Does it contact external services?

Local browsing does not. Installation downloads the selected approved GitHub release. Optional online retrieval contacts the configured trusted public GitHub catalog; the server sees the requesting IP. The Library does not send a site URL, user ID or plugin inventory and contains no telemetry. An embedding host’s separate updater may make its own documented requests.

## Requirements and installation

### Why is an installation unavailable?

Check the card for WordPress/PHP requirements and the selected release. Missing mother plugins or themes are advisory for catalog versions with a verified safe-pause rule: installation and activation remain available while dependent features pause. Older installed versions may still have required dependencies. Native WordPress restrictions and platform requirements remain effective. Prerequisites are not installed automatically; activation is separate.

### Can I hide it?

Use Settings → deckerweb Library (Network Settings on Multisite). Hiding discovery preserves dependency checks and existing managed updates. Disable online catalog retrieval separately to stop its requests.

## Catalog and update checks

### Does each plugin release require a new Library?

No. An approved online catalog revision can carry a newer plugin version independently of the embedded component.

### Why can the catalog and updater show different freshness?

Discovery is cached for 24 hours; installed-plugin updates use an independent cache in the WordPress cycle. Package actions recheck approval freshly.

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

Choose Plugin status → Update available. The filter compares known stable installed versions with the approved catalog version. Search, series and compatibility filters still apply; the result count reflects their combination. It does not query GitHub separately or include unrelated WordPress.org updates.

### What does Reset filters keep?

Reset filters clears search, series and installation compatibility and selects All statuses. It keeps the personal sort order and existing random order. Shuffle again deliberately changes the random sequence. Preferences are saved per WordPress user.

### What does a verification error mean?

Library 1.2.0 distinguishes catalog verification, package download, checksum and archive stages. It uses safe connection/TLS/DNS/timeout or HTTP descriptions without exposing remote response bodies or credentials. Refresh the catalog or retry after a temporary server problem. A refused approval is never bypassed. The host’s separate updater can still display a more general message. See [Updater](UPDATER) and [Testing](TESTING).


