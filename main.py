import time, requests
import pandas as pd
import config as cfg
import matplotlib.pyplot as plt


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

# backpack("Earbuds", "Unique", "backpack_test")

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
    
steam("Haunted%20Voodoo-Cursed%20Soldier%20Soul")

# helper function
def plot(df, time, metric):
    plt.plot(time,df[metric],label=metric)
    plt.xlabel("Date")
    plt.ylabel("Price (£)")
    plt.legend()


# computes 8 metrics
# Moving Averages -> Simple and Exponential MA - 7 days and 30 days
# Momentum - 7 Days and 30 Days 
# Volatility - yearly and monthly
def compute_stats(fname):
    df = pd.read_csv(fname)

    # dataset cleaning
    df['timestamp_str'] = df['timestamp_str'].str[:-7]
    df['timestamp_str'] = pd.to_datetime(df['timestamp_str'])
    df = df.drop(df.columns[0],axis=1)
    df.set_index('timestamp_str', inplace=True)
    # df = df.drop(df.columns[0],axis=0)
    print(df.columns)
    # print(df)
    # df.set_index('timestamp_str', inplace=True)
    # df.drop(df.columns[0], axis=1)
    # print(df.columns)
    # df = df.resample('3D').mean().dropna().reset_index()

    df["SMA_7"] = df['price'].rolling(window=7).mean()
    df["SMA_30"] = df['price'].rolling(window=30).mean()
    df['EMA_7'] = df['price'].ewm(span=7, adjust=False).mean()
    df['EMA_30'] = df['price'].ewm(span=30, adjust=False).mean()
    df["MOMENT_30"] = df['price'].pct_change(periods=30)
    df["MOMENT_7"] = df['price'].pct_change(periods=7)
    graphs = ["price","SMA_7","SMA_30","EMA_7","EMA_30","MOMENT_7","MOMENT_30",""]
    # plt.plot(df.index,df['SMA_30'],label="normal")
    for i in range(7):
        plt.subplot(3,3,i+1)
        plot(df, df.index, graphs[i])

    # volatility_yearly = df.groupby(df.index.dt.year)['price'].std() * (365 ** 0.5)
    volatility_yearly = df.resample('Y')['price'].std() * (365 ** 0.5)
    volatility_monthly = df.resample('M')['price'].std() * (30 ** 0.5)
    plt.subplot(3,3,8)
    plt.plot(volatility_yearly.index,volatility_yearly,label="VOL_365")
    plt.xlabel("Year")
    plt.ylabel("Percent")
    plt.legend()
    plt.subplot(3,3,9)
    plt.plot(volatility_monthly.index,volatility_monthly,label="VOL_30")
    plt.xlabel("Date")
    plt.ylabel("Percent")
    plt.legend()
    plt.show()

# grouping by month - see price comparison for each month on average, see which months tend to be more expensive (short term investing/trading)
# and volatility - what months tend to be volatile or unstable
def monthly_comparison(fname):
    df = pd.read_csv(fname)
    df['timestamp_str'] = df['timestamp_str'].str[:-7]
    df['timestamp_str'] = pd.to_datetime(df['timestamp_str'])
    volatility = df.groupby(df['timestamp_str'].dt.month)['price'].std() * (365 ** 0.5)
    average_price = df.groupby(df['timestamp_str'].dt.month)['price'].mean() 

    plt.subplot(2,1,1)
    plt.plot(volatility.index,volatility,label="volatility")
    plt.xlabel("Month")
    plt.ylabel("Percent")
    plt.legend()
    plt.subplot(2,1,2)
    plt.plot(average_price.index,average_price,label="price")
    plt.xlabel("Month")
    plt.ylabel("Price")
    plt.legend()
    plt.show()


# compute_stats("steam_test.csv")
monthly_comparison("steam_test.csv")