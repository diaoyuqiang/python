#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools as ft

# Defining the decorator
def hi(func):
    def wrapper():
        "Hi has taken over Hello Documentation"
        print("Hi geeks")
        func()

        # Note The following Steps Clearly

    # print(f'WRAPPER ASSIGNMENTS:{ft.WRAPPER_ASSIGNMENTS}')
    # print(f'UPDATES:{ft.WRAPPER_UPDATES}')

    # Updating Metadata of wrapper
    # using update_wrapper
    # functools.update_wrapper(wrapper, wrapped): 把被封装函数的name、module、doc和 dict都复制到封装函数去
    ft.update_wrapper(wrapper, func)
    return wrapper


@hi
def hello():
    "this is the documentation of Hello Function"
    print("Hey Geeks")


print(hello.__name__)
print(hello.__doc__)
# help(hello)