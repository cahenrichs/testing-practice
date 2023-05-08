
import timeit
import unittest
from challenge import EfficiencyAdding


class TestEfficiency(unittest.TestCase):

    def setUp(self):
        self._efficiency = EfficiencyAdding()
        self._efficiency_data = dict()

    def test_first_adding_method(self):
        starting_time = timeit.timeit()

        self._efficiency.adding_two_first_method(300)

        ending_time = timeit.timeit()

        self._efficiency_data["adding_two_first_method"] = ending_time - starting_time

        # print (self._efficiency_data)

        # Todo: start timing your program.
        # Todo: use the object self._efficiency to call the adding_two_first_method.
        # Todo: end timing your program.
        # Todo: add the result to self._efficiency_data dictionary.

    def test_second_adding_method(self):
        starting_time = timeit.timeit()

        self._efficiency.adding_two_second_method(300)

        ending_time = timeit.timeit()

        self._efficiency_data["adding_two_second_method"] = ending_time - starting_time
        # Todo: start timing your program.
        # Todo: use the object self._efficiency to call the adding_two_second_method.
        # Todo: end timing your program.
        # Todo: add the result to self._efficiency_data dictionary.

    def tearDown(self):
        print(self._efficiency_data)
        self._efficiency = None


if __name__ == '__main__':
    unittest.main()