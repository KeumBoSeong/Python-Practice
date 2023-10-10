####################################################################
# 가변인자 (가변인수)
#  .n개의 인수를 유동적으로 받아서 처리하기
####################################################################

# *ints 라는 가변 인자 변수를 설정하여 intsum 을 호출 할 때, n개의 인수를 전달하는 예시

def intsum(*ints):
    sum = 0
    for num in ints :
        sum += num
    return sum

print(intsum(1,2,3))



# 인수 인자 데이터 형식에 구애받지 않고 모두 수용하여 처리

def intsum(*ints):
    sum = 100
    return sum
print(intsum(1,True,10.12, '안녕하세요'))


#  가변인자는 튜플 형태이며 임의로 수정할 수없다.
def intsum(*ints):
    ints[0] = 10    
print(intsum(1,True,10.12, '안녕하세요'))



####################################################################
# 가변 인자의 위치
# 반드시 인자 배열의 마지막 위치에 등록되어야 한다.
####################################################################

# 담을 범위가 모호해 지므로 가변 인자는 인자의 앞이나 중간에 올 수 없다.

def intsum(*sValue, *sValue2) :
    print("안녕하세요")

intsum(1,2,3,4,5,6,7,8,9)



# 가변인자는 앞에 위치 할 수없다. 

def intsum(*sValue, sValue2) :
    print("안녕하세요")

intsum(1,2,3,4,5,6,7,8,9)


# Python은 Overloading 기능을 지원하지 X
# Overloading
#  . 같은 이름의 메서드 (함수) 를 인자의 구성에 따라서 여러개 만들 수 있도록 하는 기능

def intsum(sValue, *Values):
    print(sValue, "첫 번째 함수")


def intsum(sValue) :
    print(sValue, "두 번째 함수")

intsum("1")
intsum("1", 1,2,3,4)




####################################################################
# 선택적 인수
# 인자의 기본 값을 주는 기능
# 코드의 유지보수성을 향상 시키기 위하여 사용
####################################################################

# 선택적 인수 기능을 통하여 기존에 사용하던 로직은 수정하지 않고 유연하게 프로젝트를 유지 할 수있음

def sumCal(iValue1, iValue2, iValue3 = 0) :
    print(iValue1 + iValue2 + iValue3)

sumCal(10,20)
sumCal(20,30)
sumCal(40,40)
sumCal(10,20,30)


# 키워드 인수
# 인자를 직접 지칭하는 인수

def sumCal(iValue1, iValue2, iValue3) :
    print(iValue1 + iValue2 + iValue3)

sumCal(iValue1=10, iValue2=20, iValue3=30)
sumCal(10, iValue2=20, iValue3=30)
sumCal(iValue1=10, iValue3=20, iValue2=30) # 위치 교환



####################################################################
# 키워드 가변로직(키워 가변인수)
# - 가변 인자에 변수 명을 포함하여 전달하는 방법
#  . 가변 인자의 설정은 **[변수명] 으로 한다.
#  . 인수의 키워드와 같은 각각 가변인자 튜플의 key 와 Value로 할당된다.
####################################################################

# 키워드 가변인수의 예시
def calstep(**params) :
    # 키워드 가변 인자의 속성 값
    begin = params['begin']
    end   = params['end']
    sum   = 0
    # for num in range(begin, end + 1 , params[0]): # index 로 호출 할 경우 에러발생
    for num in range(begin, end + 1 , params['step']):
        sum += num
    return sum

print('범위의 홀수합은 : ', calstep(begin = 1, end = 100, step = 2))


# 가변인자와 키워드 가변인자의 혼용
def calstep(name, *score, **option):
    print(name)
    sum = 0

    for jumsu in score : 
        sum += jumsu
    print('총점 : ', sum)

    if option['avg'] == True :
        print("평균 : ", sum / len(score))

calstep("김범수", 90,80,80,90, avg = True)
calstep("이수", 80,90, avg = False)
