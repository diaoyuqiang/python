#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint, pformat

company = {
    "Apple":    {"founder": "Steven Jobs", "prodctions":["IPhone", "Mac"]}, "Site": "www.",
    "MicroSoft":{"founder": "Bill Gates", "prodctions": ["Windows", "Office","Xbox"]},
}

# 每行的长度默认是 60 个字符,对字典进行升序排序
pprint(company, width=60)
print(company)

name = 'admin'
# pformat: 写入字符串
with open('file_test.py', 'w') as f:
    f.write('company = ' + pformat(name))

import file_test
pprint(file_test.company)

