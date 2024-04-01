# In the context of time series data, "Normality" typically refers to the statistical property of the data distribution. 
# Specifically, it refers to whether the data follows a normal distribution, also known as a Gaussian distribution or bell curve.
#
# A time series is considered "normally distributed" if its values at each time point, or over intervals, approximate a Gaussian distribution.

#! Shapiro-Wilk Normality test

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro, probplot

# Read CSV file
df = pd.read_csv('../data/wlev.csv')

# Extract 'WLEV' column
wlev_data = df['WLEV'].dropna()  # Drop any NaN values

# Perform Shapiro-Wilk test for normality
statistic, p_value = shapiro(wlev_data)

# Set significance level
alpha = 0.01

# Print the results
print(f'Shapiro-Wilk Test for Normality:')
print(f'Statistic: {statistic}')
print(f'P-value: {p_value}')

# Check the null hypothesis
if p_value > alpha:
    print('The data follows a normal distribution (fail to reject the null hypothesis).')
else:
    print('The data does not follow a normal distribution (reject the null hypothesis).')

# Plot the histogram
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(wlev_data, bins=20, edgecolor='black')
plt.title('Histogram of WLEV Data')
plt.xlabel('WLEV')
plt.ylabel('Frequency')

# Plot the probability plot (Q-Q plot)
plt.subplot(1, 2, 2)
probplot(wlev_data, plot=plt)
plt.title('Probability Plot (Q-Q Plot) of WLEV Data')

plt.tight_layout()
plt.show()