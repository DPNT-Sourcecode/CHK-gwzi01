import unittest

from hello_solution import hello

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        inputs_and_outputs = [
            ("John", "John says Hello World!"),
            ("Dave", "Dave says Hello World!"),
            (2, "A string must be passed to this function")
        ]

        for case in inputs_and_outputs:
            self.assertEqual(hello(case[0]), case[1])

if __name__ == '__main__':
    unittest.main()