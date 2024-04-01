# Gaussian kernel-based change point detection is a statistical method used to identify abrupt changes or shifts in the underlying distribution of a time series. 
# The technique employs a Gaussian kernel to smooth the time series data and then detects significant changes in the smoothed data that may indicate a change point.

# Gaussian kernel-based change point detection is a powerful technique for detecting structural changes in time series data and has applications in 
# various fields, including signal processing, finance, environmental monitoring, and quality control. However, the choice of kernel bandwidth and 
# detection algorithm parameters can significantly impact the performance and reliability of the method. 
# Therefore, careful tuning and validation are essential for accurate change point detection.

#! Kernel-based Change Point Detection

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ruptures as rpt

# Read CSV file
df = pd.read_csv('../data/wlev.csv')

# Extract 'WLEV' column
wlev_data = df['WLEV'].values
timestamp_data = df['TIMESTAMP'].values

# Convert 1D array to 2D array (required by ruptures library)
wlev_data_2d = wlev_data.reshape(-1, 1)

# # Linear kernels - Can detect changes in the mean of a signal
# result = rpt.KernelCPD(kernel="linear").fit(wlev_data_2d).predict(pen=100)

# Guassian kernel (Radial Basis Function) - Can detect changes in the distribution of an i.i.d. process; Non-parametric
# CostRBF function - https://centre-borelli.github.io/ruptures-docs/user-guide/costs/costrbf/
result = rpt.KernelCPD(kernel="rbf").fit(wlev_data_2d).predict(pen=10)

# result = rpt.Window(width=20).fit(wlev_data_2d).predict(pen=5)
# result = rpt.Binseg().fit(wlev_data_2d).predict(pen=20)

# Ensure indices are within bounds
result = [idx for idx in result if 0 <= idx < len(wlev_data)]

# Plot the time series and add vertical lines at the change points
plt.plot(wlev_data, label='WLEV Time Series')
for change_point in result:
    plt.axvline(x=change_point, color='#FFAAAA', linestyle='-', label='Change Point')

print (timestamp_data[result])

plt.title('Kernel-based Change Point Detection')
plt.xlabel('Time')
plt.ylabel('Sensor Value')
plt.show()