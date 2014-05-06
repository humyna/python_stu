#encoding:utf-8

#只要是可迭代对象，无论有无下标，都可以迭代

#==================迭代dict========================
dict = {'a':1,'b':2,'c':3}

#迭代key
for key in dict:
    print key
#因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样


#迭代value
for value in dict.itervalues():
    print value

#同时迭代key和value
for k,v in dict.iteritems():
    print k,v


#================迭代字符串=======================
for ch in 'ABC':
    print ch

#================判断一个对象是否可迭代===============================
#当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
#方法是通过collections模块的Iterable类型判断
from collections import Iterable

print isinstance('abc',Iterable) #str是否可迭代
print isinstance([1,2,3],Iterable) #list是否可迭代
print isinstance(123,Iterable) #整数是否可迭代

#==========enumerate函数==============
#如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成[索引-元素]对，这样就可以在for循环中同时迭代索引和元素本身
for i,value in enumerate(['A','B','C']):
    print i,value

#for循环里，同时引用了两个变量，在Python里是很常见的
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x,y

#=============小结===================
#任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。

