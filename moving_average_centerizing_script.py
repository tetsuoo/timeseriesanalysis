
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from pandas import Series
import statsmodels.tsa.stattools as ts


##REAL WAGE
dfw = pd.read_csv("real_wage.csv")
dfw = dfw.set_index('year')
dfw.index = dfw.index.map(str)
year = dfw.index

first = dfw.iloc[:,0]+ dfw.iloc[:,1] + dfw.iloc[:,3]
second = dfw.iloc[:,3]+ dfw.iloc[:,4] + dfw.iloc[:,5]
third = dfw.iloc[:,6]+ dfw.iloc[:,7] + dfw.iloc[:,8]
fourth = dfw.iloc[:,9]+ dfw.iloc[:,10] + dfw.iloc[:,11]

#print(first.head(), '\n', second.head(),'\n', third.head(),'\n', fourth.head())

first = first.to_frame()
first.columns = ['first']
second = second.to_frame()
second.columns = ['second']
third = third.to_frame()
third.columns = ['third']
fourth = fourth.to_frame()
fourth.columns = ['fourth']

#print(first)

dfw = pd.concat([first,second,third, fourth], axis=1)

#print(dfw)

z = dfw.iloc[0]
for i in range(len(dfw.index)-1):
    i = i + 1
    x = dfw.iloc[i]
    z = z.append(x)

#print(z)

period = ['Q1', 'Q2', 'Q3', 'Q4']
dfw =[]
for i in range(len(z)):
    dfw.append(z[i])

date = []
time = []
t = 0
for i in range(len(year)):
    for j in range(len(period)):
        t +=1
        date.append(year[i] + '-' + period[j])
        time.append(t)


dfw = pd.DataFrame(dfw, date, columns=['real_wage'])

##CREATE OTEHR VALUES
#Log
#dfw["log_wage"] = np.log(dfw.real_wage)

#Moving Average
dfw["moving_ave_wage1"] = dfw.real_wage.rolling(window=4, center=True).mean()
moving_ave_wage2 = dfw.moving_ave_wage1.drop(index='1990-Q1', axis=0)
moving_ave_wage2 = moving_ave_wage2.values.tolist()
moving_ave_wage2.append(np.nan)

dfw['moving_ave_wage2'] = moving_ave_wage2
dfw['moving_ave_wage3'] = (dfw['moving_ave_wage1'] + dfw['moving_ave_wage2'])/ 2
print(dfw.loc[:,['moving_ave_wage1','moving_ave_wage2','moving_ave_wage3']].head(), dfw.loc[:,['moving_ave_wage1','moving_ave_wage2','moving_ave_wage3']].tail())
print("\n")

#dfw.to_csv("real_wage_final.csv")
