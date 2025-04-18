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

# deleting duplicate & unnecessary fields
merged_df = (merged_df.drop(
    columns=['make', 'model', 'year','baseModel','VClass','guzzler',
             'Nr_Available','BODY_STYLE','VEHICLE_TYPE','DRIVE_TRAIN','fuelType','trany']))

merged_df = merged_df[[
    'car_key',
    'OVERALL_STARS',
    'NUM_OF_SEATING',
    'comb08',
    'Avg_Value_per_mile',
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
    numbers = re.findall(r'\d+', str(value)) # extract numbers from strings
    if numbers:
        nums = list(map(int, numbers))
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
               'Avg_Value_per_mile',
               'youSaveSpend',
               'ROLLOVER_STARS']])
scaled_df = pd.DataFrame(scaled_features,
            columns=['OVERALL_STARS',
                     'NUM_OF_SEATING',
                     'comb08',
                     'Avg_Value_per_mile',
                     'youSaveSpend',
                     'ROLLOVER_STARS'])

weights = {
    'OVERALL_STARS': 0.25,
    'NUM_OF_SEATING': 0.15,
    'comb08': 0.35,
    'Avg_Value_per_mile': 0.15,
    'youSaveSpend': 0.05,
    'ROLLOVER_STARS': 0.05
}

scaled_df['utility_score'] = (
    scaled_df['OVERALL_STARS'] * weights['OVERALL_STARS'] +
    scaled_df['NUM_OF_SEATING'] * weights['NUM_OF_SEATING'] +
    scaled_df['comb08'] * weights['comb08'] +
    scaled_df['Avg_Value_per_mile'] * weights['Avg_Value_per_mile']+
    scaled_df['youSaveSpend'] * weights['youSaveSpend']+
    scaled_df['ROLLOVER_STARS'] * weights['ROLLOVER_STARS']
)

ranked_cars = merged_df.copy()
ranked_cars['utility_score'] = scaled_df['utility_score']
ranked_cars = ranked_cars.sort_values(by='utility_score', ascending=False)

# print(ranked_cars.head(20))

# export data to output folder
final = get_data.export("output","ranked.csv")
# ranked_cars.to_csv(final, index=False)

# ========================== VISUALIZATION ==========================
import seaborn as sns
import matplotlib.pyplot as plt

# filter duplicates and drop rows with missing values
ranked_cars = ranked_cars.dropna(subset=['car_key', 'utility_score'])
ranked_cars = ranked_cars.drop_duplicates(subset=['car_key'])

top_cars = ranked_cars.head(10).round(1)

# bar graph ==========================
plt.figure(figsize=(12,6))
sns.barplot(data=top_cars, x='car_key', y='utility_score')
plt.title('Top 10 Cars by Utility Score')

# rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
# plt.show()

# export graph to output folder
barchart = get_data.export("output","ranked.png")
# plt.savefig(barchart)

# table ==========================
fig, ax = plt.subplots(figsize=(23,5))
ax.axis('off')  # hide axes

# create
table = ax.table(
    cellText=top_cars.values,
    colLabels=top_cars.columns,
    cellLoc='center',
    loc='center')

# style
table.auto_set_font_size(False)
table.set_fontsize(7)

# export table to output folder
tbl = get_data.export("output","table.png")
plt.savefig(tbl, bbox_inches='tight', dpi=300)
