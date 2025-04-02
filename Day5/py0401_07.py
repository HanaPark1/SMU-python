number = [273, 103, 5, 32, 65, 9, 72, 800, 99]

# 100 이상의 숫자만 출력, 그리고 그 합계

sum = 0
for i in range(len(number)):
    if number[i] >= 100:
        print(f"자리수: {i},  값: {number[i]}", end=" ")
        sum += i

print()       
print(f"합계 :{sum}")

#딕셔너리 생성
dic1 = {1:"a", 2:"b", 3:"c"}
print(dic1)

students_list = [1,"홍길동",100]
students = {"no":1, "name":"홍길동", "kor":100}
print(students)

stu = {'학번': 1000, '이름' : '홍길동', '학과' : '컴퓨터공학'}

# 딕셔너리 추가
dic = {}
dic['no'] = 1
dic['name'] = '홍길동'
dic['kor'] = 100

# 딕셔너리 삭제
del dic['no']
print(dic)

# 딕셔너리 수정
dic['name'] = '이순신'

# 딕셔너리 출력
print(dic)
# print(dic['total']) # 없는 값 출력시 에러
print(dic.get('total')) # 없으면 None

print(dic.keys())
print(dic.values())
print(dic.items())

# 전체 출력 - 키, 값 모두 출력
for i, value in enumerate(dic):
    print(f"{i} : {value}")
    
# 키를 돌려줌
for key in dic:
    print(key)
    
if 'name' in dic:
    print("키 값이 존재합니다. ")
    
if 'no' in dic:
    print(f"no: {dic['no']}")
else:
    print("no 키는 존재하지 않습니다")