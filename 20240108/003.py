# 문자열(string) 타입
str1='10'
str2='3.14'
str3='홀짝홀짝홀짝홀짝'

# 문자열의 연산
print(str1+str2)    # 연산
print(str1*10)      # 반복(*숫자 만큼 반복)
print(str1+str3)

# 인덱스 연산 [~] : ~자리에 오는 값을 출력 -> sequence와 동일
print(str3[0])
# 슬라이싱(slicing) 연산 -> sequence와 동일
print(str3[0:3])    # 홀짝홀
str4='72568'
print(str4[0:3])    # 725
print(str4[1:])
print(str4[::2])

str5='0123456789'
# 홀수만 출력(13579)
# 3의 배수만 출력(0369)
print(str5[1::2])
print(str5[::3])

# 내장함수 -> len : 길이를 재는 내장함수
print(len('hello'))
print(len(str(15)))

a=(10,20,30,40,50)
print(len(a))

# 문자열은 변경불가능 (immutable <-> mutable)
str6='hello'
list6=['h','e','l','l','o']
list6[0]='z'

str11='hello'
str11=str11+'python'
print(str11)


