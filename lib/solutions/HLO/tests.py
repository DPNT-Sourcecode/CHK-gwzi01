import unittest

from hello_solution import hello

class TestHelloWorld(unittest.TestCase):
    def test_hello_world_with_string(self):
        inputs_and_outputs = [
            ("John", "John says Hello World!"),
            ("Dave", "Dave says Hello World!"),
        ]

        for case in inputs_and_outputs:
            self.assertEqual(hello(case[0]), case[1])

    def test_non_string_raises_error(self):
        with self.assertRaises()

if __name__ == '__main__':
    unittest.main()