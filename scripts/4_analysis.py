import pandas as pd
import get_data

pd.set_option('display.max_columns', None)

filtered_df = get_data.find("filtered_govdata.csv")
agg_df = get_data.find("agg_data.csv")

if filtered_df is None or agg_df is None:
    print("Whoops! Couldn't find the files you were looking for. Please check the spelling and try again.")
    exit()

# ========================== STANDARDIZATION ==========================
    # check field names to see what you can use as a key

# merging the fields on the new key
merged_df = pd.merge(filtered_df, agg_df, on='car_key', how='outer')

# ========================== RANKING ==========================
# deleting duplicate fields
merged_df = (
    merged_df.drop(columns=['make', 'model', 'year','baseModel','VClass','guzzler'])
             .sort_values(['OVERALL_STARS','Avg_Value_per_mile','comb08'],
                ascending=[False,False,False])
)
merged_df = merged_df[[
    'car_key',
    'OVERALL_STARS',
    'NUM_OF_SEATING',
    'comb08',
    'Avg_Value_per_mile',
    'Avg_Price',
    'Avg_Mileage',
    'youSaveSpend',
    'Nr_Available',
    'BODY_STYLE',
    'VEHICLE_TYPE',
    'DRIVE_TRAIN',
    'cylinders',
    'fuelType',
    'trany',
    'ROLLOVER_POSSIBILITY',
    'ROLLOVER_STARS']]
# print(merged_df.head(20))

# export data to output folder
final = get_data.export("output","ranked.csv")
merged_df.to_csv(final, index=False)