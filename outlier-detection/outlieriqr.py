
# ! Outlier detection using Inter-quartile Range (IQR)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def detect_outliers_iqr(data, k=1.5):
    q75, q25 = np.percentile(data, [75 ,25])
    iqr = q75 - q25
    lower_bound = q25 - k * iqr
    upper_bound = q75 + k * iqr
    return np.where((data < lower_bound) | (data > upper_bound))[0], (q25, q75), (lower_bound, upper_bound)

# Read CSV file
file_path = './data/simdata2outliers.csv'
df = pd.read_csv(file_path)

# Select the column with numeric data for outlier detection
data = df['value_column'].values

# Detect outliers using IQR
outliers_iqr, (q25, q75), (lower_bound, upper_bound) = detect_outliers_iqr(data, k=1.5)

# Plot the original data with outliers highlighted using a box plot
plt.figure(figsize=(10, 6))

# Plot data
plt.plot(df.index, data, label='Data')

# Plot IQR range
plt.fill_between(df.index, q25, q75, color='lightblue', label='IQR', alpha=0.3)

# Plot outliers
plt.scatter(df.index[outliers_iqr], data[outliers_iqr], color='red', label='Detected outliers', zorder=5)

# Plot upper and lower bound for outliers
plt.axhline(upper_bound, color='gray', linestyle='--', label='Upper Bound')
plt.axhline(lower_bound, color='gray', linestyle='--', label='Lower Bound')

plt.title('Outlier Detection Using IQR')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.show()
