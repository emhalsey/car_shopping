import get_data

df = get_data.find("NHSTA_data.csv")

if df is None:
    print("Failed to load data. Exiting the script.")
    exit ()

# Filter the values
df = df[
    (df['ROLLOVER_STARS'].equals(5)) &
    (df['OVERALL_STARS'].between(4, 5)) &
    (df['BODY_STYLE'].str.contains(r"\bSUV\b|\bSport Utility Vehicle\b", case=False, na=False)) &
    (df['MODEL_YR'].between(2017, 2024)) &
    (~df['HEAD_SAB_MEET_REQUIREMENTS'].str.contains("Yes", case=False, na=False))
]


# Data integrity - check for expected columns. This line was written with the help of ChatGPT
expected_columns = ['ROLLOVER_STARS', 'OVERALL_STARS', 'BODY_STYLE', 'MODEL_YR', 'HEAD_SAB_MEET_REQUIREMENTS']
if not all(col in df.columns for col in expected_columns):
    print(f"Missing columns: {set(expected_columns) - set(df.columns)}")
    exit()


# export cleaned data to output folder
cleaned = get_data.export("data","cleaned_NHTSA.csv")
df.to_csv(cleaned, index=False)