import pandas as pd
import get_data

# ========================== READING ==========================
pd.set_option('display.max_columns', None)

filtered_df = get_data.find("filtered_govdata.csv")
agg_df = get_data.find("agg_data.csv")

if filtered_df is None or agg_df is None:
    print("Whoops! Couldn't find the files you were looking for. Please check the spelling and try again.")
    exit()

# ========================== ORGANIZATION ==========================
    # check field names to see what you can use as a key

# merging the fields on the new key
merged_df = pd.merge(filtered_df, agg_df, on='car_key', how='outer')

# only keeping necessary fields
merged_df = merged_df[[
    'car_key',
    'OVERALL_STARS',
    'NUM_OF_SEATING',
    'comb08',
    'Avg_Price',
    'Avg_Mileage',
    'youSaveSpend',
    'cylinders',
    'ROLLOVER_POSSIBILITY',
    'ROLLOVER_STARS']]

import re
import numpy as np

# average number of seats when there's a range
def parse_seating(value):
    if pd.isnull(value):
        return np.nan
    numbers = re.findall(r'\d+', str(value))
    if numbers:
        # only keep numbers between 1 and 12 (reasonable car seating)
        nums = [int(n) for n in numbers if 1 <= int(n) <= 12]
        if nums:
            return sum(nums) / len(nums)
    return np.nan

merged_df['NUM_OF_SEATING'] = merged_df['NUM_OF_SEATING'].apply(parse_seating)

# print(merged_df.head(20))

# ================== MULTI-ATTRIBUTE DECISION MAKING (MADM) ==================
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaled_features = scaler.fit_transform(
    merged_df[['OVERALL_STARS',
               'NUM_OF_SEATING',
               'comb08',
               'Avg_Price',
               'ROLLOVER_POSSIBILITY']])
scaled_df = pd.DataFrame(scaled_features,
            columns=['OVERALL_STARS',
                     'NUM_OF_SEATING',
                     'comb08',
                     'Avg_Price',
                     'ROLLOVER_POSSIBILITY'])

weights = {
    'OVERALL_STARS': 0.29,
    'NUM_OF_SEATING': 0.30,
    'comb08': 0.29,
    'Avg_Price': 0.02,
    'ROLLOVER_POSSIBILITY': 0.10
}

# smaller values are preferred
scaled_df['Avg_Price'] = 1 - scaled_df['Avg_Price']
scaled_df['ROLLOVER_POSSIBILITY'] = 1 - scaled_df['ROLLOVER_POSSIBILITY']

scaled_df['utility_score'] = (
    scaled_df['OVERALL_STARS'] * weights['OVERALL_STARS'] +
    scaled_df['NUM_OF_SEATING'] * weights['NUM_OF_SEATING'] +
    scaled_df['comb08'] * weights['comb08'] +
    scaled_df['Avg_Price'] * weights['Avg_Price'] +
    scaled_df['ROLLOVER_POSSIBILITY'] * weights['ROLLOVER_POSSIBILITY']
)

ranked_cars = merged_df.copy()
ranked_cars['utility_score'] = scaled_df['utility_score']
ranked_cars = ranked_cars.sort_values(by='utility_score', ascending=False)

# export data to output folder
final = get_data.export("output","ranked.csv")
ranked_cars.to_csv(final, index=False)

# ========================== VIZ W/ PYGAL ==========================
import pygal

# filter duplicates and drop rows with missing values
ranked_cars = ranked_cars.dropna(subset=['car_key', 'utility_score'])
ranked_cars = ranked_cars.drop_duplicates(subset=['car_key'])

top_cars = ranked_cars.head(10)

# print(top_cars)

# bar graph ==========================

horizontal_chart = pygal.HorizontalBar()
horizontal_chart.title = "Top 10 Cars by Utility Score"

for index, row in top_cars.iterrows():
    horizontal_chart.add(row['car_key'], row['utility_score'])

# export graph to output folder
graph = get_data.export("output","ranked.svg")
horizontal_chart.render_to_file(graph)