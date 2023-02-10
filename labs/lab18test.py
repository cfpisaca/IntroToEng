import unittest
from labs import lab18
import os

class MyTestCase(unittest.TestCase):

    oneLineFName = "oneline.txt"
    twoLineFName = "twolines.txt"

    def setUp(self) -> None:
        with open(self.oneLineFName, "w") as f:
            print("as to me and to as", file=f)
        with open(self.twoLineFName, "w") as f:
            f.write("k1, key2, kthree\n")
            print("val1, vtwo, v3", file=f)

    def tearDown(self) -> None:
        if os.path.exists(self.oneLineFName):
            os.remove(self.oneLineFName)
        if os.path.exists(self.twoLineFName):
            os.remove(self.twoLineFName)

    def test_two_lists_to_dict(self):
        l1 = ["k1", "k2", "k3"]
        l2 = ["v1", "v2", "v3"]
        result = lab18.two_lists_to_dict(l1, l2)
        self.assertDictEqual({"k1":"v1", "k2":"v2", "k3":"v3"}, result)
        l2.append("v4")
        result = lab18.two_lists_to_dict(l1, l2)
        self.assertDictEqual({"k1":"v1", "k2":"v2", "k3":"v3"}, result)
        l1 = l1 + ["k4", "k5"]
        result = lab18.two_lists_to_dict(l1, l2)
        self.assertDictEqual({"k1":"v1", "k2":"v2", "k3":"v3", "k4":"v4", "k5":None}, result)

    def test_dict_from_file(self):
        result = lab18.dict_from_file(self.twoLineFName)
        expected = {"k1":"val1", "key2":"vtwo", "kthree":"v3"}
        self.assertDictEqual(expected, result)

    def test_list_word_count(self):
        result = {}
        l1 = "do re do me fa re do".split()
        lab18.list_word_count(l1, result)
        self.assertDictEqual({"do": 3, "re":2, "me": 1, "fa":1}, result)

    def test_file_total_words(self):
        result = {}
        lab18.file_total_words(self.oneLineFName, result)
        expected = {"numWords": 6}
        self.assertDictEqual(expected, result)

    def test_file_distinct_words(self):
        result = {}
        lab18.file_distinct_words(self.oneLineFName, result)
        expected= {"as":2, "to":2, "me":1, "and":1}
        self.assertDictEqual(expected, result)

if __name__ == '__main__':
    unittest.main()