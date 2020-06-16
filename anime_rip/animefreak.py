# wafiq's comment
import re
from urllib import parse

from . import base


websitename = "https://www.animefreak.tv/"

class Episodes(base.Episodes):
    base_url = "https://www.animefreak.tv/{}"
    tags = ["animefreak", "af"]

    def enumerate_episodes(self):
        episodes = self.soup.select(".check-list a")
        return [
            parse.urljoin(websitename, episode.attrs["href"])
            for episode in episodes
        ]

    def generate_episode(self, url):
        return Episode(url)