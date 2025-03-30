from factory import GainerFactory
from wsj import GainerDownloadWSJ, GainerProcessWSJ
from yahoo import GainerDownloadYahoo, GainerProcessYahoo

class ProcessGainer:
	__init__(self, gainer_downloader, gainer_normalizer):
		self.downloader = gainer_downloader
		self.normalizer = gainer_normalizer

	_def _download(self):
		self.downloader.download()

	_def _normalize(self):
		self.normalizer.normalize()

	_def _save_to_file(self):
		self.normalizer.save_with_timestamp()

	_def process(self):
		self._download()
		self._normalize()
		self._save_to_file()

if __name__=="__main__":
	# Our sample main file would look like this
	import sys

	# Make our selection, 'one' choice
	choice = sys.argv[1]

	# let our factory get select the family of objects for processing
	factory = GainerFactory(choice)
	downloader = factory.get_downloader()
	normalizer = factory.get_processor()

	# create our process
	runner = ProcessGainer(downloader, normalizer)
	runner.process()
