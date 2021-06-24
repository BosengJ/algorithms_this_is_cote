def bubbleSort(li):                            # 오름차순 함수
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li 

def solution(S):
    alphabet = []
    number = []
    for c in S:
        if (ord(c) >= 65) and (ord(c) <= 90): # 대문자를 아스키코드로 찾아낸다
            alphabet.append(c)
        else:
            number.append(c)
    sort_alphabet_li = bubbleSort(alphabet)   # 알파벳을 오름차순 함수에 넣어 정렬한다
    sort_alphabet = ''.join(sort_alphabet_li) # 리스트를 문자열로 바꿔준다
    sum_number = 0
    for n in number:
        sum_number += int(n)
    
    answer = sort_alphabet + str(sum_number)
    return answer

S = "0A0A0000A0A0"
a = solution(S)
print(a)

'''K1KA5CB7
답: ABCKK13

AJKDLSI412K4JSJ9D
답:ADDIJJJKKLSS20

1213405500006
답:27

AAFDJN
답:AADFJN0

0A0A0000A0A0
답:AAAA0'''