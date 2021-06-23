def solution(N,map):
    location = [1,1] # 초기 위치값
    print(location)
    for direction in map:
        if direction == 'L':
            if location[1]-1 > 0:
                location[1] -= 1
                print(location,direction)
        if direction == 'R':
            if location[1]+1 < N+1:
                location[1] += 1
                print(location,direction)
        if direction == 'U':
            if location[0]-1 > 0:
                location[0] -= 1
                print(location,direction)
        if direction == 'D':
            if location[0]+1 < N+1:
                location[0] += 1
                print(location,direction)
    final_location = ''
    for loc in location:
        final_location += str(loc)
    return final_location

N = 10
map = "R R R R R R R R R R R R D D D D D D D D D D D D L L L L L L L L L L L L U U U U U U U U U U U U R D R D R D R D"
answer = solution(N,map)
print(answer)

'''test case
n1 = 5
direction1 = "R R R U D D"
답 : 3 4

n2 = 6
direction2 = "R R U D R U"
답 : 1 4

n3 = 10
direction3 = "D D D U R R L L R U"
답 : 2 2

n4 = 10
direction4 = "R R R R R R R R R R R R D D D D D D D D D D D D L L L L L L L L L L L L U U U U U U U U U U U U R D R D R D R D"
답 : 5 5
'''