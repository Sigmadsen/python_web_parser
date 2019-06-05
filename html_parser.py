import time
import random
import requests

from bs4 import BeautifulSoup
from abstract_parser import AbstractParser


class HtmlParser(AbstractParser):
    def get_name(self, session):
        url = 'https://namefake.com/'
        timeout_between_request = random.uniform(0.04, 0.11)
        try:
            time.sleep(timeout_between_request)
            response = session.get(url, timeout=0.65)
        except requests.exceptions.ReadTimeout as e:
            return self.get_name(session)
        except requests.exceptions.ConnectionError as e:
            time.sleep(3)
            return self.get_name(session)

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


if __name__ == '__main__':
    pass
