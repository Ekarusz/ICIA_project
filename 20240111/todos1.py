# 할일은 할일번호, 할일, 완료여부로 구성
# todos=[{'tno':int/str,'title':str,'finish':True/False}]
# 함수 안에서 함수 밖에 있는 변수를 사용하려면 사용한다고 적어준다 -> 함수 안에 global 변수
todos=[]
tno=4

todos.append({'tno':'1','title':'자바 공부','finish':False})
todos.append({'tno':'2','title':'파이썬 공부','finish':False})
todos.append({'tno':'3','title':'공부 안하고 놀기','finish':True})

def print_todos():
    for todo in todos:
        print(todo)

def add_todo():
    global tno
    title=input('추가할 할일:')
    todos.append({'tno':tno,'title':title,'finish':True})
    tno=tno+1

def toggle_finish():
    pass

def delete_todo():
    pass


while True:
    print('##### 할일 관리 #####')
    print('1.목록, 2.추가, 3.변경, 4.삭제, 999.종료')
    select=input('번호 선택:')
    if select=='1':
        print_todos()        # 함수 호출
    elif select=='2':
        add_todo()
    elif select=='3':
        toggle_finish()
    elif select=='4':
        delete_todo()
    elif select=='999':
        print('이용해 주셔서 감사합니다.')
        break




    # elif select=='2':
    #     input_select=input('추가할 할일:')
    #     todos.append(input_select)
    # elif select=='3':
    #     input_select2=input('변경할 할일:')
    # elif select=='4':
    #     input_select4=input('삭제할 할일:')
    #     todos.remove(input_select4)
    # elif select=='999':
    #     print('이용해 주셔서 감사합니다.')
    #     break