def stu_menu_print():
    print(" "*10,end="")
    print("[ 학생성적 프로그램 ]")
    print("-"*30)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 등수처리")
    print("0. 프로그램종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요: "))
    
    return choice

#학생 성적 입력 함수 선언
def stu_input(count, students):
    
    no = count
    name = input(f"{no}번 학생의 이름을 입력하세요: ")
    kor = int(input("국어 성적을 입력하세요: "))
    eng = int(input("영어 성적을 입력하세요: "))
    math = int(input("수학 성적을 입력하세요: "))
    total = kor + eng + math
    avg = total / 3
    rank = 0
    students.append({'no':no, 'name':name, 'kor':kor, 'eng':eng, 'math':math, 'total':total, 'avg':avg, 'rank':rank})
    print(f"{no}번 {name} 학생 성적을 등록하였습니다.")
    count += 1
    
    return count

def stu_print(title, students):
    print("[ 학생 성적 출력]")
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
    print("-"*60)
    for s in students:
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}\t")
    print()
    
def stu_change(title, students):
    temp = 0
    name = input("성적을 수정할 학생의 이름을 입력하세요 (0. 이전 화면 이동): ")
    for s in students:
        if name == s['name'] :
            temp = 1
            print(f"{name} 학생을 찾았습니다. 수정할 과목의 번호를 선택하세요: ")
            print("1. 국어")
            print("2. 영어")
            print("3. 수학")
            print('-'*10)
            choice = int(input("수정할 과목의 번호를 선택하세요: "))
            sub_list = ['', 'kor', 'eng', 'math']
            
            if choice == 1:
                score_modi(s,sub_list,title,choice)
            elif choice == 2:
                score_modi(s,sub_list,title,choice)
            elif choice == 3:
                score_modi(s,sub_list,title,choice)
            s['total'] = s['kor'] + s['eng'] + s['math']
            s['avg'] = s['total'] / 3
            print("수정이 완료되었습니다. ")
    if temp == 0:
        print(f"{name} 학생을 찾지 못했습니다. 다시 시도해 주세요.")
        
# 학생 점수 수정 함수 선언
def score_modi(s,sub_list,title,choice):
    pre_score = s[sub_list[choice]]
    print(f"현재 {title[choice+1]} 성적: {pre_score}")
    s[sub_list[choice]] = int(input("수정 성적을 입력하세요: "))
    
def stu_rank(students):
    print("[ 등수 처리 ]")
    for s in students:
        num = 1
        for ss in students:
            if s['total'] < ss['total']: # 등수 비교
                num += 1
        s['rank'] = num # 등수 입력     
    print("등수 처리가 완료되었습니다.")
    print()