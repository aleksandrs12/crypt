import time
import pandas as pd
import pandas_datareader.data as web
import datetime
import os


pd.core.common.is_list_like = pd.api.types.is_list_like

my_key = 484
start = datetime.datetime(2020, 1, 1)
end = datetime.datetime(2020, 1, 2)
SP50 = web.DataReader(['sp500'], 'fred', start, end)



def random_num(limit):
    t = str(time.time())
    pd.core.common.is_list_like = pd.api.types.is_list_like


    try:
        start = datetime.datetime(2012 + int(t[-2]), int(t[-1])+1, 1)
        end = datetime.datetime(2012 + int(t[-2]), int(t[-1])+1, 2)
        SP50 = web.DataReader(['sp500'], 'fred', start, end)
        for n in range(len(str(SP50))):
            if str(SP50)[n] == '.':
                a = int(round(int(str(SP50)[n+1:n+3])  / (100 / limit)))
                a + 10
                return a
        #return int(round(int(t[-3:-1])  / (100 / limit)))
        return random_num(limit)
    except:
        return random_num(limit)



alp = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h',
        'I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q',
        'R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z', 
        '#','.',',','<','>','/','?',"'",'@','"','£','$','1','2','3','4','5','6',
        '7','8','9','0','%','^','&','*','(',')','_','-','=','+','[',']','{','}',
        ';',':', ' ', '!']

# ., < > / ? ' @ " £ $ 1 2 3 4 5 6 7 8 9 0 % ^ & * ( ) _ - = + [ ] { } ; : ` ¬   ,~ ,| !


alpnums = {

}


for n in range(len(alp)):
    alpnums[alp[n]] = n



a = str(SP50)

def random_num(limit):
    t = str(time.time())
    pd.core.common.is_list_like = pd.api.types.is_list_like


    try:
        start = datetime.datetime(2012 + int(t[-2]), int(t[-1])+1, 1)
        end = datetime.datetime(2012 + int(t[-2]), int(t[-1])+1, 2)
        SP50 = web.DataReader(['sp500'], 'fred', start, end)
        for n in range(len(str(SP50))):
            if str(SP50)[n] == '.':
                a = int(round(int(str(SP50)[n+1:n+3])  / (100 / limit)))
                a + 10
                return a
        #return int(round(int(t[-3:-1])  / (100 / limit)))
        return random_num(limit)
    except:
        return random_num(limit)


def crypt(key):
    l = len(alp)
    f = open("text.txt", "r")
    f1 = f.read()
    f1 = f1.strip()
    
    output = ''
    for n in f1:
        output += str(alpnums[n]*key) + " "
        key += 3
    return output




o = crypt(77)

f = open("text_crypted.txt", "w")
f.write(o)
    
