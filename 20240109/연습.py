# 숫자리스트-추가,목록,삭제
numbers=[]

def print_menu():
    print('========== 메 뉴 ==========')
    print('1.추가, 2.목록, 3.삭제, 999.중단')

def input_select():
    return input('메뉴 선택:')

def add_number():
    value=int(input('숫자 입력:'))
    numbers.append(value)

def list_numbers():
    for num in numbers:
        print(num, end=" ")
    print()

def delete_number():
    value=int(input('삭제할 값 입력:'))
    index=0
    for num in numbers:
        if num==value:
            del numbers[index]
        index=index+1

while True:
    print_menu()
    select=input_select()
    if select=='1':
        add_number()
    elif select=='2':
        list_numbers()
    elif select=='3':
        delete_number()
    elif select=='999':
        break