import os
import smtplib
from email.mime.text import MIMEText

"""
Gửi email được thực hiện nhờ thư viện smtplib có sẵn của Python.
Giao thức dùng để gửi nhận email có tên là SMTP.
"""


def send_gmail(
    myemail, to_addresses, content="HIHIHI", subject="Hello from PyMivn"
):
    assert isinstance(
        to_addresses, list
    ), "to_addresses must be a list of emails"
    # Ví dụ này dùng gmail, nếu sử dụng các nhà cung cấp khác, cần thay
    # đổi các giá trị phù hợp.
    # Từ khóa: NHA_CUNG_CAP SMTP settings
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    # Gmail yêu cầu một số cài đặt để truy cập qua code.
    # Với tài khoản đăng nhập chỉ cần user/password, cần bật "Allow less secure
    # apps" tại
    # https://myaccount.google.com/lesssecureapps?gar=1

    # Với tài khoản dùng 2FA/MFA để đăng nhập
    # sử dụng link sau và tạo 1 "app password" rồi dùng thay password đăng nhập
    # https://myaccount.google.com/u/2/apppasswords

    # KHÔNG BAO GIỜ VIẾT PASSWORD VÀO TRONG CODE
    # hãy viết vào trong 1 file riêng, và nhớ không add file đó vào git.
    # ví dụ viết vào file .gmail.secret trong thư mục exercises
    with open(os.path.join(os.path.dirname(__file__), ".gmail.secret")) as f:
        app_password = f.read().strip()

    smtpserver.login(myemail, app_password)

    msg = MIMEText(content.encode("utf-8"), _charset="utf-8")
    msg["Subject"] = subject
    msg["From"] = myemail
    msg["To"] = ", ".join(to_addresses)

    smtpserver.sendmail(myemail, to_addresses, msg.as_string())


def main():
    YOUREMAIL = "FILL THIS BY YOUREMAIL"
    send_gmail(YOUREMAIL, [YOUREMAIL])
    print("sent")


if __name__ == "__main__":
    main()
