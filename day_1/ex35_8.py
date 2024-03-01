#!/usr/bin/env python3


def solve(N):
    """Create a list which contains N lists,
    each list contains N numbers from 0->N-1.

    E.g with N = 10:

    matrix = [
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      ...
      ...
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]

    Then returns a string looks like below

      0********0
      *1******1*
      **2****2**
      ***3**3***
      ****44****
      ****55****
      ***6**6***
      **7****7**
      *8******8*
      9********9
    """
    result = ""
    mid = int(N/2)
    for i in range(mid):
        result += "*" * i + str(i) + "*" * (N - i*2 - 2) + str(i) + "*"*i + "\n"
    
    for i in range(mid, N):
        result += "*" * (N-i-1) + str(i) + "*" * ((i-mid)*2) + str(i) + "*"*(N-i-1) + "\n"

    return result


def main():
    print(solve(10))


if __name__ == "__main__":
    main()
