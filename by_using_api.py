import json
import requests
import time
from user_agent import generate_user_agent


def get_name(session):
    url = 'http://api.namefake.com'
    headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
    try:
        resp = session.get(url, verify=False, timeout=0.8)
    except requests.exceptions.ReadTimeout as e:
        print(e)
        return get_name(session)
    except requests.exceptions.ConnectionError as e:
        print(e)
        time.sleep(3)
        return get_name(session)
    return json.loads(resp.text)['name']


def get_names(count):
    result = []

    with requests.Session() as s:
        while len(result) < count:
            name = get_name(s)
            result.append(name)
    return result


if __name__ == '__main__':
    # Using api is slower than parsing html page

    start_time = time.time()
    r = get_names(100)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(r)

