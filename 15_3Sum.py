#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/5 12:48
# @Author  : lichenxiao

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res_set = set()
        sum_dict = {}
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if -sum not in sum_dict:
                    sum_dict[-sum] = [(i, j)]
                else:
                    sum_dict[-sum].append((i, j))
        for i in range(len(nums)):
            if nums[i] in sum_dict:
                for item in sum_dict[nums[i]]:
                    if i not in item:
                        a, b, c = nums[i], nums[item[0]], nums[item[1]]
                        res_set.add(tuple(sorted([a, b, c])))
        res_list = []
        for item in res_set:
            res_list.append(list(item))
        return res_list

    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res_list = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    res_list.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
        return res_list


s = Solution()
print s.threeSum2([-1, 0, 1, 2, -1, -4])
