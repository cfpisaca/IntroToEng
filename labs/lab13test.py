import unittest

import lab13

class MyTestCase(unittest.TestCase):
    def test_convert_str_and_merge(self):
        input1 = " 12, 23,34"
        input2 = "1,33, 88"
        result = lab13.convert_str_and_merge(input1, input2)
        self.assertListEqual([12, 23, 34, 1, 33, 88], result)

    def test_filter_even_numbers(self):
        input = [12, 23, 34, 1, 33, 88]
        result = lab13.filter_even_numbers(input)
        self.assertListEqual([12, 34, 88], result)

    def test_word_counts(self):
        input = ["one two three", "abracadabra", "a b c d e", "runonsentence"]
        result = lab13.word_counts(input)
        self.assertEqual([3, 1, 5, 1], result)

    def test_more_consonants_than_vowels(self):
        result = lab13.more_consonants_than_vowels("education")
        self.assertFalse(result)
        result = lab13.more_consonants_than_vowels("studying")
        self.assertTrue(result)

    def test_insert_duplicate(self):
        input = [10, 12, 33]
        lab13.insert_duplicate(input, 10)
        self.assertListEqual([10, 10, 12, 33], input)
        input = [10, 12, 33]
        lab13.insert_duplicate(input, 12)
        self.assertListEqual([10, 12, 12, 33], input)
        input = [10, 12, 33]
        lab13.insert_duplicate(input, 33)
        self.assertListEqual([10, 12, 33, 33], input)
        input = [10, 12, 33]
        lab13.insert_duplicate(input, 40)
        self.assertListEqual([10, 12, 33], input)

if __name__ == '__main__':
    unittest.main()