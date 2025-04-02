# 리스트, 딕셔너리 생성
i_list = [1,2,3,4,5]
dic = {'no':1, 'name':'홍길동'}
print(dic)

# 딕셔너리 요소 삭제
del dic['no']
print(dic)

# 딕셔너리 요소 삽입
dic['kor'] = 100

# 리스트 요소 삽입
list.append(100)
print(list)

# 리스트 요소 삭제
del list[0]
print(list)

# 딕셔너리 수정
dic['name'] = '유관순'
print(dic)

# 리스트 수정
list[0] = 100
print(list)

# 딕셔너리 개별 출력
print(dic['no'])
print(dic['kor']) # 키가 없는 것을 출력할 때 에러
print(dic.get('kor')) # get() 함수 사용 시 없는 키는 None 출력

# 리스트 개별 출력
print(list[0])

# 딕셔너리 keys, values
print(dic.keys())
print(dic.values())
print(dic.items())

if 'no' in dic: # 딕셔너리를 비교할 때 key를 가지고 비교하게 됨
    print("있습니당")
    
# 딕셔너리 정렬
import operator
dic_sort = sorted(dic.items(),key=operator.itemgetter(0))
print(dic_sort)

# 리스트 정렬
list.sort
print(list.sort)

#딕셔너리 전체 출력
for k in dic:
    print(dic[k])
    
for k,v in dic.item():
    print(k,v)
    
# 리스트 전체 출력
for i in list:
    print(i)
    
# 리스트 내포
a_list = [i+1 for i in range(10)]
print(a_list)

b_list = [0]*10
print(b_list)

# c_list = [i for i in range(1,51), i%2==1]

txt_list = ['안녕', '반가워', '다음', '내일', '봐', '잘', '지내', '봐요']

#zip
for i,t in zip(i_list, txt_list):
    print(i, t)
    
# zip 사용해서 list 생성
new_list = list(zip(i_list, txt_list))
print(new_list)

# zip 사용해서 dict 생성
new_dic = dict(zip(i_list, txt_list))
print(new_dic)

#-----------
# 얕은 복사, 깊은 복사

new_list = i_list # 얕은 복사
new_list2 = [*i_list] #깊은 복사
