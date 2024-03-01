#!/usr/bin/env python3


def solve(N):
    """Create a list which contains N elements 2
    Must: use list comprehension
    Tips: list comprehension always create new list
    """

    result = [2 for i in range(N)]

    return result


def main():
    print(solve(10))


if __name__ == "__main__":
    main()
