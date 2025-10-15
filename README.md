# 💱 Mini Currency Converter

### A beginner-friendly **Python mini project** created for the [Redi School Python Foundation Course - Hamburg](https://www.redi-school.org/data-analytics/hamburg/dcp/python-foundation) :  
- It converts amounts between currencies using a local file (`rates.txt`)  
- and includes an optional advanced feature to update exchange rates from the internet.

---

## 🏗 Project Structure

- `converter.py` → Main program (reads `rates.txt` and converts currencies).  
- `rates.txt` → Text file containing exchange rates.  
- `update_rates.py` → Optional advanced script to fetch latest rates from [HexaRate API](https://hexarate.paikama.co/).  
- `update_rates_simple.py` → Beginner-friendly script for quick demonstration (updates rates and shows them in terminal).

---

## 🧾 Features

- Reads currency exchange rates from a text file  
- Simple user input via terminal  
- Converts any currency to another using USD as a base  
- Beginner-friendly: uses only loops, dictionaries, and basic math  
- Optional: updates rates from the internet using HexaRate API  

---

## ⚙️ How It Works

1. `converter.py` reads the exchange rates from `rates.txt`.  
2. User chooses **source** and **target** currencies, then enters the amount.  
3. The program calculates and prints the converted value.  
4. Optional: run `update_rates.py` or `update_rates_simple.py` to refresh the rates before conversion.  
5. `update_rates_simple.py` is beginner-friendly:  
   - Updates the same currencies  
   - Prints new rates directly to the terminal  
   - Avoids complex error handling for simplicity

---

## 📝 Conversion Logic

1. The program reads each line from `rates.txt`  
2. Stores the data in a dictionary like:  
   ```python
   { "USD": 1.0, "EUR": 0.92, "GBP": 0.79, ... }
3. The user chooses:
   - Source currency (e.g. `USD`)
   - Target currency (e.g. `EUR`)
   - Amount to convert
4. Conversion formula:

    ```python
    amount_in_usd = amount / rates[from_currency]
    converted = amount_in_usd * rates[to_currency]
    ```
---
## 🌐 Optional: Update Rates from the Internet

**update_rates.py** fetches real rates from [HexaRate](https://hexarate.paikama.co/) and updates `rates.txt`.  

**How to use:**
```bash
$ python update_rates.py
✅ Rates updated successfully in rates.txt
```
**update_rates_simple.py** is a beginner-friendly version that:

* Updates the same currencies.

* Prints the new rates directly to the terminal for demonstration.

* Avoids complex error handling for students.
---
## 🕒 About the Timestamp (Berlin Time) - in `update_rates_simple.py`

When fetching rates from the HexaRate API, each response includes a UTC timestamp showing when the rate was last updated online.
The script automatically converts this timestamp to Berlin local time (CEST = UTC + 2) for better readability.
You’ll see each rate printed together with its local update time in the `Terminal` and in `rates.txt` file.

---
## 🌍 Currency Reference List (Important Currencies)

You can choose additional currencies from this list to add to `currencies` in `update_rates_simple.py` or `update_rates.py`:

| Code | Currency Name          |
|------|----------------------|
| USD  | United States Dollar  |
| EUR  | Euro                  |
| GBP  | British Pound         |
| JPY  | Japanese Yen          |
| TRY  | Turkish Lira          |
| AUD  | Australian Dollar     |
| CAD  | Canadian Dollar       |
| CHF  | Swiss Franc           |
| CNY  | Chinese Yuan          |
| EGP  | Egyptian Pound        |

For the full list of active currencies: [ISO 4217 Active Codes](https://en.wikipedia.org/wiki/ISO_4217#Active_codes_(list_one))

---

## 🧩 Example
**rates.txt**
```
USD 1.00
EUR 0.86
GBP 0.75
JPY 151.68
TRY 41.84
```


**Run the program**
```bash
$ python converter.py
Available currencies:
- USD
- EUR
- GBP
- JPY
- TRY

Convert from (e.g. USD): EUR
Convert to (e.g. GBP): GBP
Amount: 10

10.00 EUR = 8.71 GPB
```

## 🧠 What I Learned

- Reading from text files  
- Using `for` loops and dictionaries  
- Handling user input and output  
- Simple currency conversion logic  
- Optional: Fetching data from an online API

---

## 🧰 Requirements

- Python 3 installed  
- `rates.txt` in the same folder as `converter.py`
- Optional: `requests` library for online updates (`pip install requests`) 

---

## 🧑‍💻 Author

**Omar Khouja**  
📍 Hamburg, Germany  
🔗 [okhouja on GitHub](https://github.com/okhouja)
