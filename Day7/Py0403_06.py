# 성적 처리 프로그램
# 데이터 생성 - 리스트 타입의 딕셔너리 데이터 생성
# 출력 화면
# 1. 학생 성적 입력
# - 학생 번호 자동 생성
students = []
count = 1
title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
# - 학생 성적 입력을 무한 반복 실행
def select_subj(s, subject):
    pre_score = s[subject[choice]]
    print(f"현재 {title[choice+1]} 점수: {pre_score}")
    s[subject[choice]] = int(input(f"수정할 {title[choice+1]} 점수를 입력하세요: "))
    print(f"{pre_score}에서 {s[subject[choice]]}로 변경되었습니다")
    
while True:
    print("[ 학생 성적 프로그램 ]")
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("4. 학생 성적 정렬")
    print("5. 학생 성적 검색")
    print("6. 학생 등수 처리")
    print("0. 프로그램 종료")
    choice = int(input("원하는 번호를 입력하세요: "))

    if choice == 1:
        print("[ 학생 성적 입력 ]")
        no = count
        name = input(f"{no}번째 학생을 입력하세요 (0. 이전 화면 이동): ")
        score = [0]*3
        for i in range(3):
            score[i] = int(input(f"{title[i+2]} 성적을 입력하세요: "))
        total = score[0] + score[1] + score[2]
        avg = total / 3
        rank = 0
        students.append({'no':no, 'name':name, 'kor':score[0], 'eng':score[1], 'math':score[2], 'total':total, 'avg':avg, 'rank':rank})
        print(f"{no}번 {name} 학생이 등록되었습니다. ")
        count += 1
        print()
    elif choice == 2:
        print("[ 학생 성적 출력 ]")
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
        print("-"*60)
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}\t")
    elif choice == 3:
        temp = 0
        print("[ 학생 성적 수정 ]")
        name = input("성적을 수정할 학생의 이름을 입력하세요: ")
        for s in students:
            if name == s['name']:
                temp==1
                print(f"{name} 학생을 찾았습니다. ")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                choice = int(input("수정할 과목을 선택하세요: "))
                subject = ['', 'kor', 'eng', 'math']
                if choice == 1:
                    select_subj(s,subject)
                elif choice == 2:
                    select_subj(s,subject)
                elif choice == 3:
                    select_subj(s,subject)
                s['total'] = s[subject[1]] + s[subject[2]] + s[subject[3]]
                s['avg'] = s['total'] / 3
        if temp == 0:
            print(f"{name} 학생이 존재하지 않습니다. 다시 입력해 주세요.")
    elif choice == 5:
        print("[ 학생 성적 검색 ]")
        name = input("학생의 이름을 입력해 주세요: ")
        for s in students:
            if name == s['name']:
                print("[ 학생 성적 출력 ]")
                print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
                print("-"*60)
                print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}\t")
    elif choice == 6:
        print("[ 학생 등수 처리 ]")
        for s in students:
            num = 1
            for ss in students:
                if s['total'] < ss['total']: # 등수 비교
                    num += 1
            s['rank'] = num # 등수 입력     
        print("등수 처리가 완료되었습니다.")

# - 이전 화면 이동 구현
# - 점수 입력에 대한 체크: 숫자인지 확인, 0<~100 확인
# 2. 학생 성적 출력
# - 상단 타이틀 출력
# - 각 학생별 성적 출력
# 3. 학생 성적 수정
# - 수정하고자 하는 학생 검색
# - 수정하려는 과목 선택
# - 검색이 되지 않았을 경우 구현
# 4. 학생 성적 정렬
# - 이름으로 순차 정렬
# - 합계로 순차 정렬
# 5. 학생 성적 검색
# - 찾고자 하는 학생 검색 후 있으면 화면 출력
# 6. 학생 등수 처리
# - 합계를 기준으로 등수 처리 진행
# 0. 종료
