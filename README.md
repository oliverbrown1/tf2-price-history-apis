## Overview

A comparison of the current APIs available that were working for me to obtain the price history of an item in the Team Fortress 2 market. Currently, only 2 methods are looked at, using Backpack.tf API and Steam for accessing price history. 

A simple financial analysis is performed on the retrieved API data. We compuite the rolling SMA, EMA, Momentum for both 7 days and 30 days. We also compute Volatility. There is also the option to compute the average price and volatility grouping by each month. Since the economy is heavily influenced by annual events i.e. Halloween (Scream Fortress) and Christmas (Smissmas), we can analyse statistics for each month, and can see that prices and volatility generally spikes during both of these events.

### TF2 Market

TF2 is an FPS game created by Valve, that quickly established an economy worth quite a bit of money. Its primary currency is Keys and Refined Metal

### Backpack

Backpack.tf's API requires you to create an API key by logging in through steam onto their next.backpack.tf page [here](https://next.backpack.tf/account/api-access) here. You can fetch the price history for any item, which records a new price whenever there is a significant change between the last recorded price i.e. +- 5%.

Backpack's available api for price history is quite old (v1) compared to the updated api's available (v4). Its difficult to use and has very scarce data points. Also I wasn't able to find how to access price histories for Killstreak items. 
Web scraping I am pretty sure is not encouraged for Backpack.tf as you are meant to use the free api's instead, but it would be a better way of getting the data.

To use the backpack method, create a config file with a bpAPI variable.

### Steam

Steam has API's available, just not for fetching price history, so no API key is required. On the other hand you do need to be logged in, and there is a Python library available online for web authentication, but it is too outdated to work. For this code, I recommend you create or use a burner Steam account for security purposes, as anyone can use your session cookies to login.

To obtain the required login cookies, be logged in on Steam on a browser -> Inspect -> Application -> Cookies. You should see cookies for steamcommunity.com. For the program to login it requires the sessionid and steamLoginSecure cookies. Copy and paste these into the config file as cookieSID and cookieSLS respectively, do not share these with anyone else. 

The program will store retrieved data as a csv file, which we will use for analysis.

You can also view steam price histories without the need for logging in or personal details [here](https://github.com/HilliamT/scm-price-history)

### Analysis

The program performs a simple financial analysis on the csv data. Using matplotlib, we can compute and plot the following:

* Simple Moving Average (7 and 30 days)
* Exponential Moving Average (7 and 30 days)
* Momentum (7 and 30 days)
* Volatility (monthly and yearly)

What can this be used for? Like all financial markets, investing. Using a simple financial analysis we can determine which items have low risk and higher returns over time, making them worthy investments. Furthermore, in TF2 specifically as the market is not subject to 7 day trading bans (like CS2), picking up items that are less volatile and have an increasing SMA/EMA are better for trading besides looking at trading volume and profit margins. 

## Installation

Install all necessary dependencies. Create a config.py file and fill in with necessary api key / session credentials for Backpack/Steam. Run the program. 

### Dependencies

* Python == 3.9+
* Pandas
* Matplotlib

## To-do

* Gladiator.tf and Marketplace.tf API / price history data


## Sources used

* https://gwern.net/doc/economics/2012-varoufakis-teamfortress2arbitrage.html
* https://theceoviews.com/tf2-trade-mastery-strategies-for-success-in-the-team-fortress-2-economy/
* https://www.cryptohopper.com/blog/trading-101-technical-analysis-for-beginners-168


