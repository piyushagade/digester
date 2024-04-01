import pandas as pd
import numpy as np

# Function to simulate water temperature with multiple change points
def simulate_water_temperature(num_points=100, change_points=None):
    timestamps = pd.date_range("2023-01-01", periods=num_points, freq="H")
    water_temperature = np.random.normal(loc=15, scale=2, size=num_points)

    # Simulate multiple change points (tributaries merging)
    if change_points:
        for change_point_index, change_point_value in change_points:
            water_temperature[change_point_index:] += change_point_value

    df = pd.DataFrame({"TIMESTAMP": timestamps, "RTD": water_temperature})
    return df

# Simulate water temperature data with multiple change points
# Define the change points as (index, temperature_change)
change_points = [(30, -3), (60, +5), (180, 8), (270, -5)]  # Example: Two tributaries merging at indices 30 and 60

water_temperature_df = simulate_water_temperature(num_points=500, change_points=change_points)

# Save the generated data to a CSV file
water_temperature_df.to_csv("../data/rtd.csv", index=False)

print("CSV file '../data/rtd.csv' generated successfully.")
