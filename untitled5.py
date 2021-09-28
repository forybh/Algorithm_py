import collections
def solution(info, edges):
    answer = 0
    visited = [0] * len(info)
    d = collections.defaultdict(int)
    child = [[] for x in range(len(info))]
    parent = [x for x in range(len(info))]
    for edge in edges:
        child[edge[0]].append(edge[1])
        parent[edge[1]] = edge[0]
    
    
        
            
        
    
        
    
    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],
               [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))