import unittest
from charswap import charswap

class TestCharswap(unittest.TestCase):

    def test_input(self):
        self.assertEqual(charswap("hello"), "hello")

    def test_zero_length_input(self):
        self.assertEqual(charswap(""), "")

    def test_single_char_input(self):
        self.assertEqual(charswap("a"), "a")


