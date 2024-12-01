# Use Iris flower dataset and perform following :
# 1. List down the features and their types (e.g., numeric, nominal)
# available in the dataset. 2. Create a histogram for each feature in the
# dataset to illustrate the feature distributions.


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('C:/Users/DELL/DSML_PRACTICAL/Datasets/IRIS.csv')

for column in data.columns:
    dtype = "Numeric" if data[column].dtype in ["float64","int64"] else "Nominal"
    print(f"{column}: {dtype}")

numeric_features = ["sepal_length","sepal_width","petal_length","petal_width"]

for feature in numeric_features:
    sns.histplot(data[feature],bins=15,kde=True,color='red')
    plt.title(f"Histogram of {feature}")
    plt.xlabel(feature)
    plt.ylabel("Frequency")
    plt.show()

