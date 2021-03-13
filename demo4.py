#列表的学习
#Date：2021：3：6
#list()  tuple

programming_language = ['python','C','C++','C#','GO','php']     #列表list()是一种有序的集合，可以随时添加，删除，访问，替换列表中的元素
print(programming_language)

x = len(programming_language)   #len()函数可以计算列表中元素的数量
print(x)

#索引
print(programming_language[0])      #使用索引来对列表中的元素进行访问时，索引是从0开始的
print(programming_language[3])

print(programming_language[-1])     #用 -1 作为索引可以直接访问到列表的最后一个元素
print(programming_language[-3])     #而 -3 则表明访问列表中的倒数第三个元素，这里和 -1 最好分清

#print(programming_language[7])      #当索引超出范围程序会报错！！！

#.append()
programming_language.append('HTML')     #.append()可以直接往list的末尾追加元素
print(programming_language)

#.insert()
programming_language.insert(1,'MarkDown')     #.insert()可以在指定的索引号位置添加元素
programming_language.insert(4,'Java')
print(programming_language)

#.pop()
programming_language.pop()      #.pop() 可以删除list最末端的元素
print(programming_language)
programming_language.pop(2)     #.pop(?)可以删除list()中指定位置的元素
print(programming_language)

programming_language[2] = 'CSS'
print(programming_language)

L = ['123','Hello','你好','+—=']      #list中的元素也可以是不一样的数据类型
print(L)

S = ['app','fight']
L = ['123','Hello',S,'你好','+—=']    #list中也可以包含另一个列表，而这个被包含的列表也是属于包含列表中的一个元素。
#L = ['123','Hello',['app','fight'],'你好','+—=']     #上下两种嵌套方式都是一样的
print(L)

#tuple
#tuple也是一种有序列表，称为元组，tuple和list非常相似，但是tuple一旦初始化就不能修改
classmates = ('Jack','Tom','Tim','Bob')
#classmates.append('Tonny')     #因为tuple的列表类型是属于不可更改的有序数列所以不能使用.append() .insert()  或直接位置赋值的方式来进行元素的更改

T = ('a','b',['c','d'])     #tuple的列表中可包含list型的列表，此时这里面的列表就是可以更改的
print(T)
T[2][0] = 'X'
T[2][1] = 'Y'
print(T)