#!/usr/bin/env python3
##
# @file tests_stddev_input.py
# @brief Integration tests for stddev.py focusing on terminal input processing.
# @details This module uses subprocesses to simulate various standard input (stdin) 
#          scenarios, ensuring the program correctly parses numbers across multiple 
#          lines, tabs, and spaces, while ignoring invalid non-numeric sequences.
# @author xvojtat00
# @date 2026-04-30
#

import unittest
import io
import subprocess

##
# @class TestStandardDeviationInput
# @brief Suite of integration tests for validating the terminal input handling.
#
class TestStandardDeviationInput(unittest.TestCase):
    
    ##
    # @brief Helper method to run stddev.py as a subprocess.
    # @param input_str The string to be sent to the program's standard input.
    # @return A tuple containing (stripped_stdout, stderr).
    #
    def terminal_setup(self, input_str):
        process = subprocess.Popen(['python3', 'stddev.py'],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   text=True
                                )
        stdout, stderr = process.communicate(input=input_str)
        return stdout.strip(), stderr
    
    ##
    # @brief Verifies handling of input where each number is on a separate line.
    #
    def test_one_element_per_line(self):
        # Dataflow: "1\n2\n3"
        # Expected stdout = 1.0
        stdout, stderr = self.terminal_setup("1\n2\n3")
        try:
            float(stdout)
        except ValueError:
            self.fail()
        else:
            self.assertEqual(float(stdout), 1.0)

    ##
    # @brief Verifies handling of multiple elements on a single line with irregular spacing.
    #
    def test_one_line_multiple_elements(self):
        # Dataflow: "0 3    5   4       2  6 1"
        # Expected stdout = 2.160246899
        stdout, stderr = self.terminal_setup("0 3    5   4       2  6 1")
        try:
            float(stdout)
        except ValueError:
            self.fail()
        else:
            self.assertAlmostEqual(float(stdout), 2.160246899, 7)

    ##
    # @brief Verifies parsing across multiple lines containing multiple elements.
    #
    def test_multiple_lines_multiple_elements(self):
        # Dataflow: "7 9\n8\n4 3 2"
        # Expected stdout = 2.880972058
        stdout, stderr = self.terminal_setup("7 9\n8\n4 3 2")
        try:
            float(stdout)
        except ValueError:
            self.fail()
        else:
            self.assertAlmostEqual(float(stdout), 2.880972058, 7)

    ##
    # @brief Tests robustness against empty lines and whitespaces.
    #
    def test_empty_lines(self):
        # Dataflow: "1\n\n2     3   \n \n   \n 4\n"
        # Expected stdout = 1.2909944
        stdout, stderr = self.terminal_setup("1\n\n2     3   \n \n   \n 4\n")
        try:
            float(stdout)

        except ValueError:
            self.fail()

        else:
            self.assertAlmostEqual(float(stdout), 1.2909944, 7)

    ##
    # @brief Verifies that float strings are correctly parsed from standard input.
    #
    def test_floats(self):
        # Dataflow: "0.75 1.5 2.25"
        # Expected stdout = 0.75
        stdout, stderr = self.terminal_setup("0.75 1.5 2.25")
        try:
            float(stdout)
        except ValueError:
            self.fail()
        else:
            self.assertEqual(float(stdout), 0.75)

    ##
    # @brief Tests if the program correctly skips non-numeric rubbish from the input.
    #
    def test_ignore_invalid_sequences(self):
        # Dataflow: "1 ?? _ . ,\t al 2 ; /stddev \n 3"
        # Expected stdout = 1.0
        stdout, stderr = self.terminal_setup("1 ?? _ . ,\t al 2 ; /stddev \n 3")
        try:
            float(stdout)
        except ValueError:
            self.fail()
        else:
            self.assertEqual(float(stdout), 1.0)

if __name__ == "__main__":
    unittest.main()