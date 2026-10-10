# deckerweb Plugin Library

[Deutsch](README-de)

![deckerweb Library](https://raw.githubusercontent.com/wiki/deckerweb/deckerweb-plugin-library/assets/banner-1b-en.png)

## About

The deckerweb Plugin Library adds a selected catalog of deckerweb plugins to WordPress. It comes bundled with certain plugins and gives you another way to discover and install useful additions under **Plugins → Add New → deckerweb**. The usual WordPress.org catalog remains the default.

If you found an `includes/deckerweb-plugin-library/` folder inside a plugin, this is the shared component behind that catalog. The plugin author included it deliberately; you do not need to install or configure a separate Library plugin.

This repository contains the reusable PHP component, catalog, integration examples and documentation. It is also open for developers who want to read the code, reuse it under its license or build their own approach.

Installation and activation happen directly in the selected card. Status and errors appear there; search, series filters and scroll position remain. Filesystem credentials use the native WordPress dialog. Without JavaScript, the checked form workflow remains available.

**Version:** 0.9.0 · WordPress ≥ 6.4 · PHP ≥ 8.0

[Documentation](INTEGRATION) · [FAQ by topic](FAQ) · [Security](SECURITY)

## Contents

- [At a Glance](#at-a-glance)
- [Installation](#installation)
- [Features](#features)
- [For plugin users](#for-users)
- [For developers](#for-developers)
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

See [integration](INTEGRATION), [data](DATA), [tests](TESTING) and [security](SECURITY).

[Series and filters](SERIES).

<a id="features"></a>
## Main features

### Discover suitable plugins

Use the deckerweb tab under Plugins → Add New. Combine search, QuickNav/Builder/Purify/Manage Content/Connect and Fits my installation. Each card explains missing requirements; installation and activation remain separate.

### Approved catalog updates

The public GitHub catalog address is prefilled. Enable online retrieval in Library settings. Discovery is cached for 24 hours. Approved plugin releases can change without replacing Library code. [Catalog guide](CATALOG).

### Shared preferences and safe packages

Installed hosts share settings; deactivation preserves data. Fresh release approval, checksums and archive checks guard package actions. [Data](DATA) · [Updater integration](UPDATER).

### A look at the catalog

![Illustrative deckerweb plugin catalog overview](https://raw.githubusercontent.com/wiki/deckerweb/deckerweb-plugin-library/assets/banner-en.png)

This original overview illustrates the catalog with examples of plugins and their icons. It is a schematic illustration, not a screenshot or a complete list of today's catalog. Available releases and requirements appear on the actual plugin cards.

### The catalog in WordPress

![Real catalog view in WordPress](https://raw.githubusercontent.com/wiki/deckerweb/deckerweb-plugin-library/assets/catalog-real-en.png)

A real screenshot from a Library 0.6.0 test installation. It shows plugin cards, filters, installation controls and dependency notices. The catalog and displayed versions can change; this image is an example, not a live release list.

<a id="for-users"></a>
## Found this Library in your plugin?

### You choose what gets installed

The catalog shows selected public GitHub releases, their requirements and any missing dependencies. Opening a card does not install anything. You start installation yourself; activation is a separate step. Required third-party plugins are not installed automatically.

You can hide the catalog in **Settings → deckerweb Library**, or in the network settings on Multisite. Hiding it keeps already configured update handling intact. If several installed plugins include the Library, they share one catalog and its settings rather than adding several copies of the interface.

### External connections are explained

The bundled catalog and its icons can be displayed locally. Optional online catalog retrieval is **off by default**. When enabled, it reads the public catalog from GitHub and caches discovery results for 24 hours; you can also refresh manually. Installing a selected plugin downloads its approved GitHub ZIP. Package actions in online mode check approval again before proceeding.

These requests let the serving endpoint see the requesting IP address. The Library does not send your site URL, user ID or plugin inventory and has no telemetry. Existing plugin updaters may make their own requests according to the host plugin's documentation. Public catalog retrieval and public package downloads do not require a GitHub account or user token.

### Checks before installation

The Library checks WordPress/PHP requirements, declared dependencies, the approved package identity, checksum and archive structure. These checks help reject unexpected packages; they are not a promise that every plugin is suitable for every site. Review the plugin's own documentation and use your normal backup and staging workflow.

Deactivating an embedding plugin preserves shared Library settings. Properly integrated hosts clean up temporary Library data when the last host is uninstalled; deleting settings is optional. Plugins installed through the catalog and their content remain. See [data ownership and cleanup](DATA).

<a id="for-developers"></a>
## For developers: explore, reuse, adapt

The Library is **GPL-2.0-or-later**. You are welcome to study, reuse and adapt the code under that license. Keep copyright and required provenance notices, and check the separate [artwork notes](https://github.com/deckerweb/deckerweb-plugin-library/blob/main/docs/ASSETS.md) before reusing graphics or branding.

### Start with the integration contract

The component requires **WordPress 6.4+ and PHP 8.0+**, with **ZipArchive** for package installation. A host plugin or catalog entry may have higher requirements. Copy only `lib/` into the host's `includes/deckerweb-plugin-library/` folder, then register it before `plugins_loaded`:

```php
require_once __DIR__ . '/includes/deckerweb-plugin-library/bootstrap.php';
deckerweb_library_register_v2(
    __FILE__,
    [],
    __DIR__ . '/includes/deckerweb-plugin-library'
);
```

This is the starting point, not the entire integration. Follow the [integration guide](INTEGRATION) for the required uninstall contract, host-domain translations and mixed-copy checks. Preserve the host's own updater; the [catalog bridge](UPDATER) is an optional integration. Ship the runtime, not the authoring tools or this whole repository. The current Library and deckerweb Updater are excluded from WordPress.org builds; use this kit for direct distribution.

### A useful reading path

- [`lib/bootstrap.php`](https://github.com/deckerweb/deckerweb-plugin-library/blob/main/lib/bootstrap.php): registration and selection of one compatible runtime across hosts.
- [`lib/src/Catalog.php`](https://github.com/deckerweb/deckerweb-plugin-library/blob/main/lib/src/Catalog.php): catalog validation, source restrictions and independent caches.
- [`lib/src/Requirements.php`](https://github.com/deckerweb/deckerweb-plugin-library/blob/main/lib/src/Requirements.php) and [`lib/src/Package.php`](https://github.com/deckerweb/deckerweb-plugin-library/blob/main/lib/src/Package.php): prerequisites, package verification and bounded archive processing.
- [`lib/lifecycle.php`](https://github.com/deckerweb/deckerweb-plugin-library/blob/main/lib/lifecycle.php): shared data ownership and cleanup after the final host.
- [`tools/refresh-catalog.py`](https://github.com/deckerweb/deckerweb-plugin-library/blob/main/tools/refresh-catalog.py) and [`tools/approve-catalog.py`](https://github.com/deckerweb/deckerweb-plugin-library/blob/main/tools/approve-catalog.py): prepare a candidate, review it and export the exact approved bytes. Publication remains a separate operator action.

### Building your own catalog

The shipped implementation is intentionally restricted to approved deckerweb repositories and catalog sources. It is not an unrestricted repository installer: pointing it at an arbitrary JSON URL is insufficient. For another publisher, deliberately adapt and test source restrictions, repository identities, package rules, series, translations and shared-runtime ownership. Avoid namespace/bootstrap collisions if your adaptation can run beside deckerweb plugins.

Keep catalog metadata separate from component releases, cache discovery rather than querying GitHub on every page view, and check package approval freshly before sensitive actions. Preserve independent host update paths. See the [catalog guide](CATALOG), [test guide](TESTING) and [release conventions](https://github.com/deckerweb/deckerweb-plugin-library/blob/main/docs/CONVENTIONS.md). Ideas and implementation questions are welcome in this repository's Issues and Discussions; private security reports about an embedded copy belong in its host plugin repository.


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

Library settings are shared per network. Daily Scripture 1.0.0 and newer support network activation; earlier installed versions must be updated first. Bricks QuickNav retains its per-site restriction. Permissions and dependency checks still apply.

### How do I report a vulnerability?

Use Security → Advisories → Report a vulnerability in the host plugin repository. Include host and Library versions; do not post security details in public issues. Hosts must enable private reporting before publication.

[Complete FAQ by topic](FAQ).

<a id="changelog"></a>
## Changelog

### 0.9.0 · 2026-10-10

- **New:** Update verified installed catalog plugins directly in their cards, including older releases without an updater.
- **New:** Catalog-defined series, localized categories, ordering and versioned safe-pause dependency rules.
- **Improved:** Current approved catalog packages and local original icons, including Builder Content Guide and the Admin series.
- **Improved:** Save shared preferences in place and keep Library operations inside WordPress administration.
- **Fixed:** Early fallback messages use host translation resources; activation handoff documentation is directly attached to the function.

### 0.8.1 · 2026-10-08

- **New:** Tools and Shop catalog series, with backward-compatible metadata.
- **Improved:** The bundled catalog includes all 20 approved plugins and their current local icons.
- **Improved:** Check the plugin status after interrupted inline actions without repeating a successful operation.
- **Improved:** Match builder runtime markers to the active installation and apply the versioned Oxygen QuickNav 2.0 activation contract.
- **Improved:** Updated Oxygen QuickNav2.0.0 and Quick Edit Featured Image1.4.0 packages, requirements and original icons.
- **Fixed:** Final-host uninstall removes current catalog and update caches as well as legacy caches.
- **Fixed:** The current uninstall entry point remains effective when an older cleanup copy was loaded first.

### 0.7.0 · 2026-10-07

- **Improved:** Install and activate catalog plugins directly in their cards, with inline status and errors.
- **Improved:** Use the approved three-character fallback labels when no original icon is available.

### 0.6.1 · 2026-10-07

- **Improved:** Updated approved plugin releases and original catalog icons.
- **Improved:** The settings footer shows the local Library SVG icon, name and version.
- **Fixed:** Daily Scripture 1.0.0 and newer can be network activated, including beside an older embedded Library.
- **Fixed:** Single filtered results retain normal card width on wide screens.
- **Fixed:** Multisite Toolbar Additions is also available for single websites and site activation.

### 0.6.0 · 2026-10-06

- **New:** Approved plugin releases can appear in the online catalog without replacing the embedded Library.
- **New:** Discover Purify WPCode Lite and Purify WPForms Lite in the catalog.
- **New:** Plugins can belong to several series, including Manage Content.
- **New:** Discover the Connect series and the upcoming Connect for Shopware 1.0.0 with a clear preparation notice.
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

Use the embedding host repository for ordinary issues and questions, and its private reporting channel for security details. [Security policy](SECURITY).

[Ko-fi](https://ko-fi.com/deckerweb) · [Buy Me a Coffee](https://buymeacoffee.com/daveshine) · [PayPal](https://paypal.me/deckerweb)

## Copyright & License

Copyright © 2026 David Decker — DECKERWEB. GPL-2.0-or-later. [License](https://github.com/deckerweb/deckerweb-plugin-library/blob/main/LICENSE) · [Artwork and provenance](https://github.com/deckerweb/deckerweb-plugin-library/blob/main/docs/ASSETS.md).
