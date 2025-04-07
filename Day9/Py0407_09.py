class Stu:
    def __init__(self,no,name,kor,eng):
        self.__no = no
        self.__name = name
        self.__kor = kor # __ 언더바 2개 private 접근제한 : 캡슐화
        self.__eng = eng
        
    # Setter
    def SetKor(self,kor):
        if kor >= 0 and kor <= 100:
            self.__kor = kor
        else:
            raise NotImplementedError("유효한 값이 아닙니다.")
        
    def GetKor(self):
        return self.__kor
    
    def getEng(self):
        return self.__eng
    def setEng(self,eng):
        if eng >= 0 and eng <= 100:
            self.__eng = eng
        else: raise NotImplementedError("유효한 데이터가 아닙니다")
        
    # setter가 없기 때문에 변경 불가
    def getNo(self):
        return self.__no
        
    def getName(self):
        return self.__name
    
    @property # print(Stu.kor)
    def kor(self):
        return self.__kor
    
    @kor.setter # 
    def kor(self,kor):
        if kor >= 0 and kor <= 100:
            self.__kor = kor
        else:
            raise NotImplementedError("유효한 값이 아닙니다.")
        
    def __str__(self):
        return f"{self.no},{self.name},{self.__kor},{self.eng}"
        
s = Stu(1,"홍길동",100,100)
s.__kor = 200 # s.kor
print(s.no, s.name, s.__kor) # 지역 변수의 개념 s.__kor의 값 출력
s.eng = 300
print(s)

