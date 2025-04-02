students = []

count = 1
title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']

while True:
    print("[ 학생 성적 프로그램 ]")
    print('-'*30)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("0. 프로그램 종료")
    print()
    choice = int(input("원하는 번호를 입력하세요.: "))
    
    if choice == 1:
        print("[ 학생 성적 입력 ]")
        no = count
        name = input(f"{no}번째 학생을 입력하세요: (0. 이전 화면 이동) ")
        if name == '0' :
            continue
        kor = int(input("국어 성적을 입력하세요: "))
        eng = int(input("영어 성적을 입력하세요: "))
        math = int(input("수학 성적을 입력하세요: "))
        total = kor+eng+math
        avg = total / 3
        rank = 0
        students.append(
            {'no':no, "name":name,'kor':kor, 'eng':eng, 'math':math, 
            'total':total, 'avg':avg, 'rank':rank})
        print(f"{name} 학생 성적을 등록하였습니다. ")
        
    elif choice == 2:
        print("[ 학생 성적 출력 ]")
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
        print('-'*60)
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}\t")