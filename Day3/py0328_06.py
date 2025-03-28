# 숫자 맞히기
import random

#randint(1,45) 1~45번 사이의 숫자 1개를 가져옴
lotto = random.randint(1,45)

#--------------
for i in range(1,11):
    
    inp = int(input("{}번째 도전. 1~45번 사이의 숫자를 입력하세요.>> ".format(i)))

    if lotto == inp:
        print("당첨")
        break
    elif lotto > inp:
        print("틀렸습니다 {}보다 더 큰수를 입력하세요".format(inp))
    else:
        print("틀렸습니다 {}보다 더 작은 수를 입력하세요".format(inp))
#--------------
    
print("랜덤번호: {}".format(lotto))
print("입력번호: {}".format(inp))
