n,m = map(int,input("n,m을 공백을 구분으로 입력하세요:").split())
card_arr = []
for i in range(n):
    card_arr.append(list(map(int,input("배열을 공백을 구분으로 입력하세요:").split())))
print(card_arr)

min_li = []
for i in range(n):
    min_num = card_arr[i][0]
    for j in range(m):
        if card_arr[i][j] < min_num:
            min_num = card_arr[i][j]
    min_li.append(min_num)
print(min_li)

max_num = 0
for num in min_li:
    if num > max_num:
        max_num = num
print(max_num)