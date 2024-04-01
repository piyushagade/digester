
#! This code calculates cross-correlation function for lags in the range -N to N, where N is
#! number of data points in the time series.    

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_csv(file_path):
    # Read CSV file and return a Pandas DataFrame
    return pd.read_csv(file_path)

def calculate_cross_correlation(series1, series2):
    
    # Normalize time series to convert values to [0, 1]
    normalized_series1 = (series1 - np.mean(series1)) / np.std(series1)
    normalized_series2 = (series2 - np.mean(series2)) / np.std(series2)

    # Calculate cross-correlation series with full mode
    cross_corr_series = np.correlate(normalized_series1, normalized_series2, mode='full')

    # Normalize cross-correlation to obtain similarity scores
    norm_cross_corr_series = cross_corr_series / (np.std(normalized_series1) * np.std(normalized_series2) * len(normalized_series1))

    return norm_cross_corr_series

def main():

    # Read CSV data
    file_path1 = './data/simdata1.csv'
    file_path2 = './data/simdata2.csv'

    # Read time series data from CSV files
    time_series1 = read_csv(file_path1)['value_column'].values
    time_series2 = read_csv(file_path2)['value_column'].values

    # Calculate cross-correlation series
    cross_corr_series = calculate_cross_correlation(time_series1, time_series2)

    # Find the delay at which maximum cross-correlation occurs
    max_corr_delay = len(time_series1) - 1 - np.argmax(cross_corr_series)
    max_corr_value = cross_corr_series[np.argmax(cross_corr_series)]

    print(f"Maximum Cross-Correlation:")
    print(f"Delay: {max_corr_delay}")
    print(f"Normalized Cross-Correlation Value: {max_corr_value:.4f}")

    # Plot cross-correlation series
    plt.plot(np.arange(-len(time_series1) + 1, len(time_series1)), cross_corr_series, label='Cross-Correlation')
    plt.axvline(x=-max_corr_delay, color='r', linestyle='--', label='Time Lag at Max Correlation')
    plt.legend()
    plt.grid(True)
    plt.xlabel('')
    plt.ylabel('Normalized Cross-Correlation')
    plt.title(f'Cross-Correlation Series  (Max at Time Lag: {max_corr_delay})')
    plt.show()

if __name__ == "__main__":
    main()
