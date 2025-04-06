from abc import ABC, abstractmethod

# DOWNLOADER
"""docstring"""

class GainerDownload(ABC):
	"""docstring"""
	def __init__(self, url=None):
		"""docstring"""
		self.url = url

	@abstractmethod
	def download(self):
		"""docstring"""
		pass

class GainerProcess(ABC):
	"""docstring"""
	def __init__(self):
		"""docstring"""
		pass

	@abstractmethod
	def normalize(self):
		"""docstring"""
		pass

	@abstractmethod
	def save_with_timestamp(self):
		"""docstring"""
		pass

# PROCESSORS
class GainerProcess(ABC):
	"""docstring"""
	def __init__(self):
		"""docstring"""
		pass

	@abstractmethod
	def normalize(self):
		"""docstring"""
		pass

	@abstractmethod
	def save_with_timestamp(self):
		"""docstring"""
		pass


# TEMPLATE
class ProcessGainer:
	"""docstring"""
	def __init__(self, gainer_downloader, gainer_normalizer):
		"""docstring"""
		self.downloader = gainer_downloader
		self.normalizer = gainer_normalizer

	def _download(self):
		"""docstring"""
		self.downloader.download()

	def _normalize(self):
		"""docstring"""
		self.normalizer.normalize()

	def _save_to_file(self):
		"""docstring"""
		self.normalizer.save_with_timestamp()

	def process(self):
		"""docstring"""
		self._download()
		self._normalize()
		self._save_to_file()
