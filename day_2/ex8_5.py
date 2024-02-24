#!/usr/bin/env python3
import tempfile
import unittest

"""unittest là thư viện dùng để viết code test code khác.
Để tạo một "testcase", cần định nghĩa 1 class kế thừa unittest.TestCase,
tên class phải bắt đầu bằng chữ Test. Các method để test cũng phải bắt
đầu bằng ``test_``. Test nào khi chạy mà sai sẽ raise AssertionErrror
exception.
Tham khảo thêm các test trong thư mục tests/

Tài liệu: https://docs.python.org/3/library/unittest.html
https://pymotw.com/3/unittest/index.html#module-unittest
"""


def factorial(n: int) -> int:
    if n <= 0:
        return 1
    return n * factorial(n - 1)


class TestFactorial(unittest.TestCase):
    def test_factorial_0_is_1(self):
        self.assertEqual(1, factorial(0))

    def test_factorial_3_is_6(self):
        self.assertEqual(6, factorial(3))

    def test_factorial_4_is_24(self):
        self.assertEqual(120, factorial(5))


def solve() -> bool:
    """
    Sửa lại các test case trong TestFactorial cho đúng.
    """
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFactorial)

    _, fn = tempfile.mkstemp()
    with open(fn, "w") as tmpf:
        r = unittest.TextTestRunner(stream=tmpf, verbosity=2).run(suite)
        print(dir(r))
    return r.wasSuccessful()


def main() -> None:
    test_result = solve()
    print("Test was successful? ", test_result)


if __name__ == "__main__":
    main()
