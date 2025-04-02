students = [
    {'no':1, 'name':'홍길동','kor':100,'eng':100,'math':100,'total':300,'avg':100,'rank':1},
    {'no':2, 'name':'유관순','kor':100,'eng':100,'math':99,'total':299,'avg':99, 'rank':2},
    {'no':3, 'name':'이순신','kor':100,'eng':100,'math':99,'total':299,'avg':99, 'rank':3},
]


count = 4
title = ['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
    print("-"*30)
    print(" "*5,end="")
    print("[  학생 성적 프로그램  ]")
    print("-"*30)

    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("0. 프로그램 종료")
    choice =  int(input("원하는 번호를 입력하세요: "))
    
    if choice == 1:
        print("[ 학생 성적 입력 ]")
        no = count
        name = input(f"{no}번 학생 이름을 입력하세요. (0. 이전 화면 이동): ")
        if name == '0' :
            continue
        # score = [0]*3 #kor, eng, math
        # for i in range(3) :
        #     score[i] = int(input(f"{title[i+2]} 성적을 입력하세요: "))
        else: 
            kor = int(input("국어 성적을 입력하세요: "))
            eng = int(input("영어 성적을 입력하세요: "))
            math = int(input("수학 성적을 입력하세요: "))
            total = kor + eng + math # 합계
            avg = total / 3 # 평균
            rank = 0 
        
        students.append(
            {'no':no, "name":name,'kor':kor, 'eng':eng, 'math':math, 
            'total':total, 'avg':avg, 'rank':rank})
        print(f"{name} 학생 성적이 등록되었습니다. ")
        print()
        
    elif choice == 2:
        print("[  학생 성적 출력  ]")
        print("-"*30)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
        print("-"*30)
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}\t")
    
    elif choice == 0:
        print("프로그램을 종료합니다")
        break