# Release conventions

[Deutsch](CONVENTIONS-de.md)

The component uses semantic three-part versions: feature additions increase the minor version; compatible fixes increase patch; breaking bootstrap/data/API changes require a documented compatibility plan and major version decision. Before 1.0, minor versions may change integration behavior only with clear migration instructions. Minimum increases require an explicit decision; they are not part of automatic integration.

Before a host release compare current Library/updater/footer versions, data ownership, locales and supported platforms; preserve current host code and its updater. Refresh only the approved catalog and source records. Verify dependencies and installed versions, then hashes, original package identity, current icons and dated stars. Installation never overwrites an existing directory and activation remains separate. Third-party dependency code is never copied.

Keep public documentation on the shared source in `docs/content.json` and runtime history in `lib/history.json`; generate matching FAQ/readmes/changelogs. English category order is New, Improved, Fixed, Misc; German Neu, Verbessert, Behoben, Sonstiges. The full available history is included; unknown old release dates are not invented. Before publication verify current GitHub rules and private reporting in each host repository, and run the actual shipped ZIP through the test checklist. No publication is performed by these tools.

Maintain synchronized English/German documentation and user-facing language. Use the words plugin conventions, consistent standard or shared foundation for necessary public process references. Internal working records do not enter public exports.

Current banner artwork adapts the already approved catalog layout and original product icons; it introduces no new logo. Screenshots are a low-priority supplement.
