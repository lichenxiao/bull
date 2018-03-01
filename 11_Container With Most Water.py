#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 15:06
# @Author  : lichenxiao

class Solution(object):
    def maxArea1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        for i in range(len(height)):
            for j in range(i, len(height)):
                area = (j - i) * min(height[i], height[j])
                if area > max_area:
                    max_area = area
        return max_area

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        i = 0
        j = len(height) - 1
        while i < j:
            max_area = max(max_area, (j - i) * min(height[i], height[j]))
            if height[i] <height[j]:
                i += 1
            else:
                j -= 1
        return max_area


if __name__ == "__main__":
    s = Solution()
    print s.maxArea([2, 4, 5, 1, 4, 9])
