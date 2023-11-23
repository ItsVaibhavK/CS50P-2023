import json
import requests
import sys

# get number of CLAs
argc = len(sys.argv)

# no CLA
if argc != 2:
    sys.exit("Missing command-line argument")
try:
    # convert CLA to float
    n = float(sys.argv[1])
# CLA is not a number
except ValueError:
    sys.exit("Command-line argument is not a number")


try:
    # get JSON using requests.get and URL
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    # use JSON module to interpret data
    x = response.json()
    # access correct keys to get required float USD value of current rate of Bitcoin
    value = x["bpi"]["USD"]["rate_float"]
    # multiply value by CLA entry of how many bitcoins user wants to purchase
    amount = value * n
    # print output in USD, 4 places
    print(f"${amount:,.4f}")

except requests.RequestException:
    sys.exit("Could not fetch requested data")