#변수 할당 방법

a,b = 100, 200
c = 300; d = 400
e = 500
f = 600

#관계 연산자
print(a==b)
print(a!=b)
print(a>b,a<b,a>=b,a<=b)

#조건식
a = int(input("숫자를 입력하세요: "))
if a<100:
    print("입력한 값은 100보다 작은 수입니다.")
else: 
    print("압력한 값은 100보다 큰 수입니다.")

# 양수, 음수인지 확인 - 0은 양수로
input_num = int(input("숫자를 입력하세요: "))

if input_num >= 0:
    print("양수입니다")
else:
    print("음수입니다")
    
# num ->짝수인지, 홀수인지 확인
if input_num % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")
    
# 3의 배수인지 아닌지 확인
if input_num % 3 == 0:
    print("3의 배수입니다")
else:
    print("3의 배수가 아닙니다.")
    
#if와 for 속도 차이 있음