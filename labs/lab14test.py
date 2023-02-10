import unittest
from labs import lab14


class MyTestCase(unittest.TestCase):
    def test_remove_all_even_numbers(self):
        input = [1, 2, 22, 3, 44]
        lab14.remove_all_even_numbers(input)
        self.assertListEqual([1, 3], input)




    def test_num_vowels_gt(self):
        input = "extraordinary"
        self.assertTrue(lab14.num_vowels_gt(input, 4))
        self.assertFalse(lab14.num_vowels_gt(input, 5))



    def test_most_words(self):
        input = ["one two three", "two words", "a b c d e", "runonsentence"]
        result = lab14.most_words(input)
        self.assertEqual("a b c d e", result)



    def test_vowels_consonants(self):
        input = "abcde"
        result = lab14.vowels_consonants(input)
        self.assertEqual("aebcd", result)



    def test_university_name_to_email(self):
        input = "carnegie melon university"
        result = lab14.university_name_to_email(input)
        self.assertEqual("cmu.edu", result)
        input = "syracuse university"
        result = lab14.university_name_to_email(input)
        self.assertEqual("syracuse.edu", result)
        input = "massachussets institute technology"
        result = lab14.university_name_to_email(input)
        self.assertEqual("mit.edu", result)









if __name__ == '__main__':
    unittest.main()