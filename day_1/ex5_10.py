#!/usr/bin/env python3

"""
[Không bắt buộc]

Bắt đầu từ góc trên bên trái của ô có kích thước 2x2, và chỉ cho phép di chuyển
sang phải hoặc xuống dưới, có chính xác 6 đường để đi đến góc dưới bên phải.

Có bao nhiêu đường như vậy trong ô 10x10?

Kiểm tra kết quả bằng https://projecteuler.net/problem=15
"""


def solve():
    result = None
    
    #2D array
    #store value in the path
    # A[i][j] = A[i-1][j] + A[i][j-1]

    # Viết code vào đây set result làm kết quả của tính toán
    #create 2D array 10*10
    rows, cols = (10,10)
    ArrayCount = [[0]*cols]*rows

    #init first column and first row by 1
    for i in range(cols):
        ArrayCount[0][i] = 1
        ArrayCount[i][0] = 1
        
    for i in range(1, rows):
        for j in range(1, cols):
            ArrayCount[i][j] = ArrayCount[i-1][j] + ArrayCount[i][j-1]

    result = ArrayCount[rows-1][cols-1] 

    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
