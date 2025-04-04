f = open("aa.txt", "w", encoding="UTF-8")

f.write("안녕하세요\n")

for i in range(10):
    f.write("성모야 살기 좋은 세상 만들어 줄게\n")
f.close

f = open("aa.txt", "r", encoding="UTF-8")
lines = f.readlines()

for line in lines:
    print(line)