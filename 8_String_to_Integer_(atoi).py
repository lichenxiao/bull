#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 19:32
# @Author  : lichenxiao
import sys
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0
        sign = 1
        if str[0] in ['+','-']:
            if str[0] == '-':
                sign = -1
            str = str[1:]
        num = 0
        for item in str:
            if item.isdigit():
                num = num*10 + int(item)
            else:
                break
        return max(-sys.maxint-1, min(sys.maxint, num*sign))

if __name__ == "__main__":
    s = Solution()
    print s.myAtoi("2147483648")