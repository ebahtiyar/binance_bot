# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 10:31:33 2021

@author: emreb
"""

from binance.client import Client

import constant as keys
import takeData as data
import indicator as ind
from heapq import nsmallest
api_key = keys.Binance_API_KEY
api_secret = keys.Binance_API_Secret

client = Client(api_key, api_secret)

def findOptimalCoin(trdPair1,trdPair2):
    
        rsi_list = list()
        stochrsif_list = list()
        stochrsis_list = list()
        
        for trdPair1 in trdPair1:
            tradePair = trdPair1 + trdPair2
            close_array,close_finished,openn_array,openn_finished,low_array,low_finished,high_array,high_finished = data.takeData(tradePair,"5m","500")
            rsi = ind.computeRSI(close_array, 14)
            stochrsif, stochrsis = ind.generateStochasticRSI(close_array, 14)
            
            
            rsi_list.append(rsi)
            stochrsif_list.append(stochrsif)
            stochrsis_list.append(stochrsis)
    
        rsi_list = [float(i) for i in rsi_list]
        stochrsif_list = [float(i) for i in stochrsif_list]
        stochrsis_list = [float(i) for i in stochrsis_list]
        
        coin_by_rsi = nsmallest(10,rsi_list)
        
        
        coin_index_rsi = list()
        for i in coin_by_rsi:
           coin_index_rsi.append(rsi_list.index(i))
        
        
        
        stochrsi_index = list()
        
        for i in coin_index_rsi:
            if (stochrsif_list[i]  > stochrsis_list[i] + 5 and (stochrsis_list[i] < 80)):
               stochrsi_index.append(i)
               
               
        
        stochrsi = list()
        for i in stochrsi_index:
            stochrsi.append(stochrsif_list[i])
        
    
        
        
        if len(stochrsi) == 0 :
            
            optimalCoin_index = -1
            print("optimalCoin_index = -1")
            
        else:
            optimalCoin_index = stochrsif_list.index(min(stochrsi))
            print("RSI:", rsi_list[optimalCoin_index] ,  "Stochrsisf:" , stochrsif_list[optimalCoin_index]
                ,  "Stochrsis:" ,  stochrsis_list[optimalCoin_index])
            print("optimalCoin_index: " , optimalCoin_index)
        
        return  optimalCoin_index
    
 