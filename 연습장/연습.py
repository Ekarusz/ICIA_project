# 임의의 값을 지정했을때 5보다 큰 6의 배수 근사값
num = int(input("숫자 입력 : "))
num1 = (num//6)*6
num2 = (num1 + 6)
if num > 5:
    if num1 <= num % 6 == 0:
        result = num1
    elif num1 > num % 6 == 0:
        result = num2
else:
    result = ('5보다 큰 숫자를 입력하시오')
print(result)