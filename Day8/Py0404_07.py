# 파일 읽어오기
# 1. open() 2. f.read() 3. f.close
# r: 읽기, w: 쓰기, a: 이어쓰기
f = open("Day8/stu.txt", 'r', encoding='utf-8')
while True:
    data = f.readline()
    