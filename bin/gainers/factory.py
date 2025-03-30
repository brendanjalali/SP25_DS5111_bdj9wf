from abc import ABC, abstractmethod
from wsj import GainerDownloadWSJ, GainerProcessWSJ
from yahoo import GainerDownloadYahoo, GainerProcessYahoo

# FACTORY
class GainerFactory:
	"""FACTORY"""
	def __init__(self, choice):
		assert choice in ['yahoo', 'wsj', 'test'], f"Unrecognized gainer type {choice}"
		self.choice = choice

	def get_downloader(self):
	# trigger off url to return correct downloader
		if self.choice == 'yahoo':
			return GainerDownloadYahoo()
		elif self.choice == 'wsj':
			return GainerDownloadWSJ()

	def get_processor(self):
	# trigger off url to return correct downloader
		if self.choice == 'yahoo':
			return GainerProcessYahoo()
		elif self.choice == 'wsj':
			return GainerProcessWSJ()
