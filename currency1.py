import requests

def main():
    res = requests.get("http://api.fixer.io/lastest?base=USD&symbol=EUR")
    if res.status_code != 200: #means its all ok
        raise Exception ("Error: API requested unsuccessful.")
    data = res.json()
    rate = data["rates"]["EUR"]
    print(f"1 USD is equal to {rate} EUR")

if __name__ == '__main__':
    main()
