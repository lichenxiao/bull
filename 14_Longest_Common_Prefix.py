#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 16:30
# @Author  : lichenxiao

def get_same_prefix(s1, s2):
    i = min(len(s1), len(s2))
    for j in range(i):
        if s1[j] != s2[j]:
            return s1[0:j]
    return s1[0:i]

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        set = ()
        short_index = 0
        short_len = len(strs[0])
        for i in range(1, len(strs)):
            if len(strs[i]) < short_len:
                short_index = i
        same_prefix = strs[short_index]
        for i in range(len(strs)):
            if not same_prefix:
                return ''
            if i == short_index:
                pass
            same_prefix = get_same_prefix(strs[i], same_prefix)
        return same_prefix

if __name__ == "__main__":
    a = Solution()
    b = ['fdffdf', 'f', 'fd']
    print a.longestCommonPrefix(b)
