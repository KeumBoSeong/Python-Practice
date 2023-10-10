####################################################################
# 프로그램 시스템의 정보 확인하기
# 이기종간의 통신 (다른 설비나 장비 등에 통신을 할 경우 규악을 확인하고 맞출수 있음)
# 컴퓨터가 메모리에 데이터를 저장할 때, 처리하는 방식을 확인할 수 있다.
####################################################################

import sys

print('버전', sys.version)
print("플랫폼" , sys.platform)
if ( sys.platform == 'win32') :
    print(sys.getwindowsversion)

# little 엔디언 : 데이터를 통신할 때 방식, 작은 데이터를 우선으로 받아서 처리
# big 엔디언 : 큰 데이터를 우선으로 받는다.
# little 작은것 부터 0 ~ 100 데이터가 저장.
# Big 큰 것 부터 0 ~ 100 데이터가 저장
print('바이트순서' , sys.byteorder)     ## little
print('모듈 경로', sys.path)


####################################################################
# 외부에서 파이썬 모듈 실행하기
# 달력의 정보를 표현 ( 인수에 따른 결과)
####################################################################

import sys
import time
import calendar
## 외부에서 모듈을 실행하였을 때 전달 인수를 1개만 주었을 경우 (모듈에 대한 명칭)

if (len(sys.argv)) == 1 :
    t = time.time()
    tm = time.localtime()
    calendar.prmonth(tm.tm_year, tm.tm_mon)

## 프로그램 명칭, 년도를 외부에서 전달하였을 경우

elif (len(sys.argv)) == 2 :
    print(calendar.calendar(int(sys.argv[1])))  # 전달받은 년도의 달력 보여주기

## 프로그램 명칭, 년도, 월 외부에서 전달하였을 경우
elif (len(sys.argv)) == 3 :
    # 전달받은 년도 / 월 의 달력 보여주기
    print(calendar.prmonth(int(sys.argv[1]), int(sys.argv[2])))  # 전달받은 년도의 달력 보여주기
else : 
    print("전달 받은 값의 개수가 정확하지 않습니다.")



####################################################################
# 기념일 계산하기
#  .time.mktim()
#  . 년, 월, 일, 시, 분, 초 ..... 을 튜플로 전달받아 기준시간에서 경과된 초를 구하는 함수
####################################################################

import time

year = int(input("년도 : "))
month = int(input("월 : "))
day = int(input("일 : "))

# 데이터를 전달하기 위해 튜플
# 튜플의 인수는 총 9개로, 세부적인 시간에 대한 정보를 필수로 입력해야 한다.
# 년 월 일 시 분 초 mis (x)
tm = (year, month, day,0,0,0,0,0,0)
# time.time()                          현재 시각
# time.mktime(tm)                      과거 시각
# (time.time() - time.mktime(tm))      경과된 초
# (24 * 60 * 60) :                     초를 일단위로 변경
ellaps = (time.time() - time.mktime(tm)) / (24 * 60 * 60)
print(str(ellaps) + "일 째 입니다.")
