from collections import defaultdict, deque

def solution(tickets):
    answer = []

    l = len(tickets) + 1
    d = defaultdict(list)
    for start, end in tickets:
        d[start].append(end)

    def dfs(cur, paths, d, l):
        if len(paths) == l:
            answer.append(paths[:])
            return
        if cur not in d.keys():
            return
        for i,nextpath in enumerate(d[cur]):
            paths.append(d[cur].pop(i))
            dfs(nextpath, paths, d, l)
            paths.pop()
            d[cur].insert(i, nextpath)

    dfs("ICN", ["ICN"], d, l)
    answer.sort()

    return answer[0]

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))