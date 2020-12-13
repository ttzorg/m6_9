class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def getName(self):
        return self.name


    def getGender(self):
        return self.gender


    def getAge(self):
        return self.age


class Circle:
    def __init__(self, r):
        self.r = r

    def getCircleArea (self):
        return 3.14 * self.r ** 2

Circle_1 = Circle(5)
print(Circle_1.getCircleArea())