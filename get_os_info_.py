#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import platform

def get_platform():
    """
    Get the OS name, hostname and kernel
    """
    try:
        # uname = platform.uname()  # 获取操作系统信息
        info = os.uname()  # 获取操作系统信息
        print("""
            操作系统: %s
            主机名: %s
            内核版本: %s
            硬件架构: %s
        """ % (info.sysname, info.nodename, info.release, info.machine))

        data = {'osname': info.sysname, 'hostname': info.nodename, 'kernel': info.release}

    except Exception as err:
        data = str(err)

    return data

# print(get_platform())
print(platform.uname())  # 返回操作系统名称, 机器名称(主机名), 操作系统版本号, 处理器信息