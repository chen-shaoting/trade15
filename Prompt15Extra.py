"""
1、短线抄底策略：通过月线，周线 日线的趋势，确定个股的涨势稳定性：日周月线的macd均处于零轴上方，日线短期内macd不会快速下穿0轴。
2、提供15分钟级别的抄底信号：kdj j上穿20和卖出信号：60分钟级别macd死叉。
3、交易周期预期在2个交易日，预期收益超过1%.
4、实际统计胜率，平均收益，平均损失，期望收益。
5、止损点买入价格的91%，止盈点：60分钟macd死叉。

这个策略可以简单理解为：日线含日线以上选强中强，日线可以偏弱但不应有下穿0轴风险，周线和月线macd走势越强越好；日线以下选弱中弱，60分钟线，15分钟线越弱越好。
3、买入时机尽可能选在交易日结束前
4、卖出时机尽可能再交易日前1小时内。

流程：
1、预知基础股票池列表-MBase
2、逐个获取MBase股票的月线，判断当前月线macd大于0，（尝试通过macd.histo判断走势走强还是走弱），生成WBase股票池列表，以备周线监测。
3、逐个获取WBase股票的月线，判断当前周线macd大于0，（尝试通过macd.histo判断走势走强还是走弱），生成DBase股票池列表，以备日线监测。
4、逐个获取DBase股票的日线，判断当前月线macd大于0，（尝试通过macd.histo判断走势走强还是走弱），生成potential股票池列表，以预警监测。
5、以上三个过程可以抽象为一个函数MACD check，一个策略MACD strategy。
6、生成potential后，运行目前的PromptOne的代码即可。
7、记录与统计，买入股票代码，买入时间，买入价格，买入数量，卖出时间，卖出价格，卖出数量，单次交易收益与损失。

"""


import backtrader as bt
import pandas as pd
import mailbox
import time
from datetime import datetime
import datetime as dt
import efinance as ef
from stockPool import *
FILEPATH='tempMessage.txt'

def getKDataFromEfinance(code, hp, beg, end, freq):
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

# 根据给定的日期date，获取指定类型的数据ktype,返回指定的df

#按照指定的日期，指定的股票池，指定周期的数据，运行指定的策略，选出备选股票池
def makePotential(code,ktype,strategy,hp=0):
    pass

    # 创建Cerebro
    cerebro = bt.Cerebro()
    # 读取数据
    today = datetime.now()
    endstr = '{}{}{}'.format(today.year, str(today.month).zfill(2), str(today.day).zfill(2))
    # print(endstr)
    # exit(1)
    delta = dt.timedelta(days=260)
    before = today - delta
    begstr = '{}{}{}'.format(before.year, str(before.month).zfill(2), str(before.day).zfill(2))
    dataframe = getKDataFromEfinance(code, hp, begstr, endstr, ktype)# hp- have position，0-代表空仓，监测买点 1-代表持仓，监测卖点。默认为0，空仓
    data = bt.feeds.PandasData(dataname=dataframe,
                               name=code, )
    cerebro.adddata(data)

    # 装载数据到cerebro

    # 装载策略

    cerebro.addstrategy(strategy)
    # cerebro.addstrategy(mst.statsKDJStrategy)
    # 装载分析器
    #
    # cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='SharpeRatio')
    # cerebro.addanalyzer(bt.analyzers.DrawDown, _name='DrawDown')
    # 设置现金和佣金
    cerebro.broker.setcash(1000000)
    cerebro.broker.setcommission(commission=0.0006)

    # cerebro.broker.
    # 设置sizer仓位
    cerebro.addsizer(bt.sizers.PercentSizer, percents=99)
    # 开始回测
    result = cerebro.run()
    #检测结果在策略中通过写入csv的方式返回，靠文件名规则识别--
    # cerebro.plot()
    cerebro.plot(style='candle', volume=False)

    return result






# 顺序进行月，周，日数据的运算，分别调用getKdata，获取df，通过指定的策略-MACDStrategy，对每只股票是否适合当前做短线抄底做出评价，生成ktype对应级别的BASE，

