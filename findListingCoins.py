# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 14:12:55 2021

@author: emreb
"""

from binance.client import Client
import constant as keys

api_key = keys.Binance_API_KEY
api_secret = keys.Binance_API_Secret

client = Client(api_key, api_secret)

products = client.get_products() 
data = products["data"]
coin_list = list()
    

i = 0
while i != len(data):
    coins = data[i]["s"]
    if coins.rfind("BUSD") > 0:
        coins = coins.replace("BUSD","")
        coin_list.append(coins)
        
    i = i + 1   
    
i = 0
index = list() 
while i!= len(coin_list):
    
    tradePair = coin_list[i] + "BUSD"
    
    try:
        klines = client.get_klines(symbol = tradePair ,interval = "15m",limit = "500")
        index.append(i)
        
        
    except:
        print("not add")
        
    i = i + 1
    
coins = list()
for i in index:
    coins.append(coin_list[i])

j = 0
with open("coins.txt", "w") as text_file:
    while j!=len(coins):
        text_file.write(coins[j]+"\n")
        j = j + 1
        
    
text_file.close()   

