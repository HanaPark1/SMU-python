from stuModule import  *

# 선언
students = Students()
title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']


# 상단메뉴
def tmenu_print():
    print(" "*20)
    print(" [ 학생 성적 처리 ]")
    print("-"*50)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    choice = 0
    
    try:
        choice = int(input("원하는 번호를 입력하세요: "))
    except Exception as e : print(e)
    return choice

# 학생 성적 입력 함수 선언
def stu_input():
    print("[ 학생 성적 입력 ]")
    name = input(f"{(Student.count)}번째 학생 이름을 입력하세요: ")
    score = [0]*3
    for i in range(len(score)):
        score[i] = int(input(f"{title[i+2]}점수를 입력하세요: "))
    students.add(Student(name,*score))
    print(f"{name} 학생이 등록되었습니다.")
    print()
    
def stu_ouput():
    print("[ 학생 성적 출력 ]")
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
    print("-"*60)
    for s in students.students:
        print(f"{s.no}\t{s.name}\t{s.kor}\t{s.eng}\t{s.math}\t{s.total}\t{s.avg}\t{s.rank}\t")