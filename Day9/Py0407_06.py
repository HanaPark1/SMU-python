class Student:
    
    phone = ""
    address = ""
    count = 0
    def __init__(self,name,kor,eng,math):
        self.no = Student.count
        Student.count += 1
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        self.rank = 0
    
    def total(self,kor,eng,math):
        self.total = kor+eng+math
    
    def avg(self):
        self.avg = self.total/3
        
    def s_print(self):
        print("학생: ",self.no,self.name,self.kor,self.eng,self.math,self.total, self.avg, self.rank)
        
# 객체 선언
s = Student(1,"홍길동",100,100,99)
s.s_print()
s = Student(2,"유관순",90,90,91)
s.s_print()