# 두 수를 입력받아 두 수 사이의 합계를 구하시오.
# ex) 1,7 -> 1,2,3,4,5,6,7 

num1 = int(input("첫번째 숫자를 입력하세요"))
num2 = int(input("두번째 숫자를 입력하세요"))
print(num1, num2)
t = 0
sum = 0

if (num1 > num2):
    t = num1
    num1 = num2
    num2 = t
print(num1, num2)

    
for i in range(num1, num2+1):
    sum += i
    
print("합계 : {}".format(sum))

#구구단 출력
for i in range(1,10):
    print("{}단".format(i))
    for j in range(1,10):
        print("{} * {} = {}".format(i,j,i*j))
        
# 시작단과 끝나는 단을 입력받아 출력하시오

num1 = int(input("첫번째 숫자를 입력하세요"))
num2 = int(input("두번째 숫자를 입력하세요"))

if num1 > num2:
    num1, num2 = num2, num1
    
#구구단 출력
for i in range(num1,num2+1):
    print("{}단".format(i))
    for j in range(1,10):
        print("{} * {} = {}".format(i,j,i*j))
    print()
        