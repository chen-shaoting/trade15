import myIndicators as mnd
import myStrategis_bak2 as mstbk
import myStrategis as mst
import backtrader as bt
import pandas as pd

import matplotlib.pyplot as plt
from datetime import datetime
import datetime as dt

from stockPool import *
from stockCategory import *


def getKDataFromEfinance(code, beg, end, freq):
    pass

def getKDataFromFutuCSV(code):
    filepath='etfCSVData\{}.csv'.format(code)

    df=pd.read_csv(filepath)

    df = df.iloc[:, :10]

    df.columns = ['seq','code', 'datetime', 'open', 'close', 'high', 'low', 'pre','turn', 'volume']

    df['datetime'] = pd.to_datetime(df['datetime'])

    df['openinterest'] = 0
    df = df[['datetime', 'open', 'high', 'low', 'close', 'volume', 'openinterest']]

    df.set_index('datetime', inplace=True)


    return df



# use futu KData CSV to backtest
def backtestWithFutuCSV(code):
    pass
    # 创建Cerebro
    cerebro = bt.Cerebro()
    # 读取数据



    dataframe = getKDataFromFutuCSV(code)
    data = bt.feeds.PandasData(dataname=dataframe, name='d1',fromdate=dt.datetime(2022, 1, 1),todate=dt.datetime(2022, 3, 1))
    cerebro.adddata(data)

    # 装载数据到cerebro

    # 装载策略

    cerebro.addstrategy(mst.kdj20macd60sma5_Strategy)
    # cerebro.addstrategy(mst.statsKDJStrategy)
    # 装载分析器

    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='SharpeRatio')
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='DrawDown')
    # 设置现金和佣金
    cerebro.broker.setcash(1000000)
    cerebro.broker.setcommission(commission=0.0006)

    # cerebro.broker.
    # 设置sizer仓位
    cerebro.addsizer(bt.sizers.PercentSizer, percents=99)
    # 开始回测
    result = cerebro.run()
    # 打印分析结果

    # print('夏普比率：', result[0].analyzers.SharpeRatio.get_analysis()['sharperatio'])
    profitRatio = cerebro.broker.get_value() / 1000000
    # print('最大回撤：{:.2f}'.format( result[0].analyzers.DrawDown.get_analysis()['max']['drawdown']))
    print(code, ' ', '收益率：%.2f' % (profitRatio))
    # 输出图表
    # if profitRatio != 1:
    #     pass
    cerebro.plot(style='candle', volume=True)
    return profitRatio



if __name__ == "__main__":
    symbols =[
        '159875'
    ]
    # symbols = etf
    result = []
    for s in symbols:

        if s.startswith('1'):
            s = 'SZ.' + s
        if s.startswith('5'):
            s = 'SH.' + s
        try:

            p = backtestWithFutuCSV(s)
            result.append({'code': s, 'ProfitRatio': p})
        except:
            pass


