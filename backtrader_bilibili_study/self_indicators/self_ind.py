#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import backtrader as bt
import datetime
import pandas as pd


# In[ ]:


from tusharefeed import TushareData
feed = TushareData(
    dataname='159915',
    fromdate=datetime.date(2020,1,1),
    todate=datetime.date(2020,6,1), 
)


# In[ ]:


import numpy as np

class BRindicator(bt.Indicator):
    lines = ('br',)
    params = (('period', 26),)

    plotlines = dict(br=dict(ls='--', color='blue'))

    def __init__(self):
        self.addminperiod(self.params.period+1)

    def next(self):
        th = np.array(self.data.high.get(ago=0, size=self.p.period))
        tl = np.array(self.data.low.get(ago=0, size=self.p.period))
        yc = np.array(self.data.close.get(ago=-1, size=self.p.period))
        self.lines.br[0] = np.sum(th-yc)/np.sum(yc-tl) *100


# In[ ]:


# Create a Stratey
class EmptyStrategy(bt.Strategy):
    '''
    Empty strategy is used to study indicators
    '''
    params = (
        ('none', 0),
    )
        
    def __init__(self):
        self.br = BRindicator(self.data0, period=10)
        pass
        
    def next(self):
        print('BR:{}'.format(self.br[0]))
        pass 
    
    def stop(self):
        pass


# In[ ]:


cerebro = bt.Cerebro(oldtrades=False, stdstats=False)
cerebro.adddata(feed, name='cy_daily')
#cerebro.resampledata(feed, name='cy_weekly', timeframe=bt.TimeFrame.Weeks)


cerebro.addstrategy(EmptyStrategy)

# exp indicators
#cerebro.addindicator(bt.indicators.DirectionalMovementIndex)
#cerebro.addindicator(BRindicator, period=10)

# init cash
cerebro.broker.setcash(10000.0)

print('Starting Running')

result = cerebro.run()

print('Finish Running')


# In[ ]:


params = dict(
    style='candle',
    barup='#FF0033',
    bardown='#32CD32',
    volup='#F66269',
    voldown='#43A047',
)
cerebro.plot(
    iplot=False, 
    **params
)

