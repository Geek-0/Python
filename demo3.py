#Python中的字符串学习

#Date：2021；3；2

print("包含中文的str")   #在Python3的版本中字符串是以Unicode进行编码的。

#ord().chr()
print(ord('A'))    #ord()函数,获取字符的整数表示
ord('中')
chr(66)     #chr()函数，把编码转换为对应的字符
chr(25991)

#bytes字符    通过encode()函数进行转换把str转化为指定的bytes
print('ABC'.encode('ascii'))    #纯英文的str可以通过ascii转化为bytes
print('中国'.encode('UTF-8'))    #中文的str可以通过ASCII转化为bytes
print('中国，I LOVE YOU'.encode('UTF-8'))     #英文转换为UTF-8时可以直接输出
print('我喜欢你'.encode('UTF-8'))
#print('中文'.encode('ascii'))    #报错原因'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

#decode()函数，把bytes类型的数据转化为相应的str
print(b'ABC'.decode('ascii'))
print(b'\xe6\x88\x91\xe5\x96\x9c\xe6\xac\xa2\xe4\xbd\xa0'.decode('UTF-8'))

#len()函数 查看str中含有多少个字符
print(len('ABC'))
print(len('中国'))    #直接输入计算的是字符的个数

print(len('ABC'.encode('ascii')))
print(len('中国'.encode('UTF-8')))    #使用encode()函数来转换一下，len()计算的就是bytes（字节数）

#‘%’格式化符号
#  %d——替换整数  %f——替换浮点数  %s——替换字符串  %X——替换十六进制整数
print('Hello,%s' % 'World')
print('Hello,%s' % ('World'))
print('Hello, %s. You only have %d yuan left in your bank account.' % ('Mr.Li',10))
#当不确定要用哪一个用来转换时，可以直接使用‘%s’该符号可以替换任意str

#.format()函数的转换方式
print('Hello, {0}. You only have {1} yuan left in your {2}.'.format('Mr.Li',10,'bank account'))

#f-string的方式进行替换
r = (85-72)/85
print(f'The result is {r:.1f} %')   #{r:.1f}的值被r的值所替换，而且.1f代表留下一位小数

r = (85-72)/85
print(f'The result is {r:.3f} %')