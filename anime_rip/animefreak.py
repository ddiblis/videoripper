import re
from urllib import parse

import requests
import youtube_dl
from bs4 import BeautifulSoup as BS

from . import base


class Pages(base.Pages):
    base_url = "https://www.animefreak.tv"
    tags = ["animefreak", "AF"]

    def __init__(self, name):
        self.name = name
        url = parse.urljoin(self.base_url, f"watch/{name}")
        super().__init__(name, url)
        
    @property
    def info(self):
        return re.search(r".tv/watch/(?P<series>[^/]*)", self.url)

    @property
    def get_links(self):
        if self._link_list is None:
            soup = self.soup
            self._link_list = [
                link["href"]
                for link in soup("div", class_="tnContent")[1]("a")[::-1]
            ]
        return self._link_list