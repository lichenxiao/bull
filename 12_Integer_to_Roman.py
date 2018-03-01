#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 18:01
# @Author  : lichenxiao


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        if type(num) is not int:
            return ""
        if num < 1 or num > 3999:
            return ""

        Roman_list = [(1, 'I'), (5, 'V'), (10, 'X'), (50, 'L'), (100, 'C'), (500, 'D'), (1000, 'M')]
        Roman_list.reverse()
        print Roman_list

        res_list = []
        res_list.append(num / 1000 * 'M')
        num = num % 1000

        for index in [1, 3, 5]:
            li, lj = Roman_list[index - 1]
            ni, nj = Roman_list[index + 1]
            i, j = Roman_list[index]

            if num >= i:
                if num / ni == 9:
                    res_list.append(nj + lj)
                else:
                    res_list.append(j + (num - i) / ni * nj)
            else:
                if num/ni == 4:
                    res_list.append(nj + j)
                else:
                    res_list.append((num/ni)*nj)
            num = num % ni

        return ''.join(res_list)


if __name__ == '__main__':
    s = Solution()
    print s.intToRoman(555)
