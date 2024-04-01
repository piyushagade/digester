
#! Generates two time series data files

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

def generate_time_series(length, trend_slope=0.02, noise_level=0.1, signal_range=(5, 9)):
    # Generate a synthetic time series with a linear trend, added noise, and signal between signal_range
    time = np.arange(length)
    trend = trend_slope * time
    noise = np.random.normal(0, noise_level, size=length)
    signal = np.random.uniform(signal_range[0], signal_range[1], size=length)
    time_series = trend + noise + signal
    return time_series

def main():
    # Set parameters for the synthetic time series
    series_length = 100
    drifters_distance = 5  # In distance unit
    trend_slope_drifter1 = 0.0
    trend_slope_drifter2 = 0.0

    # Generate synthetic time series for two drifters with a time lag
    time_series_drifter1 = generate_time_series(series_length, trend_slope=trend_slope_drifter1)
    time_series_drifter2 = generate_time_series(series_length, trend_slope=trend_slope_drifter2)

    # Introduce a time lag between the two drifters
    # time_series_drifter2_shifted = np.roll((time_series_drifter1 * (random.randint(4, 9) / 10.0)), int(drifters_distance))
    time_series_drifter2_shifted = np.roll(time_series_drifter1, int(drifters_distance))
    
    # Add noise
    noise_signal = np.random.uniform(low=0, high=0.75, size=len(time_series_drifter2_shifted))
    time_series_drifter2_shifted_with_noise = time_series_drifter2_shifted + noise_signal

    # Plot the generated time series
    plt.plot(time_series_drifter1, label='Drifter 1')
    plt.plot(time_series_drifter2_shifted_with_noise, label='Drifter 2 (Delayed)')
    # plt.plot(noise_signal, label='Noise')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.title('Time Series Data for Cross-Correlation Test')
    plt.show()

    # Save the synthetic time series data to CSV files
    df_drifter1 = pd.DataFrame({'value_column': time_series_drifter1})
    df_drifter2_shifted = pd.DataFrame({'value_column': time_series_drifter2_shifted_with_noise})

    df_drifter1.to_csv('./data/simdata1.csv', index=False)
    df_drifter2_shifted.to_csv('./data/simdata2.csv', index=False)

if __name__ == "__main__":
    main()
