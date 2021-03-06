# 입력받은 단위로 문자열을 쪼개주는 함수
def splitWord(unit,s):
    split_list = []
    word = ""
    for i in range(len(s)):
        word += s[i]                    # 문자 하나하나 차곡차곡 쌓아올린다
        if len(word) == unit:           # 쌓인 문자열이 입력받은 단위와 길이가 같다면 리스트에 넣어준다
            split_list.append(word)
            word = ""
        elif i == len(s)-1:             # 마지막 문자열이 단위보다 작을 수 있으므로 마지막은 그냥 무조건 리스트에 넣어준다
            split_list.append(word)
    return split_list                   # 입력받은 단위로 쪼개진 문자열을 리스트로 반환한다


def solution(s):
    # 길이가 1인 문자열은 1을 return 해준다
    if len(s) == 1:
        return 1
    
    # 길이가 2 이상인 문자열은 다음과 같이 처리한다

    # n개 단위로 자를 때 n이 가질 수 있는 최대값은 문자열의 절반이다.
    half_len_s = len(s)//2
    
    compression_li = []
    for unit in range(1,half_len_s+1):
        split_list = splitWord(unit,s)      # n개 단위로 쪼개진 문자열 리스트

        word = []
        cnt = 0
        for i in range(len(split_list)):    # 문자열을 카운트 해준다
            if i == 0:                      # 첫번째는 그냥 넣어준다
                cnt += 1
                word.append(cnt)
                word.append(split_list[i])
            elif split_list[i] == word[-1]: # 현재 문자열이 직전에 리스트에 넣은 문자열과 같다면, 하나 더 카운트 하여, 리스트에 있는 카운트를 치환시킨다
                cnt += 1
                word[-2] = cnt
            else:                           # 현재 문자열이 직전에 넣은 리스트에 넣은 문자열과 같지 않다면, 새로운 문자열이기 때문에 카운트는 1로 바꿔주고 리스트에 넣어준다
                cnt = 1
                word.append(cnt)
                word.append(split_list[i])

        compression = ""                    # 1은 필요없기 때문에 1을 제외한 모든 요소를 문자열로 만들어준다
        for ch in word:
            if ch != 1:
                compression += str(ch)
        compression_li.append(compression)
    
    min_word = len(compression_li[0])       # 각 단위별로 만들어진 문자열 중 가장 적은 길이의 문자열을 찾아낸다
    for word in compression_li:
        if len(word) < min_word:
            min_word = len(word)
            
    answer = min_word
    return answer


s = "abcabcdede"
a = solution(s)
print(a)


# def solution(raw_data):

#     min_val = len(raw_data)
#     for length in range(1, len(raw_data)//2 + 1):
#         idx = length
#         converted = ""
#         pre_str = raw_data[:length]
#         cnt = 1
#         for i in range(length, len(raw_data), length):
#             cur_str = raw_data[i:i+length]
#             if cur_str != pre_str:
#                 if cnt == 1:
#                     converted += pre_str
#                 else:
#                     converted += str(cnt) + pre_str
#                 pre_str = cur_str
#                 cnt = 1
#             else:
#                 cnt += 1
#         if cnt == 1:
#             converted += cur_str
#         else:
#             converted += str(cnt) + cur_str
#         if min_val > len(converted):
#             min_val = len(converted)
#     return min_val