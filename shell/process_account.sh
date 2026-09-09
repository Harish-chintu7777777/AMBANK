#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${AMBANK_BASE_URL:-https://mainframe.example.internal}"
ENDPOINT_PATH="/banking/account/update"
REQUEST_FILE="${1:-../config/account_request.json}"
OUTPUT_FILE="${2:-account_response.json}"

URL="${BASE_URL}${ENDPOINT_PATH}"

curl --silent --show-error \
  --request POST \
  --header "Content-Type: application/json" \
  --header "X-Source-System: AMBANK" \
  --header "X-Request-Id: WEB-$(date +%s)" \
  --max-time 30 \
  --data "@${REQUEST_FILE}" \
  --output "${OUTPUT_FILE}" \
  "${URL}"

cat "${OUTPUT_FILE}"
