todos=[]
tno=4
todos.append({'tno':1,'title':'파이썬 공부','finish':False})
todos.append({'tno':2,'title':'자바 공부','finish':False})
todos.append({'tno':3,'title':'파이썬 공부','finish':False})

def print_todo():
    for todo in todos:
        print(todo)

def add_todo():
    global tno
    title=input('추가할 할일:')
    todos.append({'tno':tno,'title':title,'finish':False})
    tno=tno+1

def toggle_todo():
    toggle_tno=int(input('변경할 할일번호:'))
    for todo2 in todos:
        if todo2['tno']==toggle_tno:
            todo2['finish']=not todo2['finish']

def delete_todo():
    delete_tno=int(input('삭제할 할일번호:'))
    for todo3 in todos:
        if todo3['tno']==delete_tno:
            todos.remove(todo3)


while True:
    print('########## 할일 목록 ##########')
    print('1.목록, 2.추가, 3.변경, 4.삭제, 999.종료')
    select=input('번호 선택:')
    if select=='1':
        print_todo()
    elif select=='2':
        add_todo()
    elif select=='3':
        toggle_todo()
    elif select=='4':
        delete_todo()
    elif select=='999':
        print('이용해주셔서 감사합니다.')
        break