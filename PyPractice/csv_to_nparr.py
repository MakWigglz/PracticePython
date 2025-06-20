import numpy as np
from datetime import datetime

# Raw data as a list of strings
data = [
    ["2019-05-31 00:00:00", 103.26, 305.46, 94.71, 31.43, 30.16, 3.0, 18.06, 178.31, 152.73, 13.65, 83.47, 2.54],
    ["2019-05-31 01:00:00", 104.47, 309.14, 74.66, 34.08, 27.02, 1.69, 18.65, 106.5, 79.98, 11.35, 76.79, 2.91],
    ["2019-05-31 02:00:00", 90.0, 314.02, 48.11, 32.6, 18.12, 0.83, 28.27, 48.45, 25.27, 5.66, 32.91, 1.59],
    ["2019-05-31 03:00:00", 78.01, 356.14, 45.45, 30.21, 16.78, 0.79, 27.47, 44.22, 21.5, 3.6, 21.41, 0.78],
    ["2019-05-31 04:00:00", 80.19, 372.9, 45.23, 28.68, 16.41, 0.76, 26.92, 44.06, 22.15, 4.5, 23.39, 0.62],
    ["2019-05-31 05:00:00", 83.59, 389.97, 39.49, 27.71, 17.42, 0.76, 28.71, 39.33, 21.04, 3.25, 23.59, 0.56],
    ["2019-05-31 06:00:00", 79.04, 371.64, 39.61, 26.87, 16.91, 0.84, 29.26, 43.11, 24.37, 3.12, 15.27, 0.46],
    ["2019-05-31 07:00:00", 77.32, 361.88, 42.63, 27.26, 17.86, 0.96, 27.07, 48.22, 28.81, 3.32, 14.42, 0.41],
    ["2019-05-31 08:00:00", 84.3, 377.77, 42.49, 28.41, 20.19, 0.98, 33.05, 48.22, 27.76, 3.4, 14.53, 0.4]
]

# Convert timestamps to datetime objects
timestamps = [datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S") for row in data]

# Convert numeric values to a NumPy array
numeric_data = np.array([row[1:] for row in data], dtype=np.float64)

print(timestamps)  # List of datetime objects
print(numeric_data)  # NumPy array of numerical values
print(numeric_data.shape)
