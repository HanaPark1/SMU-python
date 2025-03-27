# Quiz 1
# 숫자 2개를 입력받아, 사칙연산 결과값을 출력하시오.
# 포맷함수 사용

#Quiz 2
# 국어, 영어, 수학 점수를 입력받아 평균을 출력하시오
# 합계 240
# 평균 80.00 (두자리까지)

#1
num1 = int(input("첫번째 숫자를 입력하세요"))
num2 = int(input("두번째 숫자를 입력하세요"))

print("{} + {} = {:.2f}".format(num1, num2, num1+num2))
print("{} - {} = {:.2f}".format(num1, num2, num1-num2))
print("{} * {} = {:.2f}".format(num1, num2, num1*num2))
print("{} / {} = {:.2f}".format(num1, num2, num1/num2))

#2
kor = int(input("국어 점수를 입력하세요"))
eng = int(input("영어 점수를 입력하세요"))
math = int(input("수학 점수를 입력하세요"))

total = kor+eng+math
avg = (kor+eng+math)/3

print("합계: {}".format(total))
print("합계 : {} + {} + {} = {:.2f}".format(kor, eng, math, kor+eng+math))
print(f"평균 {avg:.2f}")
print(f"평균 : ({kor} + {eng} + {math}) / 3 = {avg:.2f}")