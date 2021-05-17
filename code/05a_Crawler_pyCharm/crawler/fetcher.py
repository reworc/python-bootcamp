from typing import Optional, Iterator

import requests
import time
import csv


from bs4 import BeautifulSoup
from urllib.parse import urljoin

from crawler import CrawledArticle


class ArticleFetcher:
    def __init__(self, main_page_url: str) -> None:
        self.__mainPageUrl = main_page_url
        self.__pages = {}
        self.__articles = []

    def __extract_doc(self, page_url: str) -> BeautifulSoup:
        r = requests.get(page_url)
        doc = BeautifulSoup(r.text, "html.parser")

        self.__pages[page_url] = doc
        return doc

    @staticmethod
    def __get_next_page_url(page_url: str, doc: BeautifulSoup) -> Optional[str]:
        nav = doc.select(".navigation a")
        if len(nav) == 1:
            return urljoin(page_url, nav[0].attrs["href"])
        else:
            return None

    @staticmethod
    def __fetch(doc: BeautifulSoup, page_url: str) -> Iterator[CrawledArticle]:

        for card in doc.select(".card"):
            emoji = card.select_one(".emoji").text
            content = card.select_one(".card-text").text
            title = card.select(".card-title span")[1].text
            img = urljoin(page_url, card.select_one("img").attrs["src"])

            yield CrawledArticle(title, emoji, content, img)

    def fetch__all__pages(self) -> Iterator[Iterator[CrawledArticle]]:
        url = self.__mainPageUrl

        while url is not None:
            doc = self.__extract_doc(url)
            print(f'fetch url: {url}')
            time.sleep(1)
            yield self.__fetch(doc, url)

            url = self.__get_next_page_url(url, doc)

    def write_to_file(self, file_name: str, num_articles: int) -> None:

        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["emoji", "title", "content", "image"])

            pages = self.fetch__all__pages()

            count = 0

            art_array = ([a.emoji, a.title, a.content, a.image] for pg in pages for a in pg)
            for art in art_array:
                count += 1
                if count > num_articles:
                    break

                writer.writerow(art)

    @staticmethod
    def read_from_file(file_name: str) -> list[CrawledArticle]:

        with open(file_name, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';', quotechar='"')
            result = [CrawledArticle(row[1], row[0], row[2], row[3]) for row in reader]
            del result[0]
            return result
