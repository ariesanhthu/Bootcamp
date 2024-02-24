#!/usr/bin/env python3
from fractions import Fraction


def solve(a, *args):
    """Return tổng (kiểu float) của các phân số
    https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists

    https://docs.python.org/3/library/fractions.html
    Thư viện fractions cung cấp class Fraction để tạo ra kiểu phân số trên
    Python.

    """
    result = None

    return result



def main():
    print(solve("1/10", "1/10", "1/10"))


# __name__ là một biến|name đặc biệt do Python tự tạo ra
# nó có giá trị là string "__main__" khi file được chạy bằng lệnh
# python filename.py
# và có giá trị là tên file (bỏ .py) khi được import.
if __name__ == "__main__":
    main()
