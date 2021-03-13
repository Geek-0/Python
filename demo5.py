#Date:2021,3,7
#by：Geek-Men
#条件判断  if语句

"""
age = 20
if age >= 18:       #python是一门有着严格缩进规律的语言。
    print('Your age is:',age)
    print('you are a grown men now.')
"""
age_0 = 22
if age_0 << 18:
    print('Your age is:',age_0)
    print('you are still a child.')

#if else 语句的使用
age_1 = 3
if age_1 >= 18:
    print('Your age is:',age_1)
    print('adult')
else:
    print('Your age is',age_1)
    print('teenager')

#if elif 语句的使用
age_2 = 3
if age_2 >= 18:
    print('Your age is:',age_2)
    print('adult')
elif age_2 >= 6:
    print('teenager')
else:
    print('kid')

#elif是else if的缩写，elif可以存在多个，使用elif的完整形式如下：
"""
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>  注意，if
"""

#if 语句的执行特点
a = 3
if a >= 0:
    print('Yes')    #在该程序执行的过程中，可以看见虽然a>0也>1，但是if是从上到下进行判断的，如果只要中间有一个判断是True，那么if将不会再进行判断
elif a >= 1:
    print('Hello')
else:
    print('No')

#再次说一下input和if的混合使用
age = int(input('please enter your name here:'))    #此处要声明输入的数为整数，才能进行后续的比较。

if age >= 18:
    print('adult')
else:
    print('teenager')