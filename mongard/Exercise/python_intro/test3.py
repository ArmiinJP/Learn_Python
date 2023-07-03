class A:
    aCall = 0
    
    def call(self):
        print("a call........")
        #self.aCall += 1
        A.aCall += 1
    
    def show(self):
        print(self.aCall)
        print(A.aCall)

class B(A):
    bCall = 0

class C(A):
    cCall = 0

class D(C, B):
    dCall = 0



a1 = A()
a1.call()
a1.call()

a2 = A()
a2.call()
a2.call()

a2.show()
a1.show()