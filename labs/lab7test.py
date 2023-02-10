import unittest
from labs import lab7


class MyTestCase(unittest.TestCase):
    def test_get_item_at(self):
        test_data = [12, 2, 3, 18, 19, 1, 3, 5, 24]
        result = lab7.get_item_at(test_data, 3)
        self.assertEqual(18, result)
        result = lab7.get_item_at(test_data, 0)
        self.assertEqual(12, result)
        result = lab7.get_item_at(test_data, 8)
        self.assertEqual(24, result)
        result = lab7.get_item_at(test_data, 12)
        self.assertEqual(-1, result)
        result = lab7.get_item_at(test_data, -2)
        self.assertEqual(-1, result)

    def test_get_first_digit(self):
        result = lab7.get_first_digit("asdf1qwer")
        self.assertEqual("1", result)
        result = lab7.get_first_digit("2asdfqwer")
        self.assertEqual("2", result)
        result = lab7.get_first_digit("asdfqwer3")
        self.assertEqual("3", result)
        result = lab7.get_first_digit("1asdf2qwer")
        self.assertEqual("1", result)
        result = lab7.get_first_digit("asdf5qwer2")
        self.assertEqual("5", result)

    def test_contains_boolean(self):
        positive_test_data = ["string", 98, "False", 1, True, 2]
        negative_test_data = ["string", 98, "False", 1, 2, 3, 4]
        self.assertTrue(lab7.contains_boolean(positive_test_data))
        self.assertFalse(lab7.contains_boolean(negative_test_data))
        self.assertFalse(lab7.contains_boolean([]))

    def test_shorter_list(self):
        result = lab7.shorter_list([1, 2, 3], [1, 2, 3, 4])
        self.assertListEqual([1, 2, 3], result)
        result = lab7.shorter_list([1, 2, 3, 4], [1, 2, 3])
        self.assertListEqual([1, 2, 3], result)
        result = lab7.shorter_list([1, 2, 3], [1, 2, 3])
        self.assertListEqual([], result)

    def test_first_two_items(self):
        result = lab7.first_two_items([11, 2, 35])
        self.assertListEqual([11, 2], result)
        result = lab7.first_two_items([21, 2])
        self.assertListEqual([21, 2], result)
        result = lab7.first_two_items([1])
        self.assertListEqual([1], result)
        result = lab7.first_two_items([])
        self.assertListEqual([], result)

    def test_last_n_items(self):
        result = lab7.last_n_items([11, 2, 35, 40], 3)
        self.assertListEqual([2, 35, 40], result)
        result = lab7.last_n_items([11, 2, 35, 40], 4)
        self.assertListEqual([11, 2, 35, 40], result)
        result = lab7.last_n_items([11, 2, 35, 40], 8)
        self.assertListEqual([11, 2, 35, 40], result)
        result = lab7.last_n_items([], 2)
        self.assertListEqual([], result)

    def test_shortest_word(self):
        test_data = ["hi", "bye", "hello", "!"]
        result = lab7.shortest_word(test_data)
        self.assertEqual("!", result)
        result = lab7.shortest_word(["one", "two"])
        self.assertTrue(result == "one" or result == "two")
        result = lab7.shortest_word([])
        self.assertEqual("", result)

if __name__ == '__main__':
    unittest.main()