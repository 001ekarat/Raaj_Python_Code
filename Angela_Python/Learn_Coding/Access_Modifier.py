# Access Modifiers are used to set the limit of member accessibility.
#   Name        Access Modifiers        Same_class      Same_Package        Derived_class       Other_class
#   var         Public                  Yes             Yes                 Yes                 Yes
#   _var        Protected               Yes             Yes                 Yes                 No
#   __var       Private                 Yes             No                  No                  No

# class A:                # Parent Class (A)
#     a = 10 # Public
#     _b = 20 # Protected
#     __c = None # Private
#     print(a," ",_b," ",__c)
#     def Add(self):
#         self.__c = self.a + self._b
#         print("Addition:-  ",self.__c)
# obj = A()
# obj.Add()
# print(obj.a)
# print(obj._b)
# print(obj.__c)  # AttributeError: 'A' object has no attribute '__c' because its a Private variable we can't use outside the class .

#----------------------------------------------------------------------------------------------------------------------------------------------------

# class A:                # Parent Class (A)
#     a = 10 # Public
#     _b = 20 # Protected
#     __c = None # Private
#     print(a," ",_b," ",__c)

# class B(A):     # child
#     def Show(self):
#         print(self.a)
#         print(self._b)
#         print(self.__c)     # AttributeError: 'B' object has no attribute '_B__c'. Did you mean: '_A__c'?

# obj = B()
# obj.Show()
# print(obj.a)
# print(obj._b)
# print(obj.__c)              # AttributeError: 'B' object has no attribute '_B__c'. Did you mean: '_A__c'?

#------------------------------------------------------------------------------------------------------------------------------------------------
# Single Module Multiple function/methods
class A:              
    a = 10 # Public
    _b = 20 # Protected
    __c = None # Private
    print(a," ",_b," ",__c)

class B:     
    def Show(self):
        print(A.a)
        print(A._b)
        #print(A.__c)       AttributeError: type object 'A' has no attribute '_B__c'. Did you mean: '_A__c'?  

obj = B()
obj.Show()

