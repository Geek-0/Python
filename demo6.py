#Date:2021,3,9
#循环语句的学习
#by：Geek-Men

programming_language = ['python','C','C++','C#','GO','php']
for programming_language_0 in programming_language:
    print(programming_language_0)       #这段代码，会依次打印programming_language中的每一个元素

#计算1——10的整数代数和
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

#长列表的建立
X = list(range(1000))
print(X)

#range()函数
sum = 0
for x in range(1001):
    sum = sum + x
print(sum)

#循环的第二种方式：while()循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n =n - 2
print(sum)

#小程序：利用循环将列表中的名字一一打印出来，并在名字前加上Hello
name = ['Jack','Lisa','Tom','Tim','Lucy']
for N in name:
    print('Hello',N)

#break语句  跳出循环
num = 1
while num <= 100:       #当num小于或等于100的时候一直打印输出num的值
    if num > 10:        #当num大于10的时候
        break       #跳出循环，直接执行最后的语句。
    print(num)
    num = num + 1
print('END')

#continue语句，跳过当前这一次的循环，直接开始下一次的循环
number = 0
while number < 10:
    number = number + 1
    if number % 2 == 0:     #如果number是一个偶数，那么便执行continue语句
        continue    #我们可以把continue语句理解为类break语句，continue语句会直接开始下一轮的循环，不再执行本来循环中的剩下内容。
    print(number)