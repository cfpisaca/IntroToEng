import unittest
from labs import lab22
import os

class MyTestCase(unittest.TestCase):
    files = ["gb.txt", "scores.txt"]
    def setUp(self) -> None:
        with open(self.files[0], "w") as fh:
            line1 = "jen 88:47:90"
            print(line1, file=fh)
            line2 = "joe 87:46:91"
            print(line2, file=fh)

        with open(self.files[1], "w") as fh:
            print("jen 46:88", file=fh)
            print("joe 77", file=fh)
            print("jane 88:66", file=fh)

    def tearDown(self) -> None:
        for file in self.files:
            if os.path.exists(file):
                os.remove(file)

    def test_package_dicts(self):
        d1 = {"k1": 12, "k2": 22}
        d2 = {"k3": 12, "k4": 22}
        result = lab22.package_dicts(d1, d2)
        self.assertListEqual([d1, d2], result)

    def test_cumulative_grade(self):
        input = {"name": "joe", "lab1": 88, "lab3": 92, "hw1": 8, "hw3": 6, "midterm": 85, "final": 95}
        result = lab22.cumulative_grade(input)
        self.assertEqual(result["name"], "joe")
        self.assertEqual(result["cumulative_grade"], 90)

    def test_gradebook(self):
        key_names = ["name", "lab1", "lab2", "midterm"]
        result = lab22.gradebook(key_names, self.files[0])
        self.assertIsInstance(result, list)
        self.assertEqual(2, len(result))
        self.assertIsInstance(result[0], dict)
        self.assertIsInstance(result[1], dict)
        e1 = dict(zip(key_names, ["jen", "88", "47", "90"]))
        self.assertDictEqual(e1, result[0])
        e2 = dict(zip(key_names, ["joe", "87", "46", "91"]))
        self.assertDictEqual(e2, result[1])

    def test_dict_from_file3(self):
        result = lab22.dict_from_file3(self.files[1])
        expected = {"jen": ["46", "88"], "joe":["77"], "jane":["88", "66"]}
        self.assertDictEqual(expected, result)

if __name__ == '__main__':
    unittest.main()