import pandas as pd
import statsmodels.tsa.stattools as ts


df = pd.read_csv("real_consumption_final.csv", index_col=0 )

def adf_result(dfname, timeseries):
    result = ts.adfuller(timeseries.dropna())
    print("\n[", dfname, "]")
    print('ADF Statistic: %f' % result[0])
    print('p-value: %f' % result[1])


adf_result("Row", df["real_com"])
adf_result("Moving Average", df["moving_ave_com"])
adf_result("Difference Series of Moving Average", df["diff_com"])
adf_result("YoY", df["YoY_com"])
adf_result("Difference of YoY", df["diff_YoY_com"])
