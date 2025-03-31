# while문
i = 0
while i<10:
    print(i)
    i += 1
    
# for문
for i in range(10):
    print(i)
    
# 10번의 숫자를 입력받아 합계를 구하시오
# while
sum = 0
count = 1
while count<11:
    num = int(input("10번 중 {}번째, 숫자를 입력하세요: ".format(count)))
    sum += num
    count += 1
    print("입력 숫자: {}, 합계: {}".format(num, sum))

# for
sum = 0
for i in range(10):
    num = int(input("10번 중 {}번째, 숫자를 입력하세요: ".format(i+1)))
    sum += num
    print("입력 숫자: {}, 합계: {}".format(num, sum))
    
# 로또 프로그램
# 6개 랜덤 숫자와 입력 숫자 6개를 출력하시오:

import random

#random.sample(range(1,45+1), 6)
lotto =  random.sample(range(1,45+1),6)
#lotto = [i+1 for i in range(45)]
my_input = []

for i in range(6):
    num = int(input("숫자를 입력하세요."))
    my_input.append(num)

print("랜덤 숫자: {}\n입력 숫자: {}".format(lotto, my_input))

# a_list = [i+1 for i in range(45)]
# print(a_list)

#random class
print(random.random) 
print(int(random.random()*10)+1)
print(int(random.random()*10)+0)
print(random.randint(1,10))

#반복문 - for, while

a_list = [i+1 for i in range(10)]
print(a_list)

# a_list 홀수의 합계를 구하시오
sum = 0
for i in a_list:
    if i % 2 == 1:
        sum += i
print(sum)

# 1-100까지의 숫자의 합을 구할 떄 합계가 200을 넘을 때 위치값을 출력하시오

sum = 0
for i in range(1,101):
    sum += i
    if sum >= 200:
        print("합계 200이 넘을 때\n위치: {}\n합계: {}".format(i, sum))
        print()
        print("합계 200이 넘기 전의 값\n위치: {}\n합계: {}".format(i-1, sum-i))
        break
    
# 입력한 숫자가 50을 넘으면 프로그램을 종료하고
# 총합을 구하시오
# 입력한 숫자 중 5의 배수는 제외
# continue, pass, break

sum = 0

while sum < 50:
    num = int(input("숫자를 입력하세요 (5의 배수는 합계 제외): "))
    if num % 5 == 0:
        print("숫자: {}, 합계: {}".format(num, sum))
        continue #실행 1번 중지
    else: 
        sum += num
        print("숫자: {}, 합계: {}".format(num, sum))
        
while True:
    if sum<50:
        num = int(input("숫자를 입력하세요"))
        if num % 5 == 0:
            print("입력한 숫자 :{}, 5의 배수 제외".format(num))
            continue
        sum += num
    else:
        break        
    
    
# 모양 출력
for i in range(10) :
    for j in range(i):
        print("*", end="")
    print()
    
for i in range(10):
    if i%2 == 1: continue
    print(i)
    
# 배열 역순 출력
a_list = [1,2,3,4,5,6,7,8,9]
print(a_list[::-1])

# 값을 변경할 때 1:2, 2의 위치값이 포함
a_list[1:2] = [100,200]
print(a_list)

# 2차원 리스트
aa = [
    [1,2,3,4], #[0][0], [0][1], [0][2]...
    [5,6,7,8],
    [9,10,11,12]
]


for i in range(3):
    for j in range(4):
        print(aa[i][j],end=" ")
        


# 1 2 3 4 5
# 6 7 8 9 10 ... 출력

# a = [i+1 for i in range(25)]
# [1,2,3,4,...,23,24,25]


# a = [[0]*5]*5 # 얕은 복사
a = [[0]*5 for i in range(5)] # 깊은 복사


for i in range(5):
    for j in range(5):
        a[i][j] = 5*i+(j+1)
        
print(a)

sample_list = [i+1 for i in range(25)]
random.shuffle(sample_list)

a = [[0]*5 for i in range(5)] # 깊은 복사


for i in range(5):
    for j in range(5):
        a[i][j] = sample_list[5*i+j] # 0,1,2,3,4,5,...,23,24
        
print(a)

sample_list = list()
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(0)
    sample_list.append(temp)
    
# 5 * 5 리스트 0으로 초기화
sample_list = [[0]*5 for i in range(5)]
