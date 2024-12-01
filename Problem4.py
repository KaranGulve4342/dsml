# 4. Write a program to do: A dataset collected in a cosmetics shop showing
# details of customers and whether or not they responded to a special offer
# to buy a new lip-stick is shown in table below. (Implement step by step
# using commands - Dont use library) Use this dataset to build a decision
# tree, with Buys as the target variable, to help in buying lipsticks in the
# future. Find the root node of the decision tree.

import pandas as pd

import pandas as pd
import math

# Load the dataset
data = pd.read_csv("C:/Users/DELL/DSML_PRACTICAL/Datasets/Lipstick.csv")

# Function to calculate entropy
def calculate_entropy(data, target_column):

    values = data[target_column].value_counts()
    entropy = 0
    for count in values:
        probability = count / len(data)
        entropy -= probability * math.log2(probability)
    return entropy

# Function to calculate information gain
def calculate_information_gain(data, attribute, target_col):
    total_entropy = calculate_entropy(data, target_col)
    
    # Calculate weighted entropy for the attribute
    values = data[attribute].value_counts(normalize=True)
    weighted_entropy = sum(
        values[value] * calculate_entropy(data[data[attribute] == value], target_col)
        for value in values.index
    )
    
    # Information Gain
    info_gain = total_entropy - weighted_entropy
    return info_gain

# Step-by-step decision tree creation
target_column = "Buys"
attributes = [col for col in data.columns if col != target_column]

# Calculate information gain for each attribute
info_gains = {}
for attribute in attributes:
    info_gains[attribute] = calculate_information_gain(data, attribute, target_column)

# Find the root node
root_node = max(info_gains, key=info_gains.get)

# Display the results
print("Information Gain for each attribute:")
for attr, gain in info_gains.items():
    print(f"{attr}: {gain}")

print(f"\nRoot Node of the Decision Tree: {root_node}")

