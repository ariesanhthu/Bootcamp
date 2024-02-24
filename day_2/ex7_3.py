#!/usr/bin/env python3


__doc__ = """
Yêu cầu:
- Dùng pip cài thư viện PyYAML, import yaml và dùng `yaml.safe_load` để biến nội
dung trong file thành kiểu dữ liệu trên Python.

- In ra số phần tử của kiểu dữ liệu vừa tạo. Dùng thư viện json để
 `json.dump` nội dung, ghi ra một file tên là event.json trong thư mục hiện tại.

- Dùng thư viện pickle để pickle.dump nội dung trên ra file event.pkl trong
  thư mục hiện tại. Chú ý khi mở file, phải mở ở chế độ ghi ở dạng binary. Đọc
  thêm tại đây:
  https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files`

- In ra kích thước của mỗi file đã tạo.

Gợi ý: sử dụng os.stat(filename).st_size
Read: open multiple files https://docs.python.org/3/reference/compound_stmts.html#with
"""  # NOQA


import json  # NOQA
import os  # NOQA
import pickle  # NOQA
import yaml  # NOQA


path = 'exercises\day_2\event.yaml'

def your_function():
    """Trả về số phần tử của kiểu dữ liệu sau khi dùng module `yaml` để load

    Thực hiện các yêu cầu tại ``__doc__``

    :rtype int:
    """
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    result = None

    return result


def solve():
    """không cần viết code trong hàm `solve`, chỉ thực hiện
    đổi tên lại function của mình cho phù hợp

    :rtype int:
    """
    result = your_function()

    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
