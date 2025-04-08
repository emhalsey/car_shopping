import pandas as pd
from pathlib import Path

def get_data(file_name: str):
    # Building the file path
    data_path = Path(__file__).parent.parent / "data" / file_name

    # Checking if file exists before reading
    if not data_path.exists():
        print(f"Whoops! Your file was not found at: {data_path}")
        return None

    # Exception handling
    try:
        df = pd.read_csv(data_path)
        print(f"Woohoo! Successfully found and loaded: {file_name}")
        return df
    except Exception as e:
        print(f"Whoops! Error reading your file: {e}")
        return None

kbb_df = get_data("kbb_data.csv")
fuel_df = get_data("cleaned_data.csv")

# Exit early if either failed to load
if kbb_df is None or fuel_df is None:
    exit()

# ========================== STANDARDIZATION ==========================
# Double-checking the field names to see what I can use as the key to merge the two datasets
    # Comment out after
# print(kbb_df.columns)
# print(fuel_df.columns)

# make the key that is needed to merge the fields
kbb_df['car_key'] = kbb_df['year'].astype(str) + '_' + kbb_df['make'] + '_' + kbb_df['model']
fuel_df['car_key'] = fuel_df['year'].astype(str) + '_' + fuel_df['make'] + '_' + fuel_df['model']

merged = pd.merge(kbb_df, fuel_df, on='car_key', how='left')

# making sure only one of each column remains
merged['year'] = merged['year_y']
merged = merged.drop(columns=['year_x', 'year_y'])

merged['make'] = merged['make_y']
merged = merged.drop(columns=['make_x', 'make_y'])

merged['model'] = merged['model_y']
merged = merged.drop(columns=['model_x', 'model_y'])

# Double-checking the field names (comment out after confirming)
# print("Merged Columns:", merged.columns)

# ========================== ANALYSIS ==========================
# Ensure numeric fields are actually numeric (in case they came in as strings)
merged['price'] = pd.to_numeric(merged['price'], errors='coerce')
merged['mileage'] = pd.to_numeric(merged['mileage'], errors='coerce')
merged['comb08'] = pd.to_numeric(merged['comb08'], errors='coerce')

# Create calculated columns
merged['Value_per_mile'] = merged['price'] / merged['mileage']
merged['MPG_per_dollar'] = merged['comb08'] / merged['price']

# Double-checking the field names AGAIN (comment out after confirming)
# print("Merged Columns:", merged.columns)

# Check how many missing values are in key columns
missing_data = merged[['price', 'mileage', 'comb08']].isnull().sum()
print("Missing Values in Each Column:")
print(missing_data)

# Drop rows with NaN values in key columns, or handle them differently
merged = merged.dropna(subset=['price', 'mileage', 'comb08'])

# Show a preview of the cleaned data
print(merged[['price', 'mileage', 'comb08', 'Value_per_mile', 'MPG_per_dollar']].head(20))

# # Group by 'model' and aggregate the data
# summary = merged.groupby('model').agg({
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