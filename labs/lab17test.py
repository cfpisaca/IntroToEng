import unittest
from labs import lab17


class MyTestCase(unittest.TestCase):
    def test_index_to_val(self):
        input = ["one", 12, 33, "four"]
        result = lab17.index_to_val(input, 2)
        self.assertEqual("2 -> 33", result)
        result = lab17.index_to_val(input, 5)
        self.assertEqual("", result)

    def test_val_to_index(self):
        input = ["one", 12, 33, "four"]
        result = lab17.val_to_index(input, 2)
        self.assertEqual("", result)
        result = lab17.val_to_index(input, 12)
        self.assertEqual("1 -> 12", result)

    def test_list_pretty_print(self):
        input = ["one", 12, 33, "four"]
        input_as_text = "0 -> one\n1 -> 12\n2 -> 33\n3 -> four"
        result = lab17.list_pretty_print(input)
        self.assertEqual(input_as_text, result)

    def test_list_to_dict(self):
        input = ["syracuse", "u", "eecs"]
        result = lab17.list_to_dict(input)
        self.assertDictEqual({0: "syracuse", 1: "u", 2: "eecs"}, result)

    def test_two_lists_to_dict(self):
        keys = ["one", 12, True]
        vals = [1, "int", bool]
        result = lab17.two_lists_to_dict(keys, vals)
        self.assertDictEqual({"one": 1, 12: "int", True: bool}, result)

if __name__ == '__main__':
    unittest.main()