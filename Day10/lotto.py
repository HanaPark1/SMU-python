#랜덤 1-45번까지 숫자 6개 ran_list 저장
#입력받은 숫자 6개를 my_list 저장을 시키는 프로그램을 구현하시오
#랜덤번호:
#입력 번호:
#당첨 번호:
#당첨 개수:
#중복 불가

import random

lotto = []
my_lotto = []
myWin_lotto = []

while True:
    print('-'*30)
    print('[ 로또 프로그램 ]')
    print('1. 로또 번호 생성')
    print('2. 로또 번호 입력')
    print('3. 로또 당첨 확인')
    print('0. 프로그램 종료')
    choice = int(input("원하는 번호를 입력하세요: "))

    if choice == 1:
        lotto = (random.sample(range(1,45+1),6))
        print(lotto)
        print("로또 번호가 생성되었습니다.\n")
        
    elif choice == 2:
        for i in range(1,7): 
            num = int(input(f"1-45 중 번호를 여섯 개 입력하세요 ({i}번째): "))
            my_lotto.append(num)
            print(f"{num}번을 입력하였습니다.\n")
        print(my_lotto)
        
    elif choice == 3:
        for i in lotto:
            for j in my_lotto:
                if i == j :
                    myWin_lotto.append(j)
        print("로또 번호:", lotto)
        print("입력 번호:", my_lotto)
        print("당첨 번호:", myWin_lotto)
        print(f"당첨 개수: {len(myWin_lotto)}개")
    
    elif choice == 0:
        break