# 💱 Mini Currency Converter

A beginner-friendly **Python mini project** that converts one currency to another using exchange rates stored in a local text file (`rates.txt`).

---

## 🧾 Features
- Reads currency exchange rates from a text file  
- Simple user input via terminal  
- Converts any currency to another using USD as a base  
- Beginner-friendly: uses only loops, dictionaries, and basic math  

---

## ⚙️ How It Works
1. The program reads each line from `rates.txt`
2. It stores the data in a dictionary like:  
   `{ "USD": 1.0, "EUR": 0.92, "GBP": 0.79, ... }`
3. The user chooses:
   - Source currency (e.g. `USD`)
   - Target currency (e.g. `EUR`)
   - Amount to convert
4. The amount is first converted to USD, then to the target currency.

---

## 🧩 Example
**rates.txt**

**rates.txt**
USD 1.0
EUR 0.92
GBP 0.79
JPY 151.35
TRY 34.25


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
Convert to (e.g. GBP): JPY
Amount: 10

10.00 EUR = 1641.77 JPY
```

## 🧠 What I Learned

- Reading from text files  
- Using `for` loops and dictionaries  
- Handling user input and output  
- Simple currency conversion logic  

---

## 🧰 Requirements

- Python 3 installed  
- `rates.txt` in the same folder as `converter.py`

---

## 🧑‍💻 Author

**Omar Khouja**  
📍 Hamburg, Germany  
🔗 [okhouja on GitHub](https://github.com/okhouja)
