# FAQ by topic

[Deutsch](FAQ-de)

## Getting started

### Where is the catalog?

Open Plugins → Add New → deckerweb. WordPress.org remains the default view.

### Does it contact external services?

Local browsing does not. Installation downloads the selected GitHub release. Optional online approval updates contact the configured first-party HTTPS endpoint; its server sees the requesting IP. No site URL, user ID, inventory or telemetry is sent.

## Requirements and installation

### Why is an installation unavailable?

Check the card for missing or inactive dependencies and WordPress/PHP requirements. Prerequisites are not installed automatically; activation is separate.

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

Library settings are shared per network and the introduction is per user. Network actions require appropriate capabilities and dependencies. Bricks QuickNav retains its per-site restriction pending separate host work; Daily follows its published release policy.

### How do I report a vulnerability?

Use Security → Advisories → Report a vulnerability in the host plugin repository. Include host and Library versions; do not post security details in public issues. Hosts must enable private reporting before publication.


