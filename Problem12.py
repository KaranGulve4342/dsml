# 12.Use Iris flower dataset and perform following :
# 1. Create a box plot for each feature in the dataset.
# 2. Identify and discuss distributions and identify outliers from them.


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('C:/Users/DELL/DSML_PRACTICAL/Datasets/IRIS.csv')

numeric_features = ["sepal_length","sepal_width","petal_length","petal_width"]

for feature in numeric_features:
    sns.boxplot(x=data[feature],color="red")
    plt.title(f"Box plot of {feature}")
    plt.xlabel(feature)
    plt.show()

