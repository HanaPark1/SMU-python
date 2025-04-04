f = open("Day8/stu.txt", "a", encoding="UTF-8")
count = 1
while True:
    no = count
    name = input("이름을 입력하세요:(0. 종료) ")
    if name == '0' :
        break
    kor = int(input("국어 점수를 입력하세요: "))
    eng = int(input("영어 점수를 입력하세요: "))
    math = int(input("수학 점수를 입력하세요: "))
    total = kor+eng+math
    # avg = total / 3
    lines = f"{no},{name},{kor},{eng},{total}\n"
    count += 1
    f.write(lines)
    print("학생 성적이 저장되었습니다. ")
f.close()