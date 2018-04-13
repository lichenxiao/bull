#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 17:47
# @Author  : lichenxiao
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if type(n) != int:
            return []
        if n <= 0:
            return []
        return self.gP()

    def gP(self, n):
        if n == 1:
            return ['()']
        if n == 2:
            return ['(())', '()()']


