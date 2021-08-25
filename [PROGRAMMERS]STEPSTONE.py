def get_count(distances, distance):
    count = 0
    i = 0
    while i < len(distances)-1:
        if distances[i] < distance:
            count += 1
            distances[i+1] += distances[i]
            distances.pop(i)
            i -= 1
        i += 1
    #print(distances)
    return count

def solution(distance, rocks, n):
    answer = 0
    distances = []
    now = 0
    rocks.sort()
    for rock in rocks:
        distances.append(rock-now)
        now = rock
    distances.append(distance - rock)
    left = 0; right = distance
    while left <= right:
        mid = (left + right) // 2
        cnt = get_count(distances.copy(), mid)
        if cnt > n:
            right = mid -1
        elif cnt <= n:
            answer = mid
        #    print("answer : ", answer)
            left = mid + 1    
    return answer

print(solution(16, [4,8,11], 2))