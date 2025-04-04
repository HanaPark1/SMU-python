# 람다식과 정렬 정리
# 람다식 lambda -> 함수 축약형
# def 함수명(매개변수) : return 값

def func2(a,b):
    return a+b

lambda a:a*20

a_list = [1,2,3,4,5] # list 모든 값에 제곱을 해서 리스트를 생성
aa_list = []
def func1(x):
    return x**2
print(list(map(func1,a_list)))


for i in a_list:
    aa_list.append(i**2)

# map(함수, 리스트)
map(func1,a_list)

# 람다식 - map() 함수를 lambda로 사용하면 코드를 줄일 수 있음
print(list(map(lambda x:x**2,a_list)))

#map() - 리스트에 함수를 적용해서 다시 리스트로 반환
#filter() 함수 - 리스트에 함수를 적용해서 조건에 맞는 것만 다시 리스트로 반환

def func3():
    if i%2==0:
        return x
    
b_list = list(filter(func3(),a_list))
print(b_list)

c_list = list(filter(lambda x:x%2==0,a_list))
print(c_list)
        
students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
]

# 리스트 sort 정렬됨
a_list = [20,50,10,40,90]
a_list.sort()
a_list.sort(reverse=True)

# student.sort() 에러 , 딕셔너리라서 대소비교 불가능
students.sort(key=lambda x:x['name']) # 이름으로 순차정렬
students.sort(key=lambda x:x['name'],reverse=True) # 이름으로 역순정렬
students.sort(key=lambda x:x['total']) # 합계로 순차정렬

# sort() 기존의 리스트의 값을 변경시킴
# sorted() 기존의 리스트 유지, 새로운 리스트 생성
s_list = sorted(students, key=lambda x:x['name'])
print(s_list)
print(students)
