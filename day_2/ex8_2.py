#!/usr/bin/env python3

__doc__ = """
Yêu cầu: Viết script ex8_2.py:
- khi gọi với -h tên_file sẽ in ra 10 dòng đầu tiên của file (h == head),
- khi gọi với -t tên_file sẽ in ra 10 dòng cuối cùng của file (t == tail).

Usage::

  ex8_2.py -h file_path

  -> Print 10 first lines of file_path

  ex8_2.py -t file_path

  -> Print 10 last lines of file_path

Use ``sys.argv``
Đọc thêm: https://pymotw.com/3/sys/runtime.html#command-line-arguments
"""


import logging
import sys
from typing import List

logger = logging.getLogger(__name__)
file_path = 'ex8_2.txt'


def your_function(option: str, n: int, file_path: str) -> List[str]:
    """Trả về list chứa n dòng tùy thuộc vào `option` (-t hoặc -h) sau khi
    đọc dữ liệu từ file

    :param option: tùy chọn để in ra các dòng đầu hoặc cuối: -h hoặc -t
    :param file_path: đường dẫn tới file
    :rtype list:
    """
    result = None

    return result


def solve(option, file_path):
    """Hàm `solve` sử dụng với mục đích `test`, không cần chỉnh
    sửa gì thêm

    :param option: tùy chọn để in ra các dòng đầu hoặc cuối: -h hoặc -t
    :param file_path: đường dẫn tới file
    :rtype list:
    """
    # Lưu ý: sửa lại tên function của mình cho phù hợp
    logger.debug("Using %s option with file %s", option, file_path)

    n = 10
    # gán n = giá trị đọc được ở file ../setup.cfg trong section [flake8]
    # key max-line-length
    import os

    with open(os.path.join(os.path.dirname(__file__), "../setup.cfg")) as f:
        print(f.read())
    # Sử dụng thư viện có sẵn configparser
    # https://docs.python.org/3.6/library/configparser.html
    # để đọc file config này,
    # đây là định dạng tương tự file INI hay gặp trên Windows.
    # Các chương trình thường sử dụng các file cấu hình để chứa các giá trị
    # cần thay đổi cho chương trình thay vì viết trực tiếp vào file code
    # bao gồm cả user, password... Khi dùng git, tránh commit các file cấu
    # hình có chứa password để tránh bị lộ.
    # các file cấu hình thường theo format INI nói trên, JSON hay YAML.
    # Một cách khác hay gặp trên các hệ điều hành khác Windows là đọc từ
    # "biến môi trường" (environment var) bằng cách truy cập os.environ['KEY'].
    result = your_function(option, n, file_path)

    return result


def main():
    option, file_path = None, None

    # Viết code xử lí truyền 2 argument `option` và `file_path` bên dưới
    # option: tùy chọn để in ra các dòng đầu hoặc cuối: -h hoặc -t
    # file_path: đường dẫn tới file
    # Gợi ý: sử dụng sys.argv
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("chưa xử lí `argument`")
    option = sys.argv[1]
    file_path = sys.argv[0]
    
    lines = solve(option, file_path)
    for line in lines:
        line = line.rstrip()
        print(line)


if __name__ == "__main__":
    main()
