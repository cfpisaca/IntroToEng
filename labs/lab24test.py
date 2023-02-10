import unittest
from labs import lab24


class MyTestCase(unittest.TestCase):
    def test_string_to_dict(self):
        input ="[[jen, 98], [joe, 77], [jill, 85]]"
        result = lab24.string_to_dict(input)
        self.assertIsInstance(result, dict)
        self.assertDictEqual({"jen":98, "joe":77, "jill":85}, result)

    def test_list_of_lists_to_dict(self):
        input = [["jen", 98, 82], ["joe", 77], ["jill", 95, 72, 88]]
        result = lab24.list_of_lists_to_dict(input)
        self.assertIsInstance(result, dict)
        self.assertDictEqual({"jen":[98, 82], "joe":[77], "jill":[95, 72, 88]}, result)

    def test_union(self):
        one = {"k1":1, "k11":11, "k101":101}
        two = {"k2":1, "k11":12, "k101":102}
        result = lab24.union(one, two)
        self.assertIsInstance(result, dict)
        self.assertDictEqual({"k1":[1], "k2":[1], "k11":[11,12], "k101":[101, 102]}, result)

    def test_intersection(self):
        one = {"k1":1, "k11":11, "k101":101}
        two = {"k2":1, "k11":12, "k101":102}
        result = lab24.intersection(one, two)
        self.assertIsInstance(result, dict)
        self.assertDictEqual({"k11":[11,12], "k101":[101, 102]}, result)

if __name__ == '__main__':
    unittest.main()