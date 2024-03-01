#!/usr/bin/env python3


def solve(N):
    """Creates a list like this - odd numbers repeat six times.

      ['111111', '333333', ..., '999999', '111111111111',..., NNNNNN]

    Must: use list comprehension
    Tips: list comprehension always create new list
    """

    result = [str(i)*6 for i in range(1,N,2)]


    return result


def main():
    print(solve(20))


if __name__ == "__main__":
    main()
