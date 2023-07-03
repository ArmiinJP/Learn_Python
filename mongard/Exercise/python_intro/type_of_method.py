import datetime

class Person():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    """در پایتون instance method 
    به متدهای عادی گفته میشود که در کلاس‌ها وجود دارد
    """
    def show(self):
        print(f'name is: {self.name}, height is: {self.height}, age is: {self.age}')


    """برخلاف instance method
    که آبجکت را به عنوان اولین آرگومان میگرفتند، 
    class method
    خود کلاس را به عنوان اولین آرگومان‌ میگیرند.
    """
    @classmethod
    def from_birth(cls, name, height, age):
        return cls(name, height, datetime.datetime.now().year - age)


    """
    برخلاف متدهای class و instance 
    هیچ مقداری را به عنوان اولین آرگومان نیاز ندارند.
    متدهای static 
    متدهایی هستند که از نظر منطقی شبیه به کلاس مورد استفاده دارند اما نیازی به آبجکت یا خود کلاس ندارند
    """
    @staticmethod
    def is_adult(age):
        if age >= 18:
            print("Yes")
        else:
            print("No")



p1 = Person("ali", 180, 1999)
p1.show()

p2 = Person.from_birth("reza", 188, 1965)
p2.show()

Person.is_adult(24)