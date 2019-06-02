import random

import requests
import time

from collections import Counter
from bs4 import BeautifulSoup

EXCLUDED = ['Dr.', 'Prof.', 'DVM', 'II', 'Mr.', 'Mrs.', 'Sr.', 'Jr.', 'V', 'DDS', 'IV', 'I', 'III', 'PhD', 'Miss', 'MD',
            'Ms.']


def get_name(session):
    url = 'https://namefake.com/'
    timeout_between_request = random.uniform(0.04, 0.11)
    try:
        time.sleep(timeout_between_request)
        response = session.get(url, timeout=0.65)
    except requests.exceptions.ReadTimeout as e:
        return get_name(session)
    except requests.exceptions.ConnectionError as e:
        time.sleep(3)
        return get_name(session)

    soup_site_content = BeautifulSoup(response.text, "html.parser")

    content = soup_site_content.findAll(class_=['container', 'col-sm-9 col-sm-push-3'])

    list_of_raw_names = []

    for item in content:
        if item('h2'):
            raw_name_as_list = item('h2')[:1][0].get_text()
            full_name = raw_name_as_list
            if full_name in list_of_raw_names:
                continue
            list_of_raw_names.append(full_name)
    return list_of_raw_names[0]


def get_names(count):
    result = []
    with requests.Session() as s:
        while len(result) < count:
            name = get_name(s)
            result.append(name)
    return result


def break_names_to_pieces(list_of_names):
    result = []
    for full_name in list_of_names:
        result += full_name.split(" ")
    return result


def get_count_of_unique_items(list_of_pieces):
    counts = Counter(list_of_pieces)
    for item in EXCLUDED:
        if counts[item]:
            del counts[item]
    return counts


def print_top_ten_frequently_appearing_words(collection_with_words):
    for word, frequency in collection_with_words.most_common()[:10]:
        print(word, frequency)


if __name__ == '__main__':
    start_time = time.time()
    list_of_names = get_names(100)
    list_of_pieces = break_names_to_pieces(list_of_names)
    result = get_count_of_unique_items(list_of_pieces)
    print_top_ten_frequently_appearing_words(result)
    print("--- %s seconds ---" % (time.time() - start_time))
