'''
Exception Handling Approaches
--> Specific Exception Handling
--> Generic Exception Handling
--> Default Exception Handling
'''

'''
Specific Exception Handling - If we are Aware of the error or,exception then we go with specific.
try:
    problem
    statement
except ErrorName:
    resolution 
    solution code
'''
# n1,n2=21,0
# try:
#     result=n1/n2
#     print(result)
# except ZeroDivisionError:
#     # Solution code
#     print('Please do not choose zero as the denominator')
# # Further execution code
# print('further execution line 01')
# print('further execution line 02')

# try:
#     a,b,c=1,2
#     print(a,b,c)
# except ValueError:
#     print("not enough values to unpack")
'''
Generic:-
We cant remember all the error names so we can use the generic "Exception" keyword
That contains all the exception it is the parent Exception class
'''
# try:
#     a,b,c=1,2
#     print(a,b,c)
# except Exception:
#     print("not enough values to unpack")

## Drawback- using generic "exception handling",we cant handel keyboard interruption
import time 
# try:
#     while True:
#         print(time.time())
# except Exception:
#     print("Error occured")

# try:
#     while True:
#         print(time.time())
# except KeyboardInterrupt:
#     print("Error occured")

'''
Default Exception
- Eat 5 star do nothing
- Just write except
- It is the type of exception handling in which we can handel 
  all the types of error or exceptions excepty "SyntaxError"
'''

# try:
#     while True:
#         print(time.time())
# except:
#     print("Error occured")

      
# num=int(input())
# if(num>=18):
#     print('eligible')
# else:
#     raise KeyboardInterrupt('not eligible')

# class MyException(Exception):
#     pass
# n1,n2=10,0
# if(n2==0):
#     raise MyException('Second num can not be Zero!')
# else:
#     print(n1/n2)

s=input('Enter a string:')
assert s==s[::-1],'it is not a palindromic String!'
print('It is palindromic') 