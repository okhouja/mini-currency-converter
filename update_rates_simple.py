# update_rates_simple.py
import requests

currencies = ["USD", "EUR", "GBP", "JPY", "TRY"]
rates = {}

print("🔄 Fetching latest currency rates from HexaRate...")

for cur in currencies:
    if cur == "USD":
        rates[cur] = 1.0
        continue
    URL = f'https://hexarate.paikama.co/api/rates/latest/USD?target={cur}'
    data = requests.get(URL).json()
    rates[cur] = data['data']['mid']

with open("rates.txt", "w") as file:
    for cur, val in rates.items():
        file.write(f"{cur} {val:.2f}\n")
print("✅ Rates updated successfully in rates.txt")

# Show the updated rates for students to see immediately
print("✅ Rates updated:")
for cur, val in rates.items():
    print(f"{cur}: {val:.2f}")