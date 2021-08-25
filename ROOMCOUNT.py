import collections

def solution(arrows):
    answer = 0
    points = [(0,0)]
    now = [0,0]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    for arrow in arrows:
        y = now[0] + dy[arrow]
        x = now[1] + dx[arrow]
        for i in range(2):
            y = now[0] + dy[arrow]
            x = now[1] + dx[arrow]
            now = [y, x]
            points.append((y,x))
 #   s = list(set(points))
    
    
    point_visited = collections.defaultdict(int)
    edge_visited = collections.defaultdict(int)
 #   point_visited = [0 for x in range(len(s))]
 #   edge_visited = [[0 for x in range(len(s))] for y in range(len(s))]
    
    for idx, point in enumerate(points):
        cur_index = point
        past_index = points[idx-1]
        if point_visited[cur_index] > 0: #이미 한번 지남
            if edge_visited[(cur_index,past_index)] == 1 or edge_visited[(past_index,cur_index)] == 1:
                continue
            else:
                answer += 1
        point_visited[cur_index] += 1
        edge_visited[(cur_index,past_index)] = 1
        edge_visited[(past_index,cur_index)] = 1
        
    return answer

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))