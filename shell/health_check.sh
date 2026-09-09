#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${AMBANK_BASE_URL:-https://mainframe.example.internal}"
HEALTH_ENDPOINT="/health"

URL="${BASE_URL}${HEALTH_ENDPOINT}"

curl --silent --show-error \
  --request GET \
  --header "Accept: application/json" \
  --max-time 10 \
  "${URL}"

echo ""
