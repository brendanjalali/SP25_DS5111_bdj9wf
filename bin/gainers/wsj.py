import sys
import re
import pandas as pd


class GainerDownloadWSJ(GainerDownload):
    def __init__(self):
        pass

    def download(self):
        print("Downloading WSJ gainers")


class GainerProcessWSJ(GainerProcess):
    def __init__(self):
        pass

    def normalize(self):
        print("Normalizing WSJ gainers")

    def save_with_timestamp(self):
        print("Saving WSJ gainers")
