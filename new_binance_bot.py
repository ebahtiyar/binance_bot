# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 10:27:57 2021

@author: emreb
"""

import time
from binance.client import Client
import takeData as data

import indicator as ind 
import constant as keys
import chooseOptimalCoin as opi

api_key = keys.Binance_API_KEY
api_secret = keys.Binance_API_Secret
client = Client(api_key, api_secret)


trdPair1 = ['SXP','ENJ','KAVA','RUNE','XLM','LINA',"XRP","DOT","EOS","SRM","LUNA","SOL",
            "BTT","VET","WIN", "LTO","CHZ","DEGO","TWT","1INCH","ALICE","HOT"
            ,"DOT","MATIC","SUSHI","BAKE","NEO","COTI","AUTO","CRV","REEF","XVS","ICP","IOST","ADA"
            ,"ALGO","ATOM"]

trdPair2 = 'BUSD'


#read coin list

f =  open('coins.txt', 'r') 
coins = list(f)
coin_list = list()
for i in coins:
    
    coin_list.append(i.strip())
    
trdPair1 = coin_list    

tradeControl = True
mainControl = True

while mainControl:
    
    optimalCoin_index = opi.findOptimalCoin(trdPair1,trdPair2)
    
    optimalCoin = trdPair1[optimalCoin_index]
    
    if optimalCoin_index == -1:
       print("Not Found")
       tradeControl = False
    else:
        optimalCoin = trdPair1[optimalCoin_index]
        tradePair = optimalCoin + "BUSD"
        tradeControl = True
        print(optimalCoin)
    
    time.sleep(10)
    
    while tradeControl:
        #try:
            price = client.get_ticker(symbol=tradePair)
            sigNum = len(str(int(float(price['askPrice']))))
            sigNumOfCoin = '.' + str(len(str(int(float(price['askPrice']))))) + 'f'
        
            busdCount = client.get_asset_balance(asset = trdPair2)
            busdCount = float(busdCount['free'])
        
            
        
            # Price & Server Time
            coitime = client.get_server_time()
            coitime = time.strftime('%m/%d/%Y %H:%M:%S',
                                time.gmtime(coitime['serverTime']/1000.))
            close_array,close_finished,openn_array,openn_finished,low_array,low_finished,high_array,high_finished = data.takeData(tradePair,"15m","500")
            stochrsif, stochrsis = ind.generateStochasticRSI(close_array, 14)
        #BUY
            if busdCount > 5:
               balance = client.get_asset_balance(asset = trdPair2)
               coiNumber = float(balance['free'])
               coiprice = format(float(price['askPrice']), '.4f')
               test = format(float(coiNumber)/float(coiprice) - 5*10**-sigNum, sigNumOfCoin)
               order = client.order_market_buy(symbol=tradePair, quantity=test)
               print(coitime + " Buying:" + tradePair + " ...")
         #SELL
            elif float(stochrsif) + 5 > float(stochrsis):
                trades = client.get_my_trades(symbol=tradePair)
                trades = trades[len(trades)-1] 
                sym = trades["symbol"]
                balance = client.get_asset_balance(asset = optimalCoin)
                coiNumber = format(float(balance['free']) - 5*10**-sigNum, sigNumOfCoin) 
                coiprice = format(float(price['askPrice']), '.4f')
            
                order = client.order_market_sell(
                    symbol=sym,
                    quantity= float(coiNumber),
                    price= coiprice)
                tradeControl = False
                print(coitime + " Selling:" + tradePair + " ...")
            else:
                print(coitime + " Hodl: " + tradePair)
    
            time.sleep(10)
