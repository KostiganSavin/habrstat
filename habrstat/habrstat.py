from habr_parser import fetch_raw_habr_pages, parse_habr_page

def calculate_word_stat():
    pass


def output_stat():
    pass


def main():
    raw_pages = fetch_raw_habr_pages(pages=10)
    articles_info = []
    for raw_page in raw_pages:
        # print(raw_page)
        articles_info += parse_habr_page(raw_page)
        print(articles_info)
    # world_stat = calculate_word_stat(articles_info)
    # get_nouns_from_pages()
    # count_stat_for_nouns()
    output_stat()


if __name__ == '__main__':
    main()
