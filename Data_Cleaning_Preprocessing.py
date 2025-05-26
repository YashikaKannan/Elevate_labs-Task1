import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Importing the dataset and exploring the basic info
df = pd.read_csv("Titanic-Dataset.csv")
print("Initial Data Info:")
print(df.info())
print("Missing Values:")
print(df.isnull().sum())

# Handling missing values using mean/median/mode
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Converting categorical features into numerical using encoding
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

# Droping non-useful columns
df.drop(columns=['Cabin', 'Name', 'Ticket', 'PassengerId'], inplace=True)

# Normalizing the numerical features
scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

# Visualizing outliers using boxplots
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
sns.boxplot(data=df, x='Age', ax=axes[0])
axes[0].set_title("Boxplot of Age (After Cleaning)")

sns.boxplot(data=df, x='Fare', ax=axes[1])
axes[1].set_title("Boxplot of Fare (After Cleaning)")

plt.tight_layout()
plt.show()
