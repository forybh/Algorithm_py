#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 13:08:53 2021

@author: yubyeongheon
"""

def solution(N, K):
    answer = 0
    while N != 1:
        if N % K != 0:
            N -= 1
            answer += 1
        else:
            N /= K
            answer += 1
    return answer

print(solution(25, 3))