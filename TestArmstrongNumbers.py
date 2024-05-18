import unittest
from ArmstrongNumbers import is_armstrong_number


class TestArmstrongNumbers(unittest.TestCase):

    def test_single_digit_numbers(self):
        self.assertTrue(is_armstrong_number(0))
        self.assertTrue(is_armstrong_number(1))
        self.assertTrue(is_armstrong_number(2))
        self.assertTrue(is_armstrong_number(3))
        self.assertTrue(is_armstrong_number(4))
        self.assertTrue(is_armstrong_number(5))
        self.assertTrue(is_armstrong_number(6))
        self.assertTrue(is_armstrong_number(7))
        self.assertTrue(is_armstrong_number(8))
        self.assertTrue(is_armstrong_number(9))

    def test_double_digit_numbers(self):
        self.assertFalse(is_armstrong_number(10))
        self.assertFalse(is_armstrong_number(11))
        self.assertFalse(is_armstrong_number(99))

    def test_known_armstrong_numbers(self):
        self.assertTrue(is_armstrong_number(153))
        self.assertTrue(is_armstrong_number(370))
        self.assertTrue(is_armstrong_number(371))
        self.assertTrue(is_armstrong_number(407))
        self.assertTrue(is_armstrong_number(9474))

    def test_known_non_armstrong_numbers(self):
        self.assertFalse(is_armstrong_number(9475))
        self.assertFalse(is_armstrong_number(100))
        self.assertFalse(is_armstrong_number(123))
        self.assertFalse(is_armstrong_number(400))


if __name__ == '__main__':
    unittest.main()
