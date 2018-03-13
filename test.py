#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 12:09
# @Author  : lichenxiao


def letterCombinations(digits):
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
    digits = digits
    return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])


if __name__ == "__main__":
    print letterCombinations('')
    print reduce(lambda x, y: [a + b for a in x for b in y], ['123', '45'], [''])
