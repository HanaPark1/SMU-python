students = [
    [1, "홍길동", 100, 100, 100, 300, 100, 0, 1],
    [2, "유관순", 100, 100, 99, 299, 99, 67, 2],
    [3, "이순신", 100, 100, 99, 299, 99, 67, 2],
    ]

count = 4 # 학생 번호 생성
title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']

while True:
    print("-"*30)
    print(" "*5,end="")
    print("[  학생 성적 프로그램  ]")
    print("-"*30)

    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("4. 학생 성적 삭제")
    print("5. 학생 성적 정렬")
    print("6. 학생 성적 검색")
    print("7. 등수 처리")
    print("0. 프로그램 종료")
    print("-"*30)
    choice =  int(input("원하는 번호를 입력하세요: "))
    
    # 학생 성적 입력
    if choice == 1:
        print("[ 학생 성적 입력 ]")
        no = count 
        name = input(f"{no}번째 학생의 이름을 입력하세요: ")
        kor = int(input("국어 성적을 입력하세요: "))
        eng = int(input("영어 성적을 입력하세요: "))
        math = int(input("수학 성적을 입력하세요: "))
        total = kor + eng + math # 합계
        avg = total / 3 # 평균
        rank = 0
        students.append([no, name, kor, eng, math, total, avg, rank]) # 리스트 삽입
        print(f"{name} 학생을 추가하였습니다. ")
        
    # 학생 성적 출력
    elif choice == 2:
        print("[ 학생 성적 출력 ]")
        for s in students:
            # 리스트 선택 후 요소 출력
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}\t".format(*s))
            
    
    # 학생 성적 수정
    elif choice == 3:
        print("[ 학생 성적 수정 ]")
        name = input("수정할 학생의 이름을 입력하세요: ")
        temp = 0 # temp 초기화
        for idx, s in enumerate(students):
            if name in s:
                temp = 1 # 수정할 학생을 찾은 경우
                
                print(f"수정할 {name} 학생을 찾았습니다")
                print()
                print("[ 수정하려는 과목 선택 ]")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("0. 취소")
                
                choice = int(input("수정할 과목을 선택해 주세요"))
                if choice == 1:
                    print(f"현재 국어 성적: {s[2]}")
                    s[2] = int(input("변경할 국어 성적: "))
                elif choice == 2:
                    print(f"현재 영어 성적: {s[3]}")
                    s[3] = int(input("변경할 영어 성적: "))
                elif choice == 3:
                    print(f"현재 수학 성적: {s[4]}")
                    s[4] = int(input("변경할 수학 성적: "))
                elif choice == 0:
                    print(f"{name} 학생의 성적 수정을 취소합니다. 다시 입력하세요.")
                    break
                s[5] = s[2]+s[3]+s[4] # 합계
                s[6] = s[5]/3 # 평균
                print(f"{name} 학생의 성적 수정했습니다.")
        if temp == 0:
            print("학생을 찾지 못했습니다. 다시 입력하세요. ")
    
    # 학생 성적 삭제   
    elif choice == 4:
        print("[ 학생 성적 삭제 ]")
        name = input("삭제할 학생의 이름을 입력하세요: ")
        temp = 0
        for s in students:
            if name in s:
                temp = 1
                choice = int(input((f"{name} 학생을 찾았습니다. 성적을 삭제할까요? (0. 취소 1. 실행)")))
                if choice == 1 :
                    del students[s[0]-1]
                    print(f"{name} 학생의 성적을 삭제했습니다.")
                else:
                    print(f"{name} 학생의 성적 삭제를 취소합니다. 다시 입력하세요.")
        if temp == 0:
            print(f"{name} 학생을 찾지 못하였습니다. 다시 입력하세요.")
    
    elif choice == 0:
        print("프로그램을 종료합니다")
        break