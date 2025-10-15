# update_rates.py
# -----------------------
# This script fetches the latest currency exchange rates from HexaRate API
# for multiple currencies individually and updates the local 'rates.txt' file.
# All steps are explained in English for beginners.

import requests  # Import the requests library to send HTTP requests

# List of currencies to update (relative to USD)
currencies = ["USD", "EUR", "GBP", "JPY", "TRY"]

# Dictionary to store the fetched rates
rates = {}

print("🔄 Fetching latest currency rates from HexaRate...")

for cur in currencies:
    if cur == "USD":
        # USD is the base currency, rate = 1.0
        rates[cur] = 1.0
        continue

    # HexaRate API URL for the specific currency
    URL = f'https://hexarate.paikama.co/api/rates/latest/USD?target={cur}'

    try:
        response = requests.get(URL)
        response.raise_for_status()  # Raise error if HTTP request fails

        data = response.json()  # Convert JSON response to Python dict
        timestamp = data['data']['timestamp'] # Extract the timestamp of the rate

        if data.get('status_code') == 200 and 'data' in data:
            rates[cur] = data['data']['mid']  # Extract the mid-market rate
        else:
            print(f"⚠️ Failed to fetch rate for {cur}. Full response:", data)

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Failed to fetch rate for {cur}. Error:", e)

# Write all rates to 'rates.txt'
with open("rates.txt", "w") as file:
    for cur, value in rates.items():
        file.write(f"{cur} {value:.2f}\n")  # Save with 2 decimals for precision

print("✅ Rates updated successfully in rates.txt")
print("Current rates:")
for cur, value in rates.items():
    print(f"{cur}: {value:.2f} (updated: {timestamp})")
