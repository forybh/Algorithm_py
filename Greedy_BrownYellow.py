#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 15:37:28 2021

@author: yubyeongheon
"""

def solution(brown, yellow):
    answer = []
    y = 1
    x = (brown + yellow); 
   # print("x : ", x , "y : ", y )
    while brown != 2*x + 2*y - 4:
        y += 1
        x = (brown + yellow)/y
      #  print("x : ", x , "y : ", y)
        
    answer = [int(x), y]
    return answer

if __name__ == '__main__' :
    print(solution(24, 24))