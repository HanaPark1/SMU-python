# # 로또 프로그램
# # 랜덤 숫자 6개 생성
# import random
# lotto = random.sample(range(1,45+1),6)

# # 6개 입력한 번호 생성
# input_lotto = []
# for i in range(6):
#     num = int(input("로또 번호를 입력하세요"))
#     input_lotto.append(num)
    
# # 당첨 번호 확인
# win_lotto = []
# for i in lotto:
#     for j in input_lotto:
#         if i == j :
#             win_lotto.append(j)

# # 출력
# print(f"로또 번호: {lotto}")
# print(f"입력 번호: {input_lotto}")
# print(f"당첨 번호: {win_lotto}")
# print(f"당첨 개수: {len(win_lotto)}")

import random
lotto = random.sample(range(1,45+1),6)
print_sample_lotto = [i + 1 for i in range(45)]
input_lotto = []

def print_sample():
    global print_sample_lotto
    for i in range(45):
        if i == 0:
            pass
        elif 1 % 7 == 0:
            print()
        print(print_sample_lotto[i], end="\t")
    
while True:
    print("[ 로또 프로그램 ]")
    print("1. 로또 번호 입력")
    print("2. 입력 번호 확인")
    print("3. 로또 당첨 확인")
    print("0. 프로그램 종료")
    choice = int(input("원하는 번호를 입력해 주세요"))
    
    if choice == 1:
        print("[ 로또 번호 입력 ]")
        count = 0
        while True:
            if count < 6:
                print_sample()
                num = int(input("원하는 로또 번호를 입력하세요: "))
                if 0 > num or num > 45:
                    print(f"{num}은 로또 번호가 아닙니다. 다시 입력하세요")
                    continue
                if i not in print_sample_lotto:
                    print("이미 등록된 번호입니다. 다시 입력하세요.")
                    continue
                input_lotto.append(num)
                print_sample_lotto[num-1] = "X"
                count += 1
            else: 
                break
        print()
        
    elif choice == 2:
        print(input_lotto)
        
    elif choice == 3:
        # 당첨 번호 확인
        win_lotto = []
        for i in lotto:
            for j in input_lotto:
                if i == j :
                    win_lotto.append(j)
    
        print(f"로또 번호: {lotto}")
        print(f"입력 번호: {input_lotto}")
        print(f"당첨 번호: {win_lotto}")
        print(f"당첨 개수: {len(win_lotto)}")
        