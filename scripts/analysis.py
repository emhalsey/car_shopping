import pandas as pd
import get_data

df = get_data.find("filtered_data.csv")
"""
# ========================== ANALYSIS ==========================
# Ensure numeric fields are actually numeric (in case they came in as strings)
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['mileage'] = pd.to_numeric(df['mileage'], errors='coerce')
df['comb08'] = pd.to_numeric(df['comb08'], errors='coerce')

# Create calculated columns
df['Value_per_mile'] = df['price'] / df['mileage']
df['MPG_per_dollar'] = df['comb08'] / df['price']

# Double-checking the field names AGAIN (comment out after confirming)
# print("Merged Columns:", df.columns)

# Check how many missing values are in key columns
missing_data = df[['price', 'mileage', 'comb08']].isnull().sum()
print("Missing Values in Each Column:")
print(missing_data)

# Drop rows with NaN values in key columns, or handle them differently
df = df.dropna(subset=['price', 'mileage', 'comb08'])

# Show a preview of the cleaned data
print(df[['price', 'mileage', 'comb08', 'Value_per_mile', 'MPG_per_dollar']].head(20))

# # Group by 'model' and aggregate the data
# summary = df.groupby('model').agg({
#     'price': 'mean',
#     'mileage': 'mean',
#     'comb08': 'mean',
#     'Value_per_mile': 'mean',
#     'MPG_per_dollar': 'mean'
# }).rename(columns={
#     'price': 'AVG Price',
#     'mileage': 'AVG Mileage',
#     'comb08': 'AVG Combined MPG',
#     'Value_per_mile': 'AVG Value_per_mile',
#     'MPG_per_dollar': 'AVG MPG_per_dollar'
# }).sort_values('AVG MPG_per_dollar', ascending=False)
#
# # Print the summary
# print(summary)
"""