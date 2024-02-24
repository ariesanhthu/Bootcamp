#!/usr/bin/env python3
"""
Read:

- https://pymi.vn/tutorial/string1/
- https://www.familug.org/2015/07/go-strings-package-xu-ly-string.html
"""

data = """
Come to the
River
Of my
Soulful
Sentiments
Meandering silently
Yearning for release.
Hasten
Earnestly
As my love flows by
Rushing through the flood-gates
To your heart.
"""

# https://www.poetrysoup.com/poem/cross_my_heart_609765


def solve(input_data):
    """Trả về tiêu đề bài thơ ghép từ các chữ cái đầu tiên của mỗi dòng.
    Chỉ viết hoa chữ cái đầu tiên.

    chú ý thay đổi trên input_data chứ không dùng trực tiếp data.
    """
    ListLine = input_data.split('\n')
    
    result = ""

    for line in ListLine:
        if len(line):
            result += line[0]

    result.lower()
    result[0].upper()
    
    return result


def main():
    """
    Cross my heart là một bài thơ thuộc thể loại "acrostic".
    Khi ghép các chữ cái HOẶC các từ đầu tiên lại với nhau thu được một
    thông điệp
    """
    print(solve(data))
    print("Result should be Pymi: {}".format(solve("P\nY\nM\nI")))


if __name__ == "__main__":
    main()
