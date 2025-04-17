import pandas as pd
import get_data

pd.set_option('display.max_columns', None)

safety_df = get_data.find("NHTSA.csv")
fuel_df = get_data.find("vehicles.csv")

if safety_df is None or fuel_df is None:
    print("Whoops! Couldn't find the files you were looking for. Please check the spelling and try again.")
    exit()

# ========================== STANDARDIZATION ==========================
    # check field names to see what you can use as a key

# make a merged column to act as the key
safety_df['car_key'] =(
        safety_df['MODEL_YR'].map(str) + ' ' + safety_df['MAKE'].map(str.upper) + ' ' + safety_df['MODEL'].map(str.upper))
fuel_df['car_key'] =(
        fuel_df['year'].map(str) + ' ' + fuel_df['make'].map(str.upper) + ' ' + fuel_df['baseModel'].map(str.upper))

    # check the field names to see if it worked (comment out after confirming)
# print(safety_df.columns)
# print(fuel_df.columns)

# merging the fields on the new key
merged_df = pd.merge(safety_df, fuel_df, on='car_key', how='outer')

# deleting duplicate fields
merged_df = merged_df.drop(columns = ['MAKE','MODEL','MODEL_YR'])

    # check if it worked (comment out after confirming)
# print(merged_df)

    # export merged data to output folder to check the output
# checker = get_data.export("output","merged_data.csv")
# merged_df.to_csv(checker, index=False)

# ========================== FILTERING ==========================
merged_df = merged_df[
    (merged_df['DRIVE_TRAIN'].str.contains(r"\bAWD\b|\b4WD\b|\b4x4\b", case=False, na=False)) &
# safety rating
    (merged_df['OVERALL_STARS'].between(4, 5)) &
# combined mpg
    (merged_df['comb08'] > 22) &
# includes gas & hybrid
    (merged_df['fuelType'].str.contains("Regular", case=False, na=False)) &
    (merged_df['VClass'].str.contains(r"\bSUV\b|\bSport Utility Vehicle\b", case=False, na=False)) &
    (merged_df['year'].between(2017, 2024)) &
# gas tax by EPA
    (~merged_df['guzzler'].str.contains("G|T", case=False, na=False))
]

# Data integrity - check for expected columns. This line was written with the help of ChatGPT
expected_columns = ['DRIVE_TRAIN','OVERALL_STARS','comb08', 'fuelType', 'VClass', 'year', 'guzzler']
if not all(col in merged_df.columns for col in expected_columns):
    print(f"Missing columns: {set(expected_columns) - set(merged_df.columns)}")
    exit()

    # export cleaned data to output folder
# filtered = get_data.export("output","filtered_data.csv")
# merged_df.to_csv(filtered, index=False)