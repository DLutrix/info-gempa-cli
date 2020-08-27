import requests
from xml.etree import ElementTree


class Base:
    def __init__(self, url):
        self.response = requests.get(url)
        self.root = ElementTree.fromstring(self.response.content)
        self.date = []
        self.time = []
        self.coordinates = []
        self.lat = []
        self.long = []
        self.magnitude = []
        self.depth = []
        self.location = []
        self.data = []