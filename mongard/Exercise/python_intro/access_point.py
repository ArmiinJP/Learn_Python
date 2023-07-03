
class Person:
    name =  'armin' #public
    _age = 23 #protected
    __height = 176 #private


    def __test(self):
        return "yohoo"


class Male(Person):
    def show(self):
        print("public var: ", super().name)     #NO Error: public
        #print("public var: ", self.name)        #NO Error: public
        
        print("protected var: ", super()._age)     #NO Error: protected
        #print("protected var: ", self._age)        #NO Error: protected

        #print(super().__height)        #Error: private
        #print(self.__height)           #Error: private

        print("private var but use name mangling: ", super()._Person__height)    #No Error: private but name mangling
        #print("private var but use name mangling: ", self._Person__height)       #No Error: private but name mangling
        


print("\n------------------ test access point in inheritence class")
m1 = Male()
m1.show()


print("\n------------------ test access point in outer class")
p = Person()
print("public var: ", p.name)                                           # No Error : public    
print("protected var: ", p._age, "(disAllow but python no Error!)")     # No Error : protected : disAllow but python NO error
#print(p.__height)                                                      # Error : private
print("private var:", p._Person__height, "(but use name mangling)")     #No Error: private but using "name mangling"
#p.__test()                                                             #Error : private
print("private method: ", p._Person__test(), "(but use name mangling)") #No Error: private but using "name mangling"

