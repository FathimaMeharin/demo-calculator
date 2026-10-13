
#from if_sample import checkNegOrPos
#checkNegOrPos(-9)
#import if_sample as ifs
#ifs.checkNegOrPos(10)
#from if_sample import checkNegOrPos as check
#check(10)
#check(-10)
#import platform
#print(platform.python_compiler())
b=0
try:
    a=10/b
    print(a)
    print('try completed')
except ZeroDivisionError:
    print("can't divide by zero")

print('program completed')