print("-"*30)
print(" "*5,end="")
print("[  학생 성적 프로그램  ]")
print("-"*30)

count = 1
while True:
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("4. 학생 성적 삭제")
    print("5. 학생 성적 정렬")
    print("6. 학생 성적 검색")
    print("0. 프로그램 종료")
    print("-"*30)
    
    # 번호 입력
    choice = int(input("원하는 번호를 입력하세요: "))
    print()
    
    students = list()
    count = 1
    
    # 원하는 프로그램 실행
    if choice == 1:
        
        print("[ 학생 성적 입력 ]")
        student = []
        no = 1
        name = input("이름을 입력하세여: ")
        kor = int(input("국어 점수를 입력하세여: "))
        eng = int(input("영어 점수를 입력하세여: "))
        math = int(input("수학 점수를 입력하세여: "))
        total = kor+eng+math
        avg = total/3
        rank = 0
        student = [no, name, kor, eng, math, total, avg, rank]
        students.append(student)
        
    if choice == 2:
        print("[ 학생 성적 출력 ]")
        while True:
            print("[ 학생 성적 프로그램 ]")
            print("-"*60)
            print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수\t")
            print("-"*60)

            for stu in students:
                for i,s in enumerate(stu):
                    if i != 6:
                        print(s, end='\t')
                    else:
                        print(f"{s:.2f}",end='\t')
                print()
        
    if choice == 0:
        print("[ 프로그램 종료 ]")
        break
    print()