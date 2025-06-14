## Overview

A comparison of the current APIs available that were working for me to obtain the price history of an item in the Team Fortress 2 market. 

Currently, only 2 methods are looked at, using Backpack.tf API and Steams API for accessing price history. 

## TF2 Market

TF2 is an FPS game created by Valve, that quickly established an economy worth quite a bit of money. Its primary currency is Keys and Refined Metal

## Installation

Create a config.py file and fill in with necessary api key / session credentials for Steam. For this I used cookies for my current Steam session (idk if this is a bad idea)

## To-do (for me)

* Basic financial analysis of recorded data
* Gladiator.tf and Marketplace.tf API / price history data

## Notes

Backpack's available api for price history is quite old (v1) compared to the updated api's available (v4). Its difficult to use and has very scarce data points. Also I wasn't able to find how to access price histories for Killstreak items. 
Web scraping I am pretty sure is not encouraged for Backpack.tf as you are meant to use the free api's instead, but it would be a better way of getting the data.

You can also view steam price histories without the need for logging in or personal details [here](https://github.com/HilliamT/scm-price-history)

Sources used:

https://gwern.net/doc/economics/2012-varoufakis-teamfortress2arbitrage.html
https://theceoviews.com/tf2-trade-mastery-strategies-for-success-in-the-team-fortress-2-economy/


