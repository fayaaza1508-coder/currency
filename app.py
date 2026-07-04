import streamlit as st
import requests

st.title("World Currency Converter")

amount = st.number_input("Enter Amount", min_value=0.0)

from_currency = st.text_input("From Currency", "INR").upper()
to_currency = st.text_input("To Currency", "USD").upper()

if st.button("Convert"):
    url = f"https://open.er-api.com/v6/latest/{from_currency}"

    response = requests.get(url)
    data = response.json()

    if data["result"] == "success":
        if to_currency in data["rates"]:
            converted = amount * data["rates"][to_currency]
            st.success(f"{amount} {from_currency} = {converted:.2f} {to_currency}")
        else:
            st.error("Invalid TO currency")
    else:
        st.error("API error")