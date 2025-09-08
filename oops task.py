# class mobile:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
# mobile1=mobile('Samsung','M14')
# print(mobile1.model)
# mobile2=mobile('oppo','a59')
# print(mobile2.brand)

# class Student:
#     def __init__(self, name, roll_no):
#         self.name = name
#         self.roll_no = roll_no

#     def display(self):
#         print(f"Name: {self.name}, Roll No: {self.roll_no}")
# s1 = Student("Vishalika", 101)
# s1.display()


# class Animal:
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound
#     def speak(self):
#         print(f"{self.name} says {self.sound}")
# dog = Animal("Dog", "Bark")
# cat = Animal("Cat", "Meow")
# dog.speak()
# cat.speak()


class Fruit:
    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.taste = taste
    def details(self):
        print(f"{self.name} is {self.color} in color and tastes {self.taste}.")
apple = Fruit("Apple", "Red", "Sweet")
banana = Fruit("Banana", "Yellow", "Sweet")
lemon = Fruit("Lemon", "Green", "Sour")
apple.details()
banana.details()
lemon.details()
