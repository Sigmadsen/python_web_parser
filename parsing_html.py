import timeit
import requests
from bs4 import BeautifulSoup
import time


# WANTED_STRINGS = ['''<h1 style="font-size: 2rem;">Fake Name Generator</h1>''',]

def get_name(response):
    soup_site_content = BeautifulSoup(response.text, "html.parser")
    # site content
    # print(soup_site_content)

    content = soup_site_content.findAll(class_=['container', 'col-sm-9 col-sm-push-3'])

    # list_of_tags = []
    list_of_raw_finded_names = []

    for item in content:
        if item('h2'):
            raw_name_as_list = item('h2')[:1][0].contents
            full_name = raw_name_as_list[0]
            if full_name in list_of_raw_finded_names:
                continue
            list_of_raw_finded_names.append(full_name)
    return list_of_raw_finded_names[0]


def get_names(count):
    url = 'https://namefake.com/'
    result = []
    idx = 0
    while len(result) <= count:
        if idx % 5 == 0:
            time.sleep(0.2)
        try:
            response = requests.get(url)
            name = get_name(response)
            print(idx, '---', name)
            result.append(name)
        except requests.exceptions.ConnectionError as e:
            print(e)
        idx += 1
    return result


if __name__ == '__main__':
    # r = get_names(100)
    # print(r)
    time = timeit.timeit('get_names(100)', 'from __main__ import get_names', number=1)
    print(time)
    # print(get_names(100))
