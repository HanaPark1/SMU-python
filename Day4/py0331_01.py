a_list = [1,2,3,4,5]
a = 10
b_list = []

print("a:", a)

a_list[0] = 100
print("a_list:", a_list)

#a변수와 b변수는 다른 변수임
b = a
b = 1000

print("a:", a) # 10
print("b:", b) # 1000

# a_list와 b_list 다른 리스트인가?? => 새롭게 복사 (깊은 복사)
a_list = [1,2,3,4,5]
b_list = [*a_list]
b_list[1] = 200

# a_list와 b_list 다른 리스트인가?? => 주소값 복사 (앝은 복사)
# 주소값이 같은 곳을 바라봄
b_list = a_list
b_list[1] = 200

print(a_list) #[100,2,3,4,5]


# for i in a_list:
#     print(i)
    

# 구구단 (for문 사용)
for i in range(2,10):
    print("{}단".format(i))
    for j in range(1,10):
        print("{} * {} = {}".format(i,j,i*j))
    print()
    
