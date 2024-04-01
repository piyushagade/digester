import pandas as pd
from fastdtw import fastdtw

def read_csv(file_path):
    # Read CSV file and return a Pandas DataFrame
    return pd.read_csv(file_path)

def calculate_dtw_distance(series1, series2):
    # Perform DTW and get the distance
    distance, path = fastdtw(series1, series2)
    return distance

def main():
    # Replace 'path_to_file1.csv' and 'path_to_file2.csv' with your actual file paths
    file_path1 = '../data/simdata1.csv'
    file_path2 = '../data/simdata2.csv'

    # Read time series data from CSV files
    time_series1 = read_csv(file_path1)['value_column'].values
    time_series2 = read_csv(file_path2)['value_column'].values

    # Calculate DTW distance (dissimilarity score)
    dtw_distance = calculate_dtw_distance(time_series1, time_series2)

    # Output the similarity score (1 - normalized DTW distance)
    similarity_score = 1 - (dtw_distance / max(len(time_series1), len(time_series2)))

    print(f"DTW Distance: {dtw_distance}")
    print(f"Similarity Score: {similarity_score}")

if __name__ == "__main__":
    main()