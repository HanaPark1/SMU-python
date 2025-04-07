class Car:
    speed = 0
    tire = 4
    door = 5
    def speedUp(self, s):
        self.speed += s
        print("현재 속도 ",self.speed)
        
class Sedan(Car):
    color = "red"
        
c = Car()

s = Sedan(Car)
s.color = "red"