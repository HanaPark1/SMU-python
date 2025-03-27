#
num = 7
if 10 >= num >=0:
    print("10에 해당되는 숫자입니다. ")
    
if 10 >= num and num >= 0:
    print("10에 해당되는 숫자입니다. ")
    
# 3,4,5 봄
# 6,7,8 여름
# 9,10,11 가을
# 12,1,2 겨울

month = int(input("숫자를 입력하세요"))
if month >= 3 and month <=5 :
    print("봄입니다")
elif month >=6 and month <=8:
    print("여름입니다") 
elif month >=9 and month <=11:
    print("가을입니다")
else:
    print("겨울입니다")