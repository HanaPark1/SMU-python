# 파일 입출력 : 파일 열기 -> 파일 읽기, 쓰기 -> 파일 닫기

# 파일 열기 - 3가지 모드:  r: 읽기모드, w: 쓰기모드, a: 추가모드
f = open("a.txt", "r")
f = open("a.txt", "w")
f = open("a.txt", "a")

# 파일 읽기 - r
f = open("Day8/a.txt", "r",encoding="utf-8")
print(type(f))
for line in f:
    print(line.strip())
print("완료")
f.close()

# 파일 읽기 - r 모두 읽기
f = open("Day8/a.txt", "r",encoding="utf-8")
lines = f.readlines()
for line in lines:
    print(line.strip())
print("완료")
f.close()

# 파일 읽기 - 절대경로
f = open("/Users/hana/SMU-stydy/SMU-python/Day8/a.txt", "r",encoding="utf-8")
lines = f.readlines()
for line in lines:
    print(line.strip())
print("완료")
f.close()

f = open("Day8/news.txt", "r", encoding="UTF-8")
lines = f.readlines()
for line in lines:
    print(line.strip())
f.close