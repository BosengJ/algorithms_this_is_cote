# dictionary 이용하여 다시 풀어보기

def solution(N,map):
    # 초기 위치값
    location_x = 1
    location_y = 1

    # 방향별로 이동하는 좌표값을 딕셔너리로 만들어준다 
    location_dict = {'L':[0,-1],'R':[0,1],'U':[-1,0],'D':[1,0]}

    # 입력받은 지도 값으로 이동 한 후 이동 가능한지 여부를 따져 좌표 값을 도출한다
    for direction in map:
        for k,v in location_dict.items():
            if direction == k:
                location_x += v[0]
                location_y += v[1]

                if location_x < 1 or location_x > N:
                    location_x -= v[0]    
                if location_y < 1 or location_y > N:
                    location_y -= v[1]
    return [location_x,location_y]

    # dir = {'L' : [0, -1]}
    # for direction in map:
    #     if direction == 'L':
    #         if location[1]-1 > 0:
    #             location[0] += dir['L'][0]
    #             location[1] += dir['L'][1]
    #             print(location,direction)
    #     if direction == 'R':
    #         if location[1]+1 < N+1:
    #             location[1] += 1
    #             print(location,direction)
    #     if direction == 'U':
    #         if location[0]-1 > 0:
    #             location[0] -= 1
    #             print(location,direction)
    #     if direction == 'D':
    #         if location[0]+1 < N+1:
    #             location[0] += 1
    #             print(location,direction)
    # final_location = ''
    # for loc in location:
    #     final_location += str(loc)
    # return final_location

# def solution(N,map):
#     location = [1,1] # 초기 위치값
#     print(location)
#     dir = {'L' : [0, -1]}
#     for direction in map:
#         if direction == 'L':
#             if location[1]-1 > 0:
#                 location[0] += dir['L'][0]
#                 location[1] += dir['L'][1]
#                 print(location,direction)
#         if direction == 'R':
#             if location[1]+1 < N+1:
#                 location[1] += 1
#                 print(location,direction)
#         if direction == 'U':
#             if location[0]-1 > 0:
#                 location[0] -= 1
#                 print(location,direction)
#         if direction == 'D':
#             if location[0]+1 < N+1:
#                 location[0] += 1
#                 print(location,direction)
#     final_location = ''
#     for loc in location:
#         final_location += str(loc)
#     return final_location

N = 6
map = "R R U D R U"
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