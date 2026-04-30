#!/usr/bin/env python3
##
# @file stddev_num_generator.py
# @brief Utility script for generating random datasets for testing and profiling.
# @details This script generates a sequence of random floating-point numbers 
#          within a specified range and writes them to standard output. 
#          It is mainly used to create inputs for profiling execution time.
# @author xvojtat00
# @date 2026-04-30
#

import sys
import random

##
# @brief Generates and prints a sequence of random numbers.
# @details Each number is a uniform random float between -999 999 and 999 999.
#          Numbers are written directly to stdout followed by a newline.
#
# @param n The number of random values to generate.
#
def generate(n):
    for i in range(n):
        num = random.uniform(-999999, 999999)
        sys.stdout.write(f"{num}\n")

##
# @brief Entry point for the generator script.
# @details Reads the desired count from command-line arguments. 
#          Defaults to 1 000 000 if no valid argument is provided.
#
if __name__ == "__main__":
    count = 1000000
    if len(sys.argv) > 1:
        try: 
            count = int(sys.argv[1])
        except ValueError:
            pass

    generate(count)