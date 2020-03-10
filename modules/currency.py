import requests


def getRate():
    res = requests.get("https://api.exchangeratesapi.io/latest?base=USD&symbols=TRY")
    js = res.json()
    rate = str(js['rates']['TRY'])
    return "USD = " + rate[:5] + "TL"
