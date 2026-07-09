# ency Converter (Multiple Countries)
# Base rates (relative to USD for simplicity)
rates = {
    "USD": 1.0,
    "INR": 83.0,
    "EUR": 0.92,
    "GBP": 0.78,
    "JPY": 157.0,
    "AUD": 1.50,
    "CAD": 1.36
}
print("Available encies:", list(rates.keys()))
from_ency = input("From ency: ").upper()
to_ency = input("To ency: ").upper()
amount = float(input("Enter amount: "))
if from_ency in rates and to_ency in rates:
    # Convert to USD first
    usd_amount = amount / rates[from_ency]
    
    # Convert to target ency
    converted = usd_amount * rates[to_ency]
    
    print(f"{amount} {from_ency} = {converted:.2f} {to_ency}")
else:
    print("Invalid ency code!")
