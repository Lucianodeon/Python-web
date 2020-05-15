import requests

def main():
    res = requests.get("http://api.fixer.io/lastest?base=USD&symbol=EUR")
    if res.status_code != 200: #means its all ok
        raise Exception ("Error: API requested unsuccessful.")
    data = res.json()
    print(data)

if __name__ == '__main__':
    main()
