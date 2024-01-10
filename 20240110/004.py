# 정수변수를 2개 만들어, 나눗셈 결과를 출력하시오
# 예외처리가 필요하면 예외처리하시오

try:
    def int_x(a:int,b:int):
        if a>b:
            return a/b
        else:
            return b/a

    print(int_x(10,0))
except:
    print('0으로 나눌 수 없습니다.')