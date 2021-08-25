
#1. 현재 심사 할 수 있는 심사관 중 가장 짧은 사람 선택
#2. 심사 끝나면 다시 배열에 넣어줘야함
#3. 모두 심사 중이면 가장 먼저 비는 사람이 해야함
# 처음에 모든 심사관이 심사 -> 두번째 부터 어떻게 할지가 문제
# 제일 먼저 끝난 사람이 할테지만 
# 남은 시간을 계산해야함
# times[n] - time + times[n]


def count_done(time, times):
    count = 0
    for t in times:
        count += time // t
    return count

def solution(n, times):
    answer = 0
    left = 0; right = max(times) * n * 2
    while left < right:
        mid = (left+right)//2
        if count_done(mid, times) >= n:
            answer = mid
            right = mid
        elif count_done(mid, times) < n:
            left = mid + 1
    return answer

print(solution(2, [1,2]))