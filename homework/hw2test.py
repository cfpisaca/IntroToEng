import unittest
from homework import hw2


class MyTestCase(unittest.TestCase):
    def test_third_char(self):
        result = hw2.third_char("tw")
        self.assertEqual("", result)
        result = hw2.third_char("two")
        self.assertEqual("o", result)
        result = hw2.third_char("twofer")
        self.assertEqual("o", result)

    def test_nth_char(self):
        result = hw2.nth_char("abcde", 0)
        self.assertEqual("", result)
        result = hw2.nth_char("abcde", 1)
        self.assertEqual("a", result)
        result = hw2.nth_char("abcde", 5)
        self.assertEqual("e", result)
        result = hw2.nth_char("abcde", 6)
        self.assertEqual("", result)

    def test_two_chars_at_index_n(self):
        result = hw2.two_chars_at_index_n("abcde", 0)
        self.assertEqual("", result)
        result = hw2.two_chars_at_index_n("abcde", 1)
        self.assertEqual("ab", result)
        result = hw2.two_chars_at_index_n("abcde", 4)
        self.assertEqual("de", result)
        result = hw2.two_chars_at_index_n("abcde", 5)
        self.assertEqual("e", result)
        result = hw2.two_chars_at_index_n("abcde", 6)
        self.assertEqual("", result)

    def test_m_chars_at_index_n(self):
        result = hw2.m_chars_at_index_n("abcde", 3, 1)
        self.assertEqual("abc", result)
        result = hw2.m_chars_at_index_n("abcde", 7, 1)
        self.assertEqual("abcde", result)

    def test_first_n_chars(self):
        result = hw2.first_n_chars("abcdef", 3)
        self.assertEqual("abc", result)
        result = hw2.first_n_chars("abcdef", 4)
        self.assertEqual("abcd", result)
        result = hw2.first_n_chars("abcdef", 7)
        self.assertEqual("abcdef", result)

    def test_last_n_chars(self):
        result = hw2.last_n_chars("abcdef", 3)
        self.assertEqual("def", result)
        result = hw2.last_n_chars("abcdef", 4)
        self.assertEqual("cdef", result)
        result = hw2.last_n_chars("abcdef", 7)
        self.assertEqual("abcdef", result)

    def test_first_letter_of_each_string(self):
        input = ["one", "and", "two", "three"]
        result = hw2.first_letter_of_each_string(input)
        self.assertEqual("oatt", result)

    def test_second_letter_of_each_string(self):
        input = ["one", "and", "two", "three"]
        result = hw2.second_letter_of_each_string(input)
        self.assertEqual("nnwh", result)

    def test_complicated(self):
        input = ["one", "and", "two", "three"]
        result = hw2.complicated(input)
        self.assertEqual("onoe", result)

    def test_second_word(self):
        result = hw2.second_word("one two three")
        self.assertEqual("two", result)

    def test_nth_word(self):
        result = hw2.nth_word("one two three", 0)
        self.assertEqual("", result)
        result = hw2.nth_word("one two three", 1)
        self.assertEqual("one", result)
        result = hw2.nth_word("one two three", 3)
        self.assertEqual("three", result)
        result = hw2.nth_word("one two three", 4)
        self.assertEqual("", result)

    def test_remove_second_word(self):
        result = hw2.remove_second_word("one two three")
        self.assertEqual("one three", result)

    def test_remove_nth_word(self):
        result = hw2.remove_nth_word("one two three", 0)
        self.assertEqual("", result)
        result = hw2.remove_nth_word("one two three", 1)
        self.assertEqual("two three", result)
        result = hw2.remove_nth_word("one two three", 3)
        self.assertEqual("one two", result)
        result = hw2.remove_nth_word("one two three", 4)
        self.assertEqual("", result)

    def test_second_half_of_second_word(self):
        result = hw2.second_half_of_second_word("one:1 two:23 three:34")
        self.assertEqual("23", result)

    def test_second_half_of_nth_word(self):
        result = hw2.second_half_of_nth_word("one:1 two:23 three:34", 0)
        self.assertEqual("", result)
        result = hw2.second_half_of_nth_word("one:1 two:23 three:34", 1)
        self.assertEqual("1", result)
        result = hw2.second_half_of_nth_word("one:1 two:23 three:34", 3)
        self.assertEqual("34", result)
        result = hw2.second_half_of_nth_word("one:1 two:23 three:34", 4)
        self.assertEqual("", result)

    def test_first_word_from_each_line(self):
        input = "some words\nmore words\nlast line"
        result = hw2.first_word_from_each_line(input)
        self.assertEqual("some more last", result)

    def test_complicated_word_line(self):
        input = "some words here\nand more there\nlast line ends"
        result = hw2.complicated_word_line(input)
        self.assertEqual("some more ends", result)

    def test_first_half_joined_with_dashes(self):
        input = "one and two and three four"
        result = hw2.first_half_joined_with_dashes(input)
        self.assertEqual("one-and-two", result)

    def test_filter_out_word(self):
        input = "one and two or three four maybe five"
        result = hw2.filter_out_word(input, "and")
        self.assertEqual("one two or three four maybe five", result)

    def test_filter_out_all_words_in_p2(self):
        input = "one and two or three four maybe five"
        filterd = ["and", "or", "maybe"]
        result = hw2.filter_out_all_words_in_p2(input, filterd)
        self.assertEqual("one two three four five", result)
        
    def test_filter_out_all_words_in_p2_str(self):
        input = "one and two or three four maybe five"
        filterd = "and or maybe"
        result = hw2.filter_out_all_words_in_p2_str(input, filterd)
        self.assertEqual("one two three four five", result)

if __name__ == '__main__':
    unittest.main()
