from typing import Dict
import efinance as ef
import pandas as pd
import time
from datetime import datetime

def getData(code):

    # stock_codes = ['贵州茅台', '腾讯', '苹果']
    # 数据间隔时间为 60 分钟
    freq = 60
    df = ef.stock.get_quote_history(code,klt=freq)
    return df

def renEFinanceDFforBT(df):
    df = df.iloc[:,:13]
    df.columns = ['name','code','Datetime','open','close','high','low','amount','volume','amplitude','updownratio','updownamount','exchange']
    df['Datetime'] = pd.to_datetime(df['Datetime'])

    df['openinterest'] = 0
    df = df[['Datetime','open','high','low','close','volume','openinterest']]
    df.set_index('Datetime', inplace=True)
    return df

if __name__=="__main__":
    data=getData('贵州茅台')
    print(data)
    data = renEFinanceDFforBT(data)
    print(data)
