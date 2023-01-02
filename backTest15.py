import myIndicators as mnd
import myStrategis as mst
import backtrader as bt
import pandas as pd

import matplotlib.pyplot as plt
from datetime import datetime
import datetime as dt
import efinance as ef
from stockPool import *
from stockCategory import *

def getKDataFromEfinance(code,beg,end,freq):

    df = ef.stock.get_quote_history(code,beg=beg, end=end,klt=freq)
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
#use futu KData CSV to backtest
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
    data = bt.feeds.PandasData(dataname=dataframe, name='d1')
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
    print(code,' ','收益率：%.2f' % (profitRatio))
    #输出图表
    if profitRatio!=1:
        cerebro.plot(style='candle', volume=False)
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
    print(code,' ','收益率：%.2f' % (profitRatio))
    #输出图表
    if profitRatio!=1:
        cerebro.plot(style='candle', volume=False)
    return profitRatio

if __name__ =="__main__":
    #symblos_potential 最新的选股结果：沪深三百股票， 上升通道， 前一个月换手率从高到低排序前十名
    symbols_potential = [

    ]
    symbols_potential += etf
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
    result=[]
    for s in symbols:
        try:
            p = backtest(s)
            result.append({'code':s,'ProfitRatio':p})
        except :
            pass

    # for r in result:
    #     print(r['code'],' ',r['ProfitRatio'])


'''
20221201 potential(沪深三百 上升通道 9 10 11 三个月平均换手率前十名):
        '601658',
        '002064',
        '601919',
        '600426',
        '600050',
        '000425',
        '600176',
        '002142',
        '601668',
        '601800'


20221201 in position:
        '512660',
        '515790',
        '561160',
        '600026',
        '600613',
        '600941',
        '601012',
        '603650',
        '688981',
        '002474',
        '002594',
        '002657',
        '159841',
        '300274',
        

沪深三百股票， 上升通道， （前一个月）10月换手率从高到低排序前十名：

'601658',
'002064',
'601919',
'600426',
'600176',
'002142',
'000425',
'601668',
'601390',
'601601'

沪深三百 上升通道 按换手率排序 1.08 ：
'600050',
'601800',
'000425',
'601825',
'601919',
'600426',
'601186',
'601668',
'601601',
'600176'


新能源 按换手率排序 排除下降通道 1.08
'300335',
'605289',
'002580',
'600956',
'000899',
'000040',
'301162',
'002953',
'002407',
'300068'

证券 按换手率排序 排除下降通道 1.07：
'601456',
'002926',
'600095',
'600906',
'601788',
'601696',
'300059',
'000728',
'600109',
'600958'
医疗 按换手率排序 排除下降通道 1.05 ：
'688052',
'002382',
'688665',
'002332',
'300607',
'003021',
'300709',
'688621',
'300660',
'300453'

半导体 按换手率排序 排除下降通道 1.04：
'002579',
'688362',
'002077',
'600237',
'301369',
'688372',
'300672',
'301176',
'688252',
'688259'


军工 按换手率排序 排除下降通道
十月日均成交额大于5亿，换手率大于3，排除下降通道 1.05
        '000948',
        '300068',
        '002603',
        '000519',
        '688152',
        '002514',
        '002432',
        '601975',
        '002077',
        '688063'
美股：
'AAPL',
'MSFT',
'TSLA',
'TSMC',
'AMZN',
'KO',
'META',
'BABA'

'''



