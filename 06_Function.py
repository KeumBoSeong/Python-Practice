####################################################################
# 함수의 필요성
####################################################################
# 순차적인 정수를 누적 합산하는 값을 구하는 문제가 존재한다고 가정
# 아래와 같이 누적 합산 로직을 하나씩 작성하여 프로그래밍 가능
sum = 1
for num in range(5):
    sum += num
print("~ 4 합은 : ", sum) #0~4 까지 합

sum = 1
for num in range(6):
    sum += num
print("~ 5 합은 : ", sum) #0~5 까지 합

sum = 1
for num in range(7):
    sum += num
print("~ 6 합은 : ", sum) #0~6 까지 합

sum = 1
for num in range(8):
    sum += num
print("~ 7 합은 : ", sum) #0~7 까지 합

# 만약 누적 합산이 아닌 누적 곱이라고 할 때
# 모든 로직을 수정해야 한다. (유지 보수성이 떨어짐)

# 1부터 100 까지의 모든 합을 표현하는 로직을 구현할 때
# 100 번의 반복되는 로직을 모두 작성해야 한다. (반복성)


####################################################################
# 함수 (재 사용성과 유지보수성의 증가)
#  . 반복적인 코드를 작성해 두고 언제든지 재 사용 할 수 있도록 할 수있다.
#  . 함수의 내용을 수정 시 함수를 호출 하는 모든 구문의 결과가 일괄 수정된다.
####################################################################

## 함수의 생성 def
def MyFunction() :
    print("안녕하세요")

## 함수의 호출

MyFunction()


# 함수의 인수와 인자 
# 함수로 전달하는 값 : 인수
# 함수가 전될받기로 약속 한 값 : 인자

def MyFunction(param) :  # param : 인자 (어떠한 값을 받을 수 있는 변수 명)
    print(param)

MyFunction("안녕하세요")


def MyFunction(param) :  # param : 인자 (어떠한 값을 받을 수 있는 변수 명)
    print(param)

MyFunction(500)


# 잘못된 함수의 호출 (약속된 인자의 값을 전달하지 않았을 경우 오류 발생)
def MyFunction(param) :
    print(param)

MyFunction()



####################################################################
# 위의 예에서 반복되는 구문 함수로 만들기
####################################################################

반복되는 구문 삭제 후 함수로 만들기

def MyFunction() :
    sum = 1
    for num in range(5):
        sum += num
    print("~ 4 합은 : ", sum) #0~4 까지 합


# 함수가 처리해야 할 상황에 따른 인자값 설정

def MyFunction(val) :
    sum = 0
    for num in range(val+1):
        sum += num
    print("~ ", val, "합은 : ", sum) #0~4 까지 합


# 함수가 호출하여 테스트
MyFunction(5)
MyFunction(6)
MyFunction(7)
MyFunction(8)

# 완성된 결과에서 재검토
i : 함수를 실행할 때 더해져야 하는 정수
for i in range(5,10) :
    MyFunction(i)



####################################################################
# 함수의 결과를 반환하는 return
# 파이썬의 경우 함수 반환 데이터 유형을 지정 하지 않아도 유동적으로
# 데이터를 함수를 호출 한 곳으로 반환 할 수 있다.
####################################################################
# 함수의 결과를 호출한 곳으로 반환함으로서 결과값으로 로직을 이어서 구현하기 위함

def calsum(end):
    sum = 0
    for i in range(end+1):
        sum += i
    return sum

result = int(input("값을 입력하세요. : "))
print('입력한 값의 누적 합은', calsum(result), '입니다.')


# 인자를 n개 생성할 수 있다.
def calsum(end1, end2, end3):
    sum = 0
    for i in range(end1+1):
        sum += i
    return sum

calsum(10) # 인수를 3개 전달해야 한다. (Error)



# pass
# 로직을 완성하지 않았지만 미완성 로직으로 인해 오류를 잠정적으로 막고싶을 때,
# 인터프리터 언어 (프로그램을 실행 할 때 비로소 오류)

for i in range(10):
    pass # 로직의 완성을 미룰 때
print()


# 정수로 시작과 끝의 범위와 몇배수 인지 의 정보를 인자로 받는 함수를 작성
# 시작과 끝 범위 내에 있는 배수를 모두 표현하는 로직

n = int(input("찾을 배수:"))
for i in range(int(input("시작 정수 값 : ")), int(input("종료 정수 값 : "))):
    
    if i % n == 0:
        print(i,end=',')


def Multiprint(sv,ev,mv):
    message = ''
    for i in range (sv,ev+1):
        if i % mv == 0 : 
            message += str(i) + ','
    return message
    

start  = int(input("시작 값 :"))
end    = int(input("종료 값 :"))
mvalue = int(input("배수 값 :"))
 
print(mvalue, "의 배수 나열 데이터 :",Multiprint(start,end,mvalue))
 




####################################################################
# 재귀 호출
#  . 자기 자신을 반복적으로 호출 하도록 구현된 함수
#  . 코드가 간결해지고 가독성이 높아 진다.
#  . 실행 하는데에 시간이 오래 걸릴 수 있음
#  . 반드시 종료하는 시점의 값을 return 하는 구문이 필요
####################################################################

def factorial(n):
    if n == 0:
        return 1
    else :
        return n * factorial(n-1)
result = factorial(5)
print(result) #120

