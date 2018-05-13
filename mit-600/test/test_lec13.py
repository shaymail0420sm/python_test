# encoding: utf-8

import unittest
from lec13 import *

fib_dict = dict()
# fib_dict[0] = 1
# fib_dict[1] = 1
# fib_dict[2] = 2
# fib_dict[3] = 3
# fib_dict[4] = 5
# fib_dict[5] = 8
fib_dict[6] = 13


class TestLec13(unittest.TestCase):

    def test_fib(self):
        self.fibx(fib_dict, fib)

    def test_mem_fib(self):
        self.fibx(fib_dict, mem_fib)

    def fib_x(self, fib_dict, fiber):
        for item in fib_dict.items():
            print(item)
            first = fiber(item[0])
            self.assertEqual(first, item[1])

    def test_max_value(self):
        weights = [1, 5, 3, 4]
        values = [15, 10, 9, 5]
        res = max_value(weights, values, len(values) - 1, 8)
        print('max value is %d' % res)
        self.assertEqual(res, 29)

    def test_max_value_2(self):
        weights = [1, 1, 5, 5, 3, 3, 4, 4]
        values = [15, 15, 10, 10, 9, 9, 5, 5]
        res = max_value(weights, values, len(values) - 1, 8)
        print('max value is %d' % res)
        self.assertEqual(res, 48)

    def test_max_value_x(self):
        weights = [1, 1, 5, 5, 3, 3, 4, 4]
        values = [15, 15, 10, 10, 9, 9, 5, 5]
        res = max_value_x(weights, values, len(values) - 1, 8)
        print('max value is %d' % res)
        self.assertEqual(res, 48)
