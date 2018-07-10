import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from pandas import Series
import statsmodels.tsa.stattools as ts


df = pd.read_csv("real_wage.csv")
df = df.set_index('year')
month = np.array(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])
df.index = df.index.map(str)
year = df.index
#print(month)
#print(year)
#print(df)
#print(df.iloc[:,1])

#print(type(month))
#print(type(year))
#print(df.head())

data = []
first = df.iloc[:,0]+ df.iloc[:,1] + df.iloc[:,3]
second = df.iloc[:,3]+ df.iloc[:,4] + df.iloc[:,5]
third = df.iloc[:,6]+ df.iloc[:,7] + df.iloc[:,8]
fourth = df.iloc[:,9]+ df.iloc[:,10] + df.iloc[:,11]

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

df = pd.concat([first,second,third, fourth], axis=1)

#print(df)

z = df.iloc[0]
for i in range(len(df.index)-1):
    i = i + 1
    x = df.iloc[i]
    z = z.append(x)

#print(z)

period = ['Q1', 'Q2', 'Q3', 'Q4']
data =[]
for i in range(len(z)):
    data.append(z[i])

date = []
time = []
t = 0
for i in range(len(year)):
    for j in range(len(period)):
        t +=1
        date.append(year[i] + '-' + period[j])
        time.append(t)


data = pd.DataFrame(data, date, columns=['real_wage'])

##CREATE OTEHR VALUES
#Log
data["log_wage"] = np.log(data.real_wage)

#Moving Average
data["moving_ave"] = data.real_wage.rolling(window=4,center=True).mean()

#Grouwth Rate
data["rate_of_change"]= data['moving_ave'].pct_change()

#Differenre of moving average
data["diff"]= data['moving_ave'].diff(periods=1)

#2nd orderDifferenre of moving average
data["diff_two"]= data['moving_ave'].diff(periods=2)

#Year over Year
data['YoY']= np.nan
#print(data)

for i in range(len(data.YoY)):
    if i>=4:
        data.ix[i,'YoY'] = data.ix[i,'real_wage']/data.ix[i-4,'real_wage']

#Difference of of YoY
data["diff_YoY"] = data['YoY'].diff(periods=1)


#print(data.head(),data.tail())


def standard_plot(timeseries):
    plt.plot(data.index, timeseries)
    plt.xlabel('Time')
    plt.ylabel('')
    plt.xticks(['1990-Q1', '1995-Q1', '2000-Q1', '2005-Q1', '2010-Q1', '2015-Q1'],
               ['1990-Q1', '1995-Q1', '2000-Q1', '2005-Q1', '2010-Q1', '2015-Q1'])
    plt.show()

def adf_result(dataname, timeseries):
    result = ts.adfuller(timeseries.dropna())
    print("\n[", dataname, "]")
    print('ADF Statistic: %f' % result[0])
    print('p-value: %f' % result[1])

adf_result("Row", data["real_wage"])
adf_result("Log", data["log_wage"])
adf_result("Moving Average", data["moving_ave"])
adf_result("The Rate of Change", data["rate_of_change"])
adf_result("Difference of Moving Average", data["diff"])
adf_result("Twice Difference of Moving Average", data["diff_two"])
adf_result("YoY", data["YoY"])
adf_result("Difference of YoY", data["diff_YoY"])

