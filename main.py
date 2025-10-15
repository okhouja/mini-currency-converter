# Currency Converter - Simple Version
# Author: Omar Khouja
# Description:
# Reads currency exchange rates from a text file (rates.txt)
# and allows the user to convert between currencies.

# Step 1: Read rates from file and store in a dictionary
rates = {}  # store currency rates here

# Open the rates.txt file
with open("rates.txt", "r") as file:
    for line in file:
        parts = line.strip().split()  # split each line by space
        currency = parts[0]           # e.g. "EUR"
        rate = float(parts[1])        # e.g. 0.92
        rates[currency] = rate        # add to dictionary

# Step 2: Show available currencies
print("Available currencies:")
for c in rates:
    print("-", c)

# Step 3: Ask the user for input
from_currency = input("\nConvert from (e.g. USD): ").upper()
to_currency = input("Convert to (e.g. EUR): ").upper()
amount = float(input("Amount: "))

# Step 4: Convert the amount
# First, convert the amount to USD, then to the target currency
amount_in_usd = amount / rates[from_currency]
converted = amount_in_usd * rates[to_currency]

# Step 5: Show result
print(f"\n{amount:.2f} {from_currency} = {converted:.2f} {to_currency}")
# Example output:
# 100.00 USD = 92.00 EUR