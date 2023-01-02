"""
My Strategies Module
我的策略模块，包含了自定义的策略


"""
import datetime

import backtrader as bt
import myIndicators as mnd

# ---------------------------------------------------------------------------------------------------------------------

'''
以下策略在34项ETF的15分钟级别数据应用效果良好：胜率84%，60天期望收益为110%。
    次数 平均收益 样本占比     收益加权平均
负    5	0.97	0.161290323	0.156451613
胜   26	1.126	0.838709677	0.944387097
			        期望收益 1.10083871



标的选择：A股及港股主要34个ETF 见StockPool
买点：核心：kdj 金叉
     稳定：d小于20不少于10周期

卖点：
--------------------------

（15个周期内，每周期15分钟，MACD 2次金叉） 且 （KDJ J上穿20 且 KDJ金叉 1次，dif dea > 0 ）
    或者
     （15个周期内，每周期15分钟，MACD 1次金叉） 且 （KDJ J上穿20 且 KDJ金叉 2次）
卖点：
    macd在0轴上方死叉 
    或者
    close低于sma5的80%
    或者
    close 低于 买入价的90%
    或者
    close 低于 前一周期close的99%



'''


# macd for week line, kdj for day line
class kdjmacd_Strategy(bt.Strategy):

    def log(self, txt, dt=None):
        if not self.allowedLog:
            return
        """Logging function for this strategy"""
        dt = dt or self.data0.datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # 如果不需要输出过程日志可以设置False关闭
        self.allowedLog = False
        self.order = bt.Order.Market
        self.buycomm = None
        self.buyprice = None
        self.bar_executed = None
        self.count = 1
        self.sma5 = bt.indicators.MovingAverageSimple(self.data0.close, period=5)
        self.macd = bt.indicators.MACDHisto(self.data0,
                                            plot=True)  # macd = dif, macd.signal = dea, macd.histo = macd Bar
        # self.dif, self.dea, self.macd = mnd.myMACD(self.data0.close)
        self.macdW = bt.indicators.MACDHisto(self.data1,
                                            plot=True)
        # self.crossup = bt.indicators.CrossUp(self.dif, self.dea)
        # self.crossdown = bt.indicators.CrossDown(self.dif, self.dea)
        self.k = bt.indicators.StochasticFull(self.data0,
                                              period=9,
                                              period_dfast=5,
                                              movav=bt.indicators.ExponentialMovingAverage,
                                              period_dslow=5

                                              )
        self.kW = bt.indicators.StochasticFull(self.data1,
                                              period=9,
                                              period_dfast=5,
                                              movav=bt.indicators.ExponentialMovingAverage,
                                              period_dslow=5

                                              )

        self.close = self.data1.close
        self.cross = bt.indicators.CrossOver(self.k.percD,self.k.percDSlow)

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
        # print('data0',self.data0.datetime.date(0).isoformat())
        # print('data1:',self.data1.datetime.date(0).isoformat())

    def next(self):
        # print('next data0',self.data0.datetime.date(0).isoformat())
        # print('next self.kW',self.kW[0])
        if not self.position:
            c1 = self.kW[0] < 30
            c2 = self.macdW.signal[0] > 1
            if c1 and c2:
                now = datetime.datetime.now()
                delta = datetime.timedelta(days=30)
                now = now - 3 * delta
                date = self.data1.datetime.date(0)
                nstr= str(now.year) + str(now.month)
                dstr = str(date.year) + str(date.month)
                if nstr == dstr:
                    self.order = self.buy(exectype=bt.Order.Market)
                    # print(date.isoformat())
# -----------------------------------------------------------------------------------------------------------------------


#