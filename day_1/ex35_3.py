#!/usr/bin/env python3


def solve(N):
    """Creates a list which contains N first even integers. ``[2, 4 ...]``
    Must: use list comprehension
    Tips: list comprehension always create new list
    """
    result = [i for i in range(2,N*2+1,2)]

    return result


def main():
    print(solve(6))


if __name__ == "__main__":
    main()
