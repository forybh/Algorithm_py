import heapq

def solution(operations):
    hq1 = []
    hq2 = []
    heapq.heapify(hq1)
    heapq.heapify(hq2)
    cnt = 0

    for op in operations:
        cmd, num = op.split()
        if cmd == 'I':
            heapq.heappush(hq1, -int(num))
            heapq.heappush(hq2, int(num))
            cnt += 1
        elif cmd == 'D':
            if cnt == 0:
                continue
            cnt -= 1
            if num == '1':
                tmp = -heapq.heappop(hq1)
                hq2.remove(tmp)
            else:
                tmp = -heapq.heappop(hq2)
                hq1.remove(tmp)
        print(hq1, hq2)
    if cnt == 0:
        return [0, 0]
    return [-hq1[0], hq2[0]]


print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))

# -45 - 45 333