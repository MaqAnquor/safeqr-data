# safeqr-data

Region/currency metadata for [SafeQR](https://github.com/MaqAnquor)'s payment-QR analysis.

`regions.json` maps ISO 4217 numeric currency codes to national QR payment scheme metadata (currency symbol, scheme name, and a documented local scam pattern). The SafeQR app fetches this file daily and merges it over its built-in table, so new countries and corrected scam notes reach every install **without an app-store release**.

## Shape

```json
{
  "<ISO 4217 numeric code>": {
    "symbol": "₹",
    "name": "INR",
    "country": "India",
    "scheme": "UPI / Bharat QR",
    "scamNote": "One documented local scam pattern, shown to users as a warning."
  }
}
```

## Adding a country

Edit `regions.json`, keep scam notes factual and sourced, and merge to `main`. All installs pick it up within 24 hours.