class MACDStrategy(bt.Strategy):

    def log(self, txt, dt=None):
        if not self.allowedLog:
            return
        """Logging function for this strategy"""
        dt = dt or self.data0.datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # 如果不需要输出过程日志可以设置False关闭
        self.allowedLog = False


        self.macd = bt.indicators.MACDHisto(self.data0,plot = True)# macd = dif, macd.signal = dea, macd.histo = macd Bar
        self.macdsignalSMA = bt.indicators.SmoothedMovingAverage(self.macd.signal,period = 5)


    def prenext(self):
        pass
    def next(self):
        now = datetime.now()
        if not self.position:
            if self.macd.signal[0] > 0:
                now =  self.data0.datetime.datetime(0) # 这是测试时用的，用以修改触发策略的时间条件
                if now.year == self.data0.datetime.datetime(0).year:
                    if now.month == self.data0.datetime.datetime(0).month:
                        if now.day == self.data0.datetime.datetime(0).day:
                            # if now.hour == self.data0.datetime.datetime(0).hour:
                            # print(self.data0.datetime.date(0).isoformat(),self.data0.close[0],self.macd.signal[0],self.macd.histo[0])
                            # print(self.data0.datetime.date(0).isoformat(),self.data0.close[0],self.highest10[0])
                            # print(self.data0.datetime.date(0).isoformat(),self.upd[0])
                            print(self.data0.datetime.date(0).isoformat(),self.data0.close[0],self.macdsignalSMA[0])

# 判断是否处于macd0轴上方，若处于macd0轴上方，计算出持续的时间，最近macd.histo的走势，若macd.histo趋近于0，以当前的速度，预计大约多少周期将接触零轴。


class PromptStrategy(bt.Strategy):
    pass
#判断买点与卖点，提供预警。

def prompt15(potential):
    pass
#根据给定的股票池，在交易日根据给定的策略进行预警。



# 主程序入口
if __name__ == "__main__":
    # 填入待监测的股票代码
    symbols_planned = [
        # '000001',
        'de'
    ]
    # symbols_planned +=zhongzitou
    # symbols_planned +=laolongtou
    # symbols_planned +=etf



    # 去除重复的股票
    symbols_potential = []
    for i in symbols_planned:
        if i not in symbols_potential:
            symbols_potential.append(i)
    result =[]
    ktype= {
        'day':101,
    }


    for s in symbols_potential:
        result=makePotential(s,ktype['day'],MACDStrategy)
        print(result[0][0])











# ----------------------------------------------------------以上为编辑中的代码-----------------------------------------------------------

# ----------------------------------------------------------以下为参考代码--------------------------------------------------------------
def myMACD(price):
    dif = bt.indicators.ExponentialMovingAverage(price, period=12) - bt.indicators.ExponentialMovingAverage(price,
                                                                                                            period=26)
    dea = bt.indicators.ExponentialMovingAverage(dif, period=9)
    macd = 2 * (dif - dea)

    return dif, dea, macd


