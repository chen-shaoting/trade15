# from __future__ import (absolute_import, division, print_function,
#                         unicode_literals)
import runningStrategisDec22 as runst
import strategiesDec22 as mst
import backtrader as bt
import pandas as pd

import matplotlib.pyplot as plt
from datetime import datetime
import datetime as dt
import efinance as ef
from stockPool import *
from stockCategory import *

import argparse

import backtrader.feeds as btfeeds

def getKDataFromEfinance(code, beg, end, freq):
    df = ef.stock.get_quote_history(code, beg=beg, end=end, klt=freq, fqt=1)
    df = df.iloc[:, :13]
    df.columns = ['name', 'code', 'datetime', 'open', 'close', 'high', 'low', 'amount', 'volume', 'amplitude',
                  'updownratio', 'updownamount', 'exchange']
    df['datetime'] = pd.to_datetime(df['datetime'])
    df['openinterest'] = 0
    df = df[['datetime', 'open', 'high', 'low', 'close', 'volume', 'openinterest']]
    # df['dif'],df['dea'],df['macd'] = mnd.myMACD(df['close'])
    df.set_index('datetime', inplace=True)
    # df.to_csv('test.csv')
    return df


def getKDataFromFutuCSV():
    pass


def runETFTestWithFutuCSV():
    pass


# use futu KData CSV to backtest


def parse_args():
    parser = argparse.ArgumentParser(
        description='Pandas test script')

    parser.add_argument('--dataname', default='', required=False,
                        help='File Data to Load')

    parser.add_argument('--timeframe', default='weekly', required=False,
                        choices=['daily', 'weekly', 'monhtly'],
                        help='Timeframe to resample to')

    parser.add_argument('--compression', default=1, required=False, type=int,
                        help='Compress n bars into 1')

    return parser.parse_args()

def backtest(code):
    # 创建Cerebro
    cerebro = bt.Cerebro()
    # 读取数据
    today = datetime.now()
    endstr = '{}{}{}'.format(today.year, str(today.month).zfill(2), str(today.day).zfill(2))
    # print(endstr)
    # exit(1)
    delta = dt.timedelta(days=520)
    before = today - delta
    begstr = '{}{}{}'.format(before.year, str(before.month).zfill(2), str(before.day).zfill(2))
    dataframe = getKDataFromEfinance(code, begstr, endstr, 101)
    data = bt.feeds.PandasData(dataname=dataframe, name='d1')
    # 装载数据到cerebro
    cerebro.adddata(data)
    args = parse_args()
    tframes = dict(
        daily=bt.TimeFrame.Days,
        weekly=bt.TimeFrame.Weeks,
        monthly=bt.TimeFrame.Months)

    # Add the resample data instead of the original
    cerebro.resampledata(data,
                         timeframe=tframes[args.timeframe],
                         compression=args.compression)


    # 装载策略

    cerebro.addstrategy(runst.kdj20macd60sma5_Strategy)
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
    # print(code, ' ', '收益率：%.2f' % (profitRatio))
    # 输出图表
    if profitRatio != 1:
        pass
        print("'{}',".format(code))
        # cerebro.plot(style='candle', volume=False)
    return profitRatio


if __name__ == "__main__":
    symbols_potential = [
        'ABBV',
        'ABC',
        'ADM',
        'ADP',
        'AEE',
        'AEP',
        'AJG',
        'AMGN',
        'AMT',
        'ATO',
        'AZO',
        'BMY',
        'BR',
        'CDNS',
        'CF',
        'CHRW',
        'CI',
        'CMG',
        'CMI',
        'CMS',
        'CNC',
        'COST',
        'CPB',
        'CTAS',
        'CTRA',
        'CTVA',
        'CVX',
        'DG',
        'DLTR',
        'DTE',
        'DUK',
        'DVN',
        'ED',
        'ENPH',
        'EQT',
        'EXR',
        'FANG',
        'FDS',
        'GD',
        'GPC',
        'GWW',
        'IBM',
        'JKHY',
        'K',
        'KLAC',
        'KO',
        'LLY',
        'LW',
        'MCD',
        'MCK',
        'MNST',
        'MOH',
        'MPC',
        'MPWR',
        'MSI',
        'MTB',
        'NEE',
        'NOC',
        'NUE',
        'O',
        'ON',
        'ORLY',
        'OXY',
        'PAYX',
        'PEP',
        'PGR',
        'PSX',
        'PWR',
        'PXD',
        'RJF',
        'RSG',
        'SEDG',
        'SNA',
        'SNPS',
        'SO',
        'SRE',
        'STZ',
        'TAP',
        'TMUS',
        'TRGP',
        'UNH',
        'VICI',
        'VLO',
        'VRTX',
        'WEC',
        'XEL',
        'XOM',
    ]

    symbols_position = [

    ]
    symbols_position = [

    ]
    symbols = symbols_potential + symbols_position
    result = []
    for s in symbols:
        try:
            p = backtest(s)
            result.append({'code': s, 'ProfitRatio': p})
        except:
            pass

    # for r in result:
    #     print(r['code'],' ',r['ProfitRatio'])

