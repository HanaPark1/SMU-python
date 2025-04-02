a_list = [1,2,3,4,5]

# 리스트 삭제
del a_list[0] # index 번호를 가지고 삭제
a_list.pop() # 마지막 데이터 삭제
a_list.pop(1) #1번 위치 데이터 삭제
a_list.remove(2) #2라는 값 삭제
a_list.clear() # 전체 삭제

# 리스트 삽입
a_list.append(1)
a_list.append(2)
a_list.insert(1,2)
a_list.extend([1,2,3])

# 리스트 출력
for i in a_list:
    print(i)

# 리스트에 여러 데이터 묶음도 추가 가능 - 리스트 안에 리스트 추가 가능
a_list.append(['컴공', '소공'])

# 리스트 길이
print(len(a_list))

s_list = [1,2,3,1,2,2,2,1,3,4,5,7,7,7]
print("{} : {}".format(1, s_list.count(1)))

num = 0
for s in s_list:
    if s == 1:
        num += 1
print("{} : {} ".format(1, num))

s_list.sort()

s_list.sort(reverse=True) # 역순 정렬
s_list.reverse()