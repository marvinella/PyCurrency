# Project: Currency Converter
# Author: Sude Nur Kara
# Location: Málaga / 2026

import requests

api_key = "6fce9de3a8dbce8cfdd54984"

print("--- Welcome  ---\n")
print("Press 'q' to exit\n")

while True:
    try:
        currency = input("which currency do you want to change from? \n").upper()
        if currency == q: break
        
        currency_at = input("which currency do you want to change ar? \n").upper()

        amount = float(input(f"how much {currency} you want to change? \n"))

        x = requests.get(f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{currency}")
        x.raise_for_status() #bağlantı hatası olursa yakalar

        data_dictionary = x.json()

        c_from = data_dictionary["conversion_rates"][currency]
        c_at = data_dictionary["conversion_rates"][currency_at]

        response =  float(c_from * c_at * amount)

        print(f"Your {currency} in {currency_at} is {response:2f}")

    except ValueError:
        print("Error: Please enter a number in amount")
    except KeyError:
        print(f"Error: '{currency}' or '{currency_at}' is not valid")
    except requests.exceptions.ConnectionError:
        print("Error: Check your internet connection")
    except Exception as e:
        print(f"Unexpected error: Exception as {e}") #e error un ne olduğunu vercek. Eğer benim öngöremediğim genel bir hata (Exception) oluşursa, bu hatayı yakala ve bütün teknik detaylarını e isimli değişkenin içine koy.

    input("\nPress enter to continue").lower()
