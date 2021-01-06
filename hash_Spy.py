#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 14:32:53 2021

@author: yubyeongheon
"""

def solution(clothes):
    answer = 1
    kind_of_clothes = set(a[1] for a in clothes)
    count = [0 for x in range(len(kind_of_clothes))]
        
    for i in range(len(clothes)):
        for idx, j in enumerate(kind_of_clothes):
            if clothes[i][1] == j:
                count[idx] +=1
    
    for x in count:
        answer *= (x+1)
        
    answer -= 1
        
    return answer

print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]))


