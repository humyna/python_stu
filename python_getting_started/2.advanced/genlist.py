#encoding:utf-8

#=================列表生成式====================
#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

#生成[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print range(1,11)

#生成[1x1, 2x2, 3x3, ..., 10x10]
L = []
for x in range(1,11):
    L.append(x * x)
print L

#循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list
print [x * x for x in range(1,11)]

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
print [x * x for x in range(1,11) if x % 2 ==0]

#使用两层循环，可以生成全排列
print [m + n for m in 'ABC' for n in 'XYZ']

#=====================实用技巧===========================
#运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os
print [d for d in os.listdir('../.')] ## os.listdir可以列出文件和目录


#for循环其实可以同时使用两个甚至多个变量，比如dict的iteritems()可以同时迭代key和value
dict  = {'x':'A','y':'B','z':'C'}
for k,v in dict.iteritems():
    print k,'=',v

#列表生成式也可以使用两个变量来生成list
print [k + '=' + v for k,v in dict.iteritems()]


#把一个list中所有的字符串变成小写
L = ['life','Money','Job','Love']
print [i.lower() for i in L ]


#===================小结========================
#运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list

#==================思考题=====================
#如果list中既包含字符串，又包含整数，怎么把list中所有的字符串变成小写  注意：由于非字符串类型没有lower()方法，所以列表生成式会报错
L = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() if isinstance(s,str) else s for s in L ]
