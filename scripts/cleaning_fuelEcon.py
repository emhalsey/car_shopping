import get_data

df = get_data.find("vehicles.csv")

if df is None:
    print("Failed to load data. Exiting the script.")
    exit ()

# Filter the values
    # comb08 is the combined mpg & trany is the transmission type
    # guzzler is a "gas guzzler" tax created by the EPA - we don't want that!
df = df[
    (df['comb08'] > 22) &
    (df['drive'].str.contains(r"\b4-Wheel\b|\All-Wheel Drive\b", case=False, na=False)) &
    (df['fuelType'].str.contains("Regular", case=False, na=False)) &
    (df['trany'].str.contains(r"\bAutomatic\b", case=False, na=False)) &
    (df['VClass'].str.contains(r"\bSUV\b|\bSport Utility Vehicle\b", case=False, na=False)) &
    (df['year'].between(2017, 2024)) &
    (~df['guzzler'].str.contains("G|T", case=False, na=False))
]


# Data integrity - check for expected columns. This line was written with the help of ChatGPT
expected_columns = ['comb08', 'drive', 'fuelType', 'trany', 'VClass', 'year', 'guzzler']
if not all(col in df.columns for col in expected_columns):
    print(f"Missing columns: {set(expected_columns) - set(df.columns)}")
    exit()


# export cleaned data to output folder
cleaned = get_data.export("data","cleaned_fuelEcon.csv")
df.to_csv(cleaned, index=False)