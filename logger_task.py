#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import logging

logger = logging.getLogger("uer")  # 生成日志处理器
logger.setLevel(logging.DEBUG)  # 设置日志等级
logger.addHandler(logging.StreamHandler())  # 处理器输出到标准错误输出

logger.info("正常")
logger.error("错误")