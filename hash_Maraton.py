#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 16:03:31 2021

@author: yubyeongheon
"""
import collections

def solution(participant, completion):
    answer = collections.Counter((participant))- collections.Counter(completion)
        
    return list(answer.keys())[0]

if __name__ == '__main__':
    print(solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']))