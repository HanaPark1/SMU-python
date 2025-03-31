# 좌표 맞추기 프로그램
import random 

# 1차원 배열 생성 후 랜덤으로 섞기
random_list = [i+1 for i in range(25)]
random.shuffle(random_list)

# 2차원 배열 생성
a_list = [[0]*5 for i in range(5)]

# 2차원 배열에 1차원 랜덤 번호 삽입
for i in range(5):
    for j in range(5):
        a_list[i][j] = random_list[5*i+j]
        

while True:
    print("[좌표 맞추기 프로그램] \n")

# X축 인덱스 번호 기입
    print("* |\t", end="")
    for i in range(5):
        print(f"{i}", end="\t")

    print()
    print("-"*60)

    for i in range(5):
# Y축 인덱스 번호 기입
        print(f"{i} |",end='\t')
        for j in range(5):
            print(a_list[i][j],end='\t')
        print()
    print()   
# input 받기
    num = int(input("숫자를 입력하세요"))

# 받은 input과 일치할 시 X로 수정
    for i in range(5):
        for j in range(5):
            if a_list[i][j] == num:
                a_list[i][j] = "X"