import math
def quadratic(a,b,c):       #定义了一个名为quadratic的函数，可以在后面的程序中被调用，也可以直接运行
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    return x1,x2

z = float(input('please enter a:'))
v = float(input('Please enter b:'))
n = float(input('Please enter c:'))

if z == 0:
    print('这不是二元一次函数')
elif v ** 2 - 4 * z * n < 0:
    print("方程无解")
else:
    print('方程%sX^2+%X+%s=0 的解是%s' % (z,v,n,quadratic(z,v,n)))

"""
def quadratic(a,b,c):
    if not isinstance((a,b,c),int):
        raise TypeError('bad operant type')
    if a == 0:
        print('超出本题探讨范围')
    elif b ** -4 * a * c > 0:
        x1 = -b + (math.sqrt(b ** -4 * a * c)) / (2 * a)
        x2 = -b - (math.sqrt(b ** -4 * a * c)) / (2 * a)
        print(x1,x2)
    elif b ** -4 * a * c < 0:
        print('方程无解')
    else:
        x3 = -b / (2 * a)
        print(x3)
    quadratic(2,1,4)
print(quadratic(int(input()),int(input()),int(input())))
"""