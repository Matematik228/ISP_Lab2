import unittest
import task2
import json


class X:
    def __init__(self):
        self.a = 2
        self.d = 'Some text \t \f \n \' \" /'
        self.dict = {1: 2, 10: "228"}
        self.array = [2392, "Text", True, False, None, (1, 2, {8: 3, 5: "Deep"})]


class Test(unittest.TestCase):
    def test_class(self):
        x = X()
        self.assertEqual(task2.to_json(x), json.dumps(x.__dict__))

    def test_string(self):
        string = "Text \\ \' \" \n \f another text \b \t \r"
        self.assertEqual(task2.to_json(string), json.dumps(string))

    def test_dict(self):
        my_dict = {1: 2, 10: 228.1337, 'str': ['a', 'b', 'c']}
        self.assertEqual(task2.to_json(my_dict), json.dumps(my_dict))

    def test_error(self):
        x = {1, 2, 3}
        self.assertEqual(task2.to_json(x), json.dumps(x))


if __name__ == '__main__':
    unittest.main()
