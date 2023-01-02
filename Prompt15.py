'''
循环以下步骤：
获取最新数据
加载cerebro数据，策略，运行
当且仅当数据时间与系统时间处于一个周期中：年月日相同，小时数相同，才触发策略
策略触发邮件发送




'''
import backtrader as bt
import pandas as pd
import mailbox
import time
from datetime import datetime
import datetime as dt
import efinance as ef
from stockPool import *
FILEPATH='tempMessage.txt'
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

# 主程序入口
if __name__ == "__main__":
    # 填入待监测的股票代码
    symbols_planned = [
        '300274',
        '600050',

    ]
    symbols_planned +=zhongzitou[:50]
    symbols_planned +=laolongtou
    symbols_planned +=etf
#填入持仓股票代码
    symbols_position = [

    ]
    symbols_position += position
    symbols_potential = []

    # 去除重复的股票
    for i in symbols_planned:
        if i not in symbols_potential:
            symbols_potential.append(i)
    while True:
        print('running......')
        # 开市时间内运行
        if not (datetime.now().hour > 7 and datetime.now().hour < 16):
            continue
        if not (int(datetime.now().minute / 10) == 3 or int(datetime.now().minute / 10) == 0):
            time.sleep(60)
            continue
        #clear tempMessage file .
        file = open(FILEPATH, 'w')
        file.write('{}'.format(datetime.now().isoformat()))
        file.close()
        for s in symbols_potential:
            bp = buysellPointCheck(s, 0)

        for s in symbols_position:
            sp = buysellPointCheck(s, 1)
#send mail here.
        file=open(FILEPATH,'r')
        message=[]
        for i in file.readlines():
            message.append(i)
        message= str(message)
        mailbox.send(mailbox.makeMessage(message).as_string())
        # nextTime = dt.datetime.now()
        # sDelta=dt.timedelta(seconds=1800)
        time.sleep(1800)

'''

11月日均成交额大于15亿元：

'600519',
'002603',
'300750',
'300059',
'601012',
'002317',
'000858',
'002466',
'002594',
'002241',
'600536',
'601899',
'300274',
'002460',
'002432',
'600036',
'601318',
'601888',
'600056',
'603259',
'600438',
'000002',
'000568',
'002475',
'000032',
'600522',
'002371',
'000625',
'600196',
'002077',
'002129',
'000948',
'688185',
'600048',
'000831',
'000001',
'600111',
'300014',
'600276',
'600745',
'002271',
'300760',
'000792',
'600050',
'600418',
'000333',
'603986',
'002223',
'600809',
'601788',
'601668',

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


'''
