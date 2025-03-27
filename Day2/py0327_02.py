## 달력을 입력하면, 원화 환산해서 출력하시오.
# 1달러 -> 1467원 환산
# $120 -> 120*1467₩

rate = 1467
money = int(input("달러를 입력하세요"))
result =  money * rate

#:.2f == 소수점자리수 출력, 천단위 출력 :,d
print("입력한 달러 {:,d} / 한화: {:,d}원".format(money, result))

# 1759원 - > 동전으로 변경

money =  int(input("동전으로 변경할 금액을 입력하세요"))
ch500 = money//500
ch100 = (money%500)//100
ch50 = ((money%500)%100)//50
ch10 = (((money%500)%100)%50)//10
ch1 = ((((money%500)%100)%50)%10)//1

print("{}원은 500원 {}개, 100원 {}개, 50원 {}개, 10원 {}개, 1원 {}개".format(money, ch500, ch100, ch50, ch10, ch1))

#원의 넓이 3.14 * 반지름 * 반지름
#원의 둘레 2 * 3.14 * 반지름
#반지름을 입력받아, 원의 넓이를 구하는 프로그램을 구현하시오.

radius = int(input("원의 반지름을 입력하세요."))
extent =  3.14 * radius * radius
circumference = 2 * 3.14 * radius
print("원의 넓이는 {:.2f}cm2, 원의 둘레는 {:.2f}cm입니다.".format(extent, circumference))

#직사각형 가로, 세로 길이를 입력받아 넓이와 둘레를 구하시오
g = int(input("직사각형의 가로를 입력하세요"))
s = int(input("직사각형의 세로를 입력하세요"))

square_ex = g*s
square_cir =(g*2) + (s*2)

print("직사각형의 넓이는 {:.2f}cm2, 직사각형의 둘레는 {:.2f}cm입니다.".format(square_ex, square_cir))

#직삼각형 밑변, 높이 길이를 입력받아 넓이를 구하시오
t_w = int(input("직삼각형의 밑변를 입력하세요"))
t_h = int(input("직삼각형의 높이를 입력하세요"))

triangle_ex = (t_w*t_h)/2

print("직삼각형의 넓이는 {:.2f}cm2입니다.".format(triangle_ex))