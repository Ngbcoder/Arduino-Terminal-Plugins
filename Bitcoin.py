import requests

def get_screen_data(): try: r = requests.get("[https://api.coinbase.com/v2/prices/BTC-USD/spot](https://api.coinbase.com/v2/prices/BTC-USD/spot)", timeout=2) price = r.json()['data']['amount']
f"BTC Price: |${float(price):,.0f}" except: return "Crypto Error |Check Connection"
