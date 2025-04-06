from abc import ABC, abstractmethod
from bin.gainers.wsj import GainerDownloadWSJ, GainerProcessWSJ
from bin.gainers.yahoo import GainerDownloadYahoo, GainerProcessYahoo

# FACTORY
"""docstring"""

class GainerFactory:
	"""FACTORY"""
	def __init__(self, choice):
		"""docstring"""
		assert choice in ['yahoo', 'wsj', 'test'], f"Unrecognized gainer type {choice}"
		self.choice = choice

	def get_downloader(self):
		"""docstring"""
	# trigger off url to return correct downloader
		if self.choice == 'yahoo':
			return GainerDownloadYahoo()
		elif self.choice == 'wsj':
			return GainerDownloadWSJ()

	def get_processor(self):
		"""docstring"""
	# trigger off url to return correct downloader
		if self.choice == 'yahoo':
			return GainerProcessYahoo()
		elif self.choice == 'wsj':
			return GainerProcessWSJ()
