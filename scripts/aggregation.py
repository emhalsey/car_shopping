import pandas as pd
import get_data

scraped_df = get_data.find("scraped_data.csv")

if scraped_df is None:
    print("Whoops! Couldn't find the files you were looking for. Please check the spelling and try again.")
    exit()

# ========================== AGGREGATION ==========================
# Ensure numeric fields are actually numeric (in case they came in as strings)
scraped_df['price'] = pd.to_numeric(scraped_df['price'], errors='coerce')
scraped_df['mileage'] = pd.to_numeric(scraped_df['mileage'], errors='coerce')

# Check how many missing values are in key columns
missing_data = scraped_df[['price', 'mileage']].isnull().sum()
# print("Missing Values in Each Column:" + missing_data)

# Drop rows with NaN values in key columns if applicable
# df = scraped_df.dropna(subset=['price', 'mileage'])

# calculated field
scraped_df['Value_per_mile'] = scraped_df['price'] / scraped_df['mileage']

# Show a preview of the data
# print(scraped_df[['price', 'mileage', 'Value_per_mile']].head(20))

# Group by 'model' and aggregate the data
summary = scraped_df.groupby('model').agg({
    'price': 'mean',
    'mileage': 'mean',
    'Value_per_mile': 'mean'
}).rename(columns={
    'price': 'Avg_Price',
    'mileage': 'Avg_Mileage',
    'Value_per_mile': 'Avg_Value_per_mile'
}).sort_values('Avg_Value_per_mile', ascending=False)

# print(summary)

# export data to output folder
agg = get_data.export("output","agg_values.csv")
# summary.to_csv(agg, index=True)