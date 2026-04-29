#!/usr/bin/env python3
import sys
import random


def generate(n):
    for i in range(n):
        num = random.uniform(-999999, 999999)
        sys.stdout.write(f"{num}\n")

if __name__ == "__main__":
    count = 10000000
    if len(sys.argv) > 1:
        try: 
            count = int(sys.argv[1])
        except ValueError:
            pass

    generate(count)