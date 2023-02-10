import unittest
from labs import lab9


class MyTestCase(unittest.TestCase):
    def test_filter_strings(self):
        test_data = ["hell", "hello", "hellion"]
        result = lab9.filter_strings(test_data, "hel")
        self.assertListEqual(["hell", "hello", "hellion"], result)
        result = lab9.filter_strings(test_data, "hello")
        self.assertListEqual(["hello"], result)
        result = lab9.filter_strings(test_data, "helli")
        self.assertListEqual(["hellion"], result)

    def test_average_list(self):
        test_data = [12, 23, 22, 26, 99]
        result = lab9.average_list(test_data)
        self.assertEqual(36.4, result)
        result = lab9.average_list([])
        self.assertEqual(0.0, result)

    def test_first_name_first(self):
        result = lab9.first_name_first("Doe, Jane")
        self.assertEqual("Jane Doe", result)
        result = lab9.first_name_first("Smith, John")
        self.assertEqual("John Smith", result)

    def test_last_name_first(self):
        result = lab9.last_name_first("Jane Doe")
        self.assertEqual("Doe, Jane", result)
        result = lab9.last_name_first("Jane Q. Doe")
        self.assertEqual("Doe, Jane Q.", result)
        result = lab9.last_name_first("Jane Quinn Doe")
        self.assertEqual("Doe, Jane Quinn", result)

    def test_find_min(self):
        test_data = [1, 12, 24, 99]
        result = lab9.find_min(test_data)
        self.assertEqual(1, result)
        test_data = [99, 12, 24, 1]
        result = lab9.find_min(test_data)
        self.assertEqual(1, result)
        test_data = [24, 12, 1, 99]
        result = lab9.find_min(test_data)
        self.assertEqual(1, result)

    def test_two_smallest_ints(self):
        test_data = [1, 12, 24, 99]
        result = lab9.two_smallest_ints(test_data)
        self.assertEqual(type(result), type([]))
        self.assertListEqual([1, 12], result)
        test_data = [24, 12, 1, 99]
        result = lab9.two_smallest_ints(test_data)
        self.assertEqual(type(result), type([]))
        self.assertListEqual([1, 12], result)
        test_data = [12, 24, 120, 99, 1]
        result = lab9.two_smallest_ints(test_data)
        self.assertEqual(type(result), type([]))
        self.assertListEqual([1, 12], result)

if __name__ == '__main__':
    unittest.main()