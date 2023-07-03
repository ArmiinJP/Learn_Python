"""
در این مثال سه تا کامنت هست، یکبار خروجی را برای همین چیزی که هست صدا بزن و ترتیب چیزی که کال میشه را حدس بزن

یک بار هم کامنت ها را بردار و مجدد صدا بزن و چیزی که نمایش میشه را ببین

به خروجی MRO توجه کنض
"""

class A:
    aCall = 0    
    def call(self):
        print("a call........")
        A.aCall += 1

#class B():
class B(A):
    bCall = 0
    def call(self):
        print("b call........")
        B.bCall += 1
        super().call()

class C(A):
    cCall = 0
    def call(self):
        print("c call........")
        C.cCall += 1
        super().call()

class D(C, B):
    dCall = 0
    def call(self):
        print("d call........")
        D.dCall += 1
        super().call()


d = D()
d.call()

print(D.dCall, C.cCall, B.bCall, A.aCall)
print(help(d))