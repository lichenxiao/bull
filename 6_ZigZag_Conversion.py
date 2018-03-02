#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 17:54
# @Author  : lichenxiao

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        tuple_len = 2 * numRows - 2
        max_col = len(s) / tuple_len * 2
        if len(s) % tuple_len != 0:
            max_col += 1
        if (len(s) % tuple_len) > numRows:
            max_col += 1
        new_list = [''] * max_col * numRows

        for i in range(len(s)):
            col = i / tuple_len * 2
            row = i % tuple_len
            if row > numRows - 1:
                col += 1
                row = numRows - 1 - (row - numRows + 1)
            new_list[row * max_col + col] = s[i]
        return ''.join(new_list)


if __name__ == "__main__":
    s = Solution()
    print s.convert("ABCDEFGHIJKLMNOPQ", 6)
