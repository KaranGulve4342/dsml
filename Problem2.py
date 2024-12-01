# 2. Perform the following operations using Python on the Telecom_Churn
# dataset. Compute and display summary statistics for each feature available
# in the dataset using separate commands for each statistic. (e.g. minimum
# value, maximum value, mean, range, standard deviation, variance and
# percentiles).


import pandas as pd

# Load the Telecom Churn dataset
file_path = "C:/Users/DELL/DSML_PRACTICAL/Datasets/Telecom Churn.csv"  # Update the path as needed
telecom_data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(telecom_data.head())

# Summary statistics for each feature
for column in telecom_data.select_dtypes(include=['number']).columns:
    print(f"\nStatistics for {column}:")
    
    # Minimum value
    print(f"Minimum: {telecom_data[column].min()}")
    
    # Maximum value
    print(f"Maximum: {telecom_data[column].max()}")
    
    # Mean
    print(f"Mean: {telecom_data[column].mean()}")
    
    # Range
    data_range = telecom_data[column].max() - telecom_data[column].min()
    print(f"Range: {data_range}")
    
    # Standard deviation
    print(f"Standard Deviation: {telecom_data[column].std()}")
    
    # Variance
    print(f"Variance: {telecom_data[column].var()}")
    
    # Percentiles
    percentiles = telecom_data[column].quantile([0.25, 0.5, 0.75]).to_dict()
    print(f"25th Percentile: {percentiles[0.25]}")
    print(f"50th Percentile (Median): {percentiles[0.5]}")
    print(f"75th Percentile: {percentiles[0.75]}")
