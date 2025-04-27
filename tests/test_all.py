import sys
import os
import pandas as pd
import pytest

sys.path.append('.')

import bin.normalize_csv

import get_gainer
from bin.gainers.base import GainerDownload, GainerProcess
from bin.gainers.factory import GainerFactory
from bin.gainers.wsj import GainerDownloadWSJ, GainerProcessWSJ
from bin.gainers.yahoo import GainerDownloadYahoo, GainerProcessYahoo

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

def test_get_gainers():
	factory = get_gainer.GainerFactory("yahoo")
	downloader = factory.get_downloader()
	processor = factory.get_processor()
	runner = get_gainer.ProcessGainer(downloader, processor)
	assert isinstance(runner, get_gainer.ProcessGainer)

def test_base():
	class DummyDownloader(GainerDownload):
		def download(self):
			pass

	class DummyProcessor(GainerProcess):
		def normalize(self):
			pass
		def save_with_timestamp(self):
			pass

	downloader = DummyDownloader("https://example.com")
	processor = DummyProcessor()
	assert isinstance(downloader, GainerDownload)
	assert isinstance(processor, GainerProcess)

def test_factory():
	factory = GainerFactory("wsj")
	downloader = factory.get_downloader()
	processor = factory.get_processor()
	assert isinstance(downloader, GainerDownloadWSJ)
	assert isinstance(processor, GainerProcessWSJ)

def test_wsj():
	downloader = GainerDownloadWSJ()
	processor = GainerProcessWSJ()
	assert isinstance(downloader, GainerDownload)
	assert isinstance(processor, GainerProcess)

def test_yahoo():
	downloader = GainerDownloadYahoo()
	processor = GainerProcessYahoo()
	assert isinstance(downloader, GainerDownload)
	assert isinstance(processor, GainerProcess)
