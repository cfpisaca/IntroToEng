import unittest
import lab11

class MyTestCase(unittest.TestCase):
    def test_combo(self):
        result = lab11.combo("abc", "1234567")
        self.assertEqual("1234567abc1234567", result)
        result = lab11.combo("abc", "abc")
        self.assertEqual("equal", result)
        result = lab11.combo("1234567", "1234567")
        self.assertEqual("equal", result)
        result = lab11.combo("abcdef", "123")
        self.assertEqual("abcdef123abcdef", result)

    def test_convert_string_to_list(self):
        input = "[a, b, c]"
        result = lab11.convert_string_to_list(input)
        self.assertListEqual(["a", "b", "c"], result)
        input = "[aaa, bb, cccc]"
        result = lab11.convert_string_to_list(input)
        self.assertListEqual(["aaa", "bb", "cccc"], result)

    def test_convert_string_to_list2(self):
        input = "[1,234, 45]"
        result = lab11.convert_string_to_list2(input)
        self.assertListEqual([1, 234, 45], result)
        input = "[1, 2,456]"
        result = lab11.convert_string_to_list2(input)
        self.assertListEqual([1, 2, 456], result)

    def test_merge_wo_dupes(self):
        in1 = [1, 23, 33, 2, 1, 5]
        in2 = [23, 45, 2]
        result = lab11.merge_wo_dupes(in1, in2)
        self.assertListEqual([1, 23, 33, 2, 5, 45], result)

    def test_intersection(self):
        in1 = [1, 23, 33, 2, 1, 5]
        in2 = [23, 45, 2]
        result = lab11.intersection(in1, in2)
        self.assertListEqual([23, 2], result)

if __name__ == '__main__':
    unittest.main()