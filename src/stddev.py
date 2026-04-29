#!/usr/bin/env python3
import sys
import math_lib

def stddev_calc(n, sum_numbers, sum_squares):
    if n < 2:
        return 0.0
        #if the sequence has less than 2 elements, we will return 0.0 as the StdDev

    arithmetic_mean = math_lib.div(sum_numbers, n)
    s = math_lib.sqrt(math_lib.div((sum_squares - n*math_lib.square(arithmetic_mean)), (n-1)))
    return max(0.0, s) #if the result is negative and close to 0, we will return 0.0


def main():
    count = 0
    sum_of_numbers = 0.0
    sum_of_squares = 0.0

    for line in sys.stdin:
        char_seqs = line.split()
        for char_seq in char_seqs:
            char_seq.replace(',', '')

            try:
                number = float(char_seq)
            except ValueError:
                #not a number
                continue
            else:
                sum_of_numbers += number
                sum_of_squares += math_lib.square(number, 2)
                count += 1

    result = stddev_calc(count, sum_of_numbers, sum_of_squares)
    print(result)


if __name__ == "__main__":
    main()