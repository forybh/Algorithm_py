def traped(roads, r):
    new_roads = []
    for road in roads:
        if r in road[:-1]:
            new_road = [road[1],road[0],road[2]]
            new_roads.append(new_road)
        else: new_roads.append(road)
    return new_roads

def solution(n, start, end, roads, traps):
    answers = []
    if start == end:
        return 0
    for road in roads:
        if road[0] == start:
            new_start = road[1]
            distance = road[2]
            if road[1] in traps:
                new_roads = traped(roads, new_start)
                return distance  + solution(n, new_start, end, new_roads, traps)
            else:
                return distance  + solution(n, new_start, end, roads, traps)
                
    return 0

print(traped([[1, 2, 1], [3, 2, 1], [2, 4, 1]], 4))
print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2,3]))