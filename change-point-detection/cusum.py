
#! Change point detection using CUSUM algorithm

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ruptures as rpt

breakpoints = 4

# Function to apply CUSUM algorithm
def cusum(data, threshold=1.0):
    n = len(data)
    mean_reference = np.mean(data)
    cusum_values = np.zeros(n)

    for i in range(1, n):
        cusum_values[i] = max(0, cusum_values[i-1] + (data[i] - mean_reference))

    return cusum_values

# Function to detect change points using ruptures library
def detect_change_points(data, method, threshold=1.0):
    algo = rpt.Dynp(model=method).fit(data)
    result = algo.predict(n_bkps=breakpoints)
    return result

# Read CSV file
df = pd.read_csv('../data/rtd.csv')

# Extract 'WLEV' column
wlev_data = df['RTD'].values

# Apply CUSUM algorithm
cusum_values = cusum(wlev_data)

# Detect change points using ruptures library
change_points = detect_change_points(np.array([cusum_values]).T, 'l2', threshold=10.0)

# Ensure indices are within bounds
change_points = [idx for idx in change_points if 0 <= idx < len(wlev_data)]

# Plot the time series, CUSUM values, and detected change points
plt.subplot(2, 1, 1)
plt.plot(wlev_data, label='Water Level')
plt.title('Water Level with CUSUM')
plt.xlabel('Time')
plt.ylabel('Water Level')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(cusum_values, label='CUSUM Values', color='orange')
plt.scatter(change_points, cusum_values[change_points], color='red', label='Change Points')
plt.title('CUSUM Values and Detected Change Points')
plt.xlabel('Time')
plt.ylabel('CUSUM Values')
plt.legend()

plt.tight_layout()
plt.show()