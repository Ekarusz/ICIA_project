# def sample(a):
#     print(a)

# sample(10)
# sample('hello')

# 정수 2개를 인자로 받아 덧셈후 출력하는 함수를 정의하고 호출
def plus(a,b:int|float):
    print(a+b)


def plus2(a:int|float,b:int|float):
    # return 결과 -> 함수를 종료하고 결과로 바꿔라
    return a+b

plus2(3,4)

result=plus2(3,4)