#!/usr/bin/env python3

import json
import urllib.request

"""
Read https://docs.python.org/3/howto/urllib2.html#urllib-howto
"""


def repositories(github_login):
    """
    Trả về list name của các repos của GitHub user github_login
    """
    with urllib.request.urlopen(
        "https://api.github.com/users/{}/repos".format(github_login)
    ) as f:
        repos = json.load(f)
        print(repos[0])
    # Sửa function cho phù hợp, trả về kết quả yêu cầu.
    result = None

    return result




def solve(input_data):
    return repositories(input_data)


def main():
    for repo_name in solve("pallets"):
        print(repo_name)
        # print('hàm Main')


if __name__ == "__main__":
    main()
