
def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x : x[2])
    connect = set()
    connect.add(costs[0][0])
    while len(connect) != n:
        for idx, cost in enumerate(costs):
            if cost[0] in connect and cost[1] in connect:
                continue
            if cost[0] in connect or cost[1] in connect:
                connect.add(cost[0])
                connect.add(cost[1])
                answer += cost[2]
                break         

        
    return answer

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))