todos=[
    {'tno':1,'title':'자바공부','finish':False},
    {'tno':3,'title':'파이썬공부','finish':False}
]
# print(todos[0]['finish'])

# Create
tno=4
title=input('할일 입력:')
todo={'tno':tno,'title':title,'finish':False}
todos.append(todo)
tno=tno+1

# del_num=input('삭제할 번호 입력:')

# Read : for로 todos 출력
for item in todos:
    print(item)

# Update : tno(번호)로 todos를 찾아 finish를 toggle(toggle=변경?)
#          못 찾으면 아무것도 하지 않는다
    
# input_tno=int(input('찾을 할일번호:'))
# for todo2 in todos:
#     if todo2['tno']==input_tno:
#         todo2['finish']=not todo2['finish']
#         break
# print(todos)

# toggle : 


# Delete : 입력한 tno에 해당하는 todo3을 todos에 찾는다
# 
input_del_tno=int(input('삭제할 할일번호:'))
for todo3 in todos:
    if todo3['tno']==input_del_tno:
        todos.remove(todo3)
        break

print(todos)




