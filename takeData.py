# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 10:38:59 2021

@author: emreb
"""
from binance.client import Client
import numpy as np


import constant as keys


api_key = keys.Binance_API_KEY
api_secret = keys.Binance_API_Secret

client = Client(api_key, api_secret)


def takeData(sym,intrvl , lmt):
    klines = client.get_klines(symbol = sym ,interval = intrvl,limit = lmt)
    
    close = [float(entry[4]) for entry in klines]
    close_array = np.asarray(close) 
    close_finished = close_array[:-1]
     
    openn = [float(entry[1]) for entry in klines]
    openn_array = np.asarray(openn)
    openn_finished = openn_array[:-1]
     
    low = [float(entry[3]) for entry in klines]
    low_array = np.asarray(low)
    low_finished = low_array[:-1]
    
    high = [float(entry[2]) for entry in klines]
    high_array = np.asarray(high)
    high_finished = high_array[:-1]  
    
    return close_array,close_finished,openn_array,openn_finished,low_array,low_finished,high_array,high_finished