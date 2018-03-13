#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 11:04
# @Author  : lichenxiao
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if '' == digits: return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return reduce(lambda x, y: [a + b for a in x for b in kvmaps[y]], digits, [''])

if __name__ == "__main__":
    s = Solution()
    print s.letterCombinations('23')