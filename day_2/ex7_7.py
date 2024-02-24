#!/usr/bin/env python3

import xml.etree.ElementTree as ET  # NOQA


data = """<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
"""


def country_ranks(xmldata):
    """Python hỗ trợ xử lý file định dạng XML/HTML. Sử dụng thư viện
    xml.etree.ElementTree có thể dễ dàng "parse" các văn bản định dạng XML/HTML
    (biến từ text thành dữ liệu có cấu trúc).

    https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree  # NOQA

    Trả về list các tuple (tên quốc gia, thứ hạng)
    """

    result = None

    return result


def solve(input_data):
    result = country_ranks(data)
    return result


def main():
    print(solve(data))


if __name__ == "__main__":
    main()
