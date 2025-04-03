import stu_func
# 임포트 대상 별칭 사용 방법
# import stu_func as stu

students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
]

count = 4
title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
choice = 0

# 함수 사용
# - 1. 중복된 코드의 재사용
# - 2. 소스의 가독성 증대

# 화면 출력 함수 선언

while True:
    choice = stu_func.stu_menu_print()
    
    if choice == 1:
        count = stu_func.stu_input(count, students)

    elif choice == 2 :
        stu_func.stu_print(title, students)
        
    elif choice == 3 :
        stu_func.stu_change(title, students)
    elif choice == 4 :
        stu_func.stu_rank(students)
    elif choice == 0 :
        break