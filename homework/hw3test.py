import unittest
from homework import hw3


class MyTestCase(unittest.TestCase):
    def test_key_in_dict_more_than_once(self):
        input = {}
        self.assertFalse(hw3.key_in_dict_more_than_once("k1", input))
        input = {"k1": 12, "k2": 23, "k3": 34}
        self.assertFalse(hw3.key_in_dict_more_than_once("k999", input))
        input = {"k1": 12, "k2": 23, "k3": 34}
        self.assertFalse(hw3.key_in_dict_more_than_once("k1", input))
        input = {"k1": 12, "k2": 23, "k3": 34, "k1": 111}
        self.assertFalse(hw3.key_in_dict_more_than_once("k1", input))

    def test_val_in_dict_more_than_once(self):
        input = {"k1": 12, "k2": 23, "k3": 12}
        self.assertFalse(hw3.val_in_dict_more_than_once(input, 99))
        self.assertTrue(hw3.val_in_dict_more_than_once(input, 12))
        self.assertFalse(hw3.val_in_dict_more_than_once(input, 23))

    def test_fetch(self):
        input = {"k1": 12, "k2": 23, "k3": 34}
        result = hw3.fetch("k0", input)
        self.assertEqual(0, result)
        result = hw3.fetch("k1", input)
        self.assertEqual(12, result)

    def test_fetch_list(self):
        input = {"k1": 12, "k2": 23, "k3": 34}
        result = hw3.fetch_list(["k0", "k9"], input)
        self.assertEqual([], result)
        result = hw3.fetch_list(["k0", "k2"], input)
        self.assertEqual([23], result)
        result = hw3.fetch_list(["k3", "k2"], input)
        self.assertEqual([23, 34], result)

    def test_add_list(self):
        input = {"k1": 12, "k2": 23, "k3": 34}
        keys = ["k4", "k5"]
        vals = [44, 55]
        expected = {"k1": 12, "k2": 23, "k3": 34, "k4": 44, "k5":55}
        hw3.add_list(keys, vals, input)
        self.assertDictEqual(expected, input)

        input = {"k1": 12, "k2": 23, "k3": 34}
        keys = ["k4", "k3"]
        vals = [44, 333]
        expected = {"k1": 12, "k2": 23, "k3": 333, "k4": 44}
        hw3.add_list(keys, vals, input)
        self.assertDictEqual(expected, input)

    def test_overwrite(self):
        input = {"k1": 12, "k2": 23, "k3": 34}
        keys = ["k4", "k5"]
        vals = [44, 55]
        expected = {"k1": 12, "k2": 23, "k3": 34}
        hw3.overwrite(keys, vals, input)
        self.assertDictEqual(expected, input)

        input = {"k1": 12, "k2": 23, "k3": 34}
        keys = ["k4", "k3"]
        vals = [44, 333]
        expected = {"k1": 12, "k2": 23, "k3": 333}
        hw3.overwrite(keys, vals, input)
        self.assertDictEqual(expected, input)

    def test_add_new_keys(self):
        input = {"k1": 12, "k2": 23, "k3": 34}
        keys = ["k4", "k5"]
        vals = [44, 55]
        expected = {"k1": 12, "k2": 23, "k3": 34, "k4":44, "k5":55}
        hw3.add_new_keys(keys, vals, input)
        self.assertDictEqual(expected, input)

        input = {"k1": 12, "k2": 23, "k3": 34}
        keys = ["k4", "k3"]
        vals = [44, 333]
        expected = {"k1": 12, "k2": 23, "k3":34, "k4":44}
        hw3.add_new_keys(keys, vals, input)
        self.assertDictEqual(expected, input)

    def test_vals_for_keys_matching(self):
        input = {"k1": 12, "l2": 23, "k3": 34, "k12": 123}
        result = hw3.vals_for_keys_matching("k12", input)
        self.assertListEqual([123], result)
        result = hw3.vals_for_keys_matching("k1", input)
        self.assertListEqual([12, 123], result)
        result = hw3.vals_for_keys_matching("k", input)
        self.assertListEqual([12, 34, 123], result)

    def test_move_vals_to_list(self):
        input = {"k1": 12, "k2": 23, "k3": 34}
        hw3.move_vals_to_list(input)
        expected = {"k1": [12], "k2": [23], "k3": [34]}
        self.assertDictEqual(expected, input)

    def test_move_nonlist_vals_to_list(self):
        input = {"k1": [12], "k2": 23, "k3": [34], "k4": 45}
        hw3.move_nonlist_vals_to_list(input)
        expected = {"k1": [12], "k2": [23], "k3": [34], "k4": [45]}
        self.assertDictEqual(expected, input)

    def test_remove_item(self):
        input = {"k1": 12, "k2": 23, "k3": 34}
        hw3.remove_item("k99", input)
        expected = {"k1": 12, "k2": 23, "k3": 34}
        self.assertDictEqual(expected, input)
        hw3.remove_item("k2", input)
        expected = {"k1": 12, "k3": 34}
        self.assertDictEqual(expected, input)

    def test_remove_first_item(self):
        input = {"k1": 12, "k2": 23, "k3": 34}
        hw3.remove_first_item(23, input)
        expected = {"k1": 12, "k3": 34}
        self.assertDictEqual(expected, input)

        input = {"k1": 12, "k2": 23, "k3": 34, "k4": 23}
        hw3.remove_first_item(23, input)
        expected = {"k1": 12, "k3": 34, "k4": 23}
        self.assertDictEqual(expected, input)

    def test_remove_all_items(self):
        input = {"k1": 12, "k2": 23, "k3": 34, "k4": 23}
        hw3.remove_all_items(23, input)
        expected = {"k1": 12, "k3": 34}
        self.assertDictEqual(expected, input)

    def test_remove_n_items(self):
        input = {"k1": 12, "k2": 23, "k3": 34, "k4": 23, "k5": 23}
        hw3.remove_n_items(23, input, 0)
        expected = {"k1": 12, "k2": 23, "k3": 34, "k4": 23, "k5": 23}
        self.assertDictEqual(expected, input)
        hw3.remove_n_items(23, input, 2)
        expected = {"k1": 12, "k3": 34, "k5": 23}
        self.assertDictEqual(expected, input)
        hw3.remove_n_items(23, input, 2)
        expected = {"k1": 12, "k3": 34}
        self.assertDictEqual(expected, input)



if __name__ == '__main__':
    unittest.main()
