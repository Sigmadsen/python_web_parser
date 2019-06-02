import requests
from bs4 import BeautifulSoup
import time


def get_name(session):
    url = 'https://namefake.com/'
    try:
        time.sleep(0.07)
        response = session.get(url, timeout=0.65)
        print('resp')
    except requests.exceptions.ReadTimeout as e:
        print(e)
        return get_name(session)
    except requests.exceptions.ConnectionError as e:
        print(e)
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


if __name__ == '__main__':
    start_time = time.time()
    r = get_names(100)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(r)

