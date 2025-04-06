# with 함수 사용시 f.close() 생략
# 모든 학생 영어 점수 +2 하시오

aStr = "1,홍길동,100,99,199"
a_list = aStr.split(",")
print(a_list)
with open("Day8/stu.txt", "r" ,encoding="UTF-8") as f:
    for line in f:
        print(line.strip())
        
f = open("Day8/stu2.txt", 'r', encoding="UTF-8")
while True:
    lines = f.readlines()
    if not lines:
        break
    for line in lines:
        a_list = line.strip().split(',')
        print(a_list)
        print(int(a_list[3])+1)
        print(int(a_list[4])+1)
        a_list[3] = a_list[3]+1
        a_list[4] = a_list[4]+1
    f.close

students = []

f = open("Day8/stu2.txt", 'r', encoding="UTF-8")
line = f.readline()
a_list = line.strip().split(",")
print(a_list[3])
# students.append(f"{'no': {a_list[0]}, 'name': {a_list[1]}, 'kor': {a_list[2]}, 'eng': {a_list[3]}, 'total': {a_list[4]}}")
students.append({
    'no': a_list[0],
    'name': a_list[1],
    'kor': a_list[2],
    'eng': a_list[3],
    'total': a_list[4]
})

with open("Day8/stu2.txt", 'a', encoding="UTF-8") as f: 
    for s in students:
        f.write(str(s) + "\n")


students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
]

# 1. students 리스트를 문자열로 변환
# 2. 파일 쓰기해서 문자열을 저장

# stu.txt
# 1,홍길동,100,100,100,300,100,0,1
# 2,유관순,100,100,99,299,99,67,0,1
# 3,이순신,100,100,99,299,99,67,0,1

with open("Day8/stu.txt", 'w', encoding="UTF-8") as f:
    for s in students:
        text = str(f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}\n")
        f.write(text)
        
with open("Day8/stu.txt",'r',encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
        
# stu.txt 읽기
# 리스트, 딕셔너리 타입으로 변환하기
# students= [] 안에 넣기

students = []

with open("Day8/stu.txt",'r',encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        s = line.strip().split(',')
        students.append({
            'no': int(s[0]),
            'name': s[1],
            'kor' : int(s[2]),
            'eng': int(s[3]),
            'math' : int(s[4]),
            'total' : int(s[5]),
            'avg' : float(s[6]),
            'rank' : int(s[7])
        })
        
for s in students:
    print(s)