from stuModule import *
from stuFunc import *

# 학생 성적 프로그램
while True:
    #상단 메뉴
    choice = tmenu_print()
    #학생성적입력 함수
    if choice == 1:
        stu_input()
    elif choice == 2:
        print("[ 학생 성적 출력 ]")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
        print("-"*60)
        for s in students:
            print()