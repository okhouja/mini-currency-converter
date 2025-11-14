# update_rates_simple.py
# ----------------------
# This script fetches latest currency exchange rates relative to USD
# from HexaRate API and updates a local file 'rates.txt'.
# 
# API Request Example:
# curl --request GET \
#   --url 'https://hexarate.paikama.co/api/rates/latest/USD?target=GBP'
#
# Example API Response:
# {
#   "status_code": 200,
#   "data": {
#     "base": "USD",
#     "target": "GBP",
#     "mid": 0.780945,
#     "unit": 1,
#     "timestamp": "2025-10-153T05:16:50.272Z"
#   }
# }
#
# Explanation of fields:
# - base: the base currency for conversion (USD)
# - target: the target currency (e.g., GBP)
# - mid: the mid-market exchange rate
# - unit: number of units (usually 1)
# - timestamp: UTC time when the rate was last updated
#
# The script converts the UTC timestamp to Berlin time (CEST, UTC+2)
# and prints both rates and timestamps for the selected currencies.

import requests
from datetime import datetime, timedelta

# List of currencies to update (relative to USD)
currencies = ["USD", "EUR", "GBP", "JPY", "TRY", "CAD", "AUD", "CHF", "CNY", "INR"]
rates = {}
timestamps = {}

print("🔄 Fetching latest currency rates from HexaRate...")

for cur in currencies: # Loop through each currency
    if cur == "USD":
        rates[cur] = 1.0
        timestamps[cur] = "Base currency"  # Add timestamp for USD
        continue

    # Fetch latest rate from HexaRate API
    URL = f"https://hexarate.paikama.co/api/rates/latest/USD?target={cur}"
    data = requests.get(URL).json()

    # Extract rate and timestamp
    rate = data['data']['mid']              # Extract the mid-market rate
    utc_time = data['data']['timestamp']    # UTC time from API

    # Convert UTC to local time (Berlin time, CEST = UTC+2)
    dt = datetime.fromisoformat(utc_time.replace("Z", "+00:00"))
    local_time = dt + timedelta(hours=2)

    # Save rate in dictionary
    rates[cur] = rate
    timestamps[cur] = local_time.strftime("%Y-%m-%d %H:%M:%S")  # Format timestamp

# Write all rates to 'rates.txt'
with open("rates.txt", "w") as file:
    for cur, val in rates.items():
        file.write(f"{cur} {val:.2f} (updated in Berlin Time: {timestamps[cur]}) \n")
print("✅ Rates updated successfully in rates.txt")

# Show the updated rates to see immediately
print("✅ Rates updated:")
for cur, val in rates.items():
    print(f"{cur}: {val:.2f} (updated in Berlin Time: {timestamps[cur]})")