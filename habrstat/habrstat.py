import re
import pymorphy2
import itertools
import datetime
from habr_parser import fetch_raw_habr_pages, parse_habr_page

morph = pymorphy2.MorphAnalyzer()

DAY_IN_WEAK = 6
today = datetime.datetime.now()

def flat_list(_list):
    return list(itertools.chain(*_list))


def calculate_word_stat():
    pass


def output_stat():
    pass


def get_nouns_from_words(words):
    nouns = [morph.parse(word)[0].normal_form for word in words
             if len(word) > 2 and morph.parse(word)[0].tag.POS == 'NOUN']
    return nouns


def main():
    raw_pages = fetch_raw_habr_pages(pages=30)
    articles_info = []
    for raw_page in raw_pages:
        articles_info += parse_habr_page(raw_page)

    lower_letters_regex = re.compile('[^a-zа-я]')

    nouns_by_week = []
    day_end_week, day_start_week = None, None
    week_number = None
    for article in articles_info:
        print(article['date'].isocalendar())
        article_week_number = article['date'].isocalendar()[1]
        if week_number is None or article_week_number != week_number:
            # @TODO Add flatten list to list.
            # time_delta = 
            week_number = article_week_number
        print(article_week_number)
        words_string = '{} {}'.format(article['title'], article['preview'])
        words_string = words_string.lower().strip()
        current_words = lower_letters_regex.sub(
            ' ',
            words_string
        ).split()

        nouns = get_nouns_from_words(current_words)
        # print(article['date'], nouns)
        # current_article_words = []
    # world_stat = calculate_word_stat(articles_info)
    # get_nouns_from_pages()
    # count_stat_for_nouns()
    output_stat()


if __name__ == '__main__':
    main()
