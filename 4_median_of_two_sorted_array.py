#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 19:28
# @Author  : lichenxiao
def median_of_two_sort_list(nums1, nums2):
    all_len = len(nums1) + len(nums2)
    if all_len % 2 == 0:
        last = all_len / 2 + 1
    else:
        last = (all_len + 1) / 2

