import unittest
from main import checkpolz
from main import checkfile
from main import checkurl


class TestCheck(unittest.TestCase):
    def testuserstrinvalid(self):
        result = checkpolz("123-123-12-00")
        self.assertEqual(result, "Коректных снилсов нет")

    def testuservalid(self):
        result = checkpolz("123-123-124 00 и 456-456-789 12")
        self.assertEqual(result, ["123-123-124 00", "456-456-789 12"])

    def testuserstrempty(self):
        result = checkpolz("")
        self.assertEqual(result, "Коректных снилсов нет")

    def testuserfile(self):
        result = checkfile("1.txt")
        self.assertEqual(result, ["123-123-123 11"])

    def testuserurl(self):
        result = checkurl("https://en.wikipedia.org/wiki/SNILS_(Russia)")
        self.assertEqual(result, ["123-456-789 12"])


