students = [
    {'no': 1, 'name': '홍길동', 'kor': 60, 'eng': 100, 'math': 100, 'total': 260, 'avg': 86.66666666666667, 'rank': 3},
    {'no': 2, 'name': '유관순', 'kor': 100, 'eng': 80, 'math': 99, 'total': 279, 'avg': 93.0, 'rank': 1},
    {'no': 3, 'name': '이순신', 'kor': 100, 'eng': 100, 'math': 55, 'total': 255, 'avg': 85.0, 'rank': 4},
    {'no': 4, 'name': '강감찬', 'kor': 80, 'eng': 60, 'math': 71, 'total': 211, 'avg': 70.33333333333333, 'rank': 5},
    {'no': 5, 'name': '김구', 'kor': 90, 'eng': 90, 'math': 98, 'total': 278, 'avg': 92.66666666666667, 'rank': 2}
]

# stu.txt 파일의 문자를 읽어와서 리스트타입으로 변경
# --------------
# 리스트 타입을 -> stu.txt
# 딕셔너리 형태를 -> 1,홍길동,60,100,100,260,86.66666666666667,3
a = {'no': 1, 'name': '홍길동', 'kor': 60, 'eng': 100, 'math': 100, 'total': 260, 'avg': 86.66666666666667, 'rank': 3}
aSt = f"{a['no']},{a['name']},{a['kor']},{a['eng']},{a['math']},{a['total']},{a['avg']},{a['rank']}"
print(aSt)

f = open("Day8/stu.txt",'w',encoding='utf-8')
for a in students:
    data = f"{a['no']},{a['name']},{a['kor']},{a['eng']},{a['math']},{a['total']},{a['avg']},{a['rank']}\n"
    f.write(data)
f.close