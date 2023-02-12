from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):

    def test_multiply_numbers(self):

        res = calc.multiply(2, 51)

        self.assertEqual(res, 102)

    def test_difference(self):

        res = calc.difference(24, 41)

        self.assertEqual(res, 17)
