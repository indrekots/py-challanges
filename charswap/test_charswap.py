import unittest
from charswap import charswap

class TestCharswap(unittest.TestCase):

    def test_input(self):
        self.assertEqual(charswap("hello"), "oellh")

    def test_zero_length_input(self):
        self.assertEqual(charswap(""), "")

    def test_single_char_input(self):
        self.assertEqual(charswap("a"), "a")

    def test_number_input(self):
        self.assertEqual(charswap(3), "3")


