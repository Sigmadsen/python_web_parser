import time
from collections import Counter

import requests

import json
import random

from bs4 import BeautifulSoup

from core.request.request_parser import RequestParser


class NamefakeParser(RequestParser):
    EXCLUDED = ['Dr.', 'Prof.', 'DVM', 'II', 'Mr.', 'Mrs.', 'Sr.', 'Jr.', 'V', 'DDS', 'IV', 'I', 'III', 'PhD', 'Miss',
                'MD', 'Ms.']
    api_url = 'http://api.namefake.com'
    web_url = 'https://namefake.com/'

    def get_count_of_unique_items(self, list_of_pieces):
        counts = Counter(list_of_pieces)
        for item in self.EXCLUDED:
            if counts[item]:
                del counts[item]
        return counts

    def make_request(self, session, url, timeout):
        try:
            time.sleep(timeout)
            response = session.get(url, verify=False, timeout=0.8)
            return response
        except requests.exceptions.ReadTimeout as e:
            print(e)
            return self.make_request(session, url, timeout)
        except requests.exceptions.ConnectionError as e:
            print(e)
            time.sleep(3)
            return self.make_request(session, url, timeout)

    def parse_name_by_api(self, count):
        list_of_names = []

        with requests.Session() as session:
            i = 0
            while i < count:
                timeout = random.uniform(0.04, 0.11)
                response = self.make_request(session, self.api_url, timeout)
                name = json.loads(response.text)['name']
                list_of_names.append(name)
                i += 1

        list_of_pieces = self.break_names_to_pieces(list_of_names)
        return self.get_count_of_unique_items(list_of_pieces)

    def parse_name_by_html(self, count):
        list_of_names = []

        with requests.Session() as session:
            i = 0
            while i < count:
                timeout = random.uniform(0.04, 0.11)
                response = self.make_request(session, self.web_url, timeout)

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

                list_of_names.append(list_of_raw_names[0])
                i += 1

        list_of_pieces = self.break_names_to_pieces(list_of_names)
        return self.get_count_of_unique_items(list_of_pieces)

    @staticmethod
    def print_top_ten_frequently_appearing_words(collection_with_words):
        for word, frequency in collection_with_words.most_common()[:10]:
            print(word, frequency)

    @staticmethod
    def break_names_to_pieces(list_of_names):
        result = []
        for full_name in list_of_names:
            result += full_name.split(" ")
        return result
