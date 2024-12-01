# 1. Perform the following operations using Python on a data set : read data
# from different formats(like csv, xls),indexing and selecting data, sort data,
# describe attributes of data, checking data types of each column. (Use
# Titanic Dataset).

import pandas as pd

# read data from different formats(like csv, xls)
df1 = pd.read_csv('C:/Users/DELL/DSML_PRACTICAL/Datasets/Titanic.csv')

# df2 = pd.read_csv('C:/Users/DELL/DSML_PRACTICAL/Datasets/Titanic.xls')

print(df1.head())

print(df1.sample())

# indexing and selecting data
print("setting passengerId as index")
df1.set_index("PassengerId", inplace = True)

print("Selecting a specific column")
print(df1["Name"].head())

print("selecting rows using loc (label based)")
print(df1.loc[1:5,["Name","Survived"]])

print("selecting rows using iloc (position based)")
print(df1.iloc[0:5,0:3])


# sort data
print("sort data")
sorted_data = df1.sort_values(by="Age",ascending=True)
print(sorted_data.head())   

# Describing numerical attributes
print(df1.describe())

# Describing all attributes, including categorical
print(df1.describe(include='all'))

# Checking dataset structure and memory usage
print(df1.info())


# Displaying data types of all columns
print(df1.dtypes)
