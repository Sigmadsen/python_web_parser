import abc
import requests
import time

from collections import Counter


class AbstractParser:
    EXCLUDED = ['Dr.', 'Prof.', 'DVM', 'II', 'Mr.', 'Mrs.', 'Sr.', 'Jr.', 'V', 'DDS', 'IV', 'I', 'III', 'PhD', 'Miss',
                'MD', 'Ms.']

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_name(self):
        """Method implementation"""
        return

    def get_names(self, count):
        result = []
        with requests.Session() as s:
            while len(result) < count:
                name = self.get_name(s)
                result.append(name)
        return result

    def get_count_of_unique_items(self, list_of_pieces):
        counts = Counter(list_of_pieces)
        for item in self.EXCLUDED:
            if counts[item]:
                del counts[item]
        return counts

    def print_final_result(self, count):
        start_time = time.time()
        list_of_names = self.get_names(count)
        list_of_pieces = self.break_names_to_pieces(list_of_names)
        result = self.get_count_of_unique_items(list_of_pieces)
        self.print_top_ten_frequently_appearing_words(result)
        print("--- %s seconds ---" % (time.time() - start_time))

    @staticmethod
    def break_names_to_pieces(list_of_names):
        result = []
        for full_name in list_of_names:
            result += full_name.split(" ")
        return result

    @staticmethod
    def print_top_ten_frequently_appearing_words(collection_with_words):
        for word, frequency in collection_with_words.most_common()[:10]:
            print(word, frequency)
