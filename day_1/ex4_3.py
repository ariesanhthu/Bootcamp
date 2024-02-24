#!/usr/bin/env python3
import string

def solve(words):
    """Trả về list chứa điểm tương ứng của các từ trong `words`

    Nếu a b c d (không phân biệt chữ hoa thường) .... lần lượt bằng 1 2 3 4 ...
    thì từ ``attitude`` có giá trị bằng 100.

    Gợi ý::

      import string
      print(string.ascii_lowercase)
    """
    
    result = []

    for word in words:
        score = 0
        for character in word:
            score += ord(str(character))- ord('a') + 1

        result.append(score)

    return result


def main():
    words = [
        "numpy",
        "django",
        "saltstack",
        "discipline",
        "Python",
        "FAMILUG",
        "pymi",
        "attitude"
    ]

    print(solve(words))


if __name__ == "__main__":
    main()
