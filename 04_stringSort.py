def bubbleSort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li 

def solution(S):
    alphabet = []
    number = []
    for c in S:
        if (ord(c) >= 65) and (ord(c) <= 90): # 대문자 아스키코드
            alphabet.append(c)
        else:
            number.append(c)
    sort_alphabet_li = bubbleSort(alphabet)
    sort_alphabet = ''.join(sort_alphabet_li)
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