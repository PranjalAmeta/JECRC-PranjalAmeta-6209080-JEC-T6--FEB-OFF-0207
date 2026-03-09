class Abc:
    @staticmethod
    def greet():
        print("hello")
a=Abc()
a.greet()


class Temp:
    def sum(self,a,b):
        print(a+b)
    def sum(self,a,b,c):  # Overwrites the reference of previous sum
        print(a+b+c)
t=Temp()
t.sum(1,2)
# To solve this we use monkey patching.

class Temp:
    def sum(self,a,b):
        print(a+b)
    add_two_sum=sum
    def sum(self,a,b,c):  # Wont Overwrite the reference of previous sum
        print(a+b+c)
t=Temp()
t.add_two_sum(1,2)  # Dont use sum
t.sum(1,2,3)