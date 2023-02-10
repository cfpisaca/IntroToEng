import unittest
import lab20
import os

class MyTestCase(unittest.TestCase):

    files = ["scores.txt", "tuples.txt", "tmp.txt"]

    def setUp(self) -> None:
        with open(self.files[0], "w") as f:
            print("jen, 88, 47, 90", file=f)

        tuples = "(jen 66), (joe 77), (jane 88)"
        with open(self.files[1], "w") as f:
            print(tuples, file=f)

    def tearDown(self) -> None:
        for f in self.files:
            if os.path.exists(f):
                os.remove(f)

    def test_populate_dict(self):
        keyNames = ["name", "lab1", "lab2", "midterm"]
        result = lab20.populate_dict(keyNames, self.files[0])
        expected = {"name": "jen", "lab1": "88", "lab2": "47", "midterm": "90"}
        self.assertDictEqual(expected, result)

    def test_dict_from_file(self):
        result = lab20.dict_from_file(self.files[1])
        expected = {"jen": 66, "joe": 77, "jane": 88}
        self.assertDictEqual(expected, result)

    def test_write_to_dict(self):
        input = {"jen": 66, "joe": 77, "jane": 88}
        lab20.write_dict_to_file(input, self.files[2])
        self.assertTrue(self.files[2])
        with open(self.files[2], "r") as fh:
            lines = fh.readlines()
        expected = ["jen: 66\n", "joe: 77\n", "jane: 88\n"]
        for i in range(len(expected)):
            self.assertEqual(expected[i], lines[i])

    def test_num_failing_scores(self):
        input = {"jen": 46, "joe": 77, "jane": 88}
        result = lab20.num_failing_scores(input)
        self.assertEqual(1, result)
        input["joe"] = 39
        result = lab20.num_failing_scores(input)
        self.assertEqual(2, result)
        input["jane"] = 29
        result = lab20.num_failing_scores(input)
        self.assertEqual(3, result)

if __name__ == '__main__':
    unittest.main()