"""
My Indicators Module
我的指标模块，包含了重新实现的指标函数或类。
"""
import  backtrader as bt
import pandas as pd
import numpy




class Ketler(bt.Indicator):
    params = dict(ema=20, atr=17)
    lines = ('expo', 'atr', 'upper', 'lower')
    plotinfo = dict(subplot=False)
    plotlines = dict(
        upper=dict(ls='--'),
        lower=dict(_samecolor=True)

    )

    def __init__(self):
        self.l.expo = bt.talib.EMA(self.data0.close, timeperiod=self.params.ema)
        self.l.atr = bt.talib.ATR(self.data.high, self.data.low, self.data.close, timeperiod=self.params.atr)
        self.l.upper = self.l.expo + self.l.atr
        self.l.lower = self.l.expo - self.l.atr


def myMACD(price):

    dif = bt.indicators.ExponentialMovingAverage(price, period=12) - bt.indicators.ExponentialMovingAverage(price, period=26)
    dea = bt.indicators.ExponentialMovingAverage(dif, period=9)
    macd = 2 * (dif - dea)

    return dif,dea,macd

