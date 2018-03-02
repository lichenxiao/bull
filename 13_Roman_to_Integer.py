#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 10:46
# @Author  : lichenxiao

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        for i in range(len(s)):
            num += Roman_dict[s[i]]
            if i >= 1:
                if Roman_dict[s[i - 1]] < Roman_dict[s[i]]:
                    num -= 2*Roman_dict[s[i - 1]]
        return num


if __name__ == "__main__":
    a = Solution()
    print a.romanToInt("MCMXCVI")
