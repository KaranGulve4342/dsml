# 13. Use the covid_vaccine_statewise.csv dataset and perform the following
# analytics.
# a. Describe the dataset
# b. Number of persons state wise vaccinated for first dose in India
# c. Number of persons state wise vaccinated for second dose in India

import pandas as pd

# Load the dataset
data = pd.read_csv('C:/Users/DELL/DSML_PRACTICAL/Datasets/Covid Vaccine Statewise.csv')

# a. Describe the dataset
print("Dataset Description:\n")
print(data.describe())
print("\nDataset Info:\n")
print(data.info())

# b. Number of persons state-wise vaccinated for the first dose
statewise_first_dose = data.groupby('State')['First Dose Administered'].sum()
print("\nState-wise First Dose Administered:\n")
print(statewise_first_dose)

# c. Number of persons state-wise vaccinated for the second dose
statewise_second_dose = data.groupby('State')['Second Dose Administered'].sum()
print("\nState-wise Second Dose Administered:\n")
print(statewise_second_dose)
