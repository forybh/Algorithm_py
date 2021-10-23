def solution(start_date, end_date, login_dates):
    fri_day = 1
    holly_day = {2, 3}
    answer = 0

    yesterDay = 0
    day_cnt = 1
    for date in login_dates:
        if start_date <= date <= end_date: #범위 안의 날짜일때
            day = int(date[3:])
            dayOfWeek = day % 7 #요일 구하기

            if dayOfWeek == fri_day: #금요일 예외처리
                yesterDay = day + 2 # 일요일
                day_cnt += 1
            else :
                if dayOfWeek in holly_day:
                    continue
                if day == yesterDay + 1: #연속
                    day_cnt += 1
                else: #불연속
                    answer = max(answer, day_cnt)
                    day_cnt = 1
                yesterDay = day
    answer = max(answer,day_cnt)
    return answer

print(solution("05/04", "05/30",
               ["05/06","05/07","05/08","05/09","05/10","05/11","05/21","05/22",
                "05/23","05/25","05/26","05/27"]))

