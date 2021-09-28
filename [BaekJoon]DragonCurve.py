#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:43:45 2021

@author: yubyeongheon
"""

n = int(input())
curves = []
board = [[0] * 101 for x in range(101)]
direct = [(0, 1), (-1, 0), (0, -1), (1, 0)]

for i in range(n):
    tmp = list(map(int, input().split()))
    curves.append(tmp)
    
def checkSquare(start):
    if board[start[0]][start[1]] == 1 and board[start[0]+1][start[1]] == 1 and board[start[0]][start[1]+1] == 1 and board[start[0]+1][start[1]+1] == 1: return 1
    return 0

def solution():
    answer = 0
    for curve in curves:
        start = [curve[1], curve[0]]
        board[start[0]][start[1]] = 1
        d = curve[2]
        g = curve[3]
        directions = [d]
        for i in range(g): #90도 회전
            tmp = directions.copy()
            for j in range(len(tmp)):
                tmp[j] += 1
                if tmp[j] == 4:
                    tmp[j] = 0
            tmp.reverse()
            directions += tmp
        for direction in directions: 
            start[0] += direct[direction][0]
            start[1] += direct[direction][1]
            board[start[0]][start[1]] = 1
                
    for y in range(100):
        for x in range(100):
            answer += checkSquare((y, x))
    return answer


print(solution())
        
    
    
    
    
    
    
