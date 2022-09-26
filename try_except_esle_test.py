#!/usr/bin/env python
# -*- coding: utf-8 -*-
def run():
    try:
        print(1/0)
    except Exception as e:
        print(e)
    else:
        print("okk")

if __name__ == '__main__':
    run()