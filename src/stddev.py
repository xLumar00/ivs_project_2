#!/usr/bin/env python3
import sys

def stddev_calc(n, sum_numbers, sum_squares):
    if n < 2:
        return 0.0
        #the standard deviation of 2 elements is always 0

    arithmetic_mean = sum_numbers / n
    s = ((sum_squares - n*arithmetic_mean**2)/(n-1))**(0.5) #TODO CALL MATHLIB ONCE READY
    return max(0, s)


def main():
    count = 0
    sum_of_numbers = 0.0
    sum_of_squares = 0.0

    for line in sys.stdin:
        print(line, end="")


if __name__ == "__main__":
    main()