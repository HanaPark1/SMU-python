# 5*5 2차원 리스트 -> 랜덤으로 1-25까지 숫자를 넣기
# 1차원 리스트 생성
# 1차원 리스트 랜덤으로 섞기
# 2차원 리스트 생성
# 2차원 리스트에 1차원 랜덤 번호를 넣기

import random

# 1차원 리스트 생성
first_list = [i+1 for i in range(25)]

# 1차원 리스트 랜덤으로 섞기
random.shuffle(first_list)

# 2차원 리스트 생성
a_list = [[0]*5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        # 2차원 리스트에 1차원 랜덤 번호를 넣기
        a_list[i][j] = first_list[5*i+j]
        
print(a_list)

# 2차원 형태로 출력
while True:
    
    print("\t[좌표 맞추기 프로그램]")
    print()
    print("* |",end="\t")
    for i in range(5):
        print(i,end="\t")
    print()
    print("-"*45)
    for i in range(5):
        print(f"{i} |",end="\t")
        for j in range(5):
            print(a_list[i][j], end="\t")
        print()

    # 입력 부분
    print("-" * 45)
    
    num1 = int(input("X 좌표: "))
    num2 = int(input("Y 좌표: "))
    
    if num1 < 5 and num2 < 5:
        # 좌표에 값 넣기
        a_list[num2][num1] = "X"
    else:
        print("좌표를 잘못 입력하였습니다. 다시 입력하세요.")



