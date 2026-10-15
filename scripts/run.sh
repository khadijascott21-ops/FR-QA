#!/usr/bin/env bash
# Launches the Currency Converter. Works from the distribution zip (bin/) or from the project (after mvn package).
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
for base in "$DIR/.." "$DIR/../target"; do
  JAR="$(ls "$base"/currency-converter-*.jar 2>/dev/null | head -n 1 || true)"
  [ -n "$JAR" ] && break
done
if [ -z "${JAR:-}" ]; then
  echo "currency-converter jar not found. Run 'mvn package' first." >&2
  exit 1
fi
exec java -jar "$JAR" "$@"
