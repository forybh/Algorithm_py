#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:54:22 2021

@author: yubyeongheon
"""

def solution(l):
    temp = max([min(x) for x in l])
    return temp

print(solution([[7,3,1,8], [3,3,3,4]]))