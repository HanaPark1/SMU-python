fruits = ['사과', '배', '딸기', '바나나', '멜론']
# 1. 사과
# 2. 배
# 3. 딸기...

# enumerate index 번호를 받을 수 있음
for i, fruit in enumerate(fruits):
    if (i+1) != len(fruits):
        print("{}.{}".format(i+1, fruit), end=", ")
    else:
        print("{}.{}".format(i+1, fruit), end="")
    
scores = [65, 90, 100, 100, 50]

for score in scores:
    print(score, end=" ")