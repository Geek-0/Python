#数据类型和变量
#数据类型 整数，浮点数，字符串（转义字符“\”）

#整数
print('100','20','123')
print(1_000_000)
print(100+23,'',50+50)  #整数的运算 永远精确

#浮点数
print('0.1',0.123,1.23e10,1.23e-10)
print(1.23e8-1.23e-6)   #浮点数的运算可能会存在“四舍五入的误差”

#字符串
print('50+50','',50+50)    #''单的双引号内的内容会原封不动的被打印出来
print('I\'m ok.')
print('I\'m learning\nPython')  #\n是转义字符中的换行符，把\n后的字符换行显示
#print(\\\n\\)

print(r'\\\t\\')
print(r'''line1
line2
line3''')    #''''''这种格式可以直接在程序中多行显示,前面加上‘r’也可以。

#布尔值
#True and True   #and,与运算,全真为真，全假为真，一真一假为假
#True and False
#False and False

#True or True   #or,或运算，全假为假，其余为真
#True or False
#False or False

#not True   #not,非运算，单目运算，真变假，假变真
#not False
age = int(input('please enter your name here:'))    #此处要声明输入的数为整数，才能进行后续的比较。

if age >= 18:
    print('adult')
else:
    print('teenager')