# print(" "*10,end="")
# print("[ 학생성적 프로그램 ]")
# print("-"*30)
# print("1. 학생 성적 입력")
# print("2. 학생 성적 출력")
# print("3. 학생 성적 수정")
# print("4. 학생 등수 처리")
# print("5. 학생 성적 정렬")
# print("6. 학생 성적 삭제")
# print("7. 학생 성적 저장")
# print("0. 프로그램종료")
students = []
title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
count = 1

# with open("Day8/stu.txt", 'r', encoding='utf8') as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         line_info = line.strip().split(',')
#         students.append({
#             'no':int(line_info[0]),
#             'name':line_info[1],
#             'kor' : int(line_info[2]),
#             'eng' : int(line_info[3]),
#             'math' : int(line_info[4]),
#             'total' : int(line_info[5]),
#             'avg' : float(line_info[6]),
#             'rank' : int(line_info[7])
#         })

def score_change(score_title, choice):
    pre_score = s[score_title[choice]]
    s[score_title[choice]] = int(input(f"현재 {title[choice+1]} 성적 {pre_score}, 수정할 성적을 입력하세요: "))
    
while True:
    print("[ 학생성적 프로그램 ]")
    print("-"*30)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("4. 학생 등수 처리")
    print("5. 학생 성적 정렬")
    print("6. 학생 성적 삭제")
    print("7. 학생 성적 저장")
    print("0. 프로그램종료")
    choice = int(input("원하는 번호를 입력하세요: "))
    
    if choice == 1:
        print("[ 학생 성적 입력 ]")
        no = count
        name = input(f"{no}번 학생의 이름을 입력하세요 (0. 이전 화면 이동): ")
        if name == '0':
            continue
        kor = int(input("국어 성적을 입력하세요: "))
        eng = int(input("영어 성적을 입력하세요: "))
        math = int(input("수학 성적을 입력하세요: "))
        total = kor + eng + math
        avg = total / 3
        rank = 0
        students.append({
            'no' : no,
            'name' : name,
            'kor' : kor,
            'eng' : eng,
            'math' : math,
            'total' : total,
            'avg' : avg,
            'rank' : rank
        })
        print(f"{no}번 {name} 학생을 입력했습니다.")
        count += 1
        print()
        
    elif choice == 2:
        print("[ 학생 성적 출력 ]")
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
        print("-"*60)
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        print()  

    elif choice == 3:
        print("[ 학생 성적 수정 ]")
        temp = 0
        score_title = ['', 'kor', 'eng', 'math']
        name = input("수정할 학생의 이름을 입력하세요: (0. 이전 화면 이동)")
        if name == '0':
            continue
        for s in students:
            if name == s['name']:
                temp = 1
                print(f"{name}학생을 찾았습니다. ")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                choice = int(input("수정할 과목을 선택하세요: "))
                if choice == 1:
                    score_change(score_title, choice)
                elif choice == 2:
                    score_change(score_title, choice)
                elif choice == 3:
                    score_change(score_title, choice)
                s['total'] = s[score_title[1]]+s[score_title[2]]+s[score_title[3]]
                s['avg'] = s['total'] / 3
                print(f"{s['name']} 학생의 성적을 수정하였습니다.")
                
    elif choice == 4:
        print("[ 학생 등수 처리 ]")
    elif choice == 5:
        print("[ 학생 성적 정렬 ]")
    elif choice == 6:
        print("[ 학생 성적 삭제 ]")
    elif choice == 7:
        print("[ 학생 성적 저장 ]")