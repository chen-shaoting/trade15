"""
My Strategies Module
我的策略模块，包含了自定义的策略


"""
import backtrader as bt
import myIndicators as mnd


# 策略类class模板


class runningStrategy(bt.Strategy):

    pass


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
        self.macdCross = 0
        self.kdjCross = 0
        self.macdCrossDuration = 0
        self.kdjCrossDuration =0
        self.DurationLimit = 15

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

        # print(self.dif[0],self.dea[0],self.macd[0])
        # print(self.macd[0],self.macd.signal[0],self.macd.histo[0])
        # exit()

        # 两次相邻的金叉应在self.DurationLimit周期内发生。
        if self.macdCross>0:
            self.macdCrossDuration +=1
        if self.kdjCross >0:
            self.kdjCrossDuration +=1
        if self.macdCrossDuration >self.DurationLimit:
            self.macdCross =0
            self.macdCrossDuration =0
        if self.kdjCrossDuration >self.DurationLimit:
            self.kdjCross =0
            self.kdjCrossDuration =0

        # macd under zero golden cross
        if self.macd[-1] < self.macd.signal[-1] and self.macd[0]>self.macd.signal[0] and (self.macd[0]<0 and self.macd.signal[0]< 0):
            self.macdCross += 1


        #kdj J cross up 20 or kd golden cross
        if (self.k[0]>20 and self.k[-1]<20 ) and (self.k.percD[-1]<self.k.percDSlow[-1] and self.k.percD[0]>self.k.percDSlow[0]):
           self.kdjCross += 1
        #


        if not self.position:
            c1 = (self.kdjCross == 2 and self.macdCross > 0 and self.macd[0] > 0.01 and self.macd.signal[0] > 0.01)
            c2= (self.macdCross == 2 and self.kdjCross ==1 )or (self.kdjCross ==2 and self.macdCross==1)
            if c1:

                # print('position',self.data0.datetime.date(0).isoformat())
                # print(self.kdjCross,self.macdCross,self.kdjCrossDuration,self.macdCrossDuration,self.macd[0],self.k[0])
                # print('self.macd[-1]{}self.macd.signal[-1]{}self.macd[0]{}self.macd.signal[0]{}'.format(self.macd[-1],self.macd.signal[-1],self.macd[0],self.macd.signal[0]))
                # print('self.k[0]{} self.k[-1]{}self.k.percD[-1]{}self.k.percDSlow[-1]{} self.k.percD[0]{}self.k.percDSlow[0]{}'.format(self.k[0], self.k[-1],self.k.percD[-1],self.k.percDSlow[-1] , self.k.percD[0],self.k.percDSlow[0]))
                self.order = self.buy(exectype=bt.Order.Market)
        else:
            # c1 = self.dif[-1] > self.dea[-1]
            # c2 = self.dif[0] <= self.dea[0]
            c1 = self.macd[-1] > self.macd.signal[-1]
            c2 = self.macd[0] <= self.macd.signal[0]
            c3 = self.macd[0]>0 and self.macd.signal[0]>0 # macd 处在0线以上
            c4 = self.close[0] < self.sma5[0]*0.8
            c5 = self.close[0] < self.buyprice * 0.9
            c6 = self.close[0] < self.close[-1] * 0.99 # 若在上升通道 此止损点设置影响收益，可以去除,否则应加上。
            # c3 = self.dif[0] > 0 and self.dea[0] > 0
            c7 = self.close[0] > self.buyprice *1.2 #
            # if (c1 and c2 and c3) or c5 or c4 or c6:
            if (c1 and c2 and c3) or c4 or c5 or c6:

                self.order = self.sell(exectype=bt.Order.Market)


# -----------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------


# macd 60 sma5
class macd60sma5_Strategy(bt.Strategy):

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
        self.dif, self.dea, self.macd = mnd.myMACD(self.data0.close)

        self.close = self.data0.close

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
        # print('ma5:',self.sma5[0])
        # print(self.data0.close[0], '--',self.dif[0])
        #
        # print(self.count)
        # self.count += 1
        # pass
        # print(self.data0.close[0],self.dif[0],self.dea[0],self.macd[0])
        # # print(self.dif[0],self.dea[0],self.macd[0])
        if not self.position:

            c1 = self.dif[-1] < self.dea[-1]
            c2 = self.dif[0] >= self.dea[0]
            if c1 and c2:
                print("self.dif[-1]{:.2f},self.dea[-1]{:.2f},self.dif[0]{:.2f},self.dea[0]{:.2f}".format(self.dif[-1],
                                                                                                         self.dea[-1],
                                                                                                         self.dif[0],
                                                                                                         self.dea[0]))

                self.order = self.buy(exectype=bt.Order.Market)
        else:
            c1 = self.dif[-1] > self.dea[-1]
            c2 = self.dif[0] <= self.dea[0]
            c3 = self.dif[0] > 0 and self.dea[0] > 0
            c4 = self.close[0] < self.sma5[0]
            if (c1 and c2 and c3) or (self.close[0] < self.buyprice * 0.9) or c4:
                print(
                    "----self.dif[-1]{:.2f},self.dea[-1]{:.2f},self.dif[0]{:.2f},self.dea[0]{:.2f}".format(self.dif[-1],
                                                                                                           self.dea[-1],
                                                                                                           self.dif[0],
                                                                                                           self.dea[0]))

                self.order = self.sell(exectype=bt.Order.Market)

# -----------------------------------------------------------------------------------------------------------------------
#
