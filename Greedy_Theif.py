#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 11:51:54 2021

@author: yubyeongheon
"""
from collections import Counter

def solution(n, lost, reserve):
    answer = 0
    l = [1 for x in range(n)]

    for i in lost:
        l[i-1] -= 1
        

    for j in reserve:
        l[j-1] += 1

    for idx, k in enumerate(l):
        if k == 0:
            if idx != 0:
                if l[idx-1] == 2:
                    l[idx] += 1
                    l[idx-1] -= 1
                    continue
                
            if idx != n-1:
                if l[idx+1] == 2:
                    l[idx] += 1
                    l[idx+1] -= 1
    
  
    answer = Counter(l)[1]  + Counter(l)[2]            
    return answer
        

print(solution(5, [2,4], [1,3,5]))