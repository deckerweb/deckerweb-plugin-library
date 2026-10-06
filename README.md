# deckerweb Plugin Library

[Deutsch](README-de.md)

![deckerweb Library](assets-github/banner-en.png)

## About

A small embedded catalog for directly distributed WordPress plugins. Only explicitly approved GitHub releases appear under Plugins → Add New → deckerweb. This is an embedding kit, not a standalone installable plugin.

Requirements: WordPress 6.4+, PHP 8.0+, ZipArchive for installation. GPL-2.0-or-later. Only direct-distribution builds; exclude Library and deckerweb Updater entirely from WordPress.org builds.

**Version:** 0.6.0 · WordPress ≥ 6.4 · PHP ≥ 8.0

[Documentation](docs/INTEGRATION.md) · [FAQ by topic](docs/FAQ.md) · [Security](SECURITY.md)

## Contents

- [At a Glance](#at-a-glance)
- [Installation](#installation)
- [Features](#features)
- [FAQ](#faq)
- [Changelog](#changelog)
- [Author and scope](#author)
- [Support](#support)

<a id="at-a-glance"></a>
## At a Glance

- Selected public GitHub releases with local icons and clear requirements.
- Search, product-family filters and installation compatibility.
- Optional daily online catalog; independent installed-plugin update checks.

<a id="installation"></a>
## Installation and first steps

See [integration](docs/INTEGRATION.md), [data](docs/DATA.md), [tests](docs/TESTING.md) and [security](SECURITY.md).

[Series and filters](docs/SERIES.md).

<a id="features"></a>
## Main features

### Discover suitable plugins

Use the deckerweb tab under Plugins → Add New. Combine search, QuickNav/Builder/Purify/Manage Content and Fits my installation. Each card explains missing requirements; installation and activation remain separate.

### Approved catalog updates

The public GitHub catalog address is prefilled. Enable online retrieval in Library settings. Discovery is cached for 24 hours. Approved plugin releases can change without replacing Library code. [Catalog guide](docs/CATALOG.md).

### Shared preferences and safe packages

Installed hosts share settings; deactivation preserves data. Fresh release approval, checksums and archive checks guard package actions. [Data](docs/DATA.md) · [Updater integration](docs/UPDATER.md).

## FAQ

### Where is the catalog?

Open Plugins → Add New → deckerweb. WordPress.org remains the default view.

### Does it contact external services?

Local browsing does not. Installation downloads the selected GitHub release. Optional online approval updates contact the configured first-party HTTPS endpoint; its server sees the requesting IP. No site URL, user ID, inventory or telemetry is sent.

### Why is an installation unavailable?

Check the card for missing or inactive dependencies and WordPress/PHP requirements. Prerequisites are not installed automatically; activation is separate.

### Can I hide it?

Use Settings → deckerweb Library (Network Settings on Multisite). Hiding discovery preserves dependency checks and existing managed updates. Disable online catalog retrieval separately to stop its requests.

### What happens when I remove a host?

Another installed host, even inactive, preserves shared data. The final host removes temporary Library data and caches. Settings remain unless optional deletion was enabled. Installed plugins and their content remain. Hosts must call the supplied uninstall contract.

### Does it support Multisite?

Library settings are shared per network and the introduction is per user. Network actions require appropriate capabilities and dependencies. Bricks QuickNav retains its per-site restriction pending separate host work; Daily follows its published release policy.

### How do I report a vulnerability?

Use Security → Advisories → Report a vulnerability in the host plugin repository. Include host and Library versions; do not post security details in public issues. Hosts must enable private reporting before publication.

[Complete FAQ by topic](docs/FAQ.md).

<a id="changelog"></a>
## Changelog

### 0.6.0 · 2026-10-06

- **New:** Approved plugin releases can appear in the online catalog without replacing the embedded Library.
- **New:** Discover Purify WPCode Lite and Purify WPForms Lite in the catalog.
- **New:** Plugins can belong to several series, including Manage Content.
- **Improved:** The catalog refreshes after 24 hours; installed-plugin update checks use an independent cache.
- **Improved:** Optional integration with the host updater keeps package approval and checksum checks current.
- **Improved:** The public GitHub catalog address is prefilled in Library settings.
- **Fixed:** Catalog and package requests use a client identifier without the website URL.
- **Fixed:** Plugins with their own updater remain independent when the catalog is unavailable.
- **Fixed:** Online catalog sources are restricted to the deckerweb GitHub raw-file host.

### 0.5.0 · 2026-10-05

- **New:** Explicit QuickNav, Builder and Purify product-family metadata, discreet card badges and a series filter. Empty families remain hidden.
- **New:** Purify Elementor joins the approved catalog and Purify family; Multisite Toolbar Additions belongs to QuickNav.
- **Improved:** Combine series and search with Fits my installation; reset filters without changing catalog settings.

### 0.4.0 · 2026-10-05

- **New:** Host-domain translations in English, informal German and formal German.
- **New:** Shared last-host cleanup with optional settings deletion and a local accessible changelog.
- **Improved:** Compatible runtime election across old and new hosts; current approved catalog sources and local icons.
- **Fixed:** Reject oversized archive contents before reading them and normalize files using bounded streams.
- **Fixed:** Preserve host code during integration and report platform conflicts without raising minimums.
- **Misc:** Bilingual documentation, private security reporting through host repositories and documented data ownership.

### 0.3.0 · 2026-10-01

- **New:** Fourteen approved plugins, twelve original local icons and dated GitHub star counts.
- **Improved:** Explicit Multisite requirements and refreshed release provenance.

### 0.2.0

- **New:** Additional catalog entries, local product icons and GitHub star snapshots.

### 0.1.0

- **New:** Embedded curated catalog, verified installation, separate activation and optional online approvals.

<a id="author"></a>
## Author and scope

Developed and published by David Decker — DECKERWEB. A shared embedded component for direct-distribution plugins, not a standalone WordPress.org plugin.

<a id="support"></a>
## Issues, security and support

Use the embedding host repository for ordinary issues and questions, and its private reporting channel for security details. [Security policy](SECURITY.md).

[Ko-fi](https://ko-fi.com/deckerweb) · [Buy Me a Coffee](https://buymeacoffee.com/daveshine) · [PayPal](https://paypal.me/deckerweb)

## Copyright & License

Copyright © 2026 David Decker — DECKERWEB. GPL-2.0-or-later. [License](LICENSE) · [Artwork and provenance](docs/ASSETS.md).
