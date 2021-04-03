import unittest
from time import sleep
from tests.exception_decorator import except_httperror
from geizhals import geizhals


class TestStringMethods(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.SLEEP_TIME = 30

    @except_httperror
    def test_URL_AT(self):
        # avoid banning from website
        sleep(self.SLEEP_TIME)
        id = geizhals._url2id(
            "https://geizhals.at/bose-quietcomfort-35-ii-schwarz-a1696985.html")

        self.assertEqual(id, "1696985")

    @except_httperror
    def test_URL_EU(self):
        # avoid banning from website
        sleep(self.SLEEP_TIME)
        id = geizhals._url2id(
            "https://geizhals.eu/bose-quietcomfort-35-ii-schwarz-a1696985.html")

        self.assertEqual(id, "1696985")

    @except_httperror
    def test_URL_DE(self):
        # avoid banning from website
        sleep(self.SLEEP_TIME)
        id = geizhals._url2id(
            "https://geizhals.de/bose-quietcomfort-35-ii-schwarz-a1696985.html")

        self.assertEqual(id, "1696985")

    @except_httperror
    def test_URL_UK(self):
        # avoid banning from website
        sleep(self.SLEEP_TIME)
        id = geizhals._url2id(
            "https://skinflint.co.uk/bose-quietcomfort-35-ii-black-a1696985.html")

        self.assertEqual(id, "1696985")

    @except_httperror
    def test_URL_PL(self):
        # avoid banning from website
        sleep(self.SLEEP_TIME)
        id = geizhals._url2id(
            "https://cenowarka.pl/bose-quietcomfort-35-ii-czarny-a1696985.html")

        self.assertEqual(id, "1696985")


if __name__ == '__main__':
    unittest.main()
