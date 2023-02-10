import unittest
import os
from labs import lab23


class MyTestCase(unittest.TestCase):
    data_file = "data.txt"
    column_names = ["name", "lab1", "lab2", "midterm", "lab3", "final"]
    data = [["jen", "88", "81", "91", "80", "99"],
            ["joe", "85", "89", "90", "80", "90"],
            ["jane", "81", "83", "92", "87", "93"]]
    def setUp(self) -> None:
        with open(self.data_file, "w") as fh:
            header = ", ".join(self.column_names)
            print(header, file=fh)
            for d in self.data:
                data_line = ", ".join(d)
                print(data_line, file=fh)












    def tearDown(self) -> None:
        if os.path.exists(self.data_file):
            os.remove(self.data_file)


    def test_gradebook1(self):
        result = lab23.gradebook1(self.data_file)
        self.assertIsInstance(result, list)
        self.assertEqual(len(self.data), len(result))
        for r in result:
            curr_data = None
            for i in range(len(self.data)):
                if r["name"] == self.data[i][0]:
                    curr_data = i
                    break
            for col in self.column_names:
                col_index = self.column_names.index(col)
                self.assertEqual(r[col], self.data[curr_data][col_index])












    def test_gradebook2(self):
        result = lab23.gradebook2(self.data_file)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result.keys()), len(self.column_names))
        for i, col in enumerate(self.column_names):
            values = result[col]
            for j in range(len(self.data)):
                self.assertEqual(values[j], self.data[j][i])







if __name__ == '__main__':
    unittest.main()