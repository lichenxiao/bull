#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 18:57
# @Author  : lichenxiao

class Solution(object):
    """
    Given a string, find the length of the longest substring without repeating characters.
    Examples:
        Given "abcabcbb", the answer is "abc", which the length is 3.
        Given "bbbbb", the answer is "b", with the length of 1.
        Given "pwwkew", the answer is "wke", with the length of 3.
        Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
    """

    def lengthOfLongestSubstring_1(self, s):
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

    def lengthOfLongestSubstring_2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        item_set = set()
        max_start = 0
        max_end = 0
        j = 0
        i = 0
        while i < len(s) and j < len(s):
            if s[j] in item_set:
                item_set.remove(s[i])
                if j - i > max_end - max_start:
                    max_start = i
                    max_end = j - 1
                i += 1
            else:
                item_set.add(s[j])
                j += 1
        if j - i > max_end - max_start:
            max_start = i
            max_end = j-1
        return max_end - max_start + 1, s[max_start:max_end + 1]


if __name__ == '__main__':
    s = Solution()
    print s.lengthOfLongestSubstring_2("dvvvvdf")
