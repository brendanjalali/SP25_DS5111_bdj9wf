import re
import pandas as pd
from bin.gainers.base import GainerDownload, GainerProcess


"""docstring"""

class GainerDownloadYahoo(GainerDownload):
	"""docstring"""
	def __init__(self):
		"""docstring"""
		super().__init__('~/SP25_DS5111_bdj9wf/data/ygainers.html')

	def download(self):
		"""docstring"""
		print("Downloading yahoo gainers")
		raw = pd.read_html('data/ygainers.html')
		raw[0].to_csv('data/ygainers.csv')
		return raw


class GainerProcessYahoo(GainerProcess):
	"""docstring"""
	def __init__(self):
		"""docstring"""
		self.csv = 'data/ygainers.csv'

	def normalize(self):
		"""docstring"""
		print("Normalizing yahoo gainers")
		df = pd.read_csv(self.csv)
		assert not df.empty, f"Error: {self.csv} is empty."
		if 'Symbol' in df.columns and 'Price' in df.columns and 'Change' in df.columns:
			df = df[['Symbol', 'Price', 'Change', 'Change %']].copy()
			df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
			df['price'] = df['price'].astype(str).apply(lambda x: re.split(r'[\s+]', x)[0]).str.replace(',', '').astype(float)
			df['price_change'] = df['price_change'].astype(str).str.replace(',', '').astype(float)
			df['price_percent_change'] = df['price_percent_change'].astype(str).str.rstrip('%').astype(float)
			assert not df['price'].isnull().all(), "Error: 'price' column is empty."
		else:
			print(f"Error: Unrecognized format in {self.csv}")
			return
		assert not df.empty, f"Error: Processed dataframe for {self.csv} is empty before saving."
		output_file = self.csv.replace('.csv', '_norm.csv')
		df.to_csv(output_file, index=False)
		print(f"Normalized file saved: {output_file}")
		return df


	def save_with_timestamp(self):
		"""docstring"""
		time = pd.to_datetime('now').strftime("%Y%m%d_%H%M%S")
		ygainers_norm = self.normalize()
		ygainers_norm.to_csv(f'data/ygainers_norm{time}.csv')
		print("Saving yahoo gainers")
