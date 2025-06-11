import time, requests
import pandas as pd
import config as cfg

def validate_response(response):
    if response.status_code == 200:
        print("Success!")
        return True
    print(f"Error! Code {response.status_code}")
    return False

# don't include the quality in item name
def backpack(item, quality, fname):


    resp = requests.get("https://backpack.tf/api/IGetPriceHistory/v1", params = {
        "appid": 440,
        "item": item,
        "quality": quality,
        # "tradable": "Tradable",
        # "craftable": "Craftable",
        # "priceindex": 2,
        # "killstreak_tier": 3,
        "key" : cfg.bpAPI,
    }, headers = {
    "accept": "application/json"})


    if validate_response(resp):
        df = pd.DataFrame(resp.json()["response"]["history"])
        if len(df) == 0:
            print("No Entries")
        else:
            df["timestamp"] = pd.to_datetime(df["timestamp"], unit='s')
            df.to_csv(f"{fname}.csv")
        return df

backpack("Earbuds", "Unique", "backpack_test")

def steam(item):
    url = "https://steamcommunity.com/market/pricehistory/"
    params = {
        "appid": 440,
        "market_hash_name": item
    }

    cookies = {
        "steamLoginSecure": cfg.cookieSLS,
        "sessionid": cfg.cookieSID
    }


    response = requests.get(url, params=params, cookies=cookies)
    if validate_response(response):
        df = pd.DataFrame(response.json()["prices"], columns=["timestamp_str", "price", "volume"])
        df.to_csv("steam_test.csv")
        return df
    
steam("Earbuds")

# to do
def compute_stats(fname):
    pass
