# 백준이 아닙니다!
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def introduce(self):
        return(f"제 이름은 {self.name}이고, 나이는 {self.age}이고, 키는 {self.height}입니다.")
    
    def yell(self):
        return("아?")
      
class Developer(Person):
    keyboard = "기계식"

    def yell(self):
        return("어?")

class Designer(Person):
    def __init__(self, name, age, height, disease):
        super().__init__(name, age, height)
        self.disease = disease

class ProductManager(Person):
    def yell(self):
        return("개발자님 여기 오류있어요")
    
    def aging(self):
        self.age += 2
        self.height -= 5
        Developer.keyboard = "멤브레인"
        return("개발자를 새로 뽑아야하나...")

d1 = Developer('하민', 20, 186)
d2 = Designer('하석', 30, 176, '허리디스크')
p1 = ProductManager('정석', 24, 180)

print(d1.introduce())
print(d1.yell())
print(d2.introduce())
print(d2.yell())
print(p1.introduce())
print(p1.yell())
print(p1.aging())
print(p1.introduce())