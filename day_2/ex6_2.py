#!/usr/bin/env python3

# lst = []
def splitListToTuples(iterable, N):
    # Sửa tên, set giá trị return

    #numberOfElements
    num = len(iterable)

    result = [tuple(iterable[i:i+N]) for i in range(0, (num - num%N), N)]

    return result
    # pass


def solve(iterable, N):
    """Chia input_data thành các tuple chứa N phần tử (chunk a list).
    Nếu tuple cuối không đủ phần tử thì bỏ đi.
    """
    result = splitListToTuples(iterable, N)

    return result


def main():
    li = ["meo", "bo", "ga", "cho", "chim", "gau", "voi"]
    print(solve(li, 2))


if __name__ == "__main__":
    main()
