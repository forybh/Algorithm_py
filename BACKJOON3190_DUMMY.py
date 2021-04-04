N = int(input())
apple = int(input())
apple_list = []
for i in range(apple):
    temp = list(map(int, (input().split())))
    temp[0]-=1
    temp[1]-=1
    apple_list.append(temp)
L = int(input())
turn_list = []
for j in range(L):
    temp = input().split()
    turn_list.append(temp)


def solution():
    time = 0
    cur_loc = [[0, 0]]
    dir_x = [0, 1, 0, -1]
    dir_y = [1, 0, -1, 0]
    cur_dir = 0

    while True:
        if len(turn_list) != 0:
            dr = turn_list.pop(0)
            x = int(dr[0]) - time
            c = dr[1]
            for _ in range(x):
                time += 1
                loc = [cur_loc[len(cur_loc) - 1][0] + dir_x[cur_dir], cur_loc[len(cur_loc) - 1][1] + dir_y[cur_dir]]
                if loc[0] < 0 or loc[0] >= N or loc[1] < 0 or loc[1] >= N:
                    return time
                if loc in cur_loc:
                    return time
                cur_loc.append(loc)
                if loc not in apple_list:
                    cur_loc.pop(0)
                else:
                    apple_list.remove(loc)
                print("cur_loc = ", cur_loc, "time = ", time)
            if c == 'D':
                cur_dir += 1
                if cur_dir == 4:
                    cur_dir = 0
            else:
                cur_dir -= 1
                if cur_dir == -1:
                    cur_dir = 3
            print("cur_dir = ", cur_dir)
        else:
            time += 1
            loc = [cur_loc[len(cur_loc) - 1][0] + dir_x[cur_dir], cur_loc[len(cur_loc) - 1][1] + dir_y[cur_dir]]
            if loc[0] < 0 or loc[0] >= N or loc[1] < 0 or loc[1] >= N:
                return time
            if loc in cur_loc:
                return time
            cur_loc.append(loc)
            if loc not in apple_list:
                cur_loc.pop(0)
            else:
                apple_list.remove(loc)

            print("cur_loc = ", cur_loc, "time = ", time)







print(solution())



















