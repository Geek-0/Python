import math
#多个函数的定义以及调用

#定义一个计算任意数平方的函数，并在结果显示过程中调用这个函数。


#x = int(input("Please enter a number in here:"))

def power_1(x):     #定义名为power_1的函数，并在后面被调用
    return x * x        #注意，这里要求返回x的平方值，所以我们要给这里赋值，赋值的方法我这里是直接在后面调用的时候赋值

def power_2(a,n):       #这里要赋值两个数，同理也可以在后面函数调用的过程中被赋值
    s = 1
    while n > 0:
        n = n - 1
        s = s * a
    return s

print('The answer is:',power_2(int(input('The thure of a matter')),int(input('The index'))))        #这里的input()函数起到了获取用户数值并赋予到x和n中的作用
print(power_1(int(input('Enter a number in here:'))))

