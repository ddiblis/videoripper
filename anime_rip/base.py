# wafiq's comment
import os
import re
from urllib import parse

import requests
from bs4 import BeautifulSoup as BS



class WebPage:
    def __init__(self, url):
        self._resp = None
        self._soup = None
        self.url = url

    @property
    def resp(self):
        if self._resp is None:
            self._resp = requests.get(self.url)
        return self._resp

    @property
    def soup(self):
        if self._soup is None:
            self._soup = BS(self.resp.text, "html.parser")
        return self._soup


class Episodes(WebPage):
    base_url = ""

    def __init__(self, name):
        self._episode_list = None
        self.name = name.replace("-", " ")
        super().__init__(self.base_url.format(name))

    @abstractmethod
    def enumerate_episodes(self):
        pass

    @property
    def episode_list(self):
        if self._episode_list is None:
            self._episode_list = self.enumerate_episodes()
        return self._episode_list

    def generate_episode(self, url):
        pass

    def episodes(self):
        return [self.generate_episode(ep) for ep in self.episode_list]