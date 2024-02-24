#!/usr/bin/env python3

"""
Input: một số nguyên trong range(1,13,1). # start=1, stop=13, step=1
Output: tên tương ứng của tháng đó bằng tiếng Anh, và số ngày trong tháng đó.
Tháng 2 tính 28 ngày.

Ví dụ:

- input_data: 2

- output: February 28
"""


def solve(input_data):
    """Trả về 1 `tuple` chứa 2 phần tử, ví dụ:

        input_data: 2
        output: ("February", 28)

    (1,2) là biểu diễn tương tự [1,2], chỉ thay dấu ngoặc vuông thành tròn.
    Đây là kiểu dữ liệu tuple.
    :param input_data: tháng bất kì
    :rtype: list
    """
    ListOfMonth = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    day = 0

    if input_data == 2: day = 28
    elif (input_data < 8 and input_data % 2) or (input_data > 7 and input_data % 2 == 0):
        day = 31
    else:
        day = 30

    result = (ListOfMonth[input_data-1], day)

    return result


def main():
    month, day = solve(2)
    print(month, day)


if __name__ == "__main__":
    main()
