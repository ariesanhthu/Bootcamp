"""
Code Python thường chạy tuần tự, một lúc chỉ làm duy nhất một việc.
Để có thể làm nhiều việc cùng lúc, xuất hiện khái niệm mới tên là "concurrency"
https://docs.python.org/3/library/concurrency.html
được thực hiện qua các thư viện threading, multiprocessing, ...

Thư viện concurrent.futures cung cấp một phương pháp đơn giản trông như map, có
thể thực hiện nhiều việc (tương tự nhau) cùng lúc.
"""

import time
from concurrent.futures import ProcessPoolExecutor


def do_sum(n):
    s = 0
    for i in range(n):
        s = s + i
    return s


def main():
    ns = [100_000_000] * 8

    # Sequential
    start = time.time()
    sequential_results = list(map(do_sum, ns))
    print(
        "Result: {} Took: {} seconds".format(
            sequential_results, time.time() - start
        )
    )

    # Concurrent
    executor = ProcessPoolExecutor()
    start = time.time()
    concurrent_results = list(executor.map(do_sum, ns))
    print(
        "Result: {} Took: {} seconds".format(
            concurrent_results, time.time() - start
        )
    )
    assert sequential_results == concurrent_results


if __name__ == "__main__":
    main()
