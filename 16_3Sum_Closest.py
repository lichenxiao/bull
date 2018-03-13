#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 17:16
# @Author  : lichenxiao

import sys


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        distance = target - nums[0] - nums[1] - nums[2]

        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
                else:
                    return target
                d = target - s
                if abs(d) < abs(distance):
                    distance = d
        return target - distance


s = Solution()
a = s.threeSumClosest([1, 6, 9, 14, 16, 70], 81)
print a
