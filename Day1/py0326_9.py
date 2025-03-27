#이름, 국어, 영어, 수학 입력받아 합계 평균을 출력하시오
#이름: 홍길동
# 합계: 300
# 평균: 100.0 소수점은 1자리까지 출력하시오.

name = input("이름을 입력하시오: ")
l = int(input("국어 성적을 입력하시오"))
e = int(input("영어 성적을 입력하시오"))
m = int(input("수학 성적을 입력하시오"))

print("이름: ", name)
print("합계: ", l+e+m)
print("평균: %.1f" % ((l+e+m)/3))

#\n 엔터, \t 탭
print("안녕하세요.\n반갑습니다.\t저는 홍길동이라고 합니다.")

#format() 문자형태 지정
a = 10
b = 5
print("%d + %d = %d" %(a,b,a+b))

str_print = ("{} + {} = {:.2f}".format(a,b,a+b))
print(str_print)

#f함수 == format()
str_print2 = f"{a} / {b} = {(a/b):.2f}"
print(str_print2)