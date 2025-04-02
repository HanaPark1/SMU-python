txt="안녕하세요"

a_list=[1,2,3,4,5]

# 문자열 인덱싱: 인덱스 번호를 가짐
print(txt[1])
print(a_list[1])

print(a_list[1:3])
print(txt[1:3])

print(txt[2:])
print(txt[:3])

print(txt*3)
print("-"*50)
print(len(txt))

print(txt[::-1])

# 문자열

txt = "abBBcDd hello apple" 
print(txt.upper()) # 대문자 출력
print(txt.lower()) # 소문자 출력
print(txt.swapcase()) # 대문자 -> 소문자, 소문자 -> 대문자
print(txt.title()) # 단어 첫글자 대문자

txt = "**야 생일 축하해....... 비록 나는 가지 못하지만"
print(txt.count("생일"))
print(txt.find("축하해"))
print(txt.find("파이썬"))

t = "aaa.py"
print(t.endswith("py")) # 있으면 True, 없으면 False

txt = " 안녕하 세요 "
print(txt)

# 공백 제거 -rstrip(): 오른쪽 공백 제거, -lstrip(): 왼쪽 공백 제거
print(txt.strip()) 

# 문자를 다른 문자로 치환: " " -> ""
print(txt.replace(" ",""))
print(txt.replace("**","성모"))

txt3 = "----성모----"
# 특정 글자 제거 "--파-이썬--"의 경우에는 "파-이썬"이됨
print(txt3.strip("-"))
print(txt3.replace("-",""))

txt = "a,b,c,d,안녕,반가워"
print(txt.split(txt))

# 데이터베이스는 리스트를 저장할 수 없음
txt = "1,홍길동,100,100,100,300,100,0,1"
txt_list = txt.split(",")
print(txt_list)
txt_list[1] = '유관순'
print(txt_list)

txt = "안녕하세요"
txt2 = txt.join("반가워")
print(txt2)

# map
score = ['100', '99', '90']
sum = 0
for s in score:
    sum += int(s)
print("합계 :", sum)

# 문자열
# map(함수, 데이터값)
score = ['100', '99', '90']
def cal(x):
    return int(x)*100

s_list = list(map(cal,score))

a = "1234"
if a.isdigit(): # 숫자로 변환 가능
    print("숫자로 가능합니다.")
    
my_input = input("숫자를 입력하세요: ")
if my_input.isdigit():
    my_input = int(my_input)
else: 
    print("숫자가 아닙니다. 숫자를 입력하세요")
    

my = int(input("숫자를 입력하세요: "))

print('1234'.isdigit()) # 정수인지 확인
print('abc'.isalpha()) # 알파벳인지 확인 - 한글 X
print('abc123'.isalnum) # 글자 및 숫자인지 확인 - abc, a1, 123 모두 가능
print('ABC'.islower()) # 소문자인지 확인
print('ABC'.isupper()) # 대문자인지 확인

