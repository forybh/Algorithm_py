#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 18:00:01 2021

@author: yubyeongheon
"""
N = int(input())
nl = list(map(int, input().split()))
nl.sort()
M = int(input())
ml = list(map(int, input().split()))
def solution():
    answer = {}
    index = 0
    for m in sorted(ml):
        cnt = 0
        while(index < N):
            if m == nl[index]:
                cnt += 1
                index += 1
            elif m > nl[index]:
                index += 1
            else: break
        answer[m] = cnt
                
    print(" ".join(str(answer[m]) for m in ml))
    
    
solution()



    

        
    