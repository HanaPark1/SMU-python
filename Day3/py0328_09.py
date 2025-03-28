# 은행 번호표 001, 002, 003...010, 011, 012...999

for i in range(1,1000):
    print("{:03d}번".format(i))
    
#구구단 출력

for i in range(2,10):
    print("{}단".format(i))
    for j in range(1,10):
        print("{} * {} = {}".format(i,j,i*j))
    print()