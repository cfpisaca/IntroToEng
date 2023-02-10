import unittest
from labs import lab16


class MyTestCase(unittest.TestCase):
    def test_reorder_words(self):
        result = lab16.reorder_words("one two three four")
        self.assertEqual("two one four three", result)
        result = lab16.reorder_words("syracuse university computer science")
        self.assertEqual("university syracuse science computer", result)

    def test_acronym(self):
        result = lab16.acronym("one two three")
        self.assertEqual("OTT", result)
        result = lab16.acronym("Los Angeles lakers")
        self.assertEqual("LAL", result)

    def test_first_three_chars(self):
        result = lab16.first_three_chars("Oakland")
        self.assertEqual("OAK", result)
        result = lab16.first_three_chars("Three longer words")
        self.assertEqual("THR", result)

    def test_two_cases(self):
        result = lab16.two_cases("only two")
        self.assertEqual("ONL", result)
        result = lab16.two_cases("different two")
        self.assertEqual("DIF", result)
        result = lab16.two_cases("Three tree triple")
        self.assertEqual("TTT", result)
        result = lab16.two_cases("in god we")
        self.assertEqual("IGW", result)

if __name__ == '__main__':
    unittest.main()