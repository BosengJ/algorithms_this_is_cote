# p322 문자열 재정렬

s = 'K1KA5CB7'

def bubbleSort(li):
    for i in range(len(li)-1):
        for j in range((len(li)-i-1)):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

