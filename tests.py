from abstract_parser import AbstractParser

import unittest


class TestStringMethods(unittest.TestCase):

    def test_break_names_to_pieces(self):
        list_of_names = ['Alan Smith', 'Johnnie Walker', 'Les Paul']
        self.assertEqual(AbstractParser.break_names_to_pieces(list_of_names),
                         ['Alan', 'Smith', 'Johnnie', 'Walker', 'Les', 'Paul'])
        with self.assertRaises(TypeError):
            AbstractParser.break_names_to_pieces(2)


if __name__ == '__main__':
    unittest.main()
