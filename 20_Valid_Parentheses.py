#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 15:38
# @Author  : lichenxiao

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # lparentheses_list = ['{', '[', '(']
        # rparentheses_list = [')', ']', '}']

        parentheses_dict = {')': '(',
                            '}': '{',
                            ']': '['}
        s_list = []
        for item in s:
            if item in parentheses_dict.values():
                s_list.append(item)
            elif item in parentheses_dict.keys():
                if not s_list or s_list.pop() != parentheses_dict[item]:
                    return False
        if s_list:
            return False

        return True

s = Solution()
print s.isValid('rew(fd)')