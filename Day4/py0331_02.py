a_list = [273, 10, 5, 9, 100, 1000, 50]
for idx, value in enumerate(a_list): #index 번호 부여: enumerate
    print(f"{idx+1} : {value}")
    
# list append
a_list = []
for i in range(1,11):
    a_list.append(i)
    
# 리스트 내포
a_list = []
a_list = [i+1 for i in range(1,11)]
print(a_list)
    
# append, insert, extend
a_list = [1,2,3]
a_list.append(4)
print(a_list) # 가장 뒤에 추가

a_list.insert(1, 100)
print(a_list) # 지정 위치에 추가

a_list.extend([100, 200, 300]) 
print(a_list) # 가장 뒤에 다른 리스트 요소를 추가

#삭제 del, pop, remove, clear
a_list = [1,2,3,4,5] # 특정 위치 삭제
del a_list[2]
print(a_list) # [1,2,4,5]

a_list.pop() #맨뒤 삭제, 특정 위치 삭제 .pop(1)
print(a_list) #[1,2,5]

a_list.remove(1) #데이터값으로 삭제
print(a_list) #[2,5]

a_list.clear # 전체 삭제
print(a_list)