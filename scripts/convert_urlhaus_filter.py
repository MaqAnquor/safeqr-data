#!/usr/bin/env python3
"""Convert urlhaus-filter (Adblock format) into the plain feed SafeQR reads.

Why this exists: urlhaus.abuse.ch retired its public download files (HTTP 410
since late Oct 2026) and its API now needs an account key. urlhaus-filter
(https://gitlab.com/malware-filter/urlhaus-filter, CC0 + MIT) rebuilds the same
URLhaus data from the API twice a day and publishes it without a key.

Input lines look like      ||host/path^$all   or   a bare host / IP
Output lines look like     http://host/path   or   http://host

The app (src/analysis/threatDb.ts, parseFeedText) only keeps lines starting
with http(s):// and caps each feed at 30,000 entries, so we write at most that
many. Selection:
  1. every host-only entry (the whole host is malicious: the strongest signal)
  2. then path entries, ordered by a stable hash so the same URL stays in or
     out from run to run (no alphabetical bias, little commit churn)

Usage: convert_urlhaus_filter.py <input.txt> <output.txt> [max_entries]
"""
import hashlib
import sys
from urllib.parse import urlsplit

MAX_ENTRIES = 30000


def parse_line(line: str):
    line = line.strip()
    if not line or line.startswith(("!", "#", "@@")):
        return None  # comments, and allow-list rules (never block those)
    # Path rules carry a "||" prefix; whole-host entries are bare hosts/IPs.
    rule = line[2:] if line.startswith("||") else line
    # Drop the "^" separator and any "$options" suffix.
    rule = rule.split("$", 1)[0].rstrip("^")
    if not rule or " " in rule or "*" in rule:
        return None
    url = "http://" + rule
    try:
        parts = urlsplit(url)
    except ValueError:
        return None
    if not parts.hostname:
        return None
    return url, (parts.path not in ("", "/"))


def main() -> int:
    src, dst = sys.argv[1], sys.argv[2]
    limit = int(sys.argv[3]) if len(sys.argv) > 3 else MAX_ENTRIES

    updated = ""
    hosts, paths = [], []
    seen = set()
    with open(src, encoding="utf-8", errors="replace") as f:
        for raw in f:
            if raw.startswith("! Updated:"):
                updated = raw.split(":", 1)[1].strip()
            parsed = parse_line(raw)
            if not parsed:
                continue
            url, has_path = parsed
            if url in seen:
                continue
            seen.add(url)
            (paths if has_path else hosts).append(url)

    paths.sort(key=lambda u: hashlib.sha256(u.encode()).hexdigest())
    chosen = (hosts + paths)[:limit]

    with open(dst, "w", encoding="utf-8") as out:
        out.write("# SafeQR malware URL feed (URLhaus data via urlhaus-filter)\n")
        out.write("# Source: https://gitlab.com/malware-filter/urlhaus-filter (CC0)\n")
        out.write("# Original data: https://urlhaus.abuse.ch/ (CC0)\n")
        out.write(f"# Upstream updated: {updated or 'unknown'}\n")
        out.write(f"# Entries: {len(chosen)} of {len(hosts) + len(paths)} online\n")
        for url in chosen:
            out.write(url + "\n")

    print(f"hosts={len(hosts)} paths={len(paths)} written={len(chosen)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
