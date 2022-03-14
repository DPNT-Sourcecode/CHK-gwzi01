import unittest

from .hello_solution import hello

class TestHelloWorld(unittest.Testcase):
    def test_hello_world(self):
        inputs_and_outputs = [
            ("John", "John says Hello world!"),
            ("Dave", "Dave says Hello world!"),
            (2, "A string must be passed to this function")
        ]

        for case in inputs_and_outputs:
            self.assertEqual(hello(case[0]), case[1])