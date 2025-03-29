import sys
import os
import pandas as pd

sys.path.append('.')

import bin.normalize_csv

def test_normalize_csv():
	test_file = "test_data.csv"
	df = pd.DataFrame({
		"Symbol": ["AAPL", "GOOGL"],
		"Price": ["150.00", "2800.50"],
		"Change": ["+2.50", "-15.30"],
		"Change %": ["+1.5%", "-0.5%"]
	})
	df.to_csv(test_file, index=False)
	bin.normalize_csv.normalize_csv(test_file)
	assert pd.read_csv("test_data_norm.csv").shape[0] > 0
	output_df = pd.read_csv("test_data_norm.csv")
	assert list(output_df.columns) == ["symbol", "price", "price_change", "price_percent_change"]
	assert all(isinstance(val, float) for val in output_df["price"])
	assert all(isinstance(val, float) for val in output_df["price_percent_change"])

	os.remove("test_data.csv")
	os.remove("test_data_norm.csv")
