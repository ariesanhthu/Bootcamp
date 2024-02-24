"""Tính số nghiệm của bài toán lớp 3

Với các biến a,b,c,d,e,f,g,h,i là các số nằm trong khoảng 1-9 (các biến có
thể có giá trị giống nhau), dạng biểu thức:

    a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10 = 66
"""

import time

start = time.time()
result = 0
for b in range(1,10):
    for c in range(1,10):
        for d in range(1,10):
            for e in range(1,10):
                for f in range(1,10):
                    for g in range(1,10):
                        for h in range(1,10):
                            for i in range(1,10):
                                a = - 13 * b / c - d - 12 * e + f + 11 - g * h / i + 10 - 66
                                if a > 0 and a < 10:
                                    result += 1
                                    print(result)
print(result)
print("Took: {} with new For loop".format(time.time() - start))