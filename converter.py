# Currency Converter - Simple Version
# Author: Omar Khouja
# Description:
# This mini program reads currency exchange rates from a text file (rates.txt)
# and allows the user to convert between currencies.

# -----------------------------
# Step 1: Read rates from file and store in a dictionary
rates = {}  # Dictionary to store currency rates

# Open the rates.txt file
with open("rates.txt", "r") as file:  # Open the rates.txt file for reading
    for line in file:                 # Read the file line by line
        parts = line.strip().split()  # Remove extra spaces and split each line by space
        currency = parts[0]           # First part is the currency code, e.g., "EUR"
        rate = float(parts[1])        # Second part is the exchange rate as a float e.g. 0.92
        rates[currency] = rate        # Add currency and rate to the dictionary

# -----------------------------
# Step 2: Show available currencies
print("Available currencies:")
for c in rates:
    print("-", c)

# -----------------------------
# Step 3: Ask the user for input
from_currency = input("\nConvert from (e.g. USD): ").upper()    # Convert input string to uppercase
to_currency = input("Convert to (e.g. EUR): ").upper()
amount = float(input("Amount: "))     # Convert input string to float

# -----------------------------
# Step 4: Convert the amount
# Conversion logic explanation:
# All rates in rates.txt are stored relative to USD (1 USD = X currency)
# Therefore, when converting from one non-USD currency to another (e.g., JPY -> EUR),
# we first convert the amount to USD, then from USD to the target currency.
# This makes the calculation simple and consistent for all currencies.

amount_in_usd = amount / rates[from_currency]
converted = amount_in_usd * rates[to_currency]

# -----------------------------
# Step 5: Show result
print(f"\n{amount:.2f} {from_currency} = {converted:.2f} {to_currency}")
# Example output:
# 100.00 USD = 92.00 EUR