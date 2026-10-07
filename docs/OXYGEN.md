# Oxygen QuickNav compatibility

[Deutsch](OXYGEN-de.md)

The catalog offers the verified Oxygen QuickNav 2.0.0 release. Installed 1.0.0 copies retain their modern-Oxygen requirement. Installed Oxygen QuickNav 2.0.0-rc.1 and newer follows its explicit host contract: it can be activated on a site or network without a builder; settings remain accessible and navigation pauses. This installed-version rule does not change the requirements of the offered 1.0.0 package. A new public QuickNav release is added only after its real ZIP and release metadata are verified.

Modern Oxygen is identified by Oxygen mode, runtime version, builder helper and the actual active main file; helper source must belong to that installation. Breakdance uses its own mode. Advanced Scripts is matched to its loaded helper’s installation. A site-only active plugin never proves network-wide availability. Names alone cannot prove activation.

After a lost inline response, the Library checks the plugin status without repeating installation or activation. A still-running or unknown action offers Check status; only a confirmed absent plugin permits another install attempt. This read-only request checks nonce, permissions and fresh approval before offering activation. No additional persistent inventory cache is added; WordPress already caches plugin headers.

Legacy dependency metadata is retained protectively for older readers. Library0.8.0 resolves the effective requirements per target version; it shows the offered2.0.0 package without a mandatory builder. Older Libraries can conservatively require modern Oxygen until upgraded.
