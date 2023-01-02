
import us_strategies_select_1 as mst
import backtrader as bt
import pandas as pd

import matplotlib.pyplot as plt
from datetime import datetime
import datetime as dt
import efinance as ef
from stockPool import *
from stockCategory import *


def getKDataFromEfinance(code, beg, end, freq):
    df = ef.stock.get_quote_history(code, beg=beg, end=end, klt=freq)
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
def backtestWithFutuCSV(code):
    pass
    # 创建Cerebro
    cerebro = bt.Cerebro()
    # 读取数据
    today = datetime.now()
    endstr = '{}{}{}'.format(today.year, str(today.month).zfill(2), str(today.day).zfill(2))
    # print(endstr)
    # exit(1)
    delta = dt.timedelta(days=30)
    before = today - delta
    begstr = '{}{}{}'.format(before.year, str(before.month).zfill(2), str(before.day).zfill(2))
    dataframe = getKDataFromEfinance(code, begstr, endstr, 15)
    data = bt.feeds.PandasData(dataname=dataframe, name=code)
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


    bo = Bokeh()
    bo.plot_result(result)
    return profitRatio


def backtest(code):
    # 创建Cerebro
    cerebro = bt.Cerebro()
    # 读取数据
    today = datetime.now()
    endstr = '{}{}{}'.format(today.year, str(today.month).zfill(2), str(today.day).zfill(2))
    # print(endstr)
    # exit(1)
    delta = dt.timedelta(days=30)
    before = today - delta
    begstr = '{}{}{}'.format(before.year, str(before.month).zfill(2), str(before.day).zfill(2))
    dataframe = getKDataFromEfinance(code, begstr, endstr, 15)
    data = bt.feeds.PandasData(dataname=dataframe, name='d1')

    # 装载数据到cerebro
    cerebro.adddata(data)

    # 装载策略

    cerebro.addstrategy(mst.us_select_Strategy)
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
    #     print(profitRatio)
    cerebro.plot(style='candle', volume=False)


    return profitRatio



if __name__ == "__main__":
    # symblos_potential 最新的选股结果：沪深三百股票， 上升通道， 前一个月换手率从高到低排序前十名
    symbols_potential = [

    ]
    symbols_potential += us_stock
    # symbols_potential += zhongzitou
    # symbols_potential += laolongtou
    # symbols_potential += bak
    # symbols_potential += BIAOPU500
    # symbols_potential += HUSHEN300
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




