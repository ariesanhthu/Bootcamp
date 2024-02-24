#!/usr/bin/env python3


GOOD = 1
NEUTRAL = 0
BAD = -1


def solve(year1, year2):
    """Trả về tuple-3 chứa tên gọi can chi của year1, year2, và giá trị số xem
    2 tuổi này có họp hay không.

    - 1 đại diện cho hợp
    - 0 đại diện cho bình thường
    - -1 đại diện cho khắc

    Các từ trong tên đề phải viết hoa các chữ cái đầu.

    Biết có 10 thiên can::

      ['giáp', 'ất', 'bính', 'đinh', 'mậu', 'kỷ', 'canh', 'tân', 'nhâm', 'quý']

    Và 12 địa chi::

      ['tý', 'sửu', 'dần', 'mão', 'thìn', 'tị', 'ngọ', 'mui', 'thân', 'dậu',
       'tuất', 'hợi']

    Tứ hành xung: theo cặp "dần-thân", "tị-hợi" khắc nhau, còn "dần-tị/dần-hợi"
    chỉ xung nhẹ (coi là bình thường) chứ không khắc.

      ["dần", "thân", "tị", "hợi"]
      ["tý", "ngọ", "mão", "dậu"]
      ["thìn", "tuất", "sửu", "mùi"]

    Tam hợp: chỉ cần trong mỗi list là đều hợp:

      ["thân", "tý", "thìn"] - Nhóm kiên trì
      ["tị", "dậu", "sửu"] - Nhóm trí thức
      ["dần", "ngọ", "tuất"] - Nhóm độc lập
      ["hợi", "mão", "mùi"] - Nhóm ngoại giao

    Năm 2017 là năm "Đinh Dậu".

    https://vansu.net/tam-hop-tu-hanh-xung.html
    """
    result = None


    return result


def main():
    this = 1986
    that = 2002
    thiscc, thatcc, isgood = solve(this, that)
    if isgood == GOOD:
        result = "hợp"
    elif isgood == BAD:
        result = "xung"
    elif isgood == NEUTRAL:
        result = "bình thường - hợp ăn hợp ngủ là được"
    else:
        raise ValueError("Bad value {}".format(isgood))

    print(
        "Năm {0}({1}), năm {2}({3}): {4}".format(
            this, thiscc, that, thatcc, result
        )
    )


if __name__ == "__main__":
    main()

