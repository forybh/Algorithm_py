import collections


    
def solution(nodeinfo):
    answer = [[]]
    d = collections.defaultdict(list)
    for i,node in enumerate(nodeinfo):
        d[node[1]].append((node[0], i))
    keys = sorted(list(d.keys()), reverse=True)
    
    q = d[keys[0]]
    print(q)
    # 전위 순회
    
    ran = 2 ** (len(keys))
    #print(tree[1:ran])
          
    return answer


solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])