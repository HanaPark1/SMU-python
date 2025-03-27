import random

#0보다 같거나 크고, 1 미만인 랜덤실수 값을 뽑아서 전달해 줌
print(random.random)

# #랜덤 숫자를 맞히는 프로그램
# ran_num = random.randint(1,5)
# in_num = int(input("랜덤 숫자 맞히기!! 1-5까지의 숫자 1개를 입력하세요. >>"))
# if ran_num == in_num :
#     print("정답입니다~ 랜덤 숫자 {}".format(ran_num))
# else:
#     print("오답입니다!!! 랜덤 숫자 : {}, 입력 숫자 : {}".format(ran_num, in_num))
    
# 1-100까지의 숫자 10개를 입력1받음

# 반복문
# for _ in range(10): #0,1,2,3,4,5,6,7,8,9
#     print("하이")
# for n in range(1,10): #1,2,3,4,5,6,7,8,9
#     print(n)

# for n in range(10): #0,1,2,3,4,5,6,7,8,9
#     num[n].append(random.randint(1,100))
    
    
# 1-100까지의 숫자 1개를 생성
num = []
ran_num = random.randint(1,100)

for n in range(1,11):
    in_num = int(input("숫자를 입력하세요"))
    num.append(in_num) #num list타입에 데이터를 추가
    if ran_num == in_num:
        print("정답입니다. 랜덤 숫자: {}".format(ran_num))
        break
    elif ran_num > in_num:
        print("Up! 입력 숫자: {}".format(in_num))
    else:
        print("Down! 입력 숫자: {}".format(in_num))

print("도전 횟수 : {}".format(n))
print("랜덤 숫자 : {}".format(num))
print("랜덤 숫자 : {}".format(ran_num))
