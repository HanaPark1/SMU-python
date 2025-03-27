a = 100
b = 50

print(a,b) # 100, 50

#b = 100, a = 50 값을 서로 교체
# 추가 변수에 값을 보관 후 교체 

c = a

a = b
b = c
print(a,b) # 50, 100

a,b = b,a #파이썬만이 가능한 변수 교체 방법
print(a,b) # 100, 50

#input, print

print(input("숫자를 입력하세여"))

#변수() 있으면 함수 ->  기능 구현의 형태로 가짐 ex) print()

#입력 -  문자열(str) type
# 타입 변경 - 정수 : int(), 실수 : float(), 문자열: str() 중요!
num1 = input("1. 숫자를 입력하세요")
num2 = input ("2. 숫자를 입력하세요")
print(num1, num2)
print(type(num1)) # str - 문자열
print(type(num2))
print(num1 + num2) # 1020

print(int(num1) + int(num2)) #30