import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("real_consumption_final.csv", index_col=0 )


def standard_plot(timeseries):
    plt.plot(df.index, timeseries)
    plt.xlabel('')
    plt.ylabel('')
    plt.xticks(['1995-Q1', '2000-Q1', '2005-Q1', '2010-Q1', '2015-Q1'],
               ['1995-Q1', '2000-Q1', '2005-Q1', '2010-Q1', '2015-Q1'])


##
plt.figure(1)

plt.title('Original Real com Time Series \n (Average in 2015 = 100)')
standard_plot(df['real_com'])
plt.show()

##
plt.figure(1)

plt.subplot(221)
plt.title('Real com Moving Average Time Series')
standard_plot(df['moving_ave_com'])
#plt.clf()

plt.subplot(222)
plt.title('Different Series(Order =1)')
standard_plot(df["diff_com"])
#plt.clf()

plt.subplot(223)
plt.title('Year over Year')
standard_plot(df['YoY_com'])
#plt.clf()

plt.subplot(224)
plt.title('Difference of Year over Year(Order =1)')
standard_plot(df['diff_YoY_com'])
#plt.clf()


plt.show()
