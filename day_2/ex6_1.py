#!/usr/bin/env python3

data = {"first_50": 1230, "from_51_to_100": 1530, "above_100": 1786}


def calculate_cost(usage, prices):
    """Tính tiền điện
    với giá tiền cho bởi đề bài, số điện tiêu thụ `usage`
    Trả về giá tiền ở dạng biểu diễn cho người đọc dễ nhìn
    Ví dụ: 100000 -> "100,000"

    Biết:

    In [1]: "{:,}".format(10000) == "10,000"
    Out[1]: True
    """
    # Viết code tính toán vào đây
    result = None

    return result
    # pass


def solve(input_data):
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Bạn chưa làm bài này")

    # Bài này làm mẫu, gọi function định nghĩa với input để
    # tính kết quả.
    # Các bài còn lại tự định nghĩa function và gọi function để
    # tính toán kết quả `result`
    result = [
        (i[0].title(), calculate_cost(i[1], input_data["prices"])) for i in input_data["usages"]
    ]

    return result


def main():
    """
    Cho tiền điện sinh hoạt được tính theo công thức:

    - 50 số đầu: 1230 VND/số.
    - 50 số tiếp: 1530 VND/số.
    - Các số tiếp theo: 1786 VND/số.
    """
    idata = {
        "usages": [
            ("nam", "1"),
            ("pikalong", "29"),
            ("phan quan", "1235"),
            ("maria", "69"),
            ("trump", "100"),
        ],
        "prices": data,
    }
    print(solve(idata))


# __name__ là một biến|name đặc biệt do Python tự tạo ra
# nó có giá trị là string "__main__" khi file được chạy bằng lệnh
# python filename.py
# và có giá trị là tên file (bỏ .py) khi được import.
if __name__ == "__main__":
    # print(__name__)
    main()
