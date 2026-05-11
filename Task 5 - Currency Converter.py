import requests  # Used for API calls

print("--------- CURRENCY CONVERTER ---------")
print("All Currency codes are: 'USD', 'AED', 'AFN', 'ANG', 'AUD', 'BND', 'EGP', 'EUR', 'GBP', 'INR', 'JPY', 'KZT', 'NGN', 'NPR', 'NZD', 'PKR', 'QAR', 'RUB', 'ZMW'\n")

amount = int(input("Enter the amount: "))
from_currency = input("Enter the current currency: ").upper()
to_currency = input("Enter the currency to which you want to convert: ").upper()

# Free API
url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"  

response = requests.get(url)
data = response.json()

# Conversion rate
rate = data["rates"][to_currency]

# Converted amount
converted_amount = amount * rate

print(f"\n{amount} {from_currency} = {round(converted_amount, 2)} {to_currency}")
