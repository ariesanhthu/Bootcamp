#!/usr/bin/env python3


__doc__ = """
Yêu cầu:
- Viết decorator in ra thời gian chạy của 1 function
"""

import time


def your_decorator(function):
    """Tính thời gian chạy của `function` (float)"""
    def wrapper():
        start = time.time()
        function()
        return time.time() - start

    # Sửa lại tên và function cho phù hợp
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    return wrapper


# Sửa tên decorator cho phù hợp
@your_decorator
def worker():
    for i in range(10):
        pass
    time.sleep(1)


def solve():
    """Thực hiện 1 tính toán bất kì trong function `solve`

    Trả về kết quả tùy ý, gán lại vào `result`
    """
    result = worker()
    # Xoá dòng sau sau khi đã thay đổi your_decorator phù hợp
    # raise NotImplementedError("chưa thực hiện tính toán")

    a = 0
    while a < 10:
        a += 2
        time.sleep(1)
    result = worker()

    return result


def main():
    print("Function worker chạy mất: {0} giây".format(solve()))


if __name__ == "__main__":
    main()
