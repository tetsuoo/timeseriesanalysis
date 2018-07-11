import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("real_wage_final.csv", index_col=0 )


def standard_plot(timeseries):
    plt.plot(df.index, timeseries)
    plt.xlabel('Time')
    plt.ylabel('')
    plt.xticks(['1990-Q1', '1995-Q1', '2000-Q1', '2005-Q1', '2010-Q1', '2015-Q1'],
               ['1990-Q1', '1995-Q1', '2000-Q1', '2005-Q1', '2010-Q1', '2015-Q1'])


plt.figure(1)


plt.subplot(421)
plt.title('Original Real wage Time Series \n (Average in 2015 = 100)')
standard_plot(df['real_wage'])
#plt.clf()


plt.subplot(422)
plt.title('Log Real wage')
standard_plot(df['log_wage'])
#plt.clf()


plt.subplot(423)
plt.title('Real wage Moving Average Time Series')
standard_plot(df['moving_ave_wage'])
#plt.clf()


plt.subplot(424)
plt.title('Changing Rate of Real wage')
standard_plot(df["rate_of_change_wage"])
#plt.clf()

plt.subplot(425)
plt.title('Different Series(Order =1)')
standard_plot(df["diff_wage"])
#plt.clf()

plt.subplot(426)
plt.title('Different Series(Order =2)')
standard_plot(df['diff_two_wage'])
#plt.clf()


plt.subplot(427)
plt.title('Year over Year')
standard_plot(df['YoY_wage'])
#plt.clf()

plt.subplot(428)
plt.title('Difference of Year over Year(Order =1)')
standard_plot(df['diff_YoY_wage'])
#plt.clf()


plt.show()
