import pandas as pd
from pathlib import Path

def get_data(file_name: str):
    # Building the file path. This line was written with the help of ChatGPT
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

df = get_data("vehicles.csv")

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

# Build the file path to ensure it is relative to the script location. This line was written with the help of ChatGPT
final_path = Path(__file__).parent.parent / "data" / "cleaned_data.csv"

# Save the cleaned data
df.to_csv(final_path, index=False)