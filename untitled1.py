import heapq
import sys
sys.setrecursionlimit(10000)

def findParent(x, parents):
    if x not in parents.keys():
        parents[x] = x + 1
        return x
    
    p = findParent(parents[x], parents)
    parents[x] = p + 1
    return p



def solution(k, room_number):
    answer = []
    parents = {}
    for n in room_number:
        x = findParent(n, parents)
        answer.append(x)
    return answer

print(solution(10, [1,3,4,1,3,1]))