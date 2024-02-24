#!/usr/bin/env python3

"""
Bài tập không bắt buộc.

Cài đặt các chương trình dòng lệnh rất phổ biến viết bằng Python sau:

pip install asciinema youtube_dl httpie

httpie
======

Là một HTTP client (như curl, wget), có nhiều khả năng, trong đó có thể
tải file (-d)::

  http -d 'https://www.python.org/static/img/python-logo.png'


asciinema
=========

Chương trình "ghi lại" màn hình dòng lệnh (lưu thành file định dạng
JSON) rồi bạn có thể upload lên trang https://asciinema.org/. VD::

   asciinema rec pymi.cast

Xem ví dụ https://asciinema.org/a/241408
hoặc gõ trên máy, trong thư mục exercises::

   asciinema play ex7_8.cast

youtube-dl
==========

Tải file video từ Youtube::

    youtube-dl 'https://www.youtube.com/watch?v=BdPk9ipvczM'
"""


def solve(input_data):
    result = None

    return result


def main():
    print(solve(True))
