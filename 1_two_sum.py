#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/3 11:42
# @Author  : lichenxiao
class Solution(object):
    """
        Given an array of integers,
        return indices of the two numbers such that they add up to a specific target.
        You may assume that each input would have exactly one solution,
        and you may not use the same element twice.

    Example:
        Given nums = [2, 7, 11, 15], target = 9,
        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
    """

    def twoSum_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return []
        for i in range(len(nums)):
            other = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == other:
                    return [i, j]
        return []

    def twoSum_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return []
        temp_dict = {}
        for i in range(len(nums)):
            if nums[i] not in temp_dict.keys():
                temp_dict[target - nums[i]] = i
            else:
                return [temp_dict[nums[i]], i]
        return []
