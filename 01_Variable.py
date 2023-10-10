####################################################################
# 여러가지 Print() 기능
# print() : () 안의 내용을 출력하는 기능
####################################################################
print(1,2) # 칸을 띄워서 표현
print(1,3,5,7 ,sep=',') # 사이에 , 를 삽입
print(10,20 ,sep='') # 사이를 없애고 붙여서 표현
print('강아지', '고양이', end='') # 줄바꿈을 하지 않고 표현
print('ㅋㅅㅋ')


# 응용
print(12,34,sep= ' + ', end= ' = ')
print('46 입니다.')

####################################################################
# 값의 입력 input
# 프로그램 실행 중 입력한 값을 받은 후 그 결과로 다음 로직을 수행 (동기적 프로그래밍)

# 변수 = input('값')
# 변수 = 특정 데이터 값이 담기는 공간의 이름, 데이터가 할당 된 메모리 주소를 대표하는 이름.
####################################################################

age = input('몇살이세요?') # 리터럴 : 변수에 할당되는 값
print(age, "살 이시군요")

####################################################################
# 형식 변환 (형변환)
# int()
# 정수(integer) 로 데이터의 형식을 변환한다. (캐스팅, 명시적 형변환)
# 데이터 형식 :
# 컴퓨터가 데이터를 다룰 때 그 데이터가 만들어진 코드 별로 데이터를 관리하는 유형
####################################################################

#형변환의 예제
price = input("가격을 입력하세요.")
num   = input("가격을 입력하세요.")

sum = price + num
print("합은", sum, "원 입니다.")

# 형 변환
sum = int(price) + int(num)
print("총액은", sum, "원 입니다.")



####################################################################
# 변수의 정의
# 프로그래밍에 필요한 데이터를 기억하는 물리적인 공간(메모리)의 주소를 참조하는 이름
# 프로그래밍에서 사용하는 키워드는 변수명으로 사용할 수 없다.
# 명칭은 대, 소 문자를 구분한다.
# 첫글자는 숫자를 쓸 수 없다.
####################################################################

# 변수의 데이터 형식을 확인하기

age = 10 
print(type(age))
age = '십'
print(type(age))

## 대표적인 변수의 데이터 유형
age      = 28 # 정수형 변수
measure  = 11.11 # 실수형 변수
name     = "이름" # 문자형 변수
saleFlag = False # 논리연산 True/False 를 담는 변수


####################################################################
# 실습
# 사각형의 폭과 넓이를 받아서 면적을 구하는 로직을 구현해 보세요.
####################################################################

width = input("폭 :")
heigh = input("높이 :")

rec = int(width) * int(heigh)
print("사각형의 넓이는 :", rec)

                


