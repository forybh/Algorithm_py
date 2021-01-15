#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 13:44:46 2021

@author: yubyeongheon
"""

def solution(numbers, target):
    answer = 0
    
    start1 = numbers[0]
    start2 = -numbers[0]
    target1 = target - start1
    target2 = target - start2
    if len(numbers[1:]) == 0:
        if target1 == 0 and target2 == 0:
            return 2
        if target1 == 0 or target2 == 0:
            return 1
        else: return 0
    
    answer = solution(numbers[1:], target1) + solution(numbers[1:], target2)
    
    return answer

print(solution([1,1,1,1,1], 3))