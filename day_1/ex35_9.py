#!/usr/bin/env python3


def diff_attributes(object1, object2):
    """
    Biết dir(5) trả về list các attribute của object 5 (gồm cả method).
    dir([]) trả về list các attribute của object empty list (list rỗng).

    Một attribute được gọi là magic nếu nó có tên bắt đầu và kết thúc bằng `__`
    "Magic" attribute được Python dùng với ý nghĩa đặc biệt, người dùng không
    nên tự đặt tên theo kiểu magic này.

    Tìm list các "magic" attribute mà chỉ object1 có, object2 không có
    """
    result = None


    return result

def solve(input_data):
    result = diff_attributes(*input_data)
    return result


def main():
    input_data = ([], "")
    print(
        "Các attribute mà chỉ {0} có còn {1} thì không:".format(
            type(input_data[0]), type(input_data[1])
        )
    )
    print(solve(input_data))


if __name__ == "__main__":
    main()
