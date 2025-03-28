# input_list = [1,5,10,9,8,20]

# a = 5
# if a in input_list:
#     print("{}가 존재합니다".format(a))
# else: 
#     print("{}가 존재하지 않습니다".format(a))

# i = 0
# while i<10:
#     print(i)
#     i += 1
    
# print("-"*50)
# for j in range(10):
#     print(j)
    
num_list = []

# for i in range(10):
#     num = int(input("숫자를 입력하세요"))
#     if num in num_list:
#         print("이미 존재합니다")
#         continue
#     else:
#         num_list.append(num)
#         print("{} 삽입 성공".format(num))
        
# for i in range(10):
#     num = int(input("숫자를 입력하세요"))
#     if num not in num_list:
#         num_list.append(num)
        
# print(num_list)

i = 0
while i<10:
    num = int(input("{}번째 숫자를 입력하세요: ".format(i+1)))
    if num not in num_list:
        num_list.append(num)
        i += 1