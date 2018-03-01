#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 11:58
# @Author  : lichenxiao

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False
        reverse_half_x = 0

        while x > reverse_half_x:
            reverse_half_x = reverse_half_x*10 + x%10
            x = x/10
        return x == reverse_half_x or x == reverse_half_x/10

if __name__ == "__main__":
    s = Solution()
    print s.isPalindrome(13531)