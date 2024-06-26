#!/usr/bin/env python3


def solve(N):
    """Calculates sum of a list contains all integers less than N,
    which are multiple of 3 or 5.

    Given `sum` function:
    >>>  sum([1,2,3,4]) == 10

    Must: use list comprehension
    Tips: list comprehension always create new list
    """
    result = sum([i for i in range(N) if i%3 == 0 or i%5 == 0])
 
    return result


def main():
    print(solve(1000))


if __name__ == "__main__":
    main()
