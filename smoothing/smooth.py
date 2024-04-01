
#! Data smoothing using LOWESS or Savitzky-Golay algorithm

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess
from scipy.signal import savgol_filter

# Read the CSV file with a column representing the timestamp (assuming it's named 'TIMESTAMP')
df = pd.read_csv('./data/wlev.csv')

# Extract the time series column (assuming it's named 'WLEV')
time_series = df['WLEV']

# Function to apply LOWESS smoothing (Locally Weighted Scatterplot Smoothing)
def apply_lowess(series, frac=0.05):
    smooth_result = lowess(series, range(len(series)), frac=frac)
    return smooth_result[:, 1]

# Function to apply Savitzky-Golay smoothing
def apply_savgol(series, window_size=11, order=2):
    smooth_result = savgol_filter(series, window_size, order)
    return smooth_result

# Set parameters for smoothing
frac_for_lowess = 0.05
window_size_for_savgol = 9
order_for_savgol = 2

# Apply smoothing
smoothed_lowess = apply_lowess(time_series, frac=frac_for_lowess)
smoothed_savgol = apply_savgol(time_series, window_size=window_size_for_savgol, order=order_for_savgol)

# Plot the original and smoothed time series
plt.figure(figsize=(12, 6))

plt.plot(time_series, label='Original Time Series', alpha=0.7)
# plt.plot(smoothed_lowess, label=f'LOWESS Smoothing (frac={frac_for_lowess})')
plt.plot(smoothed_savgol, label=f'Savitzky-Golay Smoothing (window={window_size_for_savgol}, order={order_for_savgol})')

plt.title('Original and Smoothed Time Series')
plt.xlabel('Time')
plt.ylabel('WLEV')
plt.legend()
plt.show()

# Save the smoothed_savgol to a CSV file
smoothed_savgol_df = pd.DataFrame({'TIMESTAMP': time_series.index, 'WLEV': smoothed_savgol})
smoothed_savgol_df.to_csv('./data/wlev-savgol.csv', index=False)

# Save the smoothed_lowess to a CSV file
smoothed_lowess_df = pd.DataFrame({'TIMESTAMP': time_series.index, 'WLEV': smoothed_lowess})
smoothed_lowess_df.to_csv('./data/wlev-lowess.csv', index=False)
