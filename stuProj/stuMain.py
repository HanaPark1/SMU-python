from stuModule import *
from stuFunc import *

# 선택된 과목 수정 함수
def sub_modify(subject):
    print(f"[ {title[choice+1]} 과목 수정 ]")
    print(f"현재 {title[choice+1]}점수: {subject}")
    subject_score = int(input("수정할 점수를 입력하세요: "))
    print(f"{subject_score}점으로 변경되었습니다. ")
    return subject_score

# 학생 성적 프로그램
while True:
    #상단 메뉴
    choice = tmenu_print()
    #학생성적입력 함수
    if choice == 1:
        stu_input()
    elif choice == 2:
        stu_ouput()
    elif choice == 3:
        print("[ 학생 성적 수정]")
        search = input("수정하고자 하는 학생 이름을 입력하세요: ")
        temp = 0
        for s in students.students:
            if search == s.name:
                temp = 1
                print(f"{search} 학생을 찾았습니다. 성적을 수정합니다")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print('-'*30)
                try:
                    choice = int(input("수정할 과목의 번호를 입력하세요: "))
                except Exception as e:
                    print(e)
                if choice == 1:
                    s.kor = sub_modify(s.kor) # subject = s.kor, s.eng, e.math
                elif choice == 2:
                    s.eng = sub_modify(s.eng)
                elif choice == 3:
                    s.math = sub_modify(s.math)