import unittest
from first_project import avg

class EasyTestCase(unittest.TestCase):

    def test_easy_imput(self):
        self.assertEqual(avg(1, 2, 3), 2)

    
    def test_easy_input_two(self):
        self.assertEqual(avg(10, 10, 10, 10, 10), 10)


class MediumTestCase(unittest.TestCase):

    def test_medium_imput(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, 3, "Clint"), 2)

    def test_medium_imput_two(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(10, 10, 10, 10, "10"), 10)


class HardTestCase(unittest.TestCase):

    def test_hard_imput(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, 3, None), 2)

    def test_hard_imput_two(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(10, 10, 10, 10, float), 10)

    def test_hard_imput_three(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, 3, frozenset), 2)

    def test_hard_imput_four(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(10, 10, 10, 10, set), 10)
    # def test_medium_imput(self):
    #     pass


if __name__ == '__main__':
    unittest.main()