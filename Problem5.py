# 5. Write a program to do: A dataset collected in a cosmetics shop showing
# details of customers and whether or not they responded to a special offer
# to buy a new lip-stick is shown in table below. (Use library commands)
# According to the decision tree you have made from the previous training
# data set, what is the decision for the test data: [Age < 21, Income = Low,
# Gender = Female, Marital Status = Married]?

import pandas as pd
from sklearn.tree import DecisionTreeClassifier,export_text
from sklearn.preprocessing import LabelEncoder

# Step 1: Load the dataset

data = pd.read_csv("C:/Users/DELL/DSML_PRACTICAL/Datasets/Lipstick.csv")
print(data.head())

# Step 2: Encode categorical variables

label_encoders = {}

for column in data.columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# Step 3: Split features (X) and target (y)

X = data[["Age","Income","Gender","Ms"]]
y = data["Buys"]

# Step 4: Train a decision tree

clf = DecisionTreeClassifier(criterion="entropy",random_state=42)
clf.fit(X,y)

# Step 5: Test Data Prediction

test_data = pd.DataFrame([["<21","Low","Female","Married"]],columns=["Age","Income","Gender","Ms"])

for column in test_data.columns:
    test_data[column] = label_encoders[column].transform(test_data[column])

prediction = clf.predict(test_data)
predicted_label = label_encoders["Buys"].inverse_transform(prediction)

# Step 6: Display Results

print(f"Test data prediction: {predicted_label[0]}")

tree_rules = export_text(clf,feature_names=["Age","Income","Gender","Ms"])
print("\nDecision Tree Rules:")
print(tree_rules)