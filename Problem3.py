# 3. Perform the following operations using Python on the data set
# House_Price Prediction dataset. Compute standard deviation, variance and
# percentiles using separate commands, for each feature. Create a histogram
# for each feature in the dataset to illustrate the feature distributions

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

House_Price = pd.read_csv("C:/Users/DELL/DSML_PRACTICAL/Datasets/House Data.csv")

print(House_Price.info())


for column in House_Price.select_dtypes(include=['number']).columns:
    print(f"\nFeature distribution for {column}")

    print(f"Standard Deviation: {House_Price[column].std()}")

    print(f"Variance: {House_Price[column].var()}")

    percentiles = House_Price[column].quantile([0.25,0.5,0.75]).to_dict()

    print(f"25th percentile: {percentiles[0.25]}")
    print(f"50th percentile: {percentiles[0.5]}")
    print(f"75th percentile: {percentiles[0.75]}")



# Create histograms for each numerical feature using Seaborn
for column in House_Price.select_dtypes(include=['number']).columns:
    plt.figure(figsize=(8, 6))
    sns.histplot(House_Price[column])
    plt.title(f'Histogram of {column}', fontsize=16)
    plt.xlabel(column, fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
