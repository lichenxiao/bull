#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 16:42
# @Author  : lichenxiao


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not (l1 and l2):
            return []
        if not l1:
            return l2
        if not l2:
            return l1

        carry = 0
        sum_list = []
        i = 0

        while i < len(l1) or i < len(l2) or carry:
            val_l1 = l1[i] if (i < len(l1)) else 0
            val_l2 = l2[i] if (i < len(l1)) else 0
            temp = val_l1 + val_l2 + carry
            if temp >= 10:
                carry = 1
                sum = temp - 10
            else:
                carry = 0
                sum = temp
            sum_list.append(sum)
            i += 1
        return sum_list


if __name__ == '__main__':
    l1 = [2, 3, 4]
    l2 = [5, 9, 9]

    c = Solution()
    res = c.addTwoNumbers(l1, l2)
    print res
