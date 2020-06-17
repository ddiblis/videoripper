import re
from urllib import parse

import requests
import youtube_dl
from bs4 import BeautifulSoup as BS


# If a link hasn't been requested, request one and grab html
class WebPage:
    def __init__(self, url):
        self._response = None
        self._soup = None
        self.url = url

    @property
    def resp(self):
        if self._response is None:
            self._response = requests.get(self.url)
        return self._response

    @property
    def soup(self):
        if self._soup is None:
            self._soup = BS(self.resp.text, "html.parser")
        return self._soup


class Pages(WebPage):
    def __init__(self, name):
        self.name = name
        self._link_list = None
        super().__init__(self.url)

    @property
    def info(self):
        pass

    @property
    def get_links(self):
        pass

    def downloadlinks(self):
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(self.get_links)