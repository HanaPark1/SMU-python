import math

a = 3.141592
b = 3.51582

# 올림
print(math.ceil(a)) # 4

# 반올림
print(round(b,3)) # 3.516
print(round(a,4)) # 3.1416

# 버림
print(math.floor(b)) # 3

# a에서 소수점 3자리에서 올림하여 2자리까지 표시해서 출력하시오
a * 100 / 100
math.ceil(a*100)/100

# b에서 소수점 5자리에서 ceil 올림을 하여 4자리까지 표시해서 출력하시오
math.ceil(b * 10000) / 10000

# math 안에 있는 함수를 출력
dir(math)

import random

print(random.random())

print(random.randint(1,45))

a_list = [1,2,3,4,5]
print(random.choice(a_list))

random.sample(a_list,2)

# 카드 SPADE-4, DIAMOND-3, HEART-2, CLOVER-1
# 번호 1-A,2,3,4,5,6,7,8,9,10,11-J,12-Q,13-K

# 카드 1장 - 카드모양, 번호
# 카드 모양 4개
# 13개
# 카드 총 개수 : 52장 카드가 존재

# 리스트 - 딕셔너리
cList = []
sh = ["CLOVER", "HEART", "DIAMOND", "SPADE"]
no = ['','A','1','2','3','4','5','6','7','8','9','10','J','Q','K']

for i in range(52):
    cList.append({'shape': sh[i//13], 'no': i%13+1})
    
# 카드 랜덤 섞기
import random
random.shuffle(cList)

# myCard, youCard
myCard = []
youCard =[]

# 카드 5장씩 배분
for i in range(5):
    myCard.append(cList[i])
    
for i in range(5,10):
    youCard.append(cList[i])
    
# # 내 카드 출력 -  번호에 해당되는 글자 출력
# for i in myCard:
#     print(i)
    
for i in youCard:
    print(i)        
#     # print(f"[{sh[i['shape']]}, {no[i['no']]}]")
#     print(f"[{sh[i['shape']]}, {no[i['no']]}]")
    
# 내 카드, 상대 카드를 비교해서 - 승리,패배,무승부
# 숫자만 비교해서 숫자가 높은 카드 승리
# 0,0 1,1 2,2 3,3


# score = {"myWin":0, "youWin":0, "draw":0}
# for i in range(5):
#     if myCard[i]['no'] > youCard[i]['no']:
#         score['myWin'] += 1
#     elif myCard[i] < youCard[i]:
#         score['youWin'] += 1
#     else:
#         score['draw'] += 1
        
# print(" [ 카드 확인 ]")
# print(f"내 승리: {score['myWin']}, 상대 승리: {score['youWin']} ")
score = [0]*5
for i in range(5):
    if myCard[i]['no'] > youCard[i]['no']:
        score[i] = 2
    elif myCard[i] < youCard[i]:
        score[i] = 1
    else:
        score[i] = 0
        
print(" [ 카드 확인 ]")
print(f"내 승리: {score.count(2)}, 상대 승리: {score.count(1)} ")

# 승리한 카드 출력
for i,c in enumerate(myCard):
    if score[i] == 2:
        print(f"[{c['shape']}, {c['no']}]", end=", ")
    

# 무승부 카드 출력

# 패배 카드 출력

    
# 전체 카드 출력
for i in cList:
    print(i['shape'], i['no'])