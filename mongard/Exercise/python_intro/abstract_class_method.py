from abc import ABC, abstractclassmethod

class A(ABC):

    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def show(self):
        pass

    def show2(self):
        pass


class B(A):
    def __init__(self):
        pass
    def show(self):
        #owerwrite method show
        print("Yohoooo")
        pass


b1 = B() # OK
b1.show()

a = A()  # NOT OK