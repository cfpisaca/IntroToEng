import unittest
from labs import lab5


class MyTestCase(unittest.TestCase):
    def test_right_justify(self):
        result = lab5.right_justify("asdfa")
        self.assertEqual("---", result)
        result = lab5.right_justify("asd")
        self.assertEqual("asd", result)
        result = lab5.right_justify("qwe")
        self.assertEqual("qwe", result)
        result = lab5.right_justify("po")
        self.assertEqual(" po", result)
        result = lab5.right_justify("p")
        self.assertEqual("  p", result)
        result = lab5.right_justify("")
        self.assertEqual("   ", result)

    def test_sum_up_to(self):
        result = lab5.sum_up_to(5)
        self.assertEqual(10, result)
        result = lab5.sum_up_to(6)
        self.assertEqual(15, result)

    def test_sum_beg_end(self):
        result = lab5.sum_beg_end(2, 4)
        self.assertEqual(5, result)
        result = lab5.sum_beg_end(2, 6)
        self.assertEqual(14, result)
        result = lab5.sum_beg_end(3, 6)
        self.assertEqual(12, result)

    def test_is_vowel(self):
        self.assertTrue(lab5.is_vowel("a"))
        self.assertTrue(lab5.is_vowel("e"))
        self.assertTrue(lab5.is_vowel("i"))
        self.assertTrue(lab5.is_vowel("o"))
        self.assertTrue(lab5.is_vowel("u"))
        self.assertFalse(lab5.is_vowel("ua"))
        self.assertFalse(lab5.is_vowel("we"))
        self.assertFalse(lab5.is_vowel("w"))
        self.assertFalse(lab5.is_vowel("d"))

    def test_prepend_if_even(self):
        result = lab5.prepend_if_even(1, "qwerty")
        self.assertEqual("qwerty", result)
        result = lab5.prepend_if_even(2, "asdf")
        self.assertEqual("evenasdf", result)

    def test_fizzbuzz(self):
        result = lab5.fizzbuzz(9)
        self.assertEqual("fizz", result)
        result = lab5.fizzbuzz(10)
        self.assertEqual("buzz", result)
        result = lab5.fizzbuzz(15)
        self.assertEqual("fizzbuzz", result)
        result = lab5.fizzbuzz(29)
        self.assertEqual("", result)

if __name__ == '__main__':
    unittest.main()