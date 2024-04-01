
#! Generates a cross-correlation matrix to tabulate similarities between multiple time series data

# Initialize array with the list of all time series
time_series_list = []

import numpy as np

# Assume time_series_list is a list of your time series data
# Each element of the list represents a different time series

# Step 1: Pairwise Cross-Correlation
correlation_matrix = np.zeros((len(time_series_list), len(time_series_list)))

for i in range(len(time_series_list)):
    for j in range(i+1, len(time_series_list)):
        cross_corr = np.correlate(time_series_list[i], time_series_list[j], mode='full')
        correlation_matrix[i, j] = max(cross_corr)
        correlation_matrix[j, i] = max(cross_corr)

# Step 2: Aggregation
similarity_scores = np.sum(correlation_matrix, axis=1) / (len(time_series_list) - 1)

# Step 3: Normalization (Optional)
similarity_scores_normalized = (similarity_scores - np.min(similarity_scores)) / (np.max(similarity_scores) - np.min(similarity_scores))

# The similarity_scores or similarity_scores_normalized now represent the overall similarity for each time series.