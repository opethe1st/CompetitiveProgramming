import unittest
from SeperateTheNumbers import *
class Tests(unittest.TestCase):
    def test_zeroes(self):
        self.assertEqual(isBeautiful('010203')[0],False)