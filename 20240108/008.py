nums=[1,3,4,5,7,9]

user_input=7
print(user_input in nums)

user_input=100
print(user_input in nums)

# 메뉴로 숫자를 입력받아 처리하는 프로그램 작성
# 1.숫자 추가, 2.숫자 출력, 3.합계, 4.값으로 삭제, 999.종료

# numbers=[]
# while True:
#     print('================메뉴 선택===============')
#     print('==1.숫자 추가, 2.숫자 출력, 3.합계, 4.값으로 삭제, 999.종료==')
#     select=input('번호 입력:')
#     if select=='1':
#         num=int(input('숫자 입력:'))
#         numbers.append(num)
#     elif select=='2':
#         if len(numbers)==0:
#             print('입력한 숫자는 없습니다.')
#         else:
#             print(f'입력한 숫자는 {numbers}')
#     elif select=='3':
#         print(f'합계:{sum(numbers)}')
#     elif select=='4':
#         val=int(input('삭제할 값 입력:'))
#         if val in numbers:
#             numbers.remove(val)
#             print(f'삭제 후의 값은 {sum(numbers)}입니다.')
#     elif select=='999':
#         print('이용해 주셔서 감사합니다.')
#         break















numbers=[]
while True:
    print('=============================메뉴 선택=============================')
    print('======1.숫자 추가, 2.숫자 출력, 3.합계, 4.값으로 삭제, 999.종료======')
    select=input('번호 입력:')
    if select=='1':
        num=int(input('숫자 입력:'))
        numbers.append(num)
    elif select=='2':
        if len(numbers)==0:
            print('입력한 숫자는 없습니다.')
        else:
            print(f'입력한 숫자는 {numbers}입니다.')
    elif select=='3':
        print(f'합계는 {sum(numbers)}입니다.')
    elif select=='4':
        val=int(input('삭제할 숫자 입력:'))
        if val in numbers:
            numbers.remove(val)
        if len(numbers)==0:
            print('남아있는 입력된 숫자가 없습니다.')
        else:
            print(f'남아있는 입력된 숫자는 {numbers}입니다.')
    elif select=='999':
        print('이용해 주셔서 감사합니다.')
        break



numbers=[]
while True:
    print('=============================메뉴 선택=============================')
    print('======1.숫자 추가, 2.숫자 출력, 3.합계, 4.값으로 삭제, 999.종료======')
    select=input('번호 입력:')
    if select=='1':
        val=int(input('숫자 입력:'))
        numbers.append(val)
    elif select=='2':
        for number in numbers:
            print(number, end=" ")
        print()
    elif select=='3':
        print(f'합계:{sum(numbers)}')
    elif select=='4':
        value=int(input('삭제할 숫자:'))
        if value in numbers:
            numbers.remove(value)
    elif select=='999':
        print('이용해 주셔서 감사합니다.')
        break