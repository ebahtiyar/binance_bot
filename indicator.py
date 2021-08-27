# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 10:28:50 2021

@author: emreb
"""
import talib as ta
import pandas as pd
import numpy as np


def generateStochasticRSI(close_array, timeperiod):
    
    rsi_array = ta.RSI(close_array, timeperiod=timeperiod)
    rsi_array = rsi_array[~np.isnan(rsi_array)]

   
    stochrsif, stochrsis = ta.STOCH(rsi_array, rsi_array, rsi_array, fastk_period=14, slowk_period=3, slowd_period=3)
    
    stochrsif_df = pd.DataFrame(stochrsif)
    stochrsis_df = pd.DataFrame(stochrsis) 

    stochrsif = format(float(stochrsif_df[0].iloc[-1]),".2f")
    stochrsis = format(float(stochrsis_df[0].iloc[-1]),".2f")
    return stochrsif, stochrsis


def computeRSI (data, time_window):
    diff = np.diff(data)
    up_chg = 0 * diff
    down_chg = 0 * diff
    
    up_chg[diff > 0] = diff[ diff>0 ]
    down_chg[diff < 0] = diff[ diff < 0 ]
    
    up_chg = pd.DataFrame(up_chg)
    down_chg = pd.DataFrame(down_chg)
    
    up_chg_avg   = up_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
    down_chg_avg = down_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
    
    rs = abs(up_chg_avg/down_chg_avg)
    rsi = 100 - 100/(1+rs)
    rsi = format(float(rsi[0].iloc[-1]),".2f")
    return rsi



