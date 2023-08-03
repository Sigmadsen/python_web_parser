import time
from parsers.namefake_parser import NamefakeParser


if __name__ == '__main__':
    parser = NamefakeParser()

    start_time = time.time()
    result_by_api_data = parser.parse_name_by_api(10)
    NamefakeParser().print_top_ten_frequently_appearing_words(result_by_api_data)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    result_by_html_data = parser.parse_name_by_html(10)
    NamefakeParser().print_top_ten_frequently_appearing_words(result_by_html_data)
    print("--- %s seconds ---" % (time.time() - start_time))
