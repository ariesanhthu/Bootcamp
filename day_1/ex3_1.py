#!/usr/bin/env python3
data = 1000


def solve(input_data):
    """Đầu vào: một số nguyên dương

    Đầu ra: số nguyên tạo bởi phần từ số 1 cuối cùng trở về bên
    phải - của dạng binary của số đầu vào.

    Ví dụ::

      input_data = 5 # (0b101)
      output = 1

      input_data = 24 (11000)
      output = 1000

      input_data = 9 (1001)
      output = 1

    Hàm có sẵn: bin(10) == '0b1010'
    Hàm có sẵn tạo ra integer từ string: 69 == int('69')
    """
    # convert base 10 to base 2
    binary = bin(input_data)

    # find the first 1 from the right
    positionFirstOf1 = binary.rfind('1')

    # copy string to result
    result = int(binary[positionFirstOf1:])

    # code here

    return result

def main():
    print(solve(data))

if __name__ == "__main__":
    main()
