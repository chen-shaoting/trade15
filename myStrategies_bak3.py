"""
My Strategies Module
我的策略模块，包含了自定义的策略


"""
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
买点：（15个周期内，每周期15分钟，MACD 2次金叉） 且 （KDJ J上穿20 且 KDJ金叉 1次，dif dea > 0 ）
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
# kdj20 macd 60 sma5 with limited loss and  profit ratio
class kdj20macd60sma5_Strategy(bt.Strategy):

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
        self.macd = bt.indicators.MACDHisto(self.data0,plot = True)# macd = dif, macd.signal = dea, macd.histo = macd Bar
        # self.dif, self.dea, self.macd = mnd.myMACD(self.data0.close)


        # self.crossup = bt.indicators.CrossUp(self.dif, self.dea)
        # self.crossdown = bt.indicators.CrossDown(self.dif, self.dea)
        self.k = bt.indicators.StochasticFull(self.data0,
                                              period=9,
                                              period_dfast=5,
                                              movav=bt.indicators.ExponentialMovingAverage,
                                              period_dslow=5

                                              )

        self.close = self.data0.close
        self.kdjCrossTimes =0
        self.kdjCrossDuration=0
        self.periodLowClose=-1
        self.periodLowCloseRange=0
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
    #     print(self.data0.datetime.date(0).isoformat())
    #     exit()
    #     print(self.dif[0],self.macd[0],self.data0.close[0])
    def next(self):
        if self.periodLowClose ==-1:
            self.periodLowClose = self.data0.close[0]

        else:
            self.periodLowCloseRange+=1
            if self.periodLowClose > self.data0.close[0]:
                self.periodLowClose = self.data0.close[0]
                self.periodLowCloseRange = 0

        if (self.k.percD[-1]<20 and self.k.percD[0]>20):
            self.kdjCrossTimes +=1
            self.kdjCrossDuration +=1
        if self.k.percD[0]<20:
            self.kdjCrossDuration =0

        if not self.position:
            c1 = self.k.percD[-1]<20 and self.k.percD[0]>20  # 关键标志
            c2 = (self.macd[0]> self.macd[-1])   # 趋势
            c3 =(self.kdjCrossDuration<15  and self.kdjCrossTimes>0)  # 稳定
            c4 =  (self.macd.histo[0]*2>0.002 or self.macd.histo[0]*2<-0.002) # 稳定
            if c1 and c2 and c3 and c4:
                # print('self.k.percD[-1]{},self.k.percD[0]{}'.format(self.k.percD[-1],self.k.percD[0]))
                self.order = self.buy(exectype=bt.Order.Market)
        else:
            c1 = self.k.percD[0]>85
            c2 = (self.k[0]<self.k[-1])
            if (c1 or c2):
                self.order = self.sell(exectype=bt.Order.Market)


# -----------------------------------------------------------------------------------------------------------------------


#