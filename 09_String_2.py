# 문자열의 변경
# 특정 문자를 변경하는 기능.
svalue = "Visual Studio Code를 이용한 python course"
print(svalue.lower()) # 소문자로 변경한다.
print(svalue.upper()) # 대문자로 변경한다.
print(svalue)         # lower()나 upper() 메서드를 사용해도 원본 데이터는 변하지 않는다.

print(svalue.swapcase())    # 대 소 문자를 스위칭
print(svalue.capitalize())  # 문자열의 첫 영문자만 대문자
print(svalue.title())       # 문자열의 문단 별로 첫 영문자 소문자 (카멜롯 표기법)




# 대 / 소 문자 변경 기능의 활용
# 로그인 기능 시 대 / 소 문자 구별 하고 싶지 않을 때
# 프로그램은 대 / 소 문자를 구별하지만 사용자는 대 / 소 문자를 다른 문자로 인식하지 않는다.
# 로그인 기능

dbUserId = "Admin"  # 데이터 베이스에 등록되어 있는 사용자 아이디

while True :
    userid = input("사용자 ID를 입력하세요 : ").lower()
    if userid.lower() == dbUserId.lower() : 
        print("admin 님 반갑습니다.")
        break # 로그인 성공 시 종료
    else :
        print("아이디가 잘못 되었습니다.")






# 공백 제거
svalue = "    Python    "
print(svalue.lstrip(), '좋아요')   # 문자열 왼쪽의 모든 공백을 제거.
print(svalue.rstrip(), '좋아요')   # 문자열 오른쪽의 모든 공백을 제거.
print(svalue.strip(), '좋아요')    # 문자열 왼쪽과 오른쪽의 모든 공백을 제거    



# 문자열의 분할 ***
# split() : 특정 문자열을 기준으로 나눈 문자열을 리스트로 반환.
svalue = "Python Java C# C JavaScript"
print(svalue.split())    #() : 빈 공백을 기준으로 나눈다.



# 문자열을 하나로 합칠 때 join() <-> split()
svalue = "Python,C#,C,Java"
lists = svalue.split(',')
print(lists)                 #(',') : , 기준으로 나눈다.
print(' '.join(lists))       # 특정한 기준으로 결합.




# 특정 문자열을 원하는 문자열로 변경 replace()
svalue = "안녕하세요. ooo 입니다."
print(svalue)
print(svalue.replace("ooo", "김범수"))




# 문자열에 공백을 추가하여 정렬
message = "Hello Python"   # 12글자
message2 = "VsCode"        # 6글자
print(message.ljust(30), ":")   # 오른쪽으로 18 공백
print(message.rjust(30), ":")   # 왼쪽으로 18 공백
print(message.center(30))       # 좌, 우로 9자리 공백
print(message2.center(30))       # 좌, 우로 12자리 공백





title = "안녕하세요 2023 안동대학교 스마트팩토리 S/W 개발 교육과정을 이수하게 된 OOO 입니다. 즐겁고 보람찬 DIGITALTRANING 교육이 되었으면 합니다."
## 1. OOO (대문자 o) 본인이름 변경 후 출력
print("1.OOO (대문자 o) 본인이름 변경 후 출력")
print(title.replace("OOO","금보성"))
print()


## 2. S/W 글자위치 찾아서 출력
print("2. S/W 글자위치 찾아서 출력")
print(title.find("S/W"))
print()


## 3. 시작 단어와 마지막 단어 1자씩 출력
print("3. 시작 단어와 마지막 단어 1자씩 출력")
print(title[0], title[len(title)-1])
print()


## 4. 문자의 앞 뒤에 '-KDT-' 입력
print("4. 문자의 앞 뒤에 '-KDT-' 입력")
print("-KDT- " + title + " -KDT-")
print()


## 5. 'DIGITALTRANING' 글자만 소문자로 변경한 후 출력
print("5. 'DIGITALTRANING' 글자만 소문자로 변경한 후 출력")
result = title.replace("DIGITALTRANING", "DIGITALTRANING".capitalize())
print(result)
print()


## 6. 모든 위치의 공백 없앤후 출력
print("6. 모든 위치의 공백 없앤후 출력")
result = title.replace(" ", "")
print(result)
print()


## 7. .(문단) 을 기준으로 행을 나눠서 출력
print("7. .(문단) 을 기준으로 행을 나누기")
result = title.split(".")
for value in result[0:len(result)-1] :
    print(value.lstrip(),'.', sep='')


# 8. 7에서 나눈 문단을 좌우 공백을 일정하게 둔 가운데 정렬로 표현




