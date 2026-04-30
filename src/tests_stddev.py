#!/usr/bin/env python3
##
# @file tests_stddev.py
# @brief Unit tests for the standard deviation calculation logic.
# @details This module contains a test suite that verifies the mathematical 
#          accuracy of the stddev_calc function across various edge cases,
#          including small, large, empty, and negative datasets.
# @author xvojtat00
# @date 2026-04-30
#

import unittest
from stddev import stddev_calc

##
# @class TestStandardDeviationMath
# @brief Test suite for validating the Sample Standard Deviation algorithm.
#
class TestStandardDeviationMath(unittest.TestCase):

    ##
    # @brief Tests calculation with a standard small dataset.
    # @details Dataset: [1, 9, 8, 5, 2]. Verified up to 7 decimal places.
    #
    def test_basic_dataset(self):
        # Dataset: [1,9,8,5,2]
        # count = 5, sum = 25, sum_sq = 175
        # Expected standard deviation - 3.535533905932737 (rounded to 15 decimals)
        result = stddev_calc(5, 25, 175)
        self.assertAlmostEqual(result, 3.535533905932737, 7)
        # Since floating point numbers cannot be always 100% precise, we will only check the first 7 decimals

    ##
    # @brief Tests calculation with a simple sequence of integers.
    #
    def test_small_dataset(self):
        # Dataset: [1,2,3]
        # count = 3, sum = 6, sum_sq = 14
        # Expected standard deviation - 1.0
        result = stddev_calc(3, 6, 14)
        self.assertEqual(result, 1.0)

    ##
    # @brief Verifies the calculation when only two elements are provided.
    #
    def test_two_elements_dataset(self):
        # Dataset: [1,3]
        # count = 2, sum = 4, sum_sq = 10
        # Expected standard deviation - 1.414213562373 (12 decimals but we only check for 7)
        result = stddev_calc(2, 4, 10)
        self.assertAlmostEqual(result, 1.414213562373, 7)

    ##
    # @brief Tests the edge case of a single-element dataset.
    # @details Standard deviation is mathematically undefined for N < 2.
    #
    def test_minimal_dataset(self):
        # Dataset: [12]
        # count = 1, sum = 12, sum_sq = 144
        # Expected 0.0 (in the formula there is N-1 in the denominator, so it needs to be handled with care)
        result = stddev_calc(1, 12, 144)
        self.assertEqual(result.strip(), "Undefined.")

    ##
    # @brief Verifies handling of an empty input sequence.
    #
    def test_empty_dataset(self):
        # Dataset: (empty)
        # count = 0, sum = 0.0, sum_sq = 0.0
        # Expected 0.0 (no data, so no Standard Deviation)
        result = stddev_calc(0, 0, 0)
        self.assertEqual(result.strip(), "Undefined.")

    ##
    # @brief Tests a dataset where all elements are identical.
    # @details Deviation should be 0.0 as there is no variance.
    #
    def test_equal_elements_dataset(self):
        # Dataset: [4,4,4]
        # count = 3, sum = 12.0, sum_sq = 48.0
        # Expected 0.0 (equal elements have no deviation at all)
        result = stddev_calc(3, 12.0, 48.0)
        self.assertEqual(result, 0.0)

    ##
    # @brief Verifies mathematical accuracy with very large numerical values.
    #
    def test_large_numbers_dataset(self):
        # Dataset: [9 999 999,10 000 000,10 000 001]
        # count = 3, sum = 30 000 000, sum_sq = 300 000 000 000 002
        # Expected 1.0 (the accuracy should be same even for large numbers)
        result = stddev_calc(3, 30000000, 300000000000002)
        self.assertAlmostEqual(result, 1.0, 7)

    ##
    # @brief Tests calculation accuracy using decimal/float values.
    #
    def test_floats_dataset(self):
        # Dataset: [0.75,2.5,3.25,4.35]
        # count = 4, sum = 10.85, sum_sq = 36.2975
        # Expected 1.51293038 (only 7 of the 8 decimals will be checked)
        result = stddev_calc(4, 10.85, 36.2975)
        self.assertAlmostEqual(result, 1.51293038, 7)

    ##
    # @brief Verifies calculation with high-precision floats.
    #
    def test_precise_floats_dataset(self):
        # Dataset: [1.25, 2.5, 3.75]
        # count = 3, sum = 7.5, sum_sq = 21.875
        # Expected 1.25 exactly
        result = stddev_calc(3, 7.5, 21.875)
        self.assertAlmostEqual(result, 1.25, 7)

    ##
    # @brief Tests calculation with a dataset containing only negative numbers.
    #
    def test_negatives_dataset(self):
        # Dataset: [-3, -7, -11]
        # count = 3, sum = -21, sum_sq = 179
        # Expected 4.0
        result = stddev_calc(3, -21, 179)
        self.assertEqual(result, 4.0)

    ##
    # @brief Tests a mixed dataset including positive, negative, and zero values.
    #
    def test_zero_incorporated_dataset(self):
        # Dataset: [-5, 0, 5]
        # count = 3, sum = 0, sum_sq = 50
        # Expected 5.0
        result = stddev_calc(3, 0, 50)
        self.assertEqual(result, 5.0)

    ##
    # @brief Tests a large sequence consisting entirely of zeroes.
    #
    def test_all_zeroes_dataset(self):
        # Dataset: [0,0,0,0,0,0,0,0,0,0,0]
        # count = 11, sum = 0, sum_sq = 0
        # Expected 0.0
        result = stddev_calc(11, 0, 0)
        self.assertEqual(result, 0.0)

if __name__ == "__main__":
    unittest.main()