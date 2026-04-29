import unittest
import io
import subprocess

class TestStandardDeviationInput(unittest.TestCase):
    def terminal_setup(self, input_str):
        process = subprocess.Popen(['python3', 'stddev.py'],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   text=True
                                )
        stdout, stderr = process.communicate(input=input_str)
        return stdout.strip(), stderr
    
    def test_one_element_per_line(self):
        # Dataflow: "1\n2\n3"
        # Expected stdout = 1.0
        stdout, stderr = self.terminal_setup("1\n2\n3")
        self.assertEqual(stdout, "1.0")

    def test_one_line_multiple_elements(self):
        # Dataflow: "0 3    5   4       2  6 1"
        # Expected stdout = 2.160246899
        stdout, stderr = self.terminal_setup("0 3    5   4       2  6 1")
        self.assertAlmostEqual(float(stdout), 2.160246899, 7)

    def test_multiple_lines_multiple_elements(self):
        # Dataflow: "7 9\n8\n4 3 2"
        # Expected stdout = 2.880972058
        stdout, stderr = self.terminal_setup("7 9\n8\n4 3 2")
        try:
            float(stdout)
        except ValueError:
            self.assertTrue(False)
        else:
            self.assertAlmostEqual(float(stdout), 2.880972058, 7)

    def test_empty_lines(self):
        # Dataflow: "1\n\n2     3   \n \n   \n 4\n"
        # Expected stdout = 1.2909944
        stdout, stderr = self.terminal_setup("1\n\n2     3   \n \n   \n 4\n")
        try:
            float(stdout)

        except ValueError:
            self.assertTrue(False)

        else:
            self.assertAlmostEqual(float(stdout), 1.2909944, 7)

    def test_floats(self):
        # Dataflow: "0.75, 1.5, 2.25"
        # Expected stdout = 0.75
        stdout, stderr = self.terminal_setup("0.75 1.5 2.25")
        self.assertEqual(stdout, "0.75")

    def test_ignore_invalid_sequences(self):
        # Dataflow: "1 ?? _ . ,\t al 2 ; /stddev \n 3"
        # Expected stdout = 1.0
        stdout, stderr = self.terminal_setup("1 ?? _ . ,\t al 2 ; /stddev \n 3")
        self.assertEqual(stdout, "1.0")
