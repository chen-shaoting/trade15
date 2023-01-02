
import numpy
import talib
from talib import MA_Type

close = numpy.random.random(100)

upper, middle, lower = talib.BBANDS(close,
        timeperiod=5, nbdevup=2, nbdevdn=2, matype=MA_Type.SMA)

print("upper")
print(upper)
print("middle")
print(middle)
print("lower")
print(lower)
