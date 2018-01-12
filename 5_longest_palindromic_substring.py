#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/3 11:42
# @Author  : lichenxiao


def judge_if_palindrome(s):
    if len(s) >= 2:
        if s[0] == s[-1]:
            return judge_if_palindrome(s[1:-1])
    else:
        if len(s) in [0, 1]:
            return True
    return False


def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1


class Solution(object):
    """
    Given a string s, find the longest palindromic substring in s.
    You may assume that the maximum length of s is 1000.

    Example:
        Input: "babad"
        Output: "bab"
        Note: "aba" is also a valid answer.
    Example:
        Input: "cbbd"
        Output: "bb"
    """

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindromic_str = ''
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                res = judge_if_palindrome(s[i:j])
                if res:
                    if j - i > len(palindromic_str):
                        palindromic_str = s[i:j]
        return palindromic_str

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = expand(s, i, i)
            len2 = expand(s, i, i + 1)
            max_i = len1 if len1 > len2 else len2
            if max_i > end - start + 1:
                end = i + max_i / 2
                start = i - (max_i - 1) / 2
        return s[start:end + 1]

    def longestPalindrome3(self, s):
        new_s = '^#' + '#'.join(list(s)) + '#$'
        new_s_len = len(new_s)
        P = [0] * new_s_len
        C = 0 #以检查过回文字字符串边界的中心
        R = 0 #检查过回文字字符串的边界

        for i in range(1, new_s_len - 1):
            if R > i:
                P[i] = min(R - i, P[2 * C - i])
            while new_s[i + 1 + P[i]] == new_s[i - 1 - P[i]]:
                P[i] += 1
            if i + P[i] > R:
                C, R = i, i + P[i]

        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen) / 2: (centerIndex + maxLen) / 2]


if __name__ == '__main__':
    s = Solution()
    str_p = s.longestPalindrome3('abcbca')
    print str_p

    # print expand('abba', 1, 2)
