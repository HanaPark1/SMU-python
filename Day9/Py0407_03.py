a_list = ["52", "273", "32", "파이썬", "103"]

list_number = []
# 숫자로 변환되는 것만 list_number 저장하시오

# if
for i in a_list:
    if i.isdigit():
        list_number.append(int(i))
    else :
        print("숫자가 아님:", i)

# except
for i in a_list:
    try:
        num = int(i)
        list_number.append(num)
    except Exception as e:
        print(e)
        
print(list_number)

try: 
    num = int(input("원의 반지름을 입력하세요: "))
    print("원의 넓이 : ",3.14 * num**2)
except Exception as e:
    print(e)
else: # try 구문에 에러가 없을 시 실행
    pass

#finally: # 에러가 나지 않았을 때 모두 실행
# raise NotImplementedError # 예외를 강제로 발생시킴
# raise ZeroDivisionError