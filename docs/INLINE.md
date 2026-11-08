# Inline installation

[Deutsch](INLINE-de.md)

Library 1.3.0 installs, activates and updates catalog plugins in their cards. Installation and activation remain separate. Personal filters and sorting stay available; successful actions refresh card status and result counts. A card can disappear after an action if it no longer matches the selected status. Keyboard focus moves to an appropriate remaining control or result count when necessary.

Each action checks capabilities, action nonce, network scope, applicable requirements and release approval. Downloads retain original SHA256, archive and identity checks. A temporary installation-wide lock prevents parallel changes to the same plugin. Status recovery checks the physical result after interrupted requests without automatically repeating successful writes. A failed or unconfirmed action is not presented as success.

WordPress asks for needed filesystem credentials in its native dialog; the Library adds no credential storage. FTPS was successfully tested by a user with 1.2.0; SSH remains untested. Without JavaScript, native form workflows remain in administration; credential-dependent updates can use the Plugins screen. See [Testing](TESTING.md) and [Validation](VALIDATION-1.2.0.md).

Errors identify safe catalog/download/verification causes when available. A third-party updater may show its own message. Refresh stale offers before retrying; do not bypass a denied approval or checksum failure.


Update cards use the existing normal WordPress offer, with a submitted target version for changed-offer checks and status recovery. The catalog version is used only for first installation. The normal updater remains responsible for installed update packages; no catalog approval is requested by this update action.
