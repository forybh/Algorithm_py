#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 17:11:19 2021

@author: yubyeongheon
"""

def solution(m,n,coins):
    answer = [[0] * (m+1) for x in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [j, i] in coins:
                answer[i][j] = max(answer[i-1][j], answer[i][j-1]) # + 코인가격
            else:
                answer[i][j] =  max(answer[i-1][j], answer[i][j-1])
        
    return answer[n][m]