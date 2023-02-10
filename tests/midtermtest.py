import unittest
from tests import midterm


class MyTestCase(unittest.TestCase):
    def test_zip_code_city(self):
        # "city, state 21345" => zip: city
        result = midterm.zip_code_city("syracuse, new york 13244")
        self.assertEqual("13244: syracuse", result)

    def test_list_multiples_3(self):
        input = [2, 24, 15, 8, 31, 9]
        result = midterm.list_multiples_3(input)
        self.assertListEqual([24, 15, 9], result)

    def test_multiples_of5_first(self):
        input = [12, 13, 5, 14, 15]
        result = midterm.multiples_of5_first(input)
        self.assertListEqual([5, 15, 12, 13, 14], result)

    def test_nfl_team_abbreviation(self):
        result = midterm.nfl_team_abbreviation("Oakland Raiders")
        self.assertEqual("OAK", result)
        result = midterm.nfl_team_abbreviation("New York Giants")
        self.assertEqual("", result)
        result = midterm.nfl_team_abbreviation("New England Patriots")
        self.assertEqual("NE", result)

if __name__ == '__main__':
    unittest.main()