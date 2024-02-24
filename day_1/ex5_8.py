#!/usr/bin/env python3
import string

def solve():

    """Trả về biểu diễn của 20 mã ASCII từ 33 đến 53 theo format
    [(33, BIEUDIENCUA33), ...]
    Unicode codepoint của các số từ 0->9, a-z, A-Z.
    Unicode codepoint tương ứng với ký tự ``\t`` ``\n``, `` ``

    Gợi ý: dùng ``chr()``, ``ord()``.
    """
    result = None

    return result


def main():
    for part in solve():
        print(part)
        if isinstance(part, list):
            for elem in part:
                print(elem)


if __name__ == "__main__":
    main()
