#!/usr/bin/env python
# -*- coding: utf-8 -*-
def get_mac_address():
    """
    获取mac地址
    :return:
    """
    try:
        import uuid
        node = uuid.getnode()  # 获取网络接口的mac地址(正整数)

        mac = uuid.UUID(int=node).hex[-12:]  # 根据mac地址生成uuid，并去除“-”后截取后12位
        return mac
    except:
        return False


print(get_mac_address())

print(2**10)