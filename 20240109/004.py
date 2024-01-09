# 숫자가 numbers에 있는지(True/False) 출력
numbers=[1,3,5,7]
num=7
t=True

# 한번만 찾으면 성공, 실패는 numbers의 모든 값에 대해서 못 찾아야한다
# 성공과 실패의 조건이 다르다 -> if ~ else ~ 가 아니다
for item in numbers:
    if item==num:
        print(True)
        t=False     # numbers와 무관한 t라는 조건을 추가해서 새로운 조건을 부여
        break
if t==True:         # numbers와 상관없이 t=True라는 변수에 대한 조건문
    print(False)



