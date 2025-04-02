print() # 변수 뒤에 () 있으면 함수
def cal(x,y):
    result1 = x + y
    print(result1)
    result2 = x - y
    print(result2)
    result3 = x * y
    print(result3)
    result4 = x / y
    print(result4)
    
print("누군가 오고 있어요")
print("인사")
# add()

a,b = 10,20
result1 = a+b
result2 = a-b
result3 = a*b
result4 = a/b

c,d = 100,200
r1 = c+d
r2 = c-d
r3 = c*d
r4 = c/d

e,f = 50,100
k1 = e+f
k2 = e-f
k3 = e*f
k4 = e/f


def add(x,y) :
    print("x:", x)
    print("y:", y)
    result1 = x + y
    print("x+y:", result1)
    
a=10
b=20
c=30
d=40

add(a,b)

# 두 수를 입력받아 사칙연산 (+,-,*,/) 를 출력하시오
def cal(x,y):
    print("더하기: ", x+y)
    print("빼기: ", x-y)
    print("곱하기: ", x*y)
    print("나누기: ", (x/y))
    
num1 = int(input("첫번째 숫자를 입력하세요"))
num2 = int(input("두번째 숫자를 입력하세요"))

cal(num1,num2)

