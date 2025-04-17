import pandas as pd

import get_data

pd.set_option('display.max_columns', None)

filtered_df = get_data.findclean("filtered_data.csv")
scraped_df = get_data.find("scraped_data.csv")

if filtered_df is None or scraped_df is None:
    print("Whoops! Couldn't find the files you were looking for. Please check the spelling and try again.")
    exit()

# ========================== STANDARDIZATION ==========================
    # check field names to see what you can use as a key

# make a merged column to act as the key
filtered_df['new_key'] =(
        filtered_df['year'].map(str) + ' ' + filtered_df['baseModel'].map(str.upper))
scraped_df['new_key'] =(
        scraped_df['year'].map(str) + ' ' + scraped_df['model'].map(str.upper))

    # check the field names to see if it worked (comment out after confirming)
# print(filtered_df.columns)
# print(scraped_df.columns)

# merging the fields on the new key
merged_df = pd.merge(filtered_df, scraped_df, on='new_key', how='outer')

# deleting duplicate fields
merged_df = (merged_df.drop(columns = ['year_y','baseModel'])
             .sort_values(['OVERALL_STARS','price','mileage'], ascending=[False,True,True]))

# export data to output folder
final = get_data.export("output","final_data.csv")
merged_df.to_csv(final, index=False)