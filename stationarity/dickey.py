# Augmented Dickey-Fuller (ADF) test for stationarity
# More reference: https://www.machinelearningplus.com/time-series/time-series-analysis-python/

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

# Function to perform ADF test and print results
def adf_test(time_series):
    result = adfuller(time_series, autolag='AIC')
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])
    print('Critical Values:', result[4])

    # Null hypothesis: There is no stationarity/time series possesses a unit root and is non-stationary

    # Check the p-value against a significance level (e.g., 0.05)
    if result[1] <= 0.05:
        print("Reject the null hypothesis: The time series is likely stationary.")
    else:
        print("Fail to reject the null hypothesis: The time series may be non-stationary.")

# Read the CSV file
df = pd.read_csv('./data/wlev.csv')

# Extract the time series column (assuming it's named 'value')
time_series = df['WLEV']

# Perform the ADF test
adf_test(time_series)