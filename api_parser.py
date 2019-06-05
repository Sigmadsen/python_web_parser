import requests
import time
import json
import random

from abstract_parser import AbstractParser


class ApiParser(AbstractParser):
    def get_name(self, session):
        url = 'http://api.namefake.com'
        timeout_between_request = random.uniform(0.04, 0.11)
        try:
            time.sleep(timeout_between_request)
            response = session.get(url, verify=False, timeout=0.8)
        except requests.exceptions.ReadTimeout as e:
            print(e)
            return self.get_name(session)
        except requests.exceptions.ConnectionError as e:
            print(e)
            time.sleep(3)
            return self.get_name(session)
        return json.loads(response.text)['name']


if __name__ == '__main__':
    pass
