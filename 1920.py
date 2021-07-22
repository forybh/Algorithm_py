#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 16:48:37 2021

@author: yubyeongheon
"""


# def solution():
#     N = int(input())
#     n_l = list(map(int, input().split()))
#     M = int(input())
#     m_l = list(map(int, input().split()))
    
#     for m in m_l:
#         if m in n_l:
#             print(1)
#         else:
#             print(0)

def binary_solution(n_l, l, start, end):
    if start > end:
        return 0
    m = (start + end)//2
    if l == n_l[m]:
        return 1
    elif l < n_l[m] :
        return binary_solution(n_l, l, start, m-1)
    else:
        return binary_solution(n_l, l, m+1, end)
    
def main():
    N = int(input())
    n_l = list(map(int, input().split()))
    M = int(input())
    m_l = list(map(int, input().split()))
    n_l = set(n_l)
    for m in m_l:
        if m in n_l:
            print(1)
        else:
            print(0)
            
main()
    