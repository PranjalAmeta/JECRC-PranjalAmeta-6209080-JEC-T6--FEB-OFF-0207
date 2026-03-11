# file=open('temp.txt','w')
# file.write("Hello")     ## Always overwrites the prev data present and creates new file if not present 
# file.writelines([
#     'ky bolti public ',
#     'bole tog taklif \n',
#     '20 ka karra kahara ',
#     'me kisi ko ni batara'
# ])

# file=open('temp.txt','r')
# # print(file.read())
# # print()
# print(file.readline())
# print(file.readline())
# print(file.readline()) # will return empty list is no line present    
# # print()
# # print(file.readlines())
# file.close()    


# file=open('temp.txt','w+')
# file.writelines([
#     'ky bolti public ',
#     'bole tog taklif \n',
#     '20 ka karra kahara ',
#     'me kisi ko ni batara'
# ])
## no o/p the pointer is at last line and it will start reading from there only 
## So no lines are there after last line so we cill make the pointer go towards first line
# print(file.read())  
# So we will use seek() funcn ti make the interpreter to point to the first line
# file.seek(0)
# print(file.read())
# file.close()


# file=open('notes.txt','r')  # File not present as only w can make new file
# print(file.read())


# file=open('abc.txt','a+')
# file.write(' hello ')
# file.write('how are you')
# file.close()

import csv
from datetime import date
file=open('expense.csv','a+',newline='')
# w=csv.writer(file)
# w.writerow(['DATE','CATEGORY','AMT'])
# w.writerows(
#     [
#         [date.today(),'travel',2000],
#         [date.today(),'Food',1000],
#         [date.today(),'timepass',4000]
#     ]
# )
r=csv.reader(file)
file.seek(0)
print(list(r))
file.close()

