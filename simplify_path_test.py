#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 目录优化器
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        lpath = [v for v in path.split("/") if v != "." and v != ""]
        print(lpath)
        res = []
        for i in range(len(lpath)):
            if lpath[i] == '..':
                if i-1 >= 0:
                    res = res[:-1]
            else:
                res.append(lpath[i])
        print(res)
        return '/'+'/'.join(res)


s = Solution()
sp = s.simplifyPath('/home//foo/')  # 根目录简化
print(sp)

# r = [1]
# print(r[:-1]) # 左闭右开
# print('/'.join(r))
# sr = '/home//foo/'
# print(sr.split('/'))