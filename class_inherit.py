#클래스 상속 오버라이딩
'''
class Person:
    total_count = 0 #클래스 변수 공유가능
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        Person.total_count += 1
    def introduce(self):
        print(f'제 이름은 {self.name}이고, 나이는 {self.age}살입니다.')

p1 = Person('방재운', 17)
p1.introduce()

p2 = Person('서정민', 17)
p2.introduce()

p3 = Person('유우진', 17)
p3.introduce()

print(p3.total_count)


#상속

class Person:
    total_count = 0 #클래스 변수 공유가능
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        Person.total_count += 1
    def introduce(self):
        print(f'제 이름은 {self.name}이고, 나이는 {self.age}살입니다.')

class Student(Person):
    def __init___ (self, name, age):
        super().__init__('방재운',17)
    def run(self):
        print(f'저는 뛸 수 있어요')

s1 = Student('방재운',17)  
s1.introduce()
s2 = Student('서정민',17)  
s2.introduce()
s3 = Student('유우진',17)  
s3.introduce()
'''
#오버라이딩

class Person:
    total_count = 0 #클래스 변수 공유가능
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        Person.total_count += 1
    def introduce(self):
        print(f'제 이름은 {self.name}이고, 나이는 {self.age}살입니다.')

class Student(Person):
    def __init___ (self, name, age):                   
        super().__init__('방재운',17)
    def run(self):
        print(f'저는 뛸 수 있어요.')
    def introduce(self):
        print(f'제 이름은 {self.name}이고, 나이는 비밀입니다.')

stu1 = Student('방재운',17)
stu1.introduce()

print(Student.mro())
print(Person.mro())
