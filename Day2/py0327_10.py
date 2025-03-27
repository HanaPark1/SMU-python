# 1-100 랜덤 숫자를 생성해서 정답을 맞히는 프로그램을 구현하시오
#-------------------
# 도전 횟수 : 5
# 도전 번호: [1,2,3,4,5]
# 랜덤 번호 : 5

import random

ran_num = random.randint(1,100)
ran_list = []
n = 0

for i in range(1,11):
    in_num = int(input("숫자를 입력하세요: "))
    ran_list.append(in_num)
    if ran_num == in_num:
        print("도전 횟수:",i)
        print("도전 번호:",ran_list)
        print("랜덤 번호: ", ran_num)
        break
    elif ran_num > in_num:
        print("Up! 입력 번호: {}".format(in_num))
    else:
        print("Down! 입력 번호: {}".format(in_num))