# dictionary : 키와 값의 쌍
# 데이터를 표현 -> dictionary
# 데이터 1건 : dictionary
# 여러건 : list

# 회원
{'아이디':'spring', '나이':25, '성인여부':True}

{'책 제목':'이것이 자바다', '가격':32400, '평점':9.8}

{'아이디':'ID','비밀번호':'PW','간편 로그인':True or False}

# 키와 값의 pair로 정보를 표현 -> dictionary
{'번호':1,'이름':'코카콜라','가격':2000,'재고':20}
# dictionary로 list를 만든다
products=[
    {'번호':1,'이름':'코카콜라','가격':2000,'재고':20},
    {'번호':2,'이름':'펩시콜라','가격':1900,'재고':30}
]
print(products[0]['이름'])


