a = 10

if a>5 and a<9:
    print(a)
    
    
if a>5 or a<9:
    print(a)
    
a_list = [1,2,3,4,5]

print(a_list[1:4])
print(a_list[:3]) 
print(a_list[2:]) #시작위치부터 끝까지 출력
print(a_list[::2])
print(a_list[::3])
print(a_list[::-1]) #역순 출력
print(a_list[:-1])

print(a_list[:7]) #슬라이싱 없는 값 출력시 에러가 나지 않음
print(a_list[7]) #인덱싱 없는 것 출력 시 에러

print(len(a_list)) #리스트 요소 개수 확인
print(a_list[:len(a_list)-1])
print(len(a)) #문자열 길이

#a_list[1:11:2]
for i in range(1,11,2):
    print(i, end=" ") # 줄바꿈 없이 출력
    
sum = 0
for i in range(1,100+1):
    sum = sum+i
    
print("1~100 합계: {}".format(sum))

#합계가 100 넘는 위치의 숫자는 얼마일까요?

sum = 0
num = 0
for i in range(1,100+1):
    sum = sum+i
    if (sum > 100 and num == 0):
        num = i
        
print("합계 100 넘는 위치의 숫자는 {}입니다.".format(num))
print("1~100 합계: {}".format(sum))

#합계가 100 넘는 위치의 숫자는 얼마일까요?

sum = 0
for i in range(1,100+1):
    sum = sum+i
    if (sum >= 100):
        print("합계 100 넘는 위치의 숫자는 {}입니다. 합계: {}".format(i, sum))
        break;
        