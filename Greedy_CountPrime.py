#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 17:16:43 2021

@author: yubyeongheon
"""

from itertools import permutations

def isPrime(number) :
    if(number == 0 or number ==1) :
        return 0
    for i in range(2, number) :
        if(number%i == 0) :
            return 0
    return 1

def solution(numbers) :
    new_case = []
    count = 0
    for r in range(1,len(numbers)+1):
        tmp = permutations(numbers,r)
        for n in tmp:
           tmp_str = "".join(n) 
           new_case.append(int(tmp_str))
    new_case=list(set(new_case))
    for x in new_case :
        count += isPrime(x)
        print("x , isPrime : ", x, isPrime(x))
    return count    
           
print(solution("011"))          
        
        