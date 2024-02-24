#!/usr/bin/env python3
from functools import reduce 

def solve(numbers):
    """Calculate product of given numbers

    Use reduce, not loop. Example of using reduce

    In [6]: import functools
    In [8]: functools.reduce(lambda x,y: x+y, [1,2,3,4,5], 0)
    Out[8]: 15
    """
    result = None

    return result


def main():
    print(solve(range(1, 10)))


if __name__ == "__main__":
    main()
