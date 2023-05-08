import unittest
from chal import counter

class EasyTestCase(unittest.TestCase):
    def test_easy_input(self):
        self.assertEqual(counter("clint"), 5)

    def test_easy_input_two(self):
        self.assertEqual(counter("Mathew"), 6)

class MediumTestCase(unittest.TestCase):
    def test_medium_input(self):
        with self.assertRaises(TypeError):
            self.assertEqual(counter(45.5), 4)

    def test_medium_input_two(self):
        with self.assertRaises(TypeError):
            self.assertEqual(counter(43), 6)

class HardTestCase(unittest.TestCase):
    def test_hard_input(self):
        with self.assertRaises(TypeError):
            self.assertEqual(counter(float), 6)

    def test_hard_inupt(self):
        with self.assertRaises(TypeError):
            self.assertEqual(counter(None), 4)
        


        
        
if __name__ == '__main__':
    unittest.main()