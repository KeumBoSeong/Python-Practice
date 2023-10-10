####################################################################
# 조건문
# - 분기문
# -- 조건에 따라 로직의 흐름을 나눌 수 있다. (제어, 컨트롤)
# -- 조건의 진위 (참 or 거짓) 의 여부에 따라 명령의 실행 여부를 결정한다.
####################################################################

# if의 기본 문법
age = 19
if age < 20 :
    print("안녕하세요")
    print("미성년자 입니다.")

# 비교 연산자와 if 분기문의 사용 예시
message = input("숫자를 입력하세요")
value = int(message)
if value == 5:
    print("5입니다.")
if value > 5:
    print("5를 초과합니다..")
if value < 5:
    print("5 미만입니다.")





# 순서상 뒤쪽으로 배치되는 문자 (문자 코드)는 큰것으로 판단
if "A" > "a" :
    print("대문자 A가 더 큽니다.")
if "A" < "a" :
    print("소문자 a가 더 큽니다.")


if "Bling" > "Beaute" :
    print("Beaute 가 후순위에 있는 문자입니다.")


# != : 다르다 이고 만족하면 True를 반환한다

if 4 != 5 :
    print("4와 5는 다릅니다.")


# 논리연산자.
# 두개 이상의 조건을 동시에 비교할 경우 사용
value = int(input("숫자를 입력하세요."))
if value > 0 and value <= 10:
    print("1과 10 사이에 있는 수 입니다.")
if value > 10 or value <= 0 :
    print("1과 10 사이에 있는 수가 아닙니다.")



# 아래과 같이 표현할 수 있다.
value = int(input("숫자를 입력하세요."))
if 0 < value <= 10:
    print("1과 10 사이에 있는 수 입니다.")



# 논리연산자 not의 사용 예시
# value 가 0 일 경우 비교 연산자를 통해 True 가 되지만 not을 만나 False 로 Switching
# False 조건 이므로 메세지가 출력 되지 않는다. (C# 에서는 !)
value = int(input("숫자를 입력하세요."))
if not value == 0:
    print("0이 아닙니다.")




####################################################################
# In 과 Not In
# 포함되어 있는지 확인.
####################################################################
message = "안녕하세요"
if "안" in message :
    print("문자 \"안\" 은 포함되어 있습니다.")
if "." not in message :
    print("문자 \".\" 은 포함되어 있지 않습니다.")





####################################################################
# 코드 블럭과 n개의 분기 흐름 제어
# - 블럭단위
#  . 컴퓨터가 코드를 수행하는 단위
#  . 분기문의 경우 해당 조건에 따른 로직이 나뉘어 지고 블럭 단위의 로직을 수행 하게된다.
#  . Python 언어는 들여쓰기로 블럭을 표현한다.
####################################################################

# elif
# 상위 분기 결과가 False 일 경우 그 나머지 경우 중 조건을 만족하는 경우의 로직을 수행 하도록 제어하는 기능
number = input("번호를 입력하세요")
if number == "12345" :
    print("1등입니다.")
elif number == "123456" :
    print("2등입니다.")
else :
    print("꽝 입니다.")

print("출근준비")


# if 문의 중첩
# if 문 내에 분기의 흐름을 N개 생성 할 수 있다.
# 너무 많은 if 문을 중첩 할 경우 코드가 복잡해 지고 가독성이 떨어 질 수 있다.
number = input("번호를 입력하세요")
if number == "12345" :
    print("1등입니다.")
elif number == "123456" :
    print("2등입니다.")
else :
    bonus = input("보너스 번호를 입력하세요. : ")
    if bonus == "123458":
        print("3등 입니다.")
    else : 
        print("꽝 입니다.")

print("출근준비")




