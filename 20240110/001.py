# 나이를 입력받아 성년 또는 미성년을 리턴하는 함수
def age(a:int):
    if a>=18:
        return True
    elif a<18:
        return False

age(18)
if age()==True:
    print('당신은 출입가능합니다.')
elif age()==False:
    print('당신은 출입이 불가능합니다.')


