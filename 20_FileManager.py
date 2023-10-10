####################################################################
# 파일을 다루는데 사용되는 모듈 shutil, os
# 파일을 이동, 복사
####################################################################

# 파일 복사의 예제
import shutil

shutil.copy("C:\Python\Src\word.txt", 'C:\Python\Src\word2.txt')



####################################################################
# 절대경로 : 루트 부터 파일의 이름까지를 나타낸 경로 ex) (C:\User\a.exe)
# 상대경로 : 특정 파일의 이름만 나타낸 것 (a.exe)
####################################################################

# 파일의 절대경로를 문자열로 만들기
import os

# 현재 스크립트의 파일 경로
script_path = os.path.abspath(__file__)


# 현재 스크립트 파일이 위치한 디렉토리
script_dir = os.path.dirname(script_path)

# 파일의 절대 경로를 표현할 파일 상대 경로
file_abs  = "word.txt"




# 절대 파일 경로 만들어주는 함수
# 운영체제에 따라 파일 경로를 지정하는 표현식이 다르다
# window : \ mac, Linux : /
# join 시 절대 경로의 표현식을 운영체제에 맞게 표현해 준다.
file_full_path = os.path.join(script_dir, file_abs)

print("특정 파일의 {0} 의 절대경로 {1}".format(file_abs,file_full_path))


####################################################################
# 파일 검색 및 출력하기
# 1. 폴더 내의 항목검색
####################################################################

import os
filelist = os.listdir("C:\\Python\\Src\\MP3")
for file in filelist : 
    print(file)


####################################################################
# 2. 함수의 재귀 호출을 통하여 폴더에 존재하는 (n개의 폴더 포함) 모든 mp3 폴더 찾기
####################################################################
import os

# 폴더를 검색하는 함수
def searchDir(dirpath) :
    filelist = os.listdir(dirpath)
    for file in filelist : 
        fullpath = dirpath + "\\" + file   # C:\Python\Src\MP3\2022
        if os.path.isdir(fullpath) :       #filepath 가 폴더 인지 확인
            print("[" + fullpath + "]")
            searchDir(fullpath)            # 재귀함수 호출 : 더이상 폴더가 없을 때 까지
        else :                             # 절대경로가 폴더유형이 아닐 경우
            print("\t" + fullpath)         # C:\Python\Src\2022\a.mp3
# 검색하기 위한 폴더 명칭을 인수로 전달
searchDir("C:\Python\Src\MP3")
