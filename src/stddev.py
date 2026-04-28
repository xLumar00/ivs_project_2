#!/usr/bin/env python3
import sys

def stddev_calc(n, sum_numbers, sum_squares):
    if n < 2:
        return 0.0
        #the standard deviation of 2 elements is always 0



    #TODO THE FINALISATION OF THE RESULT (sqrt beside other things)


def main():
    count = 0
    sum_of_numbers = 0.0
    sum_of_squares = 0.0

    for line in sys.stdin:
        print(line, end="")

        char_seqs = line.split()
        for char_seq in char_seqs:
            try:
                number = float(char_seq)
            except ValueError:
                #not a number
                continue
            else:
                sum_numbers += number
                sum_squares += 0 #TODO ADD CALL FOR MATHLIB
                count += 1

    result = stddev_calc(count, sum_of_numbers, sum_of_squares)
    print(result)

if __name__ == "__main__":
    main()