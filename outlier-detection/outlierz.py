
#! Outlier detection using Z-distribution

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def detect_outliers_zscore(data, threshold=3):
    z_scores = np.abs((data - np.mean(data)) / np.std(data))
    return np.where(z_scores > threshold)[0]

# Read CSV data
file_path = './data/simdata2outliers.csv'
df = pd.read_csv(file_path)

# Select the column with numeric data for outlier detection
data = df['value_column'].values

# Detect outliers using Z-Score
# Threshold is the std. deviation count
outliers = detect_outliers_zscore(data, threshold=2)

# Plot the original data with outliers highlighted using a box plot
plt.figure(figsize=(10, 6))
plt.plot(df.index, data, label='Data')
plt.scatter(df.index[outliers], data[outliers], color='red', label='Detected outliers', zorder=5)
plt.title('Outlier Detection Using Z-Score')
plt.xlabel('Index')
plt.ylabel('Numeric Column')
plt.legend()
plt.show()


# The outlier detection method used in the provided examples is based on Z-Score, a statistical measure that quantifies how many standard deviations a data point is from the mean. Here's a brief explanation of how the Z-Score outlier detection method works:
# The Z-Score measures how many standard deviations a data point is from the mean. Positive Z-Scores indicate points above the mean, while negative Z-Scores indicate points below the mean.

# Set a Threshold:
# A threshold is chosen to determine what is considered an outlier. Common thresholds are 2, 2.5, or 3 standard deviations from the mean.
# Data points with Z-Scores beyond this threshold are flagged as potential outliers.
# Identify Outliers:

# Points with Z-Scores beyond the chosen threshold are considered outliers.
# The index or position of these outliers is stored or used for visualization.

# Visualization:
# The original data is plotted, and outliers are highlighted using markers or a different color.
# In the provided examples, the function detect_outliers_zscore calculates the Z-Scores for each data point and identifies outliers based on a user-defined threshold. The outliers are then visualized on the original data plot.

# Keep in mind that the Z-Score method assumes the data follows a normal distribution. If your data has a different distribution, or if you have specific domain knowledge about what constitutes an outlier in your context, you might consider using other methods, such as the Interquartile Range (IQR) or domain-specific techniques.