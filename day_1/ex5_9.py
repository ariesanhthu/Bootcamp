#!/usr/bin/env python3
from operator import itemgetter
data = [
    {"name": "An Giang", "population": 2153700, "area": 3536.7, "senator": 10},
    {
        "name": "Bà Rịa - Vũng Tàu",
        "population": 1039200,
        "area": 1989.5,
        "senator": 6,
    },
    {"name": "Bạc Liêu", "population": 873400, "area": 2468.7, "senator": 6},
    {"name": "Bắc Kạn", "population": 301000, "area": 4859.4, "senator": 6},
    {"name": "Bắc Giang", "population": 1588500, "area": 3848.9, "senator": 8},
    {"name": "Bắc Ninh", "population": 1079900, "area": 822.7, "senator": 6},
    {"name": "Bến Tre", "population": 1258500, "area": 2357.7, "senator": 7},
    {
        "name": "Bình Dương",
        "population": 1748000,
        "area": 2694.4,
        "senator": 8,
    },
    {"name": "Bình Định", "population": 1501800, "area": 6050.6, "senator": 8},
    {"name": "Bình Phước", "population": 912700, "area": 6871.5, "senator": 6},
    {
        "name": "Bình Thuận",
        "population": 1193500,
        "area": 7812.8,
        "senator": 7,
    },
    {"name": "Cà Mau", "population": 1217100, "area": 5294.9, "senator": 7},
    {"name": "Cao Bằng", "population": 515200, "area": 6707.9, "senator": 6},
    {"name": "Cần Thơ", "population": 1214100, "area": 1409, "senator": 7},
    {"name": "Đà Nẵng", "population": 973800, "area": 1285.4, "senator": 6},
    {"name": "Đắk Lắk", "population": 1796700, "area": 13125.4, "senator": 9},
    {"name": "Đắk Nông", "population": 543200, "area": 6515.6, "senator": 6},
    {"name": "Đồng Nai", "population": 2720800, "area": 5907.2, "senator": 11},
    {"name": "Đồng Tháp", "population": 1676300, "area": 3377, "senator": 8},
    {"name": "Điện Biên", "population": 519300, "area": 9562.9, "senator": 6},
    {"name": "Gia Lai", "population": 1342700, "area": 15536.9, "senator": 7},
    {"name": "Hà Giang", "population": 758000, "area": 7914.9, "senator": 6},
    {"name": "Hà Nam", "population": 790000, "area": 860.5, "senator": 6},
    {"name": "Hà Nội", "population": 6844100, "area": 3323.6, "senator": 30},
    {"name": "Hà Tĩnh", "population": 1230500, "area": 5997.8, "senator": 7},
    {"name": "Hải Dương", "population": 1735100, "area": 1656, "senator": 9},
    {"name": "Hải Phòng", "population": 1904100, "area": 1523.9, "senator": 9},
    {"name": "Hòa Bình", "population": 806100, "area": 4608.7, "senator": 6},
    {"name": "Hậu Giang", "population": 769700, "area": 1602.5, "senator": 6},
    {"name": "Hưng Yên", "population": 1145600, "area": 926, "senator": 7},
    {
        "name": "TP. Hồ Chí Minh",
        "population": 7681700,
        "area": 2095.6,
        "senator": 30,
    },
    {"name": "Khánh Hòa", "population": 1183000, "area": 5217.7, "senator": 7},
    {
        "name": "Kiên Giang",
        "population": 1726200,
        "area": 6348.5,
        "senator": 9,
    },
    {"name": "Kon Tum", "population": 462400, "area": 9689.6, "senator": 6},
    {"name": "Lai Châu", "population": 397500, "area": 9068.8, "senator": 6},
    {"name": "Lào Cai", "population": 646800, "area": 6383.9, "senator": 6},
    {"name": "Lạng Sơn", "population": 744100, "area": 8320.8, "senator": 6},
    {"name": "Lâm Đồng", "population": 1234600, "area": 9773.5, "senator": 7},
    {"name": "Long An", "population": 1458200, "area": 4492.4, "senator": 8},
    {"name": "Nam Định", "population": 1836900, "area": 1652.6, "senator": 9},
    {"name": "Nghệ An", "population": 2952000, "area": 16490.9, "senator": 13},
    {"name": "Ninh Bình", "population": 915900, "area": 1376.7, "senator": 6},
    {"name": "Ninh Thuận", "population": 576700, "area": 3358.3, "senator": 6},
    {"name": "Phú Thọ", "population": 1335900, "area": 3533.4, "senator": 7},
    {"name": "Phú Yên", "population": 877200, "area": 5060.6, "senator": 6},
    {"name": "Quảng Bình", "population": 857900, "area": 8065.3, "senator": 6},
    {
        "name": "Quảng Nam",
        "population": 1450100,
        "area": 10438.4,
        "senator": 8,
    },
    {"name": "Quảng Ngãi", "population": 1227900, "area": 5153, "senator": 7},
    {
        "name": "Quảng Ninh",
        "population": 1177200,
        "area": 6102.3,
        "senator": 7,
    },
    {"name": "Quảng Trị", "population": 608100, "area": 4739.8, "senator": 6},
    {"name": "Sóc Trăng", "population": 1301900, "area": 3311.6, "senator": 7},
    {"name": "Sơn La", "population": 1134300, "area": 14174.4, "senator": 7},
    {"name": "Tây Ninh", "population": 1089900, "area": 4039.7, "senator": 6},
    {"name": "Thái Bình", "population": 1868800, "area": 1570, "senator": 9},
    {
        "name": "Thái Nguyên",
        "population": 1150200,
        "area": 3534.7,
        "senator": 7,
    },
    {
        "name": "Thanh Hóa",
        "population": 3426600,
        "area": 11132.2,
        "senator": 16,
    },
    {
        "name": "Thừa Thiên - Huế",
        "population": 1114500,
        "area": 5033.2,
        "senator": 7,
    },
    {
        "name": "Tiền Giang",
        "population": 1692500,
        "area": 2508.3,
        "senator": 8,
    },
    {"name": "Trà Vinh", "population": 1015300, "area": 2341.2, "senator": 6},
    {
        "name": "Tuyên Quang",
        "population": 738900,
        "area": 5867.3,
        "senator": 5,
    },
    {"name": "Vĩnh Long", "population": 1033600, "area": 1504.9, "senator": 6},
    {"name": "Vĩnh Phúc", "population": 1020600, "area": 1236.5, "senator": 6},
    {"name": "Yên Bái", "population": 764400, "area": 6886.3, "senator": 7},
]


def solve(input_data):
    """Dùng list comprehensions để:

    - Tạo 1 list chứa tên, dân số của các thành phố có tên bắt đầu bằng chữ H,
    sắp xếp theo thứ tự tên A-Z.

    - Tạo 1 list chứa tên, dân số của các thành phố có dân số trên 1 triệu,
    sắp xếp theo thứ tự giảm dần.
    """
    result = None

    return result


def main():
    provinces = data
    for L in solve(provinces):
        for province in L:
            print(province)


if __name__ == "__main__":
    main()
