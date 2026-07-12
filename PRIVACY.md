# ScanFirst Privacy Policy

_Last updated: 12 July 2026_

ScanFirst is a safety-first QR code and barcode scanner. This policy describes what the app does — and deliberately does not do — with your data.

## The short version

ScanFirst has **no accounts, no analytics, no ads, and no tracking**. Camera images never leave your device. We do not collect, store, sell, or share personal data. The app has no server of its own.

## What stays on your device

- **Camera frames** — processed on-device only to detect QR codes and barcodes; never uploaded, never stored.
- **Scan contents** — the decoded text of what you scan is analyzed on your device. ScanFirst keeps no history of your scans.

## Network requests the app makes

ScanFirst contacts external services only for the following, each limited to the minimum data needed:

1. **Redirect resolution** — when you scan a web link, the app sends HEAD/GET requests to that link's own server(s) to reveal the true destination without opening the page. This contacts the scanned URL's server, as any browser would, but does not render or execute the page.
2. **Threat feeds** — the app periodically downloads public lists of known phishing/malware URLs (OpenPhish, URLhaus by abuse.ch) and a region-metadata file (hosted on GitHub). These are downloads only; nothing about you or your scans is sent.
3. **Product lookups** — when you scan a retail barcode (EAN/UPC), the barcode number alone is sent to Open Food Facts (openfoodfacts.org) to fetch product information. Barcode numbers identify products, not people.
4. **Optional Google Safe Browsing** — only if this feature is enabled in a build, scanned URLs are checked against Google's Safe Browsing service, which involves sending the URL to Google. Builds without an API key configured never contact Google.

## Permissions

- **Camera** — required to scan codes. Used for nothing else.

## Payments

ScanFirst never processes payments. When you choose to continue a payment QR into a payment app (e.g. a UPI app), the standard payment link is handed to that app and everything thereafter is governed by that app's own terms and privacy policy.

## Children

ScanFirst does not knowingly collect data from anyone, including children.

## Changes

Changes to this policy will be posted at this URL with an updated date.

## Contact

Questions: open an issue at https://github.com/MaqAnquor/safeqr-data/issues
