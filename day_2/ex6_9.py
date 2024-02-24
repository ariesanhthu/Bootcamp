"""
Kết hợp bài 6_6 và 6_8, truy cập vào trang ketqua.net, lấy kết quả
giải đặc biệt rồi gửi tới email của chính bạn.

Trên Ubuntu/Mac, gõ lệnh crontab -e
rồi thêm dòng sau để chạy code này lúc 18h35 hàng ngày nếu máy tính đang bật.

35 18 * * * python3 /home/hvn/me/pyfml/exercises/ex6_9.py

Thay đường dẫn trên bằng đường dẫn thật trên máy bạn.
"""

import urllib.request
from ex6_8 import send_gmail

# bài này khó. cx chưa cần làm


def main():
    # Không dùng trực tiếp được do ketqua.net chặn Python
    # f = urllib.request.urlopen("https://ketqua.net")

    # Đổi User-Agent header để đóng giả làm trình duyệt Firefox
    req = urllib.request.Request(
        url="https://ketqua.net",
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"  # noqa
        },
    )
    with urllib.request.urlopen(req) as f:
        content = f.read().decode()

    special_prize = ""
    for line in content.splitlines():
        if "Đặc biệt" in line:
            # print(line)
            special_prize = line.split("</td>")[1][-5:]
            break

    date = ""
    for line in content.splitlines():
        if "Xổ số Truyền Thống" in line:
            # print(line)
            date = line.split("ngay=")[1][:10]
            break

    subject = "Kết quả xổ số ngày {}".format(date)
    content = "Giải đặc biệt ngày {} là: {}".format(date, special_prize)
    YOUREMAIL = "TODO"
    send_gmail(YOUREMAIL, [YOUREMAIL], subject=subject, content=content)


if __name__ == "__main__":
    main()
