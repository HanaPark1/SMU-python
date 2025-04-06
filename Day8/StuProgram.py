import StuFunc
# 임포트 대상 별칭 사용 방법
# import stu_func as stu

students = []

count = 4
title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
choice = 0

# stu.txt 파일에서 데이터 읽어와 아래 배열에 데이터 입력
with open("Day8/stu.txt", 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line:
            break
        s = line.strip().split(',')
        students.append({
            'no': int(s[0]),
            'name': s[1],
            'kor' : int(s[2]),
            'eng': int(s[3]),
            'math' : int(s[4]),
            'total' : int(s[5]),
            'avg' : float(s[6]),
            'rank' : int(s[7])
        })

# 함수 사용
# - 1. 중복된 코드의 재사용
# - 2. 소스의 가독성 증대

# 화면 출력 함수 선언

while True:
    choice = StuFunc.stu_menu_print()
    
    if choice == 1:
        count = StuFunc.stu_input(count, students)

    elif choice == 2 :
        StuFunc.stu_print(title, students)
        
    elif choice == 3 :
        StuFunc.stu_change(title, students)
        
    elif choice == 4 :
        StuFunc.stu_rank(students)
        
    elif choice == 5 :
        students2 = [*students]
        print("[ 학생 성적 정렬]")
        print("1. 이름 순차 정렬")
        print("2. 이름 역순 정렬")
        print("3. 합계 순차 정렬")
        print("4. 합계 역순 정렬")
        print("5. 번호 순차 정렬")
        print("6. 번호 역순 정렬")
        print("0. 이전 화면 이동")
        print('-'*30)
        choice = int(input("원하는 번호를 입력하세요: "))
        if choice == 1:
            students2.sort(key=lambda x:x['name'])
        elif choice == 2:
            students2.sort(key=lambda x:x['name'], reverse=True)
        elif choice == 3:
            students2.sort(key=lambda x:x['total'])
        elif choice == 4:
            students2.sort(key=lambda x:x['total'], reverse=True)
        elif choice == 5:
            students2.sort(key=lambda x:x['no'])
        elif choice == 6:
            students2.sort(key=lambda x:x['no'], reverse=True)
        
        StuFunc.stu_print(title, students2)
        
    elif choice == 6 :
        print("[ 학생 성적 저장]")
        name = input("삭제하고자 하는 학생 이름을 입력하세요: ")
        temp = 0
        for i,s in enumerate(students):
            if name == s['name']:
                temp == 1
                print(f"{s['no']}번 {name} 학생을 찾았습니다")
                answer = input("학생 성적을 삭제할까요? (삭제시 복구 불가)")
                if answer == 'y':
                    del students[i]
                print(f"{name} 학생을 삭제했습니다. ")
                print()
                break
        if temp == 0:
            print(f"{name} 학생을 찾지 못했습니다. ")
        
    elif choice == 7 :
        StuFunc.stu_rank(students)
        print("[ 학생 성적 저장]")
        with open('Day8/stu.txt', 'w', encoding='utf-8') as f:
            while True:
                for s in students:
                    line = f"{s['no'],s['name'],s['kor'],s['eng'],s['math'],s['total'],s['avg'],s['rank']}\n"
                    f.write(line)
                    print("파일이 저장되었습니다")
                if not s:
                    break
                    
    elif choice == 0 :
        break