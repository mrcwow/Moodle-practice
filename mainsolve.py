import pandas_datareader.data as web
from datetime import datetime


def solve(start):
    end = datetime.today()
    f = web.DataReader('AV.UK', 'stooq', start=start, end=end)
    f = f.sort_values(by=['Open','Close'], ascending=False)
    return f