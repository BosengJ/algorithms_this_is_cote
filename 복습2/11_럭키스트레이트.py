# p321 럭키 스트레이트

n = input("정수 n을 입력하세요:")

# n = '123402'

half = len(n)//2
a = n[:half]
b = n[half:]

def sumNum(string):
    sum_num = 0
    for n in string:
        sum_num += int(n)
    return sum_num

sum_a = sumNum(a)
sum_b = sumNum(b)

if sum_a == sum_b:
    print("LUCKY")
else:
    print("READY")
