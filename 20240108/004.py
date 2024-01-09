# 웹프로그래밍 : 문자열 작업이 대부분
# 빅데이터 : 숫자 작업이 대부분
# f문자열
# replace (치환) : 문자열을 치환하는 함수 (변수=변수.replace('치환될 문자열','치환 후에 출력될 문자열')) -> method 함수
# 문자열은 변경불가능하기에 변수를 하나 더 만들어 치환해주면 된다.
# ex)str1='1,2,3,4,5' -> str1.replace(',',' ') => 변경 불가능
#    str1='1,2,3,4,5' -> str1=str1.replace(',',' ') => 변경 가능
str4='010-1111-2222'
# 함수 : 소속없는 함수 + 소속있는 method 함수
print(len(str4))
# method 함수 : 특정 타입 소속 -> 타입은 함수도 가질 수 있다
# 문자열 메소드는 새로운 문자열을 만든다
str5=str4.replace('-','.')
print(str5)

# 971011-2******
jumin='971011-2010015'
jumin=jumin.replace('010015','******')
print(jumin)

print(jumin.replace(jumin[8:],'******'))

# strip : 공백을 제거해주는 함수(문자와 문자 사이의 공백은 제거하지 않는다) -> method 함수
str5='     aa aa     '
print(str5.strip())




