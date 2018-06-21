import requests
import datetime
from bs4 import BeautifulSoup
from dateparser import parse


def fetch_raw_habr_pages(pages=10):
    raw_pages = []
    for page_num in range(pages):
        raw_pages.append(_fetch_raw_habr_page(page_num=page_num))
    return raw_pages


def parse_habr_page(raw_page):
    article_info = []

    soup = BeautifulSoup(raw_page, "html.parser")
    for article_block in soup.find_all(
            'article',
            {'class': 'post_preview'}):
        raw_article_date = article_block.find('span', {'class': 'post__time'})
        title_link = article_block.find('a', {'class': 'post__title_link'})
        text_block = article_block.find('div', {'class': 'post__text'})
        article_date = parse(raw_article_date.text, languages=['ru'])
        article_info.append({
            'date': article_date.date(),
            'title': title_link.contents[0],
            'preview': text_block.text.replace('\n', '').replace('\r', ' ')
        })
    return article_info


def _fetch_raw_habr_page(page_num=None):
    url = "https://habr.com/all/"
    if page_num:
        url += "page{}/".format(page_num)
    return requests.get(url).text
