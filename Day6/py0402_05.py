
def add(x,y,z):
    return (x+y+z)

kor = int(input("국어 점수를 입력하세요: "))
eng = int(input("영어 점수를 입력하세요: "))
math = int(input("수학 점수를 입력하세요: "))
total = add(kor,eng,math)
avg = total / 3

print(f"{kor}\t{eng}\t{math}\t{total}\t{avg}\t")

# 함수 사용
# 1. 중복 코드가 있을 때
# 2. 소스카 너무 복잡할 때
# 먼저 프로그램 모두 구현한 뒤 중복되고 있는지 확인 후 함수를 사용

## 함수를 사용해서 두 수를 입력받아
# 10~20 입력받으면 10+11+12+13+14+....+20
def add(n1, n2):
    if n1 > n2:
        n1, n2 = n2, n1
    sum = 0
    for i in range(n1, n2+1):
        sum += i
    print("합계:", sum)
        
n1 = int(input("1. 숫자를 입력하세요: "))
n2 = int(input("2. 숫자를 입력하세요: "))

add(n1,n2)

def cal(n_list):
    sum = 0
    for i in n_list:
        if i % 2 == 0 :
            sum += i
    return sum

# def even(n):
#     if n % 2 == 0:
#         return n
#     else:
#         return 0

# 입력을 5개 받아 짝수만 모두 더한 값을 출력하시오
n_list = [0]*5
for i in range(len(n_list)):
    n_list[i] = int(input(f"{i+1}번째 숫자 입력: "))
result = cal(n_list)
print("짝수의 합: ", result)

# 직사각형 넓이와 둘레를 구하는 프로그램을 구현하시오
# 가로 * 세로, 가로길이*2 + 세로길이*2

# 가로, 세로길이를 입력받아 넓이와 둘레를 구하시오
# 함수를 사용할 것


def rectangle(x,y):
    area = x * y
    circumference = (x*2) + (y*2)
    return area,circumference

x = int(input("가로 길이를 입력하세요: "))
y = int(input("세로 길이를 입력하세요: "))

area, circumference = rectangle(x,y)

print(f"넓이: {area}, 둘레: {circumference}")

# 이름, 국어, 영어, 수학, 점수를 입력받아 합계, 평균을 출력하시오

def cal(kor, eng, math):
    total = kor + eng + math
    avg = total / 3
    
    return total, avg

no = 1
name = input("이름을 입력하세요: ")
kor = int(input("국어 점수를 입력하세요: "))
eng = int(input("영어 점수를 입력하세요: "))
math = int(input("수학 점수를 입력하세요: "))
total, avg = cal(kor,eng,math)

print(f"{no}\t{name}\t{kor}\t{eng}\t{math}\t{total}\t{avg:.2f}\t")

def cal():
    pass
def stu_print():
    for s in students:
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t")
        
students = [
    {'no':1, 'name':'홍길동','kor':100,'eng':100,'math':100,'total':300,'avg':100,'rank':1},
    {'no':2, 'name':'유관순','kor':100,'eng':100,'math':99,'total':299,'avg':99, 'rank':2},
    {'no':3, 'name':'이순신','kor':100,'eng':100,'math':99,'total':299,'avg':99, 'rank':3},
]
        
print("1. 학생 성적 입력")
print("2. 학생 성적 출력")
print("3. 학생 성적 입력")
choice = int(input("선택하세요: "))
if choice == 2:
    stu_print(students)

def cal(a_list):
    a_list[0] = 100
    a_list[1] = 200 
a_list = [0,0] # 리스트 타입 변수: 주소값
a_list[0] = 10
a_list[1] = 10
print("함수 호출 전 a_list : ",a_list[0],a_list[1])

cal(a_list)
print("함수 호출 후 a_list : ",a_list[0],a_list[1])

s = {'no':1, 'name':'홍길동','kor':100,'eng':100,'math':100,'total':300,'avg':100,'rank':1}

# 매개변수로 일반 변수 전달 형태 - 리턴으로 값을 돌려서 입력해야 함

# 국어 점수 변경 함수 선언
def cal(kor):
    kor = int(input("수정할 국어 점수를 입력하세요: "))
    return kor    


kor = 100
eng = 100
math = 100

# 국어 점수 변경 함수 호출
kor = cal(kor)
print("수정된 국어 점수:", kor)

def cal(ss):
    ss['kor'] = int(input("수정할 국어 점수를 입력하세요: "))
    ss['total'] = ss['kor'] + ss['eng'] + ss['math']
    ss['avg'] == ss['total'] / 3
    
cal(s)
print("수정된 국어 점수: ", s['kor'])

# global 변수 : 전역변수
def func1():
    global a #전역변수 호출
    a = 20
    
a = 10
print(a) #10
func1()
print(a) #20

def cal(n1,n2):
    return n1+n2

def cal(n1,n2,n3):
    return n1+n2+n3

n1 = 10
n2 = 20
n3 = 30

result = cal(n1, n2)
print(result)

result2 = cal(n1,n2,n3)
print(result2)

# 가변매개변수 사용
def cal(*num):
    result = 0
    for n in num:
        result += n 
    return result

print("2개 합계:", cal(1,2))
print("3개 합계:", cal(10,20,30))
print("4개 합계:", cal(1,2,5,10))

# print() -> 매개변수가 가변매개변수
print(1,2,3,4,5)

# 키워드 매개변수
# 키워드 변수는 무조건 뒷쪽에 있어야 함
def cal(b, a=10):
    return a,b

print(cal(1))


def cal(b=10, *a):
    result = b
    for i in a:
        result += i
    return result

print(cal(1,2,3,4,5)) #15


def cal(*a, b=10): #가변 매개변수, 키워드 매개변수 함께 가용
    result = b
    for i in a:
        result += i
    return result

print(cal(1,2,b=100)) #15