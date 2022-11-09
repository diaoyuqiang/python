#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

s = "192.0.0.1?!289.0.0.1!0.0.0.0!192.163.10.20?192.0.0.1"
ips = re.split(r"\?!|!|\?", s)


def last_one(i):
    return i.split('.')[-1]


ips.sort(key=last_one)
print(ips)

