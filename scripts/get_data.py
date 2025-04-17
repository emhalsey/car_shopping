import pandas as pd
from pathlib import Path

def find(file_name: str):
    # Building the file path
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


def findclean(file_name: str):
    # Building the file path
    data_path = Path(__file__).parent.parent / "output" / file_name

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

def export(folder_name:str, file_name: str):
    # Building the file path
    data_path = Path(__file__).parent.parent / folder_name / file_name
    return data_path