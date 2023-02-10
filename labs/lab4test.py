import unittest
from labs import lab4


class MyTestCase(unittest.TestCase):
    def test_test_if_true(self):
        result = lab4.test_if_true(True)
        self.assertTrue(result)
        result = lab4.test_if_true(False)
        self.assertFalse(result)

    def test_test_if_empty(self):
        self.assertTrue(lab4.test_if_empty(""))
        self.assertFalse(lab4.test_if_empty("asdf"))

    def test_return_smaller_int(self):
        result = lab4.return_smaller_int(1, 2)
        self.assertEqual(1, result)
        result = lab4.return_smaller_int(12, 2)
        self.assertEqual(2, result)

    def test_return_shorter_param(self):
        result = lab4.return_shorter_param("hi", "hit")
        self.assertEqual("hi", result)
        result = lab4.return_shorter_param("high", "hit")
        self.assertEqual("hit", result)

    def test_either_or_true(self):
        result = lab4.either_or_true(True, False)
        self.assertTrue(result)
        result = lab4.either_or_true(True, True)
        self.assertFalse(result)
        result = lab4.either_or_true(False, True)
        self.assertTrue(result)
        result = lab4.either_or_true(False, False)
        self.assertFalse(result)

    def test_either_or_even(self):
        result = lab4.either_or_even(1, 2)
        self.assertTrue(result)
        result = lab4.either_or_even(1, 21)
        self.assertFalse(result)
        result = lab4.either_or_even(12, 21)
        self.assertTrue(result)
        result = lab4.either_or_even(12, 24)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()