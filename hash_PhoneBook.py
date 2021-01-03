#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 16:58:21 2021

@author: yubyeongheon
"""

def solution(phone_book):
    answer = True
    for idx, x in enumerate(phone_book):
        for idx2, y in enumerate(phone_book):
            if(idx2 != idx and y.startswith(x)):
                return False
            
            
    return answer

print(solution(['119', '97674223', '1195524421']))