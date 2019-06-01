import json
import requests
import timeit
from requests.adapters import HTTPAdapter
from urllib3.util import Retry


def get_name(url, session):
    print(3)

    resp = session.get(url)

    data_json = json.loads(resp.text)
    return data_json['name']


def get_names(count=1):
    print(2)
    result = []
    url = 'http://api.namefake.com'

    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    for idx in range(count):
        print(idx)
        name = get_name(url, session)
        print(idx, '---', name)
        result.append(name)
    print(result)
    return result


if __name__ == '__main__':
    print(1)
    # 37 second / 53 second
    # time = timeit.timeit('get_names(100)', 'from __main__ import get_names', number=1)
    # print(time)
    # timeit.timeit(get_names(5))
    names = get_names(100)
    print(names)
