def splitWord(unit,s):
    split_list = []
    word = ""
    for i in range(len(s)):
        word += s[i]
        if len(word) == unit:
            split_list.append(word)
            word = ""
        elif i == len(s)-1:
            split_list.append(word)
    return split_list


def solution(s):
    half_len_s = len(s)//2
    
    compression_li = []
    for unit in range(1,half_len_s+1):
        split_list = splitWord(unit,s)

        word = []
        cnt = 0
        for i in range(len(split_list)):
            if i == 0:
                cnt += 1
                word.append(cnt)
                word.append(split_list[i])
            elif split_list[i] == word[-1]:
                cnt += 1
                word[-2] = cnt
            else:
                cnt = 1
                word.append(cnt)
                word.append(split_list[i])
        print(word)
        
        compression = ""
        for ch in word:
            if ch != 1:
                compression += str(ch)
        print(compression)
        
        compression_li.append(compression)
    print(compression_li)
        
    
    answer = 0
    return answer


s = "abcabcdede"
a = solution(s)
print(a)