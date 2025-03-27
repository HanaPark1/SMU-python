# 파이썬 변수 타입
# bool, int, float, string type

#변수 선언
a = 20

#print()
print("입력된 숫자: %d" % (a))
print("입력된 숫자: {}".format(a)) # 포맷 함수 사용법 1
print(f"입력된 숫자: {a}") # 포맷 함수 사용법 2

# 입력 -  input => 타입 :  str 타입
num1 = int(input("숫자를 입력하세요: ")) #숫자 입력 시에는 int로 형변환 (int())
print("입력된 숫자: {}".format(num1))

# 학생 성적 프로그램
# 이름, 국어, 영어, 수학 입력받아 합계와 평균을 출력하는 프로그램 구현

print("-"*50)
print("학생 성적 프로그램")
print("-"*50)

name = input("이름을 입력하세요.")
kor = int(input("국어 성적을 입력하세요."))
eng = int(input("영어 성적을 입력하세요."))
math = int(input("수학 성적을 입력하세요."))
total = kor+eng+math
avg = total/3

print()
print("이름\t국어\t영어\t수학\t합계\t평균")
print("-"*50)
print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(name, kor,eng,math,total,avg))