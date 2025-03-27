#1. 두 숫자를 입력받아 합과 곱을 출력하시오

a = input("첫번째 숫자 입력")
b = input ("두번째 숫자 입력")

a = int(a)
b = int(b)

print("a+b = ",a+b)
print("a*b = ",a*b)

c = a
a = b
b = c
print(a,b)

a,b = b,a
print(a,b)

st="안녕"
print("변수값: ", a)
print("변수값: "+a) # error! str와 int이므로 서로 다른 타입은 사용 불가능
print("변수값:",st)
print("변수값:" +st)

print(a,"+",b,"=", a+b)

print(c,"*",a,"=", c*a)
print("%d * %d = %d" %(c,a, c*a))

print(c,"/",a,"=",c/a)
print("%d / %d = %.1f" %(c,a,c/a))