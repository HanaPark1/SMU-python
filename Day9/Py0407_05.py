# 변수, 함수 집합체 - 변수에 대한 그룹핑 kor,eng,math
# list, dict 타입 - 함수까지 sum, avg, rank 함수
# 입력받을 때.... 처리, 수정할때 ...직접처리
# 특정 데이터 값이 들어왔을 때 잘못된 데이터는 입력이 안 되도록 구현

# class Car:
#     color = "white"
#     speed = 0
#     tire = 4
#     door = 5
    
#     def speedUp(self,s):
#         self.spped += s
#     def speedDown(self, s):
#         self.speed -= s
        
# a_list = [1,2,3,4,5]      
# a_list2 = [1,2,3,4,5]
# a_list2 = a_list # 얕은 복사
# a_list2 = [*a_list]

# a = Car()
# a.speed = 20


# a3 = Car()
# a3.color = "blue"
# a3.tire = 5
# a3.door = 5

class Car:
    def __init__(self,color,tire,door): # 생성 init
        self.color = color #self.color : Car변수, color: 요청받은 변수
        self.tire = tire
        self.door = door
        self.speed = 0
        
    def speedUp(self,s):
        self.spped += s
    def speedDown(self, s):
        self.speed -= s
        
# 생성자를 사용한 객체선언과 동시에 데이터 입력
c = Car("red",5,4)

# 기본 형태 객체 선언 후 데이터 입력
# # a2 = Car()
# a2.color = "red"
# a2.tire = 5
# a2.door = 4