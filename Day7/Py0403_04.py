# 로또 프로그램
import random

# 랜덤 숫자 6개 생성
# 6개 입력한 번호 생성
# 당첨 번호 확인
# 출력


lotto = [i+1 for i in range(45)]
lotto2 = [i+1 for i in range(45)]
my_lotto = []
win_lotto = []
def lotto_mix():
    global lotto, lotto2
    random.shuffle(lotto)

lotto_mix()
while True:
    print("[ 로또 프로그램 ]")
    print("-"*30)
    print("1. 로또 프로그램 재실행")
    print("2. 로또 번호 입력 ")
    print("3. 로또 번호 당첨 확인")
    print("4. 전체 로또 번호 출력")
    print("5. 입력 로또번호 확인")
    print("0. 프로그램 종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요. "))

    if choice == 1:
        lotto_mix()
    elif choice == 2:
        count = 0
        while True:
            temp = 0
            print("[ 로또 번호 입력 ]")
            print("-"*45)
            for i in range(45) :
                if i%7 != 0:
                    print(lotto2[i], end="\t")
                else:
                    print()
                    print(lotto2[i], end="\t")
            print()
            choice = int(input("로또 번호를 입력하세요: "))
            print()
            # ----------------------
            if choice < 0 or choice > 45:
                print(f"{choice}번 번호는 없는 번호입니다. 다시 실행하세요.")
                continue
            for i in lotto2:
                if i == choice :
                    lotto2[i-1] = "X"
                    my_lotto.append(choice)
                    # my_lotto[count] = choice
                    count += 1
                    temp = 1
            if temp == 0 :
                print(f"{choice}번 번호를 입력하신 번호입니다. 다시 입력하세요.")
            if count >= 6:
                print("로또 번호 6개를 모두 입력하셨습니다.")
                break      
    elif choice == 3:
        print("[ 로또 당첨 번호 확인 ]")
        print("-"*30)
        for i in lotto[:6]:
            for j in my_lotto:
                if i == j:
                    win_lotto.append(j)
        print("[ 로또 당첨 번호 확인 ]")
        print("-"*30)
        print("로또 당첨 번호: ",lotto[:6])
        print("입력 로또 번호: ",my_lotto)
        print("당첨된 로또 번호: ", win_lotto)
        print("당첨 개수: ",len(win_lotto))
        print("-"*30)
    elif choice == 4:
        print(lotto)
    elif choice == 5:
        print(my_lotto)
    elif choice == 0:
        print("[ 로또 프로그램 종료 ]")
        break