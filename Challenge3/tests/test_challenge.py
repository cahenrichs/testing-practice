import sys
import unittest
from io import StringIO
from challenge import Printer

class TestPrintedOutPut(unittest.TestCase):

    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.printer = Printer()

    def test_value_name(self):
        self.printer.set_value('Clint')
        self.printer.print_value()
        self.assertEqual(sys.stdout.getvalue().strip(), 'Clint')
        # Todo: use the object printer to add the name 'Muhammad Ali' to the set_value method.
        # Todo: use the object printer to call the method print_value.
        # Todo: use assertEqual to check if the printed string is 'Muhammad Ali'
        

    def test_value_job(self):
        self.printer.set_value('Boxer')
        self.printer.print_value()
        self.assertEqual(sys.stdout.getvalue().strip(), 'Boxer')
        # Todo: use the object printer to add the job 'Boxer' to the set_value method.
        # Todo: use the object printer to call the method print_value.
        # Todo: use assertEqual to check if the printed string is 'Boxer'
        

    def tearDown(self):
        self.printer = None


if __name__ == '__main__':
    unittest.main()