import pandas as pd
import get_data

df = get_data.find("scraped_data.csv")

if df is None:
    print("Whoops! Couldn't find the files you were looking for. Please check the spelling and try again.")
    exit()

# ========================== STANDARDIZATION ==========================
# check field names to see what you can use as a key

# make a merged column to act as the key
df['car_key'] = (df['year'].map(str) + ' ' + df['make'].map(str.upper) + ' ' + df['model'].map(str.upper))

# check the field names to see if it worked (comment out after confirming)
# print(df.columns)

# ========================== CLEANING ==========================
# Ensure numeric fields are actually numeric (in case they came in as strings)
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['mileage'] = pd.to_numeric(df['mileage'], errors='coerce')

# Check how many missing values are in key columns & drop rows with NaN values if applicable
missing_data = df[['price', 'mileage']].isnull().sum()
# print("Missing Values in Each Column:"), print(missing_data)
# df = scraped_df.dropna(subset=['price', 'mileage'])

# calculated field
df['Value_per_mile'] = df['price'] / df['mileage']
# print(df[['price', 'mileage', 'Value_per_mile']].head(20))

# ========================== AGGREGATION ==========================
# Group by 'model' and aggregate the data
summary = df.groupby('car_key').agg({
    'price': 'mean',
    'mileage': 'mean',
    'Value_per_mile': 'mean',
    'city': 'count'
}).rename(columns={
    'price': 'Avg_Price',
    'mileage': 'Avg_Mileage',
    'Value_per_mile': 'Avg_Value_per_mile',
    'city': 'Nr_Available'
}).sort_values('Avg_Value_per_mile', ascending=False)

print(summary)

# export data to output folder
agg = get_data.export("data","agg_data.csv")
summary.to_csv(agg, index=True)