import random

# #반복을 해서 , ran_list 10개를 입력시키는 프로그램을 구현하시오.
# #단, 같은 숫자가 들어가지 않도록 하시오


# ran_list = []

# i = 0
# while i < 10:
#     ran_input = random.randint(1,45)
#     if ran_input not in ran_list:
#         ran_list.append(ran_input)
#         i += 1
#         print("삽입 완료", ran_list)

#랜덤 1-45번까지 숫자 6개 ran_list 저장
#입력받은 숫자 6개를 my_list 저장을 시키는 프로그램을 구현하시오
#랜덤번호:
#입력 번호:
#당첨 번호:
#당첨 개수:
#중복 불가

my_list = [] #입력 번호 저장 리스트
lotto_count = 0 #당첨 개수
lotto_list = [] #당첨 번호

ran_list = random.sample(range(1,45+1),6)
input_count = 0

print("랜덤 번호",ran_list)

while input_count < 6:
    my_input = int(input("{}번째 입력. 1-45 중 숫자 하나를 입력하세요. ".format(input_count+1)))
    if my_input not in my_list:
        my_list.append(my_input) #입력번호 추가
        input_count += 1
        
for i in range(len(my_list)):
    if my_list[i] in ran_list:
        lotto_count += 1
        lotto_list.append(my_list[i])
        
for j in range(6):
    for k in range(6):
        if ran_list[j] == my_list[k]:
            lotto_count += 1
            lotto_list.append(my_input[k])
    
        
print("입력 번호",my_list)
print("랜덤 번호",ran_list)
print("당첨 개수",lotto_count)
print("당첨 번호",lotto_list)