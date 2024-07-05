import requests
#source block_env/bin/activate

response = requests.get("https://api.coinbase.com/v2/prices/spot?currency=USD")
print()
print(response. text)
print()