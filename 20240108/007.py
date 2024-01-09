# 숫자를 입력받아 CR(합계,평균) UD
# 메뉴를 띄운다(1:숫자추가, 2:숫자출력, 999:종료)
numbers=[]
while True:
    print('==========메뉴 선택==========')
    print('(1:숫자추가, 2:합계, 3:평균, 4:삭제, 999:종료)')
    select=input('번호 입력:')
    if select=='1':
        num=int(input('숫자 입력:'))
        numbers.append(num)
    elif select=='2':
        print(f'합계:{sum(numbers)}')
    elif select=='3':
        print(f'평균:{sum(numbers)/len(numbers)}')
    elif select=='4':
        val=int(input('삭제할 값 입력:'))
        if val in numbers:
            numbers.remove(val)
    elif select=='999':
        print('이용해주셔서 감사합니다.')
        break



# elif select=='4':
# index=intput('삭제할 인덱스 입력:')
# del numbers[index]



# elif select=='4':
# val=int(input('삭제할 값 입력:'))
# 찾아서 지운다


