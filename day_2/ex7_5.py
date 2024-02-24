#!/usr/bin/env python3

import os
import sys

def solve(*args, **kwargs):
    """Return tuple chứa
    - Đường dẫn tới code của module `os`
    - list chứa các attribute của os và sys
    - Số dòng trong module `os`

    Biết dir(object) sẽ trả về tất cả thuộc tính (attribute) của object đó.
    Module cũng là object.

    In [11]: import os

    In [12]: len(dir(os))
    Out[12]: 284
    """

    # Đường dẫn tới code của module `os`
    result = None

    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
