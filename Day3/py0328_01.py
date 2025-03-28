# 파이썬 타입
# bool, int, float, str

# bool - True, False
# int - 정수
# float - 실수
# str - 문자열

# print("안녕" + 1) 타입이 다른 경우 error

print("숫자: {}".format(10/3))

if 10>3: #True
    print("정상")
    
print("1") # str

# 타입 변경 문자열이 숫자 형태일 경우 -> int("1")
print(int("1")+1)

#숫자를 타입 변경 - int 타입, float 타입으로 변경 가능
print(int(1.5)) # 1

#문자열 float 타입은 int로 변경 안 됨
#print(int("1.5")) #error
print(float("1.5")) #가능

print(str(1.5))

#----------------------------------

#변수
a = 10 # 할당의 의미 =
b = 1.5
c = "안녕"

print(c+a) #error

#list 타입
list_a = [1,2,3,4]
print(list_a)

print(list_a[0],list_a[1],list_a[2],list_a[3])

# input() : 데이터를 입력받는 명령어(함수) - str 타입 1개
score = input("데이터를 입력하세요")
print("입력 데이터: ", score)

#두 수를 입력받아 합계 평균을 출력

num1 = int(input("숫자를 입력하세요"))
num2 = int(input("숫자를 입력하세요"))

total = num1 + num2

print("합계: {}, 평균: {:.2f}".format(total, total/2))

score = int(input("점수를 입력하세요: "))
if score>=70:
    print("합격")
elif score>=60:
    print("재시험")
else:
    print("불합격")
    
score = int(input("점수를 입력하세요: "))
    
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")   
else:
    print("F")