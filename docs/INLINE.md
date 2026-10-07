# Inline installation

[Deutsch](INLINE-de.md)

Library 0.7.0 installs and activates catalog plugins in their cards without navigating away. Search, series filters and scroll position remain. Installation and activation are separate actions. Errors appear as plain text beside the action; retry remains available. If filesystem credentials are required, WordPress opens its native dialog. Credentials remain in WordPress’s page memory, not in additional Library storage. Without JavaScript, the existing checked form-based installer is used.

Each action checks permissions, nonce, network scope, fresh approval and dependencies. Installation still validates the original ZIP hash, archive and identity. One installation-wide action lock prevents concurrent modifications of the same catalog plugin. Unexpected activation output or a lost connection requires checking the installed plugin status before retrying.
