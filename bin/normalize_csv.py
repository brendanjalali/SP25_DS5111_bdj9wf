import pandas as pd
import sys
import os

def validate_input(df):
    """Validate the input DataFrame structure."""
    expected_columns = {"Symbol", "Name", "Price", "Change", "Change %", "Volume", "Market Cap"}
    actual_columns = set(df.columns)
    
    assert expected_columns.issubset(actual_columns), f"Missing expected columns: {expected_columns - actual_columns}"
    assert df["Symbol"].notnull().all(), "Symbol column contains null values"
    assert df["Name"].notnull().all(), "Name column contains null values"
    assert df["Price"].notnull().all(), "Price column contains null values"

def clean_price_column(price_str):
    """Extract numeric price from strings like '49.88 +7.79 (+18.51%)'"""
    try:
        return float(price_str.split()[0])
    except ValueError:
        return None

def normalize_csv(input_file):
    """Normalize the given CSV file and clean necessary fields."""
    df = pd.read_csv(input_file)

    df["Price"] = df["Price"].astype(str).apply(clean_price_column)

    df = df.dropna(subset=["Price"])

    df["Price"] = df["Price"].astype(float)

    validate_input(df)

    output_file = os.path.splitext(input_file)[0] + "_norm.csv"
    df.to_csv(output_file, index=False)
    print(f"Normalized CSV saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python normalize_csv.py <input_csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    normalize_csv(input_file)
