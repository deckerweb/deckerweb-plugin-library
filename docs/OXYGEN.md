# Oxygen QuickNav compatibility

[Deutsch](OXYGEN-de.md)

Oxygen QuickNav 2.0.0 supports modern Oxygen and Classic; settings remain accessible without a builder. dependency_rules are bounded metadata per dependency: since_version, optional exclusive until_version, and mode required or pause. Rules apply to the installed version for activation and to the offered version for packages. Older installed QuickNav releases retain their required dependencies. Pause rules are enabled only for verified host versions: Oxygen 2.0.0-rc.1+, Breakdance 2.0.0+, Advanced Scripts QuickNav 1.2.1+ and Purify WPCode Lite 1.1.0+. Missing dependencies are reported while affected host features pause. Native Requires Plugins headers and platform requirements remain authoritative. No expressions or code are accepted.
