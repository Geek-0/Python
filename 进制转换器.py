#Date:2021,3,4
#by:Geek-Men
#project:python中实现进制转换
#dec()十进制 bin()二进制 oct()八进制 hex()十六进制

import time as t
YourNamber=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]    #定义该列表并把16进制中的数输入进列表中。
def Dsys(Number,System):     #定义函数以及类型
    Ilist=[]    #输入一个数，并且告知该数的一个进制。
    Dlist=[]
    result=""
    dicimal = Number - int(Number)  #输入一个要转换的数。并且是整数
    interger=int(Number)    #输入该数是属于什么进制类型。

    #整数部分短除法
    while interger >= System:
        Ilist.append(YourNamber[interger%System])
        interger = interger // System   #对该类型数进行地板除
    Ilist.append(YourNamber[interger])
    #小数部分乘以二取差值
    start = t.perf_counter()
    while dicimal != 0:
        dicimal *= System
        Dlist.append(YourNamber[int(dicimal//1)])
        dicimal-=dicimal//1
        #如果在程序中出现死循环，则跳出这个程序
        if t.perf_counter()-start>=0.001:
            break
        #将储存数字的列表转换为最终结果
    for k in range(len(Ilist)):
        result+=str(Ilist.pop(-1))
    if Dlist!=[]:
        result+="."
        for k in Dlist:
            result+=str(k)
    return result

def Osys(Numberansystem,System):
    """
    输入数字及其进制
    输出转化为十进制
    """
    result=0
    interger=Numberansystem[0].split(".")[0]
    #判断是否含有小数部分。
    try:
        decimal=Numberansystem[0].split(".")[1]
    except:
        decimal="0"
    #将整数与小数部分分别转换为十进制
    for i in range(len(interger)):
        result += YourNamber.index(interger[i]) * (System ** (len(interger) - i - 1))
    for j in range(len(decimal)):
        result += YourNamber.index(decimal[j]) * (System ** (-j - 1))
    return result

def main():
    print('欢迎使用Geek进制转换器')
    NumberAndPreviousSystem=input('请输入你想要转换的数以及该数的进制类型（中间请用空格进行区分）：').split(" ")
    LaterSystem=int(input('请告诉我你最终想把这个数值转为什么进制类型（直接输入数字就行）：'))
    #判断输入的数字中是否存在负数
    symbol=""
    if NumberAndPreviousSystem[0][0]=="-":   #如果输入的数字为负数
        NumberAndPreviousSystem[0]=NumberAndPreviousSystem[0][1:]   #把这个负数转化为它的绝对值
    PreviousSystem=int(NumberAndPreviousSystem[1])
    intermidialNumber=Osys(NumberAndPreviousSystem,PreviousSystem)
    resultNember=Dsys(intermidialNumber,LaterSystem)
    #若小数不足十位则直接输出，否则输出十位小数
    try:
        print(symbol+resultNember[:resultNember.index(".")+11]+"("+str(LaterSystem)+")")
    except:
        print(symbol+resultNember+"("+str(LaterSystem)+")")
main()