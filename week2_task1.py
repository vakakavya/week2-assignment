import pandas as pd
import numpy as np

print("=== Week 2: Data Loading & Cleaning ===")

# 1. Load dataset - replace 'sample_data.csv' with your file
# If you don't have CSV yet, we create sample data below
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, np.nan, 35, 28],
    'Salary': [50000, 60000, 55000, np.nan, 52000],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance']
}

df = pd.DataFrame(data)
print("\n1. Original Data:")
print(df)

# 2. Check for missing values
print("\n2. Missing values per column:")
print(df.isnull().sum())

# 3. Fill missing Age with mean, Salary with median
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].median(), inplace=True)

print("\n3. Data after filling missing values:")
print(df)

# 4. Basic stats
print("\n4. Basic statistics:")
print(df.describe())

# 5. Save cleaned data
df.to_csv('cleaned_data.csv', index=False)
print("\n5. Cleaned data saved as 'cleaned_data.csv'")
print("Done! Week 2 Task 1 complete.")
