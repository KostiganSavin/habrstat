from habr_parser import fetch_raw_habr_pages, parse_habr_page

def get_pages_from_habr():
    pass


def get_nouns_from_pages():
    pass


def count_stat_for_nouns():
    pass


def print_stat():
    pass


def main():
    raw_pages = fetch_raw_habr_pages(pages=10)
    articles_info = []
    for raw_page in raw_pages:
        articles_info += parse_habr_page(raw_page)
    world_stat = calculate_word_stat(articles_info)
    # get_nouns_from_pages()
    # count_stat_for_nouns()
    output_stat()


if __name__ == '__main__':
    main()
