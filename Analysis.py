# Task 1: Load and Explore the Dataset

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset (synthetic sales data generated for this example)
data = {
    'Date': pd.date_range(start='2023-01-01', periods=31),
    'Product': np.random.choice(['Widget A', 'Gadget B', 'Tool C'], 31),
    'Sales': np.random.randint(100, 1000, 31),
    'Profit': np.random.randint(20, 200, 31),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 31)
}
df = pd.DataFrame(data)

# 2. Display first 5 rows
print("First 5 rows:")
print(df.head())

# 3. Check data types and missing values
print("\nData types and missing values:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

# 4. Clean data (no missing values here, but included for completeness)
df_clean = df.dropna()


# Task 2: Basic Data Analysis

# 1. Basic statistics for numerical columns
print("\nBasic statistics:")
print(df_clean[['Sales', 'Profit']].describe())

# 2. Group by 'Product' and calculate mean sales
product_sales = df_clean.groupby('Product')['Sales'].mean()
print("\nAverage sales by product:")
print(product_sales)

# 3. Observation: "Tool C" has the highest average sales


# Task 3: Data Visualization

plt.figure(figsize=(15, 10))

# 1. Line chart (Sales over time)
plt.subplot(2, 2, 1)
plt.plot(df_clean['Date'], df_clean['Sales'], marker='o')
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Sales ($)')

# 2. Bar chart (Average sales by product)
plt.subplot(2, 2, 2)
product_sales.plot(kind='bar', color=['#4CAF50', '#2196F3', '#FF5722'])
plt.title('Average Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales ($)')

# 3. Histogram (Sales distribution)
plt.subplot(2, 2, 3)
plt.hist(df_clean['Sales'], bins=8, edgecolor='black')
plt.title('Sales Distribution')
plt.xlabel('Sales ($)')
plt.ylabel('Frequency')

# 4. Scatter plot (Profit vs Sales)
plt.subplot(2, 2, 4)
plt.scatter(df_clean['Sales'], df_clean['Profit'], alpha=0.7)
plt.title('Profit vs Sales')
plt.xlabel('Sales ($)')
plt.ylabel('Profit ($)')

plt.tight_layout()
plt.show()
