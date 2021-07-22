def revese(place):
    new_place = ["","","","",""]
    for x in range(5):
        for y in range(5):
            new_place[x] +=place[y][x]
    return new_place

def answers(place):
    ans = 1
    gmask = ["PP", "POP"]
    dmask = ["POOP", "OPPO", "PXOP","XPPO","OPPX","POXP"]
    
    for x in place:
        if gmask[0] in x or gmask[1] in x:
            return 0
    r = revese(place)
    for y in r:
        if gmask[0] in y or gmask[1] in y:
            return 0
    for x in range(4):
        for y in range(4):
            if place[x][y] + place[x][y+1] + place[x+1][y] + place[x+1][y+1] in dmask:
                return 0
    return ans
        
                                    

def solution(places):
    answer = []
    for place in places:
        answer.append(answers(place))
                        
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))