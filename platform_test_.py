#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform  # 跨平台

print(platform.platform())  # 操作系统名称及版本号

print(platform.python_build())  # python内部的版本号及日期

print(platform.python_version())  # python版本号

print(platform.system())  # 操作系统的名称

print(platform.version())  # 操作系统的版本号

print(platform.processor())  # 处理器名称

print(platform.machine())  # 平台架构

print(platform.node())  # 计算机的网络名称(主机名)

print(platform.uname())  # 系统元祖信息