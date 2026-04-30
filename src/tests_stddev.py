#!/usr/bin/env python3
import unittest
from stddev import stddev_calc

class TestStandardDeviationMath(unittest.TestCase):

    def test_basic_dataset(self):
        # Dataset: [1,9,8,5,2]
        # count = 5, sum = 25, sum_sq = 175
        # Expected standard deviation - 3.535533905932737 (rounded to 15 decimals)
        result = stddev_calc(5, 25, 175)
        self.assertAlmostEqual(result, 3.535533905932737, 7)
        # Since floating point numbers cannot be always 100% precise, we will only check the first 7 decimals

    def test_small_dataset(self):
        # Dataset: [1,2,3]
        # count = 3, sum = 6, sum_sq = 14
        # Expected standard deviation - 1.0
        result = stddev_calc(3, 6, 14)
        self.assertEqual(result, 1.0)

    def test_two_elements_dataset(self):
        # Dataset: [1,3]
        # count = 2, sum = 4, sum_sq = 10
        # Expected standard deviation - 1.414213562373 (12 decimals but we only check for 7)
        result = stddev_calc(2, 4, 10)
        self.assertAlmostEqual(result, 1.414213562373, 7)

    def test_minimal_dataset(self):
        # Dataset: [12]
        # count = 1, sum = 12, sum_sq = 144
        # Expected 0.0 (in the formula there is N-1 in the denominator, so it needs to be handled with care)
        result = stddev_calc(1, 12, 144)
        self.assertEqual(result.strip(), "Undefined.")

    def test_empty_dataset(self):
        # Dataset: (empty)
        # count = 0, sum = 0.0, sum_sq = 0.0
        # Expected 0.0 (no data, so no Standard Deviation)
        result = stddev_calc(0, 0, 0)
        self.assertEqual(result.strip(), "Undefined.")

    def test_equal_elements_dataset(self):
        # Dataset: [4,4,4]
        # count = 3, sum = 12.0, sum_sq = 48.0
        # Expected 0.0 (equal elements have no deviation at all)
        result = stddev_calc(3, 12.0, 48.0)
        self.assertEqual(result, 0.0)

    def test_large_numbers_dataset(self):
        # Dataset: [9 999 999,10 000 000,10 000 001]
        # count = 3, sum = 30 000 000, sum_sq = 300 000 000 000 002
        # Expected 1.0 (the accuracy should be same even for large numbers)
        result = stddev_calc(3, 30000000, 300000000000002)
        self.assertAlmostEqual(result, 1.0, 7)

    def test_floats_dataset(self):
        # Dataset: [0.75,2.5,3.25,4.35]
        # count = 4, sum = 10.85, sum_sq = 36.2975
        # Expected 1.51293038 (only 7 of the 8 decimals will be checked)
        result = stddev_calc(4, 10.85, 36.2975)
        self.assertAlmostEqual(result, 1.51293038, 7)

    def test_precise_floats_dataset(self):
        # Dataset: [1.25, 2.5, 3.75]
        # count = 3, sum = 7.5, sum_sq = 21.875
        # Expected 1.25 exactly
        result = stddev_calc(3, 7.5, 21.875)
        self.assertAlmostEqual(result, 1.25, 7)

    def test_negatives_dataset(self):
        # Dataset: [-3, -7, -11]
        # count = 3, sum = -21, sum_sq = 179
        # Expected 4.0
        result = stddev_calc(3, -21, 179)
        self.assertEqual(result, 4.0)

    def test_zero_incorporated_dataset(self):
        # Dataset: [-5, 0, 5]
        # count = 3, sum = 0, sum_sq = 50
        # Expected 5.0
        result = stddev_calc(3, 0, 50)
        self.assertEqual(result, 5.0)

    def test_all_zeroes_dataset(self):
        # Dataset: [0,0,0,0,0,0,0,0,0,0,0]
        # count = 11, sum = 0, sum_sq = 0
        # Expected 0.0
        result = stddev_calc(11, 0, 0)
        self.assertEqual(result, 0.0)

if __name__ == "__main__":
    unittest.main()