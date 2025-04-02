# set 중복을 제거해서 키를 확인
myset1 = {1,2,2,3,3,3,5,5,7}
print(myset1)

menu_list = ['삼각김밥', '바나나', '삼각김밥', '사과', '삼각김밥', '도시락']
print(set(menu_list)) #list -> set 타입 변경 후 확인

list = [1,2,3,4,5]
# list +100*100
#list = ['10,100','10,102']

list2 = [(i+100)*100 for i in list]

#format 함수 천단위 표시
list2 = ["{:,d}".format((i+100)*100) for i in list]

print(list2)

# list2 = [i+100 for i in list]
# print(list2)

# 리스트 내포 :  if 조건절 추가 가능
n_list = [i for i in range(1,51) if i%3 == 0]
print(n_list)

# 2개의 리스트를 출력할 수 있음
n_list = ['홍길동', '유관순', '이순신', '강감찬', '김구']
t_list = [100, 99, 89, 79, 100]
for n,t in zip(n_list, t_list):
    print(f"{n} :{t}")

students = {"no":1, "name":"홍길동", "kor":100}
for k,v in students.items(): 
    print(f"{k} : {v}") # key and value
    
for k,v in enumerate(students): 
    print(f"{k} : {v}")  #index and key
    
tuple_list = list(zip(n_list, t_list))

#zip() ->  2개 리스트를 합치는 것 -> list & dict 타입 변경
print(list(zip(n_list,t_list)))
print(dict(zip(n_list,t_list)))
