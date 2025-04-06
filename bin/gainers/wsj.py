import sys
import re
import pandas as pd
from bin.gainers.base import GainerDownload, GainerProcess

class GainerDownloadWSJ(GainerDownload):
	def __init__(self):
		super().__init__('~/SP25_DS5111_bdj9wf/data/wsjgainers.html')

	def download(self):
		print("Downloading WSJ gainers")
		raw = pd.read_html('data/wsjgainers.html')
		raw[0].to_csv('data/wsjgainers.csv')
		return raw


class GainerProcessWSJ(GainerProcess):
	def __init__(self):
		self.csv = 'data/wsjgainers.csv'

	def normalize(self):
		print("Normalizing WSJ gainers")
		df = pd.read_csv(self.csv)
		assert not df.empty, f"Error: {input_file} is empty."
		if 'Unnamed: 0' in df.columns and 'Last' in df.columns and 'Chg' in df.columns:
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
		output_file = self.csv.replace('.csv', '_norm.csv')
		df.to_csv(output_file, index=False)
		print(f"Normalized file saved: {output_file}")
		return df


	def save_with_timestamp(self):
		time = pd.to_datetime('now').strftime("%Y%m%d_%H%M%S")
		wsjgainers_norm = self.normalize()
		wsjgainers_norm.to_csv(f'data/wsjgainers_norm{time}.csv')
		print("Saving WSJ gainers")
