N, M = map(int, input().split())
A = [list(map(int, input().split())) for x in range(N)]
clouds = {(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)}
directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1),
              (0, 1), (1, 1), (1, 0), (1, -1)]

for i in range(M):
    d, s = map(int, input().split())
    d -= 1
    move_clouds = set()
    for cloud in clouds:
        move_cloud_x = cloud[1] + directions[d][1] * s
        move_cloud_y = cloud[0] + directions[d][0] * s

        while not(0 <= move_cloud_x < N and 0 <= move_cloud_y < N):
            if move_cloud_x >= N:
                move_cloud_x -= N
            elif move_cloud_x < 0:
                move_cloud_x += N
            if move_cloud_y >= N:
                move_cloud_y -= N
            elif move_cloud_y < 0:
                move_cloud_y += N

        A[move_cloud_y][move_cloud_x] += 1
        move_clouds.add((move_cloud_y, move_cloud_x))

    for move_cloud in move_clouds: #물 복사 버그
        cnt = 0
        for idx in range(1, 8, 2):
            tmp_x = move_cloud[1] + directions[idx][1]
            tmp_y = move_cloud[0] + directions[idx][0]
            if 0 <= tmp_x < N and 0 <= tmp_y < N:
                if A[tmp_y][tmp_x] > 0: # 대각선에 물 있을때
                   cnt += 1
        A[move_cloud[0]][move_cloud[1]] += cnt

    clouds.clear()
    for y in range(N):
        for x in range(N):
            if A[y][x] >= 2:
                if (y, x) not in move_clouds:
                    clouds.add((y, x))
                    A[y][x] -= 2

answer = 0

for i in range(N):
    answer += sum(A[i])

print(answer)


