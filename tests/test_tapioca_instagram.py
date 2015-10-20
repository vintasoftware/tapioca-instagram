# coding: utf-8

import unittest

from tapioca_instagram import Instagram


class TestTapiocaInstagram(unittest.TestCase):

    def setUp(self):
        self.wrapper = Instagram()


if __name__ == '__main__':
    unittest.main()
