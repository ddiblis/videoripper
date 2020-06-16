import re
from urllib import parse

import requests
import youtube_dl
from bs4 import BeautifulSoup as BS


base_url = "https://www.animefreak.tv"
tags = ["animefreak", "AF"]


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
        url = parse.urljoin(base_url, f"watch/{name}")
        super().__init__(url)

    @property
    def info(self):
        return re.search(r".tv/watch/(?P<series>[^/]*)", self.url)

    @property
    def get_links(self):
        if self._link_list is None:
            self._link_list = [
                link["href"]
                for link in self.soup("div", class_="tnContent")[1]("a")[::-1]
            ]
        return self._link_list

    def downloadlinks(self):
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(self.get_links)