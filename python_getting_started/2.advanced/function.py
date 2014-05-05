#encoding:utf-8

#函数就是最基本的一种代码抽象的方式

#定义函数时，需要确定函数名和参数个数；
#如果有必要，可以先对参数的数据类型做检查；
#函数体内部可以用return随时返回函数结果；
#函数执行完毕也没有return语句时，自动return None。
#函数可以同时返回多个值，但其实就是一个tuple。


#计算3个不同大小的圆的面积
PI = 3.14
r1 = 12.34
r2 = 9.08
r3 = 73.1
s1 = PI * r1 * r1
s2 = PI * r2 * r2
s3 = PI * r3 * r3
print s1,s2,s3

#python built-in functions
#url: https://docs.python.org/2/library/functions.html

#1.内置函数
#绝对值函数abs
print abs(10)
print abs(-12)
print abs(12.34)
#print abs(12,23) #error
#print abs('str') #error

#比较函数cmp
print cmp(1,2)
print cmp(2,1)
print cmp(1,1)

#数据类型转换函数
#int()函数可以把其他数据类型转换为整数
print int('123')
print int(12.34)
print float('12.34')
print str(1.23)
print unicode(100)
print bool(1)
print bool('')


#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a =  abs #变量a指向abs函数
print a(-1)


#2.自定义函数
def my_abs(x):
    #参数检查:对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance实现
    if not isinstance(x,(int,float)):
	raise TypeError('bad oper and type')
    if x >= 0:
	return x
    else:
	return -x

print my_abs(-3)
#print my_abs('A')#error 测试参数检查

#空函数
#pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
def nop():
    pass


#返回多个值,这个功能比较好玩~~
import math

def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

x,y = move(100,100,60,math.pi / 6)

print x,y
#但其实这只是一种假象，Python函数返回的仍然是单一值,原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple
r =  move(100,100,60,math.pi / 6)
print r


#函数的参数：Python的函数定义非常简单，但灵活度却非常大。正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码设置默认参数时，有几点要注意：
#一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；二是如何设置默认参数。
#当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
#使用默认参数有什么好处？最大的好处是能降低调用函数的难度。

def power(x,n=2):
    s = 1
    while n > 0:
	n = n - 1
	s = s * x
    return s
print power(5)
print power(5,2)
print power(5,3)

#============ 函数参数，很重要的知识点=========================
#默认参数
#a.有多个默认参数时，调用的时候，既可以按顺序提供默认参数
#b.也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上
#c.默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑,如下
def add_end(L=[]):
    L.append('END')
    return L

print add_end()
print add_end() #输出有问题
print add_end() # 输出有问题

#说明：Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#所以，定义默认参数要牢记一点：默认参数必须指向不变对象！

#修改如下：
def add_end(L=None):
    if L is None:
	L = []
    L.append('END')
    return L

print add_end()
print add_end()
print add_end(['a','b'])
print add_end(['c','d'])
print add_end()

#可变参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
#定义可变参数和定义list或tuple参数相比，仅仅在参数前面加了一个*号
#在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
def calc(*nums):
    sum = 0
    for n in nums:
	sum = sum + n
    return sum

print calc(1,2,3)
print calc()

num = [1,2,5]
print calc(*num) # Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去

#关键字参数
#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
#关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求
def person(name,age,**kw):
    print 'name:',name,'age:',age,'other:',kw
person('hufo',28)
person('hufo',28,city='beijing')
person('hufo',28,gender='M',hobby='code')

#和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('hufo', 28, city=kw['city'], job=kw['job'])


#参数组合
#在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数
def func(a,b,c=0,*args,**kw):
    return 'a =',a,'b =',b,'c =',c,'args =',args,'kw = ',kw

print func(1,2)
print func(1,2,3)
print func(1,2,c=3)
print func(1,2,4,'a','b')
print func(1,2,5,'a','b',x=13)

#最神奇的是通过一个tuple和dict，你也可以调用该函数
args = (1,2,3,4)
kw = {'x':'8'}
print func(*args,**kw)
#所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的

#参数小结
#Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
#默认参数一定要用不可变对象，如果是可变对象，运行会有逻辑错误！
#要注意定义可变参数和关键字参数的语法：
#*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict。
#以及调用函数时如何传入可变参数和关键字参数的语法：
#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

#ps:vim批量注释的命令：181,189s/^/#/g


#=================递归函数=====================
#使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
def fact(n):
    if n == 1:
	return 1
    return n * fact(n - 1)

print fact(10)
print fact(100)
#print fact(1000) #error 堆栈溢出

#解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
#改写成尾递归：主要是要把每一步的乘积传入到递归函数中
def fact(n):
    return fact_iter(1,1,n)

def fact_iter(product,count,max):
    if count > max:
	return product
    return fact_iter(product * count ,count + 1,max)

print fact(5)
print fact_iter(1,1,5) #可以看到，return fact_iter(product * count, count + 1, max)仅返回递归函数本身，product * count和count + 1在函数调用前就会被计算，不影响函数调用
#print fact(1000) #error 还是有问题

#有一个针对尾递归优化的decorator，可以参考源码：
#http://code.activestate.com/recipes/474088-tail-call-optimization-decorator/

#递归小结
#使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
#针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
#Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。


