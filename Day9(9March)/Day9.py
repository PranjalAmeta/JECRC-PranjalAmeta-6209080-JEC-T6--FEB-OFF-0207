class Abc:
    def __init__(self,val):
        self.val=val
    def __str__(self):
        return str(self.val)
    def __floordiv__(self, other):
        return self.val//other.val     ##  return  smallest integer val
    def __mod__(self, other):
        return self.val%other.val
    def __truediv__(self, other):
        return self.val/other.val
    def __add__(self,*args):                
        sum=self.val
        for i in args:
            sum+=i.val
        return Abc(sum)
    def __sub__(self,*args):
        sub=self.val
        for i in args:
            sub-=i.val
        return Abc(sub)
# a=Abc(50)
# b=Abc(30)
# c=Abc(40)
# # print(a+b)
# # print(a//b)
# # print(a%b)
# # print(a/b)
# print(a+b+c)
# print((a-b)-c)

# Access Specifiers

# public 
# class Temp:
#     a,b,*c,d='0123456789'
#     def greeting(self):
#         print('Good Afternoob user :)')

# class C2(Temp):
#     pass

# c=C2()
# print(c.d)

## Protected Access Specifier
# class Temp:
#     _a=10      # __a will become private
#     _b=20
# obj=Temp()
# print(obj._a)
# print(obj._b)

## Private Access Specifier
# class Temp:
#     __a=100
#     def __status(self):
#         print('Class name is Temp!')
# obj=Temp()
# print(obj.__a) ## will give error-no attribute
# obj.__status()  ## Same

'''
We can access this by using three approaches
1. by using syntax
2. get & set method
3. by using @property decorator(setter)
'''

## By using Synax
'''
obj_name/class_name._ClassName__prop_name/__method_name (Accesssing)
obj_name/class_name._ClassName__member_name=newVal (Modifying)
'''

# print(obj._Temp__a)
# print(Temp._Temp__a)
# obj._Temp__status()
# obj._Temp__a='0123444444456789'
# print(obj._Temp__a)
# print(Temp._Temp__a)   # Till now only for obj it have changed as it is a object method
# Temp._Temp__a='123454'
# print(Temp._Temp__a)

# def new_method():
#     print('Method definition got changed')

# obj._Temp__status=new_method
# obj._Temp__status()


## By using getter and setter:-

# class Temp:
#     __a=100
#     def __status():
#         print("class name is temp")
#     def get(self):
#         print(self.__a)
#     def set(self,new_val):
#         self.__a=new_val

# obj=Temp()
# obj.get()
# obj.set(200)
# obj.get()

## By Using @property decorator
# class Temp:
#     __a=100
#     @property
#     def get(self):
#         print(self.__a)

#     @get.setter
#     def set(self,new_val):
#         self.__a=new_val

# obj=Temp()
# # obj.get() # Wont work
# obj.get
# obj.set=1000
# obj.get

# from abc import ABC,abstractmethod

# class ATM(ABC):             # Abstract class
#     @abstractmethod
#     def generate_pin(self):
#         pass
#     @abstractmethod
#     def forget_pin(self):
#         pass
#     @abstractmethod
#     def check_bal(self):
#         pass
#     @abstractmethod
#     def withdraw(self):
#         pass
#     @abstractmethod
#     def deposit(self):
#         pass

# class SBI_ATM(ATM):         # Concrete class
#     def generate_pin(self):
#         print("It is used to generate new pin")
#     def forget_pin(self):
#         pass
#     def check_bal(self):
#         print("Amount of balance in your account")
#     def withdraw(self):
#         print("Enter the amount you want to withdraw")
#     def deposit(self):
#         print("Enter the amount you want to deposit")
#     def account(self):
#         print("enter the type of account you want")
# s=SBI_ATM()
# s.check_bal()
# s.account()

# res=lambda a,b:a+b
# print(res(1,2))

# (lambda a,b:print(a+b))(int(input()),int(input()))

# l=[1,2,3]
# print(list(map(lambda x:x*x,l)))

# (lambda num:print(num*num) if num%2==0 else None)(int(input()))

# res=lambda num:num*num if num%2==0 else num*num*num
# print(res(int(input())))



(lambda x:print('POS') if x>0 else print('Neg') if x<0 else print('Zero'))(int(input()))