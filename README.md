Real-Time Currency Converter
============================

Description:
------------
This is a simple and intuitive web-based Currency Converter app built with Streamlit. It fetches real-time exchange rates using an external API and supports conversion between five major currencies: USD, EUR, GBP, PKR, and INR. All conversions are logged locally for user reference.

Author:
-------
M. Shameer Asim

Features:
---------
✔️ Real-time exchange rate conversion  
✔️ Conversion history logging  
✔️ Clear history with a button click  
✔️ Intuitive and clean user interface  
✔️ GUI Built using Streamlit  

Supported Currencies:
---------------------
- USD (US Dollar)
- EUR (Euro)
- GBP (British Pound)
- PKR (Pakistani Rupee)
- INR (Indian Rupee)

Requirements:
-------------
- Python 3.x
- Internet connection
- Libraries:
  - streamlit
  - requests

To install required libraries:
------------------------------
Open your terminal or command prompt and run:

    pip install streamlit requests

How to Run:
-----------
1. Save the Python code in a file named: `currency_converter_app.py`
2. Open a terminal and navigate to the directory containing the file.
3. Run the app using:

    python -m streamlit run currency_converter_app.py

Files:
------
- `currency_converter_app.py` : Main application script
- `conversion_log.txt`        : Auto-generated log file containing conversion history
