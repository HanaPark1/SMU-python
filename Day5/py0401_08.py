list = [1,2,3,1,2,3,4,5,8,9,10,1,2]
dic = {}

for i in list:
    # dic에 추가, dic 키가 존재하는지 확인
    if i not in dic:
        dic[i] = 0
    dic[i] = dic[i] + 1
    
for i,d in enumerate(dic):
    print(f"{i} : {dic[d]}")
    
list = ['남성모', '하유준', '박성호', '이주연','남성모','남성모',
        '남성모','남성모','남성모','남성모','남성모','남성모','남성모', 
        '하유준', '하유준', '하유준', '박성호', '박성호', '박성호',
        '이주연', '이주연', '이주연']

singer = {}

# 각각의 가수가 몇 번 존재하는지 출력하시오.

count = 0
for i in list:
    if i not in singer:
        singer[i] = 1
    else:
        singer[i] += 1

for k,v in singer.items() :
    print(f"{k} : {v}")