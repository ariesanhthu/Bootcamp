#!/usr/bin/env python3


def solve(numbers):
    """Tìm phần tử lớn nhất của list số nguyên `numbers`
    Không sử dụng function `max`, `sorted`

    Gợi ý: python có sẵn giá trị âm/dương vô cùng.
    """
    import sys

    assert isinstance(numbers, list)

    result = -sys.maxsize

    for num in numbers:
        if result < num:
            result = num

    return result


def main():
    print(solve([-1, 5, 9, 6, -999999999999999, 1]))


if __name__ == "__main__":
    main()
