#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools

def exception_handle(log_obj):
    """
    报错先自己记录log再向上层抛出异常,可用于类中魔法方法
    @param:log_obj:log对象异常 指定异常要存于哪个log
    """

    def inner1(func):
        @functools.wraps(func)
        def inner2(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                log_obj.error(e, exc_info=True)
                raise type(e)(e)

        return inner2

    return inner1