class Prompt_Strategy(bt.Strategy):

    def log(self, txt, dt=None):
        if not self.allowedLog:
            return
        """Logging function for this strategy"""
        dt = dt or self.data0.datetime.datetime(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # 如果不需要输出过程日志可以设置False关闭

        self.allowedLog = True
        self.order = bt.Order.Market
        self.buycomm = None
        self.buyprice = None
        self.bar_executed = None
        self.count = 1
        self.sma5 = bt.indicators.MovingAverageSimple(self.data0.close, period=5)
        self.dif, self.dea, self.macd = myMACD(self.data0.close)
        # self.crossup = bt.indicators.CrossUp(self.dif, self.dea)
        # self.crossdown = bt.indicators.CrossDown(self.dif, self.dea)
        self.k = bt.indicators.StochasticFull(self.data0,
                                              period=9,
                                              period_dfast=5,
                                              movav=bt.indicators.ExponentialMovingAverage,
                                              period_dslow=5

                                              )  # this K means J in regular finacial apps, percD means K.

        self.close = self.data0.close
        self.hp = self.data0.openinterest
        self.buyVectors = []
        self.sellVectors = []
        self.macdCross = 0
        self.kdjCross = 0

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # buy/sell order submitted/accepted to/by broker --nothing to do
            return
        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                if self.allowedLog:
                    self.log(
                        'Buy executed, Price:{:.2f}, Cost:{:.2f}, Comm:{:.2f}'.format(
                            order.executed.price,
                            order.executed.value,
                            order.executed.comm,

                        )
                    )
                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm


            else:  # Sell
                if self.allowedLog:
                    self.log(
                        'Sell executed, Price:{:.2f}, Cost:{:.2f}, Comm:{:.2f} '.format(
                            order.executed.price,
                            order.executed.value,
                            order.executed.comm,

                        )
                    )

            self.bar_executed = len(self)
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            if self.allowedLog:
                self.log('Order Canceled/Margin/Rejected')

        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return
        if self.allowedLog:
            self.log('Operation Profit, Gross %.2f, Net %.2f' % (trade.pnl, trade.pnlcomm))

    # def prenext(self):
    #     print(self.dif[0],self.macd[0],self.data0.close[0])
    def next(self):
        # c3 = (self.k.percD[0] > 20 and self.k.percD[-1] < 20)
        if self.dif[-1] < self.dea[-1] and self.dif[0] > self.dea[0]:
            self.macdCross += 1
        if self.k.percD[0] > 20 and self.k.percD[-1] < 20:
            self.kdjCross += 1
        if self.macdCross > 1 or self.kdjCross > 1:

            # if not self.position:
            #     #
            #     # c3 = (self.k[0] > 20 and self.k[-1] < 20)
            #
            #     if self.macdCross == 2 or self.kdjCross == 2:
            if not (divmod(int(self.hp[0]), 2)[1] == 1):
                type = 'Buy'
                # print(divmod(int(self.hp[0]),2))
                c3 = (self.k[0] > 20 and self.k[-1] < 20)

                if self.macdCross == 2 or self.kdjCross == 2:
                    now = datetime.now()
                    # now =  self.data0.datetime.datetime(0) # 这是测试时用的，用以修改触发策略的时间条件
                    if now.year == self.data0.datetime.datetime(0).year:
                        if now.month == self.data0.datetime.datetime(0).month:
                            if now.day == self.data0.datetime.datetime(0).day:
                                if now.hour == self.data0.datetime.datetime(0).hour:
                                    # print('{}  {}'.format(now.isoformat(),self.data0.datetime.datetime(0).isoformat()))
                                    print('Real buy')
                                    self.log('next:{}, {:.2f}, {:.2f}, {:.2f}'.format(self.data0.openinterest[0],
                                                                                      self.data0.close[0], self.k[0],
                                                                                      self.k[-1]))
                                    # sending email now.
                                    message = '\nType:{}, Code:{},Datetime:{},Close:{:.2f}'.format(
                                        type,
                                        str(self.hp[0]).zfill(6)[0:6],
                                        self.data0.datetime.datetime(0).isoformat(),
                                        self.data0.close[0]

                                    )
                                    # message = ('%i' % (self.data0.openinterest[0])).zfill(7)
                                    file = open(FILEPATH, 'a')
                                    file.write(message)
                                    file.close()
                                    # mailbox.send(mailbox.makeMessage(message).as_string())

                                    time.sleep(10)



        else:
            # c1 = self.dif[-1] > self.dea[-1]
            # c2 = self.dif[0] <= self.dea[0]
            type = 'Sell'
            c1 = self.dif[-1] > self.dea[-1]
            c2 = self.dif[0] <= self.dea[0]
            c3 = self.macd > 0
            c4 = self.close[0] < self.sma5[0] * 0.8
            # c5 = self.close[0] < self.buyprice * 0.9  # 在没办法把购买价格填进来之前先忽略这个条件
            c6 = self.close[0] < self.close[-1] * 0.99
            # c3 = self.dif[0] > 0 and self.dea[0] > 0
            # c7 = self.close[0] > self.buyprice *1.2 # 在没办法把购买价格填进来之前先忽略这个条件
            if (c1 and c2 and c3) or c4 or c6:
                # print("----self.dif[-1]{:.2f},self.dea[-1]{:.2f},self.dif[0]{:.2f},self.dea[0]{:.2f}".format(self.dif[-1], self.dea[-1],
                #                                                                          self.dif[0], self.dea[0]))
                reason=['Reasons to sell:']
                if (c1 and c2 and c3):
                    reason.append(' macd dead cross')
                if (c4):
                    reason.append(' close,{}, under sma5:{}'.format(self.close[0],self.sma5[0]))
                if (c6):
                    reason.append((' close,{}, fell too much after previous:{}'.format(self.close[0],self.close[-1])))
                # self.order = self.sell(exectype=bt.Order.Market)
                now = datetime.now()
                # now =  self.data0.datetime.datetime(0) # 这是测试时用的，用以修改触发策略的时间条件
                if now.year == self.data0.datetime.datetime(0).year:
                    if now.month == self.data0.datetime.datetime(0).month:
                        if now.day == self.data0.datetime.datetime(0).day:
                            if now.hour == self.data0.datetime.datetime(0).hour:
                                # print('{}  {}'.format(now.isoformat(),self.data0.datetime.datetime(0).isoformat()))
                                print('Real sell')
                                self.log('next:{}, {:.2f}, {:.2f}, {:.2f}'.format(self.data0.openinterest[0],
                                                                                  self.data0.close[0], self.k[0],
                                                                                  self.k[-1]))
                                # sending email now.
                                message = '\nType:{}, Code:{},Datetime:{},Close:{:.2f}{}'.format(
                                    type,
                                    str(self.hp[0]).zfill(6)[0:6],
                                    self.data0.datetime.datetime(0).isoformat(),
                                    self.data0.close[0],
                                    reason,

                                )
                                # message = ('%i' % (self.data0.openinterest[0])).zfill(7)
                                file = open(FILEPATH, 'a')
                                file.write(message)
                                file.close()


                                time.sleep(10)


def getKDataFromEfinance(code, hp, beg, end, freq):
    df = ef.stock.get_quote_history(code, beg=beg, end=end, klt=freq)
    df = df.iloc[:, :13]
    df.columns = ['name', 'code', 'datetime', 'open', 'close', 'high', 'low', 'amount', 'volume', 'amplitude',
                  'updownratio', 'updownamount', 'exchange']
    df['datetime'] = pd.to_datetime(df['datetime'])
    df['openinterest'] = int(code) * 10 + hp

    df = df[['datetime', 'open', 'high', 'low', 'close', 'volume', 'openinterest']]
    # df['dif'],df['dea'],df['macd'] = mnd.myMACD(df['close'])
    df.set_index('datetime', inplace=True)
    # df.to_csv('test.csv')
    return df


def buysellPointCheck(code, hp):
    # 创建Cerebro
    cerebro = bt.Cerebro()
    # 读取数据
    today = datetime.now()
    endstr = '{}{}{}'.format(today.year, str(today.month).zfill(2), str(today.day).zfill(2))
    # print(endstr)
    # exit(1)
    delta = dt.timedelta(days=60)
    before = today - delta
    begstr = '{}{}{}'.format(before.year, str(before.month).zfill(2), str(before.day).zfill(2))
    dataframe = getKDataFromEfinance(code, hp, begstr, endstr, 15)

    data = bt.feeds.PandasData(dataname=dataframe,
                               name=code, )
    cerebro.adddata(data)

    # 装载数据到cerebro

    # 装载策略

    cerebro.addstrategy(Prompt_Strategy)
    # cerebro.addstrategy(mst.statsKDJStrategy)
    # 装载分析器

    # cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='SharpeRatio')
    # cerebro.addanalyzer(bt.analyzers.DrawDown, _name='DrawDown')
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
    # profitRatio = cerebro.broker.get_value() / 1000000
    # print('最大回撤：{:.2f}'.format( result[0].analyzers.DrawDown.get_analysis()['max']['drawdown']))
    # print(code, ' ', '收益率：%.2f' % (profitRatio))
    # 输出图表
    # cerebro.plot(style='candle', volume=False)
    return None


