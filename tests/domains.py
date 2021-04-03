import unittest
from time import sleep
from tests.exception_decorator import except_httperror
from geizhals import Geizhals


class TestStringMethods(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.SLEEP_TIME = 30

    # test with ID
    @except_httperror
    def test_ID_AT(self):
        # avoid banning from website
        sleep(self.SLEEP_TIME)
        gh = Geizhals(1688629, "AT")
        device = gh.parse()

        self.assertEqual(device.name, "Apple iPhone X 64GB grau")

    @except_httperror
    def test_ID_EU(self):
        # avoid banning from website
        sleep(self.SLEEP_TIME)
        gh = Geizhals(1688629, "EU")
        device = gh.parse()

        self.assertEqual(device.name, "Apple iPhone X 64GB grau")

    @except_httperror
    def test_ID_DE(self):
        # avoid banning from website
        sleep(self.SLEEP_TIME)
        gh = Geizhals(1688629, "DE")
        device = gh.parse()

        self.assertEqual(device.name, "Apple iPhone X 64GB grau")

    @except_httperror
    def test_ID_UK(self):
        # avoid banning from website
        sleep(self.SLEEP_TIME)
        gh = Geizhals(1688629, "UK")
        device = gh.parse()

        self.assertEqual(device.name, "Apple iPhone X 64GB grey")

    @except_httperror
    def test_ID_PL(self):
        # avoid banning from website
        sleep(self.SLEEP_TIME)
        gh = Geizhals(1688629, "PL")
        device = gh.parse()

        self.assertEqual(device.name, "Apple iPhone X 64GB szary")

    # test with URL
    @except_httperror
    def test_URL_AT(self):
        # avoid banning from website
        sleep(self.SLEEP_TIME)
        gh = Geizhals(
            "https://geizhals.at/apple-iphone-x-64gb-grau-a1688629.html", "AT")
        device = gh.parse()

        self.assertEqual(device.name, "Apple iPhone X 64GB grau")

    @except_httperror
    def test_URL_EU(self):
        # avoid banning from website
        sleep(self.SLEEP_TIME)
        gh = Geizhals(
            "https://geizhals.eu/apple-iphone-x-64gb-grau-a1688629.html", "EU")
        device = gh.parse()

        self.assertEqual(device.name, "Apple iPhone X 64GB grau")

    @except_httperror
    def test_URL_DE(self):
        # avoid banning from website
        sleep(self.SLEEP_TIME)
        gh = Geizhals(
            "https://geizhals.de/apple-iphone-x-64gb-grau-a1688629.html", "DE")
        device = gh.parse()

        self.assertEqual(device.name, "Apple iPhone X 64GB grau")

    @except_httperror
    def test_URL_UK(self):
        # avoid banning from website
        sleep(self.SLEEP_TIME)
        gh = Geizhals(
            "https://cenowarka.pl/apple-iphone-x-64gb-szary-a1688629.html", "UK")
        device = gh.parse()

        self.assertEqual(device.name, "Apple iPhone X 64GB grey")

    @except_httperror
    def test_URL_PL(self):
        # avoid banning from website
        sleep(self.SLEEP_TIME)
        gh = Geizhals(
            "https://cenowarka.pl/apple-iphone-x-64gb-szary-a1688629.html", "PL")
        device = gh.parse()

        self.assertEqual(device.name, "Apple iPhone X 64GB szary")


if __name__ == '__main__':
    unittest.main()
