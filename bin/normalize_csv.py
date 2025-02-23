import pandas as pd
import sys
import re

def normalize_csv(input_file):
	df = pd.read_csv(input_file)
	assert not df.empty, f"Error: {input_file} is empty."
	if 'Symbol' in df.columns and 'Price' in df.columns and 'Change' in df.columns:
		df = df[['Symbol', 'Price', 'Change', 'Change %']].copy()
		df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
		df['price'] = df['price'].astype(str).apply(lambda x: re.split(r'[\s+]', x)[0]).astype(float)
		df['price_change'] = df['price_change'].astype(str).str.replace(',', '').astype(float)
		df['price_percent_change'] = df['price_percent_change'].astype(str).str.rstrip('%').astype(float)
		assert not df['price'].isnull().all(), "Error: 'price' column is empty."
	elif 'Unnamed: 0' in df.columns and 'Last' in df.columns and 'Chg' in df.columns:
		df = df[['Unnamed: 0', 'Last', 'Chg', '% Chg']].copy()
		df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
		df['price'] = df['price'].astype(float)
		df['price_change'] = df['price_change'].astype(float)
		df['price_percent_change'] = df['price_percent_change'].astype(float)
		assert not df['price'].isnull().all(), "Error: 'price' column is empty."
	else:
		print(f"Error: Unrecognized format in {input_file}")
		return
	assert not df.empty, f"Error: Processed dataframe for {input_file} is empty before saving."
	output_file = input_file.replace('.csv', '_norm.csv')
	df.to_csv(output_file, index=False)
	print(f"Normalized file saved: {output_file}")

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: python bin/normalize_csv.py <input_csv>")
		sys.exit(1)
	input_csv = sys.argv[1]
	normalize_csv(input_csv)
