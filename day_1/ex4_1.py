#!/usr/bin/env python3
"""
while loop

Dùng để lặp khi 1 điều kiện còn đúng:

```python
In [2]: i = 0

In [3]: while i < 5:
   ...:     print(i)
   ...:     i = i + 1
   ...:
0
1
2
3
4
```

Tham khảo:
- https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming
- https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
"""  # noqa


def solve(ip):
    """IP là địa chỉ của một máy tính trong mạng (như địa chỉ nhà).
    IPv4 được biểu diễn bằng 4 số từ 0-255, phân cách nhau bởi dấu `.`
    Mỗi số trong khoảng 0-255 được biểu diễn bằng 8 bits (1 byte),
    có tài liệu gọi 4 phần trong IPv4 này là 4 octet.
    VD: IP của Google DNS là 8.8.8.8, IP mọi máy tính dùng để chỉ chính nó
    có địa chỉ 127.0.0.1 hay thường gọi là localhost.

    Trả về string biểu diễn binary (hệ cơ số 2) của `ip`.

    Input::

      192.168.1.1

    Output::

      11000000.10101000.00000001.00000001

    Python có funtion đổi số integer thành biểu diễn ở hệ nhị phân (binary):

      In [1]: bin(168)
      Out[1]: '0b10101000'

    Khi s = '1', s.zfill(5) sẽ thêm đủ "zero" để tạo thành '00001'
    """
    result = ""
    ip = str(ip) + '.'

    while(ip):
      pos = ip.find('.')
      
      num = int(ip[:pos])
      
      num = bin(num).zfill(8)
      
      ip = ip[pos+1:]

      result += num + '.'

    result = result.removesuffix(".")

    return result


def main():
    """
    Biết function `input('Bạn tên gì?')` sẽ in ra màn hình dòng chữ "Bạn tên
    gì?"
    và chờ bạn nhập câu trả lời. Sau khi bạn gõ câu trả lời rồi enter,
    nội dung bạn vừa gõ sẽ được function trả về::

      In [4]: name = input('Bạn tên gì? ')
      Bạn tên gì? Hưng

      In [5]: print(name)
      Hưng

    Note::

      Trên Python2, function tương ứng tên là `raw_input`
    """

    ip = input("Nhập vào IP:")
    print(solve(ip))


if __name__ == "__main__":
    main()
