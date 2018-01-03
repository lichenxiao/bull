#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 16:42
# @Author  : lichenxiao

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order and each of their nodes contain a single digit.
    Add the two numbers and return it as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example
        Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 0 -> 8
        Explanation: 342 + 465 = 807.
    """

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
        sum_obj = ListNode(0)
        sum_head = sum_obj

        while l1 or l2 or carry:
            val_l1 = l1.val if l1 else 0
            val_l2 = l2.val if l2 else 0
            temp = val_l1 + val_l2 + carry
            if temp >= 10:
                carry = 1
                sum = temp - 10
            else:
                carry = 0
                sum = temp
            sum_obj.val = sum
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if l1 or l2 or carry:
                sum_obj.next = ListNode(0)
                sum_obj = sum_obj.next
            else:
                sum_obj.next = None
        res_list = []
        item = sum_head
        while item:
            res_list.append(item.val)
            item = item.next
        return res_list
        #return sum_head


if __name__ == '__main__':
    # node11 = ListNode(2)
    # node12 = ListNode(4)
    # node13 = ListNode(3)
    # node11.next = node12
    # node12.next = node13
    # node13.next = None
    #
    # node21 = ListNode(2)
    # node22 = ListNode(4)
    # node23 = ListNode(3)
    # node21.next = node22
    # node22.next = node23
    # node23.next = None

    node11 = ListNode(5)
    node11.next = None
    node21 = ListNode(5)
    node21.next = None

    c = Solution()
    res = c.addTwoNumbers(node11, node21)
    print res
