#!/usr/bin/env python3
import random

"""
Viết 1 một trò chơi đánh đối kháng giữa 2 nhân vật. Mỗi nhân vật có tên (str),
máu (int), vũ khí.
Vũ khí chọn random khi tạo nhân vật, có damage (int) bằng lượng máu trừ đi
khi đánh trúng.

Cho 2 nhân vật lần lượt đánh nhau, print kết quả mỗi lượt đánh, print người
thắng.

Đọc file class.md trong thư mục này.
"""


class Fighter:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.weapon = Weapon()


class Weapon:
    def __init__(self):
        self.damage = random.randint(1, 100)


def showResultofRound(round, player1, player2, status):
    print(f"\n Round {round}")

    if status != 0:
        print(f"Winner is: {(player2.name if status==1 else player1.name)}")
    else:
        print(
            f"Player {player1.name} damged {player2.name} \nHP of {player2.name}: {player2.hp} \n{player2.name} damged {player1.name} \nHP of {player1.name}: {player1.hp}"
        )


def solve(player1, player2):
    """Trả về tuple tên người thắng cuộc và lượng máu còn lại (int)"""
    result = ()
    roundFight = 1
    status = 0

    while player1.hp > 0 or player2.hp > 0:
        player2.hp -= player1.weapon.damage
        if player2.hp < 1:
            status = 1
            result = (player1.name, player1.hp)
            break
        player1.hp -= player2.weapon.damage
        if player1.hp < 1:
            status = 2
            result = (player2.name, player2.hp)
            break

        showResultofRound(roundFight, player1, player2, status)
        roundFight += 1

    showResultofRound(roundFight, player1, player2, status)

    return result


def main():
    # Thay đổi các dòng sau cho phù hợp
    player1 = Fighter("Nguyễn Phương Hằng", 1000)
    player2 = Fighter("Thuỷ Tiên", 100)
    print(solve(player1, player2))


"""
NOTE
sau khi thành thạo việc tạo 1 class và viết method, có thể
vào link sau lấy chứng chỉ Python basic của HackerRank
Rất dễ, làm 5-10 phút là xong.

https://www.hackerrank.com/skills-verification/python_basic
"""


if __name__ == "__main__":
    main()
