# p322 문자열 재정렬

s = input("문자열 S를 입력하세요:")
# s = 'K1KA5CB7'

def bubbleSort(li):
    for i in range(len(li)-1):
        for j in range((len(li)-i-1)):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

sorted_s = bubbleSort(list(s))

num = 0
answer = ''
for c in sorted_s:
    if (48 <= ord(c)) and (ord(c) <= 57):
        num += int(c)
    else:
        answer += c
answer += str(num)
print(answer)