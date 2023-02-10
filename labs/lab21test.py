import unittest
from labs import lab21
import os

class MyTestCase(unittest.TestCase):
    files = ["tuples.txt", "tmp.txt", "moretuples.txt"]

    def setUp(self) -> None:
        tuples = []
        tuples.append("(jen 66), (joe 77)")
        tuples.append("(jane 68), (joe 57), (john 81)")
        tuples.append("(jeri 65), (jane 97), (jen 82)")
        moretuples = []
        moretuples.append("(jen 99), (joe 90), (jeri 91)")
        with open(self.files[0], "w") as f:
            print("\n".join(tuples), file=f)
        with open(self.files[2], "w") as f:
            print("\n".join(moretuples), file=f)

    def tearDown(self) -> None:
        for f in self.files:
            if os.path.exists(f):
                os.remove(f)

    def test_convert_list(self):
        input = [66, 55, 88, 23, 97]
        lab21.convert_list(input)
        self.assertListEqual([[66], [55], [88], [23], [97]], input)

    def test_avg_score(self):
        input = {"jen": 46, "joe": 77, "jane": 88, "jim": 71}
        result = lab21.avg_score(input)
        self.assertEqual(70, result)

    def test_dict_from_file2(self):
        result = lab21.dict_from_file2(self.files[0])
        expected = {"jen": [66, 82], "joe": [77, 57], "jane":[68, 97], "john":[81], "jeri":[65]}
        self.assertEqual(expected, result)

    def test_read_two_files(self):
        result = lab21.read_two_files(self.files[0], self.files[2])
        expected = {"jen": [66, 82, 99], "joe": [77, 57, 90], "jane":[68, 97], "john":[81], "jeri":[65, 91]}

        self.assertDictEqual(expected, result)

    def test_write_dict_to_file(self):
        input = {"jen": ["66", "82"], "joe": ["77", "57"], "jane":["68", "97"], "john":["81"], "jeri":["65"]}
        lab21.write_dict_to_file(input, self.files[1])
        with open(self.files[1], "r") as f:
            lines = f.readlines()
        expected = ["jen: 66, 82\n", "joe: 77, 57\n", "jane: 68, 97\n", "john: 81\n", "jeri: 65\n"]
        for i in range(len(expected)):
            self.assertEqual(expected[i], lines[i])

if __name__ == '__main__':
    unittest.main()

