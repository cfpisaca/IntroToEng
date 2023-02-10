import unittest
from labs import lab19
import os

class MyTestCase(unittest.TestCase):
    fname = "scores.txt"
    def setUp(self) -> None:
        data = ["jen: 65", "jane: 67", "jill: 77", "jill: 37", "joe: 65"]
        with open(self.fname, "w") as f:
            for line in data:
                print(line, file=f)

    def tearDown(self) -> None:
        if os.path.exists(self.fname):
            os.remove(self.fname)

    def test_string_to_dict(self):
        input = "jen, jane, jill, jim | 88, 77, 99, 98"
        result = lab19.string_to_dict(input)
        expected = {"jen": "88", "jane": "77", "jill": "99", "jim":"98"}
        self.assertDictEqual(expected, result)

    def test_write_to_file(self):
        l1 = ["some", "set of strings", "ending up as lines", "in a file"]
        lab19.write_list_to_file(l1, "tmp.txt")
        self.assertTrue(os.path.exists("../tmp.txt"))
        with open("../tmp.txt") as f:
            lines = f.readlines()
        for i in range(len(lines)):
            self.assertEqual(l1[i], lines[i].strip())

    def test_max_and_min(self):
        result = lab19.max_and_min(self.fname)
        self.assertDictEqual({"max": 77, "min": 37}, result)

    def test_names_to_scores(self):
        result = lab19.names_to_scores(self.fname)
        expected = {"jen": ["65"], "jane": ["67"], "jill": ["77", "37"], "joe": ["65"]}
        self.assertDictEqual(expected, result)

    def test_scores_to_names(self):
        result = lab19.scores_to_names(self.fname)
        expected = {"65": ["jen", "joe"], "67": ["jane"], "77": ["jill"], "37": ["jill"]}
        self.assertDictEqual(expected, result)

if __name__ == '__main__':
    unittest.main()

