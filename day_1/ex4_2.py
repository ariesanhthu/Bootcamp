#!/usr/bin/env python3

"""
break và continue

là 2 câu lệnh dùng trong vòng lặp (for/while).

continue (tiếp tục) sẽ ngay lập tức chuyển tới vòng lặp tiếp theo mà
không chạy phần code sau nó.

break sẽ thoát khỏi vòng lặp chứa nó.

```python
In [1]: for n in ['thit bo', 'mam tom', 'rau', 'la ngon', 'ca']:
   ...:     if n == 'mam tom':
   ...:         continue
   ...:     if n == 'la ngon':
   ...:         break
   ...:     print("Tôi ăn {}".format(n))
   ...:
Tôi ăn thit bo
Tôi ăn rau
```
Chú ý: không có dòng 'mam tom' (do continue), và cũng không có dòng
'la ngon', 'ca' (do break đã thoát khỏi vòng lặp khi gặp 'la ngon').
"""


def solve(octal):
    """Trả về giá trị cần cộng thêm với octal để thu được 0o777

    Với người dùng Unix(Ubuntu, MacOS,...), mode của một file được biểu diễn ở
    dạng Octal, VD: 644, 400, 777...

    Gợi ý:

    In [1]: oct(73)
    Out[1]: '0o111'
    """

    octalBaseValue = 0o777

    result = octalBaseValue - octal

    return result


def main():
    print(solve(0o644))


if __name__ == "__main__":
    main()
