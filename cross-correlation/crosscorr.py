# Cross-correlation is a statistical technique used to measure the similarity between two time series signals. In the context of time series analysis, it is commonly employed to understand the relationship between two sets of data points collected over time.
# Here's how cross-correlation works:
#   Definition: Cross-correlation measures the similarity between two sequences of data points as a function of the displacement of one relative to the other. It computes a series of correlation coefficients, each corresponding to a particular displacement.
#   Interpretation: A high cross-correlation coefficient indicates that the two signals are similar or related at that particular displacement (lag). A peak in the cross-correlation function typically indicates the best alignment between the two signals.
#
#   Requirements:
#       Stationarity: 
#           Time series should be stationary or approximately stationary. 
#           This means that the statistical properties of the series, such as mean and variance, do not change over time. 
#           Non-stationary series may require preprocessing, such as detrending or differencing, before cross-correlation analysis.
#       Sampling Rate: 
#           Both time series should be sampled at the same rate. 
#           If they are sampled at different rates, you might need to interpolate or resample one of the signals to match the other.
#       Sufficient Length: 
#           Time series should be sufficiently long to capture meaningful patterns. 
#           Too short a series might lead to unreliable correlation estimates, especially if the underlying processes are complex.
#       Temporal Overlap: 
#           There should be some temporal overlap between the two time series being compared. 
#           If one of the series is significantly shorter than the other, meaningful cross-correlation analysis may not be possible.
#       Noisy Data: Excessive noise in the time series can distort the cross-correlation results. 
#           Preprocessing steps like smoothing or filtering might be necessary to reduce noise before performing cross-correlation.
#
# Cross-correlation is widely used in various fields such as signal processing, finance, economics, and environmental science to analyze and understand the relationships between different time-varying phenomena.

#! This code calculates cross-correlation (similarity score) at a know time lag

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_csv(file_path):
    # Read CSV file and return a Pandas DataFrame
    return pd.read_csv(file_path)

def calculate_cross_correlation(series1, series2, time_delay):

    # Normalize time series to convert values to [0, 1]
    normalized_series1 = (series1 - np.mean(series1)) / np.std(series1)
    normalized_series2 = (series2 - np.mean(series2)) / np.std(series2)

    # Calculate cross-correlation with an explicit time lag
    cross_corr = np.correlate(normalized_series1, np.roll(normalized_series2, -time_delay), mode='full')

    # Normalize cross-correlation to obtain similarity score (1 for perfect similarity)
    similarity_score = cross_corr.max() / (np.std(normalized_series1) * np.std(normalized_series2) * len(normalized_series1))

    return similarity_score

def main():
    
    # Known time lag
    known_time_lag = 5
    
    # Read CSV data
    file_path1 = '../data/simdata1.csv'
    file_path2 = '../data/simdata2.csv'

    # Read time series data from CSV files
    time_series1 = read_csv(file_path1)['value_column'].values
    time_series2 = read_csv(file_path2)['value_column'].values

    # Calculate cross-correlation similarity score
    similarity_score = calculate_cross_correlation(time_series1, time_series2, known_time_lag)

    print(f"Cross-Correlation")
    print(f"-----------------")
    print(f"Known Time Delay: {known_time_lag}")

    if similarity_score > 1:
        print(f"Similarity Score over 1.0 detected: {similarity_score}")
        similarity_score = 1.0
    else:
        print(f"Similarity Score: {similarity_score * 100:.2f}%")

    # Plot the aligned time series for visualization
    plt.plot(time_series1, label='Drifter 1')
    plt.plot(np.roll(time_series2, -known_time_lag), label='Drifter 2 (Delay removed)')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.title(f'Similarity score: {similarity_score * 100:.2f}% at delay: {known_time_lag}')
    plt.show()

if __name__ == "__main__":
    main()