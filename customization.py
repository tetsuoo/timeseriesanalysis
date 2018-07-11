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
dfw["log_wage"] = np.log(dfw.real_wage)

#Moving Average
dfw["moving_ave_wage"] = dfw.real_wage.rolling(window=4,center=True).mean()

#Grouwth Rate
dfw["rate_of_change_wage"]= dfw['moving_ave_wage'].pct_change()

#Differenre of moving average
dfw["diff_wage"]= dfw['moving_ave_wage'].diff(periods=1)

#2nd orderDifferenre of moving average
dfw["diff_two_wage"]= dfw['diff_wage'].diff(periods=1)

#Year over Year
dfw['YoY_wage']= np.nan
#print(dfw)

for i in range(len(dfw.YoY_wage)):
    if i>=4:
        dfw.ix[i,'YoY_wage'] = dfw.ix[i,'real_wage']/dfw.ix[i-4,'real_wage']

#Difference of of YoY
dfw["diff_YoY_wage"] = dfw['YoY_wage'].diff(periods=1)


print(dfw)
dfw.to_csv("real_wage_final.csv")









#############################
##REAL consumption
#############################

dfc = pd.read_csv("real_consumption.csv")
dfc = dfc.set_index('year')
dfc.columns = ['real_com']

print(dfc.head())


##CREATE OTEHR VALUES
#Log
dfc["log_com"] = np.log(dfc.real_com)

#Moving Average
dfc["moving_ave_com"] = dfc.real_com.rolling(window=4,center=True).mean()

#Grouwth Rate
dfc["rate_of_change_com"]= dfc['moving_ave_com'].pct_change()

#Differenre of moving average
dfc["diff_com"]= dfc['moving_ave_com'].diff(periods=1)

#2nd orderDifferenre of moving average
dfc["diff_two_com"]= dfc['diff_com'].diff(periods=1)

#Year over Year
dfc['YoY_com']= np.nan
#print(dfc)

for i in range(len(dfc.YoY_com)):
    if i>=4:
        dfc.ix[i,'YoY_com'] = dfc.ix[i,'real_com']/dfc.ix[i-4,'real_com']

#Difference of of YoY
dfc["diff_YoY_com"] = dfc['YoY_com'].diff(periods=1)


print(dfc)
dfc.to_csv("real_consumption_final.csv")
