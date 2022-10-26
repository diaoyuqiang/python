#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

def get_load():
    """
    Get load average
    获取过去1、5和15分钟的平均负载
    """
    try:
        data = os.getloadavg()[0]
    except Exception as err:
        data = str(err)

    return data

print(get_load())