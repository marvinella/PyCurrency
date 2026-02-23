# PyCurrency
A dynamic currency converter using ExchangeRate-API with robust error handling and interactive user loop

##Key Features
* **Live Data:** Fetches up-to-the-minute exchange rates from [ExchangeRate-API](https://www.exchangerate-api.com/).
* **Error Handling:** Built with `try-except` blocks to manage invalid inputs, missing currency codes, and connection errors gracefully.
* **Interactive Loop:** Runs continuously until the user chooses to exit by typing 'Q'.
* **User-Friendly:** Case-insensitive input handling using the `.upper()` method.

##Technical Skills Demonstrated
* **API Integration:** Using the `requests` library to communicate with RESTful APIs.
* **Data Parsing:** Managing and navigating JSON/Dictionary structures in Python.
* **Flow Control:** Implementing `while` loops and `break` statements for a seamless user experience.
* **Exception Handling:** Managing `KeyError`, `ValueError`, and `HTTPError`.

##How to Run
1. Make sure you have Python installed.
2. Install the required `requests` library:
   ```bash
   pip install requests
