from abc import ABC, abstractmethod

# DOWNLOADER
class GainerDownload(ABC):
	def __init__(self, url=None):
		self.url = url

	@abstractmethod
	def download(self):
		pass

class GainerProcess(ABC):
	def __init__(self):
		pass

	@abstractmethod
	def normalize(self):
		pass

	@abstractmethod
	def save_with_timestamp(self):
		pass

# PROCESSORS
class GainerProcess(ABC):
	def __init__(self):
		pass

	@abstractmethod
	def normalize(self):
		pass

	@abstractmethod
	def save_with_timestamp(self):
		pass


# TEMPLATE
class ProcessGainer:
	def __init__(self, gainer_downloader, gainer_normalizer):
		self.downloader = gainer_downloader
		self.normalizer = gainer_normalizer

	def _download(self):
		self.downloader.download()

	def _normalize(self):
		self.normalizer.normalize()

	def _save_to_file(self):
		self.normalizer.save_with_timestamp()

	def process(self):
		self._download()
		self._normalize()
		self._save_to_file()
