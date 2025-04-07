# 클래스
# 파일 구성 : 다른 타입 령태를 넣을 수 있다는 장점

# 변수 ->  배열(같은타입) -> 다른타입(구조체) -> 객체(클래스) -> 변수, 함수
# 객체지향언어 - 고급언어 

# 클래스 장점
# 변수와 함수 모두 포함
# 변수에 대한 값을 확인,비교
# 캡슐화 : 변수에 직접 접근을 막을 수 있다

class Stu:
    # 생성자 - 클래스가 선언될 때 데이터를 받아서 변수에 저장
    def __init__(self,no,name,kor,eng,math,total,avg,rank):
        self.no = no
        self.name = name
        self.kor = kor
        if kor >= 0 and kor <=100:
            self.kor = kor
        self.eng = eng
        self.math = math
        self.total = total
        self.avg = avg
        self.rank = rank
        
s = Stu(1,"홍길동",100,100,100,300,100.0,1)
s = Stu(1,"홍길동",200,100,100,300,100.0,1) # 클래스 내에 안 넣어짐
s.eng = 200
print(s.eng)
print(s.name)

# 클래스 선언 후 변수 선언하여 사용 가능
# class 첫글자 대문자 사용, 
# class Stu:
#     pass 

# # 클래스 선언
# s = Stu()
# # 변수 선언
# s.no = 1
# s.name = "홍길동"
# s.kor = 100

stu = [1,'홍길동',100,100,100,300,100.0,1]
while True:
    print("1. 학생 출력")
    choice = int(input("원하는 번호를 입력하세요: "))
    if choice == 1:
        print(stu)
        
