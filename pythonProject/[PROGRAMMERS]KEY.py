def solution(key, lock):
    blank = set()
    keys = []
    base_y = 0
    base_x = 0
    base_flag = True
    for y in range(len(lock)):
        for x in range(len(lock)):
            if lock[y][x] == 0:
                if base_flag:
                    base_y = y
                    base_x = x
                    base_flag = False
                blank.add((y, x))

    for y in range(len(key)):
        for x in range(len(key)):
            if key[y][x] == 1:
                keys.append([y, x])

    if len(blank) == 0:
        return True
    if len(keys) == 0:
        return False

    for i in range(4):
        if i != 0:
            for idx, k in enumerate(keys):
                tmp = [-k[1], k[0]]
                keys[idx] = tmp

        for k in keys:
            y_distance = base_y - k[0]
            x_distance = base_x - k[1]
            cnt = 0
            tmp_flag = True
            for y, x in keys:
                y += y_distance
                x += x_distance
                if (y, x) in blank:
                    cnt += 1
                elif 0 <= y < len(lock) and 0 <= x < len(lock[0]):  # 범위엔 있지만 빈칸x
                    tmp_flag = False
                    break
                else:
                    continue
            if cnt == len(blank) and tmp_flag:  # 다 채움
                return True

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))