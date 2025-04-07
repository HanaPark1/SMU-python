class Student:
    # 인스턴스 변수 - 객체선언 시 각각 변수들이 존재 : 공용으로 사용 안 됨
    count = 1 # 클래스 변수 -  모든 객체가 공용으로 사용하는 변수
    
    def __init__(self, name, kor, eng, math):
        self.no = Student.count
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = (kor+eng+math)/3
        self.rank = 0
        Student.count += 1
        
    def __str__(self):
        return f"{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg},{self.rank}"
    
class Students:
    def __init__(self):
        self.students = []
        
    def add(self,s):
        self.students.append(s)
        
    def __str__(self):
        for s in self.students:
            print(s.no,s.name,s.kor,s.eng,s.math,s.total,s.avg,s.rank)

ss = Students()           
s = Student("홍길동",100,100,100)
print(s.no,s.name,s.kor,s.eng,s.math,Student.count)
s2 = Student("유관순",99,99,88)
print(s2.no,s2.name,s2.kor,s2.eng,s2.math,Student.count)
print(s.no,s.name,s.kor,s.eng,s.math,Student.count)
s3 = Student("이순신",90,90,91)
print(s3.no,s3.name,s3.kor,s3.eng,s3.math,Student.count)
print(s)

ss.add(s)
ss