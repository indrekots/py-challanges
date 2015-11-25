import unittest
from dictToString import dictToString

class TestDictToString(unittest.TestCase):

    def test_simple_dictionary(self):
        self.assertEqual(dictToString({'test1':1}), 'test1=1;')

    def test_with_none_value(self):
        self.assertEqual(dictToString({'test1':1, 'test2':None}), 'test1=1;')

    def test_longer_input(self):
        self.assertEqual(dictToString({'test1':1, 'test2':2}), 'test1=1;test2=2;')

    def test_one_none_value(self):
        self.assertEqual(dictToString({'test':None}), '')