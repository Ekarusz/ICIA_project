# for문
# hello를 for를 이용해 3번 출력하시오
# for x in (1,2,3):
#     print('hello')

# range(~) : range가 값을 설정해줌 -> for문에서 ~횟수 만큼 반복함
# for x in range(3):
#     print(x)

# for를 이용해서 0~10까지 출력
# for item in range(11):
#     print(item)
    
# for를 이용해서 0~10사이의 짝수 출력
# for item2 in range(11):
#     if item2%2==0:
#         print(f'짝수는 {item2}')
#     else:
#         pass

# 1부터 5까지의 합계를 출력 (15)
# result=0
# for item3 in range(1,6):
#     result=result+item3
# print(result)

# 1부터 10까지의 합계 (55)
# result=0
# for item in range(1,11):
#     result=result+item
# print(result)

# 1에서 10까지의 3의 배수 출력
# for item in range(1,11):
#     if item%3==0:
#         print(item)

# for item in range(1,11):
#     if item%3!=0:
#         continue       #skip
#     print(item)

# 1~10사이의 3의 배수의 합계
# result=0
# for item in range(1,11):
#     if item%3==0:
#         result=result+item
# print(result)

# result=0
# for item in range(1,11):
#     if item%3!=0:
#         continue
#     result=result+item
# print(result)

# 1~100사이의 5과 7의 공배수를 출력

for item in range(1,101):
    if item%5==0:
        if item%7==0:
            print(item)




