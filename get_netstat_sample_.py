#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

def get_netstat():
    """
    Get ports and applications
    """
    data = []
    try:
        # 查看已经建立的tcp套接字端口跟ip信息
        pipe = os.popen(
            "ss -tnp | grep ESTAB | awk '{print $4, $5}'| sed 's/::ffff://g' | awk -F: '{print $1, $2}' "
            "| awk 'NF > 0' | sort -n | uniq -c")  # sort -n | uniq -c: 根据
        data = pipe.read().strip().split('\n')
        pipe.close()

        data = [i.split(None, 4) for i in data]

    except Exception as err:
        ret = str(err)

    return data
