import streamlit as st
import requests
from datetime import datetime
import os

CURRENCIES = ['USD', 'EUR', 'GBP', 'PKR', 'INR']
LOG_FILE = "conversion_log.txt"
API_URL = "https://api.exchangerate-api.com/v4/latest/"


def get_exchange_rate(from_currency, to_currency):
    try:
        response = requests.get(API_URL + from_currency)
        data = response.json()
        return data['rates'].get(to_currency, None)
    except:
        return None

def log_conversion(amount, from_currency, to_currency, result):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {amount} {from_currency} = {result} {to_currency}\n"
    with open(LOG_FILE, "a") as f:
        f.write(entry)
    return entry

def clear_log():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

st.set_page_config(page_title="Currency Converter", layout="centered")

# code by M. Shameer Asim

st.title("Real-Time Currency Converter")

st.divider()

amount = st.text_input("Enter Amount 💰")

col1, col2 = st.columns(2)
with col1:
    from_currency = st.selectbox("From Currency", CURRENCIES, index=0)
with col2:
    to_currency = st.selectbox("To Currency", CURRENCIES, index=1)


col_convert, col_clear = st.columns([1, 1])
convert_clicked = col_convert.button("🔄 Convert")
clear_clicked = col_clear.button("Clear Conversion History")

if convert_clicked:
    if not amount.strip():
        st.error("Enter an amount.")
    else:
        try:
            amount_value = float(amount)
            rate = get_exchange_rate(from_currency, to_currency)
            if rate is None:
                st.error("❌ Failed to fetch exchange rate. Check internet or currency codes.")
            else:
                result = round(amount_value * rate, 2)
                msg = f"✅ {amount_value} {from_currency} = {result} {to_currency}"
                st.success(msg)

                # Log conversion
                entry = log_conversion(amount_value, from_currency, to_currency, result)
                st.write(f"🕒 Conversion logged at {datetime.now().strftime('%H:%M:%S')}")
        except ValueError:
            st.error("❗ Please enter a valid numeric amount.")

if clear_clicked:
    clear_log()
    st.info("✅ Conversion history cleared.")


if os.path.exists(LOG_FILE):
    with st.expander("📜 Conversion History"):
        with open(LOG_FILE, "r") as f:
            history = f.read()
            st.text(history if history else "No conversions yet.")


st.divider()
st.caption("Converter App built by: M. Shameer Asim")

#run using: python -m streamlit run currency_converter_app.py
