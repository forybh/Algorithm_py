import heapq
import collections


def solution(n, edge):
    answer = 0
    dist = [200001 for x in range(n+1)]
    graph = collections.defaultdict(list)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    dist[0] = 0
    dist[1] = 0
    q = []
    heapq.heappush(q, (dist[1], 1))
    while q:
        current_distance, node = heapq.heappop(q)
        node_list = graph[node]
        for nd in node_list:
            if dist[nd] <= current_distance + 1:
                continue
            else:
                dist[nd] = current_distance + 1
                q.append((dist[nd],nd))
    max_dist = max(dist)
    for d in dist:
        if d == max_dist:
            answer += 1
    return answer
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))