#!/usr/bin/env python3

"""
Xét các số nguyên dương < 100, in ra các số chia hết cho 5 theo dạng::

    5 == 1 * 5
    10 == 2 * 5
    15 == 3 * 5
    ...
"""


def solve():
    """Trả về 1 `list` các `string` có dạng:

        output: ['5 == 1 * 5', '10 == 2 * 5', ...]

    Lưu ý: Thứ tự tăng dần theo bảng cửu chương
    """
    result = []

    for i in range(1,20):
        stringOperation = str(i*5) + ' == ' + str(i) + ' * 5'
        result.append(stringOperation)

    return result


def main():
    for i in solve():
        print(i)


if __name__ == "__main__":
    main()
