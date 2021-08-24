


import requests

data = open("bitcoin_180days.json", "w", encoding="UTF-8")

url = "https://api.upbit.com/v1/candles/days"

querystring = {"market":"KRW-BTC","count":"180"}

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers, params=querystring)

data.write(response.text)
data.close()