#encoding:utf-8

#函数式编程

#函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。
#函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
#Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。


#==============高阶函数==================
#像map()函数这种能够接收函数作为参数的函数，称之为高阶函数（Higher-order function）

#========map()函数==========
#map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。

def f(x):
    return x * x

print map(f,[1,2,3,4,5,6,7,8])


#========reduce()函数==========
#reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

#比方说对一个序列求和，就可以用reduce实现
def add(x, y):
    return x + y
print reduce(add,[1,2,3,4,5,6,7,8,9])

#如果要把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x,y):
    return 10 * x + y
print reduce(fn,[1,3,5,7,9])
print reduce(fn,map(int , '13579'))

#函数
def str2int(s):
    def fn(x,y):
	return x * 10 + y
    return reduce(fn,map(int,s))

print str2int('123476')

#lambda函数 
def str2int(s):
    return reduce(lambda x,y:x*10+y,map(int, s))

print str2int('6120512')


#============排序函数================
#==========sorted()函数=============
print sorted([38,27,39,12,43])

#自定义比较函数
def reversed_cmp(x, y):
    if x > y:
	return -1
    if x < y:
	return 1
    return 0

#传入自定义的比较函数reversed_cmp，就可以实现倒序排序
print sorted([38,27,39,12,43],reversed_cmp)


#字符串排序
print sorted(['about','Zoo','Love','life'])

def cmp_ignore_case(s1,s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
	return -1
    if u1 > u2:
	return 1
    return 0
#忽略大小写排序
print sorted(['about','Zoo','Love','life'], cmp_ignore_case)


#================函数作为返回值====================
def lazy_sum(*args):
    def sum():
	ax = 0
	for n in args:
	    ax = ax + n
	return ax
    return sum

f = lazy_sum(1,3,5,7,9)
print f
print f() #调用函数f时，才真正计算求和的结果


f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
print f1 == f2 #每次调用都会返回一个新的函数，即使传入相同的参数


#================实践：假设Python没有提供map()函数，请自行编写一个my_map()函数实现与map()相同的功能=========================
#TODO

