# -*- coding: utf-8 -*-
"""DSF!.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fb7tlMwgIlv3vgzLOZjmPB9Vg5DTjVDw
"""

import matplotlib.pyplot as plt
import pandas as pd

""" Matplotlib: a popular library for creating charts and plots in Python. By using plt, you can easily visualize data with graphs like line charts, bar charts, and more.
Pandas:a powerful library used for working with structured data, like tables or spreadsheets. pd allows you to manipulate and analyze data easily, including reading from CSV files, filtering, sorting, and more.
"""

# Load dataset
df = pd.read_csv('/content/FOOD-DATA-GROUP1.csv')

"""This will load the datatset in the environement."""

print(df.head())

print(df.columns)

# We filter the numeric columns only
# Select only the numeric columns
numeric_df = df.select_dtypes(include=[int, float])
# Check the number of columns
print(f"Number of numeric columns: {numeric_df.shape[1]}")
# Now selecting the first row of numeric data (height for the bar chart)
height = numeric_df.iloc[0].values  # Get the values for the bar heights
# Get the corresponding tick labels for the selected numeric columns
tick_label = numeric_df.columns
left = list(range(len(tick_label)))

"""# New section

Label for bars

# Tick labels based on column names (excluding the 'food' column)
"""

# Check that the lengths of the arrays match
print(f"Length of left: {len(left)}")
print(f"Length of height: {len(height)}")

#plotting a bar chart
plt.figure(figsize=(12, 8))
plt.bar(left, height, tick_label=tick_label, color=['red', 'green', 'blue', 'yellow'] * (len(left) // 4 + 1))
# Add labels and title
plt.xlabel('Nutritional Categories')
plt.ylabel('Values')
plt.title('Nutritional Analysis for a Specific Food Item')
# Rotate the x-axis labels for better readability
plt.xticks(rotation=90)
# Display the chart
plt.show()

"""#Histogram"""

column_name = 'Caloric Value'
data = df[column_name]
# Plot the histogram
plt.figure(figsize=(10, 6))
plt.hist(data, bins=20, color='skyblue', edgecolor='black')
# Add labels and title
plt.xlabel(column_name)
plt.ylabel('Frequency')
plt.title(f'Histogram of {column_name}')
# Display the histogram
plt.show()

"""#Scatter Plot"""

x_column = 'Caloric Value'  # X-axis data
y_column = 'Protein'        # Y-axis data
# Extract the data
x_data = df[x_column]
y_data = df[y_column]
# Plot the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, color='blue', alpha=0.5)
# Add labels and title
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title(f'Scatter Plot of {x_column} vs. {y_column}')
# Display the scatter plot
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# Load dataset
df = pd.read_csv('/content/FOOD-DATA-GROUP1.csv')

"""#Seaborn library"""

import seaborn as sns
n = 10
subset_df = df[['Protein', 'Nutrition Density']].head(n)
plt.figure(figsize=(10, 10))
sns.barplot(x='Protein', y='Nutrition Density', data=subset_df, palette='viridis')
plt.title('Bar Plot of Protein vs. Nutrition Density')
plt.xlabel('Protein')
plt.ylabel('Nutrition Density')
plt.xticks(rotation=90)
sns.despine()
plt.show()

# Create a scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Caloric Value', y='Protein', data=df, color='blue', alpha=0.5)
# Set title and labels
plt.title('Scatter Plot of Caloric Value vs. Protein')
plt.xlabel('Caloric Value')
plt.ylabel('Protein')
# Show the plot
sns.despine()
plt.show()

# Create a histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['Caloric Value'], bins=20, kde=False, color='skyblue')
# Set title and labels
plt.title('Histogram of Caloric Value')
plt.xlabel('Caloric Value')
plt.ylabel('Frequency')
# Show the plot
sns.despine()
plt.show()

"""#Missing Value"""

print(df.isnull().sum())

"""No missing value in our datatset"""

print(df['Nutrition Density'].isnull().sum())

print(df.loc[1:].isnull().sum())

"""checks for any missing (null) values in the selected rows. It returns True for each null value and False otherwise."""

print(df.isnull().sum())
print(df.dtypes)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[['Caloric Value']] = scaler.fit_transform(df[['Caloric Value']])

"""Definition: Standardization transforms the data to have a mean of 0 and a standard deviation of 1. It’s typically used when the data follows a Gaussian (normal) distribution.

This code scales the 'Caloric Value' column by standardizing its values (mean of 0 and standard deviation of 1) using the StandardScaler.
"""

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
# Scale the 'Caloric Value' column
df[['Caloric Value']] = scaler.fit_transform(df[['Caloric Value']])

"""Normalization scales the data to a fixed range, typically between 0 and 1. It’s commonly used when the data does not follow a normal distribution or to scale the data within a specific range."""

df['new_feature'] = df['Caloric Value'] + df['Nutrition Density']

df_clean = df.copy()
 # Perform your cleaning operations on df_clean
 # Print the cleaned DataFrame
print(df_clean.head())

# Check data types of columns
print(df_clean.dtypes)

# Drop the 'food' column
df = df.drop(columns='food')
# Verify the column has been dropped
print(df.head())
print(df.columns)

print(f"Dataset shape: {df.shape}")

# Compute the correlation matrix
corr_matrix = df.corr()
# Display the correlation matrix
print(corr_matrix)
# Visualize the correlation matrix using a heatmap
plt.figure(figsize=(15, 15))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()

"""The heatmap provides a visual representation of the correlation matrix.
Annotates each cell with the numeric value of the correlation.
Formats the annotations to show two decimal places,'coolwarm'specifies the color palette, where blue tones represent negative correlations, and red tones represent positive correlations.
"""

df.columns

# Drop the columns
df = df.drop(columns=[ 'Polyunsaturated Fats', 'Monounsaturated Fats', 'Vitamin B6', 'Manganese', 'Selenium'])
# Resulting DataFrame to ensure the columns were dropped
print(df.head())
print(df.columns)

# Compute the correlation matrix
corr_matrix = df.corr()
# Display the correlation matrix
print(corr_matrix)
# Visualize the correlation matrix using a heatmap
plt.figure(figsize=(15, 15))  # Adjust the figure size to fit your columns
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()