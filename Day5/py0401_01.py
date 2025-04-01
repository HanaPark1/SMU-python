# 1차원 리스트
import random
# s_list = [range(1,26)]
s_list = [i for i in range(1,26)]
random.shuffle(s_list) 
#random.random() random.randint(), random.sample(), random.shuffle()
print(s_list)

# 2차원 리스트
my_list = [[0]*5 for _ in range(5)]
# a_list = list() #리스트 초기화 

# 1차원 리스트 값 -> 2차원 리스트 입력
for i in range(5):
    for j in range(5):
        my_list[i][j] = s_list[5*i+j]
        
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
            print(my_list[i][j],end='\t')
        print()
    print()   
# input 받기
    num = int(input("숫자를 입력하세요"))
# 25개 모두 비교
# 받은 input과 일치할 시 X로 수정
    stop = 0
    for i in range(5):
        for j in range(5):
            if my_list[i][j] == num:
                my_list[i][j] = "X"
                stop = 1
                break
        if stop == 1: break
                
                
