#!/usr/bin/env python3

import time


def solve():
    """Tính số nghiệm của bài toán lớp 3

    Với các biến a,b,c,d,e,f,g,h,i là các số nằm trong khoảng 1-9 (các biến có
    thể có giá trị giống nhau), dạng biểu thức:

      a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10 = 66
    """
    result = 0

    start = time.time()

    for a in range(1,10):
        for b in range(1,10):
            for c in range(1,10):
                for d in range(1,10):
                    for e in range(1,10):
                        for f in range(1,10):
                            for g in range(1,10):
                                for h in range(1,10):
                                    for i in range(1,10):
                                        if a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10 == 66:
                                            result += 1
    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
