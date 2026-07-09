orld Currency Converter built using Python and Streamlit. Supports currency conversion between major world currencies using live exchange rates.
Currency Converter 💱

# This is a simple Currency Converter project built using Python (Flask).
💱 Currency Converter (Python CLI Project)
A simple Python command-line Currency Converter that converts amounts between different currencies using predefined exchange rates. This project demonstrates basic Python programming concepts like dictionaries, input handling, and arithmetic operations.
📌 Features
Convert between multiple currencies
Simple command-line interface (CLI)
Uses dictionary-based exchange rates
Converts via USD as base currency
Beginner-friendly Python project
🧠 How It Works
All currencies are stored in a dictionary with USD as base reference
Input currency is converted to USD first
Then USD is converted to target currency
Final result is displayed
💻 Code Overview
Python
rates = {
    "USD": 1.0,
    "INR": 83.0,
    "EUR": 0.92,
    "GBP": 0.78,
    "JPY": 157.0,
    "AUD": 1.50,
    "CAD": 1.36
}
rates → stores exchange values
.upper() → ensures currency code format (USD, INR, etc.)
float(input()) → takes decimal values for amount
▶️ How to Run
1. Install Python
   
Make sure Python 3 is installed:
Bash
python --version

## Features
- Convert currencies between countries
- Uses live exchange rate API
- Simple backend with Flask
2. Save File

## Technologies Used
- Python
- Flask
- Requests
- HTML (if frontend used)
Save your file as:

## How to Run
1. Install requirements:
currency_converter.py

3. Run Program

Bash
python currency_converter.py

🧾 Example Output

Available currencies: ['USD', 'INR', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD']

From ency: USD
To ency: INR
Enter amount: 10

10 USD = 830.00 INR
⚠️ Notes
Currency codes must be correct (USD, INR, EUR, etc.)
If invalid code is entered → program shows error message
Rates are fixed (not real-time)

🚀 Future Improvements
🌐 Add real-time API (live currency rates)
🖥️ Build web version using Flask
🎨 Add frontend (HTML/CSS)
📊 Add conversion history
📱 Mobile app version



