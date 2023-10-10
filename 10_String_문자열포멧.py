####################################################################
# 포멧팅 : 문자열 안에 세부정보를 포함하여 출력 하도록 명령하는 기능
# 문자열 사이에 특정 정보를 삽입하여 하나의 문자열을 만들어 내는 기능
####################################################################

# 표식의 사용 예제

station = '구로'
direction = False

print("이번 역은 %s 역 입니다. 내리실 문은 %s 입니다." 
      %(station, '왼쪽' if direction else "오른쪽"))



# 문자열의 서식
# 정렬을 지정

value = 123
print('###%d###' % value)     #  ###123###
print('###%5d###' % value)    #  ###  123###
print('###%3d###' % value)    #  ###123### 이미 '###' 으로 3칸을 차지 하므로, 공백을 표현하지 X



# 숫자의 경우 오른쪽 정렬이 기본임
price = [30,13500,2000]
for p in price :
    print('가격 : %10d 원' %p)   # 오른쪽 정렬

for p in price :
    print('가격 : %-10d 원' %p)  # 왼쪽 정렬




# 실수의 포멧
import math
pie = math.pi
print("%8f" %pie)
print("%8.3f" %pie)   # 총 8개의 실수를 표현하는데 소수점 4자리에서 반올림
print("%-8.3f" %pie)  # 총 8개의 실수를 표현하는데 소수점 4자리에서 반올림  (왼쪽 정렬)



####################################################################
# 신형 포멧팅 (문자열의 보간 : 누락/빈곳을 채워넣음)
####################################################################
# { } 중괄호 내의 문자열 가공
id           = "ADMIN"
MailAddress  = "dev.bs7656@gmail.com"
Name         = "관리자"

print("이름 : {}, ID : {}, 메일주소 : {}".format(Name, id, MailAddress))



# Index를 통해 인수의 순서를 배치할 수 있다.
id           = "ADMIN"
MailAddress  = "dev.bs7656@gmail.com"
Name         = "관리자"
                                               #    0        1       2
print("이름 : {2}, ID : {0}, 메일주소 : {1}".format(id, MailAddress,Name))


# { } 중괄호 안에 변수 이름을 적어두고 키워드로 값을 나열 할 수 있다.
print("이름 : {Name}, ID : {id}, 메일주소 : {MailAddress}".format(id      = "ADMIN",
                                               MailAddress  = "dev.bs7656@gmail.com",
                                               Name         = "관리자"))



# Key 와 Value 를 가지는 자료형(Dic) 을 생성하여 매핑 할 수 있다.
User = {'ID'           : 'ADMIN',
        'Name'         : '관리자' ,
        "MailAddress"  : "div.bs7656@gmail.com"}
print("이름 : {0[Name]} , 아이디 : {0[ID]}, 메일주소 : {0[MailAddress]}".format(User))



# 서식지정

Age      = 25
Name     = '관리자'
Height   = 177.12

                                                        #   0     1     2
print("이름 : {2:10s}, 나이 : {0:5d}, 키 : {1:8.2f}".format(Age,Height,Name))





####################################################################
# 실습

# 1. "차종 : 코란도C, 제조사 : 쌍용, 배기량 : 1998" 문자열에서 "제조사" 만 추출하여 출력

Model = "코란도C"
Manufacturer = "쌍용"
Engine = "1998"

print("제조사 : {}".format(Manufacturer))

value = "차종 : 코란도, 제조사 : 쌍용, 배기량 : 1988"
print(value[16:18])

# 2. 임의의 주민등록번호 13 자리를 입력받아 현재 나이 와 성별을 출력하는 프로그램을 작성해 보세요

# '-' 를 제외 한 숫자를 입력하지 않은 경우 예외 처리 한다.
# 13자리 를 입력하지 않은경우 의 예외상황 처리 한다.
# 정확한 결과를 출력할때까지 반복한다

while True :
    IDnumber = input("주민등록 번호를 입력하세요.").replace("-", "").replace(" ","")
    ## 벨리데이션 구문 <검증 로직 먼저 수행> ##
    if not IDnumber.isnumeric() : # 숫자를 입력하지 않은 경우 리턴
        print("숫자만 입력하세요")
        continue
    ## 숫자만 입력되어 있는 상태

    elif len(IDnumber) != 13 :
        print("주민등록번호는 13자리로 입력하세요")
        continue

    ## 정상적으로 데이터를 받았기 때문에 비교하는 로직
    result = "성별 : "
    sex = IDnumber[6] 
    if sex == "1" or sex == "3" :
        result += "남자"
    elif sex == "2" or sex == "4" :
        result += "여자"
    else :
        print("성별을 확인할 수 없습니다.")
        continue

    age = int(IDnumber[:2])
    result += "%d 살 입니다." %  (23 + (100-age)) if age > 23 else (23-age)
    print(result)
    break

