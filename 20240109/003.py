# 할일 관리
todos=[
    {'tno':1,'title':'할일1','reg_day':'2024-01-09','finish':False},
    {'tno':2,'title':'할일2','reg_day':'2024-01-09','finish':False},
    {'tno':3,'title':'할일3','reg_day':'2024-01-09','finish':False}
]

# CRUD
# Create
# Read : 전체읽기, 1개읽기
# 전체읽기
for todo_all in todos:
    print(todo_all)

찾았니=False
# 할일번호를 입력받아 할일을 찾아 출력
todo_num=int(input('할일 번호:'))
for todo in todos:
    if todo['tno']==todo_num:
        print(todo)
        찾았니=True
        break
if 찾았니==False:
    print('할일을 찾을 수 없습니다.')



