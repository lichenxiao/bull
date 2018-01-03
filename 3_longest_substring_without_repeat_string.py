#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 18:57
# @Author  : lichenxiao

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if type(s) != str:
            return 0, ''
        if not s:
            return 0, ''
        max_s = ''
        max_len = 0

        for i in range(len(s)):
            if (len(s) - 1 - i) <= max_len:
                break
            ret_s = s[i]
            for j in range(i + 1, len(s)):
                if s[j] not in ret_s:
                    ret_s += s[j]
                else:
                    if len(ret_s) > max_len:
                        max_s = ret_s
                        max_len = len(ret_s)
                    break
            if len(ret_s) > max_len:
                max_s = ret_s
                max_len = len(ret_s)

        return max_len, max_s


if __name__ == '__main__':
    s = Solution()
    print s.lengthOfLongestSubstring("pwwkew")
