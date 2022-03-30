import time
import pandas as pd
import pandas_datareader.data as web


pd.core.common.is_list_like = pd.api.types.is_list_like

import datetime
start = datetime.datetime(2020, 1, 1)
end = datetime.datetime(2020, 1, 2)
SP50 = web.DataReader(['sp500'], 'fred', start, end)



a = str(SP50)

def random_num():
    t = str(time.time())
    pd.core.common.is_list_like = pd.api.types.is_list_like

    import datetime
    try:
        start = datetime.datetime(2012 + int(t[-2]), int(t[-1])+1, 1)
        end = datetime.datetime(2012 + int(t[-2]), int(t[-1])+1, 2)
        SP50 = web.DataReader(['sp500'], 'fred', start, end)
        return int(t[-6:-1])
    except:
        return random_num()
print(random_num())



def crypt(num):
    
    