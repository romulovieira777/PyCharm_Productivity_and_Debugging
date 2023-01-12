from unittest import TestCase


class MathTest(TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)

    def test_subtract(self):
        self.assertEqual(2 - 1, 1)

    def test_multiply(self):
        self.assertEqual(2 * 2, 4)

    def test_divide(self):
        self.assertEqual(4 / 2, 2)

    def test_fail(self):
        self.assertEqual(4 / 2, 4)


class StringTest(TestCase):
    def test_stringcase(self):
        self.assertEqual('FOO'.isupper(), True)
        self.assertEqual('Bar'.isupper(), False)
