import unittest
import final

class MyTestCase(unittest.TestCase):

    def test_two_authors_middle_initial(self):
        result = final.two_authors_middle_initial("Thomas H. Cormen, Charles E. Leiserson")
        self.assertEqual("Cormen, Thomas and Charles Leiserson", result)
        result = final.two_authors_middle_initial("Thomas Cormen, Charles E. Leiserson")
        self.assertEqual("Cormen, Thomas and Charles Leiserson", result)
        result = final.two_authors_middle_initial("Thomas H. Cormen, Charles Leiserson")
        self.assertEqual("Cormen, Thomas and Charles Leiserson", result)
        result = final.two_authors_middle_initial("Thomas Cormen, Charles Leiserson")
        self.assertEqual("Cormen, Thomas and Charles Leiserson", result)

    def test_put_ints_in_list(self):
        input = [[1], 12, [9], 2, 3, [7]]
        final.put_ints_in_list(input)
        self.assertListEqual([[1], [12], [9], [2], [3], [7]], input)

    def test_total_len_of_strs(self):
        input = ["a", 12, "bc", "def", 34]
        result = final.total_len_of_strs(input)
        self.assertEqual(6, result)

    def test_lab_scores_as_string(self):
        input = {"lab1": "88", "lab2": "82", "midterm": "99", "final": "91", "lab3": "88"}
        result = final.lab_scores_as_string(input)
        self.assertEqual("258", result)

if __name__ == '__main__':
    unittest.main()