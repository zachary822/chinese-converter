import unittest

from chinese_converter import to_simplified, to_traditional


class TestTranslator(unittest.TestCase):
    def test_to_simplified(self):
        result = to_simplified('皇后與國王在後面共同候車吃麵')

        self.assertEqual(result, '皇后与国王在后面共同候车吃面')

    def test_to_traditional(self):
        result = to_traditional('皇后与国王在后面共同候车面食后')

        self.assertEqual(result, '皇后與國王在後面共同候車麵食後')

    def test_two_way(self):
        with self.subTest("should get same result when translated both ways"):
            trad = '皇后與國王在後面共同候車'
            result = to_traditional(to_simplified(trad))

            self.assertEqual(trad, result)

            simp = '皇后与国王在后面共同候车后'
            result = to_simplified(to_traditional(simp))

            self.assertEqual(simp, result)

    def test_other_language(self):
        text = "this is a book."

        with self.subTest("should not change text in other languages"):
            self.assertEqual(text, to_simplified(text))
            self.assertEqual(text, to_traditional(text))
