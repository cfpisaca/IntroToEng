import unittest
from labs import lab10


class MyTestCase(unittest.TestCase):
    def test_sum_range(self):
        test_data = [1, 2, 3, 4, 5, 6]
        result = lab10.sum_range(test_data, 0, 6)
        self.assertEqual(21, result)
        result = lab10.sum_range(test_data, 2, 6)
        self.assertEqual(18, result)
        result = lab10.sum_range(test_data, 3, 5)
        self.assertEqual(9, result)
        result = lab10.sum_range(test_data, 1, 2)
        self.assertEqual(2, result)
        result = lab10.sum_range(test_data, 2, 2)
        self.assertEqual(0, result)
        result = lab10.sum_range(test_data, 3, 2)
        self.assertEqual(0, result)

    def test_every_other_item(self):
        even_length_list = [1, 2, 3, 4, 5, 6]
        odd_length_list = [10, 11, 12, 13, 14]
        result = lab10.every_other_item(even_length_list)
        self.assertListEqual([1, 3, 5], result)
        self.assertListEqual([1, 2, 3, 4, 5, 6], even_length_list)
        result = lab10.every_other_item(odd_length_list)
        self.assertListEqual([10, 12, 14], result)
        self.assertListEqual([10, 11, 12, 13, 14], odd_length_list)

    def test_last_half(self):
        even_length_list = [1, 2, 3, 4, 5, 6]
        odd_length_list = [10, 11, 12, 13, 14]
        result = lab10.last_half(even_length_list)
        self.assertListEqual([4, 5, 6], result)
        self.assertListEqual([1, 2, 3, 4, 5, 6], even_length_list)
        result = lab10.last_half(odd_length_list)
        self.assertListEqual([12, 13, 14], result)
        self.assertListEqual([10, 11, 12, 13, 14], odd_length_list)

    def test_last_half_backwards(self):
        even_length_list = [1, 2, 3, 4, 5, 6]
        odd_length_list = [10, 11, 12, 13, 14]
        result = lab10.last_half_backwards(even_length_list)
        self.assertListEqual([6, 5, 4], result)
        self.assertListEqual([1, 2, 3], even_length_list)
        result = lab10.last_half_backwards(odd_length_list)
        self.assertListEqual([14, 13, 12], result)
        self.assertListEqual([10, 11], odd_length_list)

    def test_selection_sort(self):
        test_data = [10, 2, 8, 19, 4]
        result = lab10.selection_sort(test_data)
        self.assertListEqual([2, 4, 8, 10, 19], result)
        self.assertListEqual([], test_data)

if __name__ == '__main__':
    unittest.main()